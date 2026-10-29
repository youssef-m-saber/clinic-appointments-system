"""Small in-memory Clinic Appointment Booking System demo.

This intentionally demonstrates the class and sequence diagrams rather than
providing a production booking application. It uses only Python's standard library.
"""
from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime, timedelta
from typing import List

MAX_UPCOMING_APPOINTMENTS = 3  # N selected by the team; keep README/docs/tests in sync.
ACTIVE_STATUSES = {"Pending", "Accepted"}


class BookingError(ValueError):
    """Raised when a booking request violates a stated booking rule."""


class AuthorizationError(PermissionError):
    """Raised when a doctor is not authorized to access medical data."""


@dataclass(frozen=True, order=True)
class TimeSlot:
    startAt: datetime

    def toString(self) -> str:
        return self.startAt.strftime("%Y-%m-%d %H:%M")

    def __str__(self) -> str:
        return self.toString()


@dataclass
class MedicalRecord:
    recordId: str
    patientId: str
    summary: str


@dataclass
class Patient:
    patientId: str
    name: str
    medicalRecord: MedicalRecord

    def bookAppointment(self, clinic: "ClinicSystem", doctor: "Doctor", slot: TimeSlot) -> "Appointment":
        return clinic.bookAppointment(self, doctor, slot)


@dataclass
class Doctor:
    doctorId: str
    name: str
    availableSlots: List[TimeSlot]
    authorizedStaff: bool = False

    def getAvailableSlots(self, requestedDate: date, appointments: List["Appointment"]) -> List[TimeSlot]:
        now = datetime.now()
        reserved = {
            appointment.slot
            for appointment in appointments
            if appointment.doctor.doctorId == self.doctorId
            and appointment.status in ACTIVE_STATUSES
        }
        return sorted(
            slot
            for slot in self.availableSlots
            if slot.startAt.date() == requestedDate
            and slot.startAt > now
            and slot not in reserved
        )

    def reviewAppointment(
        self, clinic: "ClinicSystem", appointment: "Appointment", accepted: bool
    ) -> str:
        return clinic.reviewAppointment(self, appointment, accepted)


@dataclass
class Appointment:
    appointmentId: str
    patient: Patient
    doctor: Doctor
    slot: TimeSlot
    status: str = "Pending"

    @classmethod
    def create(cls, appointmentId: str, patient: Patient, doctor: Doctor, slot: TimeSlot) -> "Appointment":
        return cls(appointmentId=appointmentId, patient=patient, doctor=doctor, slot=slot, status="Pending")

    def accept(self) -> str:
        if self.status != "Pending":
            raise BookingError("Only a Pending appointment can be accepted.")
        self.status = "Accepted"
        return self.status

    def decline(self) -> str:
        if self.status != "Pending":
            raise BookingError("Only a Pending appointment can be declined.")
        self.status = "Declined"
        return self.status

    def isUpcoming(self, now: datetime | None = None) -> bool:
        current_time = now or datetime.now()
        return self.slot.startAt > current_time and self.status in ACTIVE_STATUSES


