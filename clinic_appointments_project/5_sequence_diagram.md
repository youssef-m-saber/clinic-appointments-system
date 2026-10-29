
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

    Patient->>ClinicSystem: bookAppointment(patient, doctor, slot)
    ClinicSystem->>ClinicSystem: getUpcomingAppointmentCount(patient)

    alt Slot is available and count is less than N
        ClinicSystem->>Appointment: create(appointmentId, patient, doctor, slot)
        Appointment-->>ClinicSystem: appointment
        ClinicSystem-->>Patient: Pending request
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
    else Slot unavailable or upcoming count is N
        ClinicSystem-->>Patient: Reject request with reason
    end
```
