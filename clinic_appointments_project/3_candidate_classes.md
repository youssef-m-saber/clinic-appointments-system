# 3. Candidate Classes (P4)

The evidence column points to the exact requirement(s) that support considering each class. “Explicit” means the domain concept is named in the requirements; “Inferred” means the design needs the concept to make the stated behavior precise; “Rejected” means there is no sufficient evidence to include it in this scope.

| Class / candidate | Evidence | Classification | Reason |
|---|---|---|---|
| `Patient` | R1, R2, R4, R5 | Explicit | The requirements repeatedly identify the patient as the user who views availability, books, and is subject to the appointment limit. |
| `Doctor` | R1, R3 | Explicit | The patient views a doctor's availability and the doctor makes the accept/decline decision. |
| `Appointment` | R2, R3, R4 | Explicit | The requirements name appointments and appointment requests, and R4 limits upcoming appointments. One class models the request lifecycle and its final decision. |
| `TimeSlot` | R1, R2 | Inferred | Days and times must be represented as selectable values, checked against the doctor's availability, and reserved while a request is pending or accepted. |
| `MedicalRecord` | R5 | Inferred | Patient medical data needs a clear object boundary so access can be guarded. This teaching model stores a small summary only, not real clinical records. |
| `ClinicSystem` | R2, R3, R4, R5 | Inferred | A coordinating class is needed to check slot availability, enforce N, create requests, record decisions, and guard medical-data access. |
| `Payment` | None | Rejected | The requirements say nothing about charging or payment. |
| `Prescription` | None | Rejected | The requirements do not request prescriptions or treatment management. |
| `Receptionist` / `NotificationService` | None | Rejected | Neither is a required actor or a separately specified feature. The system simply returns the updated status to its caller. |

## Design decisions

- `Appointment` represents the entire lifecycle: Pending → Accepted or Declined. This avoids duplicating the same booking as both an Appointment and an AppointmentRequest class.
- A `TimeSlot` is uniquely identified by its start date/time in this small model. The system treats Pending and Accepted appointments as reservations.
- `MedicalRecord` and the Doctor's `authorizedStaff` flag demonstrate the R5 access check. They do **not** constitute real authentication or a production security mechanism.
