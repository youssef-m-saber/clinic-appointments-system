# 5. Sequence Diagram (P6)

```mermaid
sequenceDiagram
    actor Patient
    participant ClinicSystem
    participant Doctor
    participant Appointment

    Patient->>ClinicSystem: viewAvailableSlots(doctor, date)
    ClinicSystem->>Doctor: getAvailableSlots(date, appointments)
    Doctor-->>ClinicSystem: availableSlots
    ClinicSystem-->>Patient: availableSlots

    Patient->>Patient: bookAppointment(clinic, doctor, slot)
    Patient->>ClinicSystem: bookAppointment(patient, doctor, slot)
    ClinicSystem->>ClinicSystem: getUpcomingAppointmentCount(patient)

    alt slot is available and upcoming count is less than N
        ClinicSystem->>Appointment: create(appointmentId, patient, doctor, slot)
        Appointment-->>ClinicSystem: appointment
        ClinicSystem-->>Patient: Pending request
        Doctor->>Doctor: reviewAppointment(clinic, appointment, decision)
        Doctor->>ClinicSystem: reviewAppointment(doctor, appointment, decision)
        alt Doctor accepts
            ClinicSystem->>Appointment: accept()
            Appointment-->>ClinicSystem: Accepted
            ClinicSystem-->>Doctor: Accepted
            ClinicSystem-->>Patient: Accepted status
        else Doctor declines
            ClinicSystem->>Appointment: decline()
            Appointment-->>ClinicSystem: Declined
            ClinicSystem-->>Doctor: Declined
            ClinicSystem-->>Patient: Declined status; release slot
        end
    else slot unavailable or upcoming count is N
        ClinicSystem-->>Patient: Reject request with reason
    end
```

## Sequence review checklist

- Availability is shown before the Patient submits a booking request.
- The system checks the Patient's upcoming appointment count before creating a new appointment.
- The Doctor reviews a `Pending` request after the request is created.
- The `alt / else` branches show both Doctor decisions and the booking-precondition failure.
- Responses use dashed arrows, and the message names match methods in the class diagram and `main.py`.
