# 4. Class Diagram (P5)

```mermaid
classDiagram
    class Patient {
        +String patientId
        +String name
        +MedicalRecord medicalRecord
        +bookAppointment(ClinicSystem, Doctor, TimeSlot) Appointment
    }

    class Doctor {
        +String doctorId
        +String name
        +Boolean authorizedStaff
        +List~TimeSlot~ availableSlots
        +getAvailableSlots(Date, List~Appointment~) List~TimeSlot~
        +reviewAppointment(ClinicSystem, Appointment, Boolean) String
    }

    class TimeSlot {
        +DateTime startAt
        +toString() String
    }

    class Appointment {
        +String appointmentId
        +TimeSlot slot
        +String status
        +create(String, Patient, Doctor, TimeSlot) Appointment
        +accept() String
        +decline() String
        +isUpcoming(DateTime) Boolean
    }

    class MedicalRecord {
        +String recordId
        +String patientId
        +String summary
    }

    class ClinicSystem {
        +Integer maxUpcomingAppointments
        +List~Appointment~ appointments
        +viewAvailableSlots(Doctor, Date) List~TimeSlot~
        +bookAppointment(Patient, Doctor, TimeSlot) Appointment
        +reviewAppointment(Doctor, Appointment, Boolean) String
        +getUpcomingAppointmentCount(Patient) Integer
        +getPatientMedicalData(Doctor, Patient) String
    }

    Patient "1" *-- "1" MedicalRecord : owns
    Patient "1" -- "0..*" Appointment : requests
    Doctor "1" -- "0..*" Appointment : reviews
    Doctor "1" o-- "0..*" TimeSlot : offers
    Appointment "0..*" --> "1" TimeSlot : requested for
    ClinicSystem "1" *-- "0..*" Appointment : manages
```

## Consistency checklist

- Every relationship includes multiplicity.
- One appointment belongs to exactly one Patient, one Doctor, and one TimeSlot.
- One Patient and one Doctor can each be related to many appointments.
- A pending or accepted appointment reserves its TimeSlot; a declined appointment releases it.
- `ClinicSystem` owns the booking rules, including the configured N and medical-data access check.
- Methods used in the sequence diagram have matching names and responsibilities here.
