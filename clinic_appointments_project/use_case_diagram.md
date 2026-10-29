# Use Case Diagram (P3)

```mermaid
flowchart LR
    P([Patient])
    D([Doctor])

    subgraph ClinicAppointments["Clinic Appointment Booking System"]
        UC1["UC1: View doctor availability"]
        UC2["UC2: Request an appointment"]
        UC3["UC3: Review appointment request"]
        UC4["UC4: Enforce upcoming-appointment limit"]
        UC5["UC5: Record appointment decision"]
    end

    P --- UC1
    P --- UC2
    D --- UC3
    UC4 -.->|«extend»| UC2
    UC5 -.->|«extend»| UC3
```

**Review checks:** Patient and Doctor are outside the system boundary; the five use cases are inside it. UC4 is system behavior supporting a booking request, and UC5 records the result of a Doctor's decision. R5–R7 are quality constraints rather than standalone use cases.
