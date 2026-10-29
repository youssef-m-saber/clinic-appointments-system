# 1. Requirements (P1)

**Chosen value: `N = 3` upcoming appointments per patient.** The task asks the team to choose and document `N`; this is a team choice, not a value copied from the supplied task. If your instructor assigned a different value on the board, replace `3` consistently in this document, `README.md`, `main.py`, and the tests.

| ID | Requirement (original wording) | Type | Category | Design implication |
|---|---|---|---|---|
| R1 | A patient can view the days and times when a doctor is available. | Functional | Availability | The system must list a doctor's future available slots for a requested date. |
| R2 | A patient can book an appointment during an available time slot. | Functional | Booking | A booking request can be created only for a real, future, unreserved slot. |
| R3 | A doctor can accept or decline an appointment request. | Functional | Decision handling | A pending request can transition to Accepted or Declined by its assigned doctor. |
| R4 | A patient can have at most **N** upcoming appointments at any given time. | Functional | Booking rule | Count future Pending and Accepted appointments before accepting a new request; reject a request when the count is already N. |
| R5 | Patient medical data shall be accessible only to authorized staff. | Non-functional | Security | Medical-data access must be checked against an authorization flag in this teaching model. |
| R6 | Available appointment times shall be displayed within 2 seconds. | Non-functional | Performance | Availability retrieval should be lightweight; a production deployment would need performance measurement under representative load. |
| R7 | The application shall be usable on mobile phone screens. | Non-functional | Usability | A production UI should be responsive. This project's command-line demo does not implement a mobile UI. |

## Classification notes

- R1–R4 describe user-visible capabilities or a domain rule, so they are classified as functional requirements.
- R5 is a security quality constraint, R6 is a performance constraint, and R7 is a usability constraint, so they are classified as non-functional requirements.
- R4's `N` is documented as `3` for this draft. It is a business rule checked when booking, not a new feature unrelated to the stated requirements.

## Scope boundaries

The supplied task names only `Patient` and `Doctor` as actors. This draft does not add receptionist, payment, insurance, prescription, or notification-service actors/features. The example code is a small in-memory model for demonstrating the requirements and diagrams; it is not a production clinical system.
