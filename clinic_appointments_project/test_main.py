import unittest
from datetime import date, datetime, timedelta

from main import (
    Appointment,
    AuthorizationError,
    BookingError,
    ClinicSystem,
    Doctor,
    MedicalRecord,
    Patient,
    TimeSlot,
)


def future_slot(days: int, hour: int = 10) -> TimeSlot:
    day = (datetime.now() + timedelta(days=days)).date()
    return TimeSlot(datetime.combine(day, datetime.min.time()).replace(hour=hour))


class ClinicSystemTests(unittest.TestCase):
    def setUp(self):
        self.clinic = ClinicSystem(maxUpcomingAppointments=3)
        self.slot1 = future_slot(2, 10)
        self.slot2 = future_slot(2, 11)
        self.slot3 = future_slot(3, 10)
        self.slot4 = future_slot(4, 10)
        self.patient = Patient("P1", "Sara", MedicalRecord("MR1", "P1", "Private summary"))
        self.doctor = Doctor("D1", "Dr. Lina", [self.slot1, self.slot2, self.slot3, self.slot4], True)
        self.other_doctor = Doctor("D2", "Dr. Adam", [self.slot1], True)

    def test_view_available_slots(self):
        available = self.clinic.viewAvailableSlots(self.doctor, self.slot1.startAt.date())
        self.assertEqual(available, [self.slot1, self.slot2])

    def test_booking_starts_pending_and_reserves_slot(self):
        appointment = self.patient.bookAppointment(self.clinic, self.doctor, self.slot1)
        self.assertEqual(appointment.status, "Pending")
        self.assertNotIn(self.slot1, self.clinic.viewAvailableSlots(self.doctor, self.slot1.startAt.date()))

    def test_doctor_can_accept_request(self):
        appointment = self.patient.bookAppointment(self.clinic, self.doctor, self.slot1)
        result = self.doctor.reviewAppointment(self.clinic, appointment, True)
        self.assertEqual(result, "Accepted")

    def test_declined_slot_is_released(self):
        appointment = self.patient.bookAppointment(self.clinic, self.doctor, self.slot1)
        self.doctor.reviewAppointment(self.clinic, appointment, False)
        self.assertIn(self.slot1, self.clinic.viewAvailableSlots(self.doctor, self.slot1.startAt.date()))
        self.assertEqual(self.clinic.getUpcomingAppointmentCount(self.patient), 0)

    def test_patient_cannot_exceed_n(self):
        for slot in (self.slot1, self.slot2, self.slot3):
            self.patient.bookAppointment(self.clinic, self.doctor, slot)
        with self.assertRaisesRegex(BookingError, "Appointment limit reached"):
            self.patient.bookAppointment(self.clinic, self.doctor, self.slot4)

    def test_double_booking_same_doctor_slot_is_rejected(self):
        self.patient.bookAppointment(self.clinic, self.doctor, self.slot1)
        another = Patient("P2", "Omar", MedicalRecord("MR2", "P2", "Summary"))
        with self.assertRaisesRegex(BookingError, "no longer available"):
            another.bookAppointment(self.clinic, self.doctor, self.slot1)

    def test_only_assigned_doctor_can_review(self):
        appointment = self.patient.bookAppointment(self.clinic, self.doctor, self.slot1)
        with self.assertRaisesRegex(BookingError, "belongs to another doctor"):
            self.clinic.reviewAppointment(self.other_doctor, appointment, True)

    def test_unauthorized_doctor_cannot_read_medical_data(self):
        unauthorized = Doctor("D3", "Dr. No Access", [], authorizedStaff=False)
        with self.assertRaises(AuthorizationError):
            self.clinic.getPatientMedicalData(unauthorized, self.patient)

    def test_authorized_doctor_can_read_medical_data(self):
        self.assertEqual(self.clinic.getPatientMedicalData(self.doctor, self.patient), "Private summary")


if __name__ == "__main__":
    unittest.main()