class ClinicSystem:
    def __init__(self, maxUpcomingAppointments: int = MAX_UPCOMING_APPOINTMENTS) -> None:
        if maxUpcomingAppointments < 1:
            raise ValueError("maxUpcomingAppointments must be at least 1.")
        self.maxUpcomingAppointments = maxUpcomingAppointments
        self.appointments: List[Appointment] = []
        self._nextAppointmentNumber = 1

    def viewAvailableSlots(self, doctor: Doctor, requestedDate: date) -> List[TimeSlot]:
        return doctor.getAvailableSlots(requestedDate, self.appointments)

    def getUpcomingAppointmentCount(self, patient: Patient, now: datetime | None = None) -> int:
        current_time = now or datetime.now()
        return sum(
            1
            for appointment in self.appointments
            if appointment.patient.patientId == patient.patientId
            and appointment.isUpcoming(current_time)
        )

    def bookAppointment(self, patient: Patient, doctor: Doctor, slot: TimeSlot) -> Appointment:
        now = datetime.now()
        if slot.startAt <= now:
            raise BookingError("The selected time slot must be in the future.")
        if slot not in doctor.availableSlots:
            raise BookingError("The selected slot is not offered by this doctor.")
        if slot not in self.viewAvailableSlots(doctor, slot.startAt.date()):
            raise BookingError("The selected slot is no longer available.")
        current_count = self.getUpcomingAppointmentCount(patient, now)
        if current_count >= self.maxUpcomingAppointments:
            raise BookingError(
                f"Appointment limit reached: a patient may have at most "
                f"{self.maxUpcomingAppointments} upcoming appointments."
            )

        appointment = Appointment.create(
            appointmentId=f"A{self._nextAppointmentNumber:03d}",
            patient=patient,
            doctor=doctor,
            slot=slot,
        )
        self._nextAppointmentNumber += 1
        self.appointments.append(appointment)
        return appointment

    def reviewAppointment(self, doctor: Doctor, appointment: Appointment, accepted: bool) -> str:
        if appointment.doctor.doctorId != doctor.doctorId:
            raise BookingError("This appointment request belongs to another doctor.")
        if appointment.status != "Pending":
            raise BookingError("Only a Pending appointment request can be reviewed.")
        return appointment.accept() if accepted else appointment.decline()

    def getPatientMedicalData(self, doctor: Doctor, patient: Patient) -> str:
        if not doctor.authorizedStaff:
            raise AuthorizationError("Access denied: doctor is not authorized staff.")
        return patient.medicalRecord.summary


def _future_slot(days_ahead: int, hour: int) -> TimeSlot:
    target_date = (datetime.now() + timedelta(days=days_ahead)).date()
    return TimeSlot(datetime.combine(target_date, datetime.min.time()).replace(hour=hour))


def main() -> None:
    clinic = ClinicSystem()
    tomorrow_10 = _future_slot(1, 10)
    tomorrow_11 = _future_slot(1, 11)
    doctor = Doctor(
        doctorId="D01",
        name="Dr. Lina",
        availableSlots=[tomorrow_10, tomorrow_11],
        authorizedStaff=True,
    )
    patient = Patient(
        patientId="P01",
        name="Sara",
        medicalRecord=MedicalRecord("MR01", "P01", "Demo medical summary"),
    )
    other_patient = Patient(
        patientId="P02",
        name="Omar",
        medicalRecord=MedicalRecord("MR02", "P02", "Demo medical summary"),
    )

    print(f"Doctor availability for {tomorrow_10.startAt.date()}:")
    for available_slot in clinic.viewAvailableSlots(doctor, tomorrow_10.startAt.date()):
        print(f"  {available_slot}")

    first = patient.bookAppointment(clinic, doctor, tomorrow_10)
    print(f"{first.appointmentId}: {first.status} for {patient.name} at {first.slot}")
    print(f"Doctor decision: {doctor.reviewAppointment(clinic, first, accepted=True)}")

    second = other_patient.bookAppointment(clinic, doctor, tomorrow_11)
    print(f"{second.appointmentId}: {second.status} for {other_patient.name} at {second.slot}")
    print(f"Doctor decision: {doctor.reviewAppointment(clinic, second, accepted=False)}")
    print(f"{second.appointmentId} declined; its slot is available again: "
          f"{tomorrow_11 in clinic.viewAvailableSlots(doctor, tomorrow_11.startAt.date())}")

    print(f"{patient.name}'s upcoming appointment count: "
          f"{clinic.getUpcomingAppointmentCount(patient)} / {clinic.maxUpcomingAppointments}")
    print(f"Authorized medical-data access: {clinic.getPatientMedicalData(doctor, patient)}")


if __name__ == "__main__":
    main()
