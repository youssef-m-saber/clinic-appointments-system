# 6. AI Journal — Review and Validation Record

> **Team action required:** This is an initial draft record. Each teammate must personally review the artifacts and add what they actually checked. Do not invent AI mistakes or claim a manual check that did not happen. If the team finds no mistake in a pass, record that honestly.

## P1 — Requirements classification

**Draft made:** R1–R4 classified as Functional; R5–R7 classified as Non-functional. The original requirement wording and IDs are retained.

**Checks to complete as a team:**
- [ ] Compare each R1–R7 line against the supplied task file.
- [x] Set the draft value to `N = 3` and checked that the requirements, use cases, diagrams, implementation, tests, and README use the same value. The full team should still agree on this value before submission.
- [ ] Confirm everyone understands why R5 is a security quality constraint and R6/R7 are performance/usability constraints.

**Observed AI mistake:** None recorded yet. Add an entry only if review reveals a concrete error.

## P2–P3 — Use cases and diagram

**Draft made:** Patient interacts with viewing availability and requesting an appointment; Doctor reviews the request. System behavior covers the N limit and recording the Doctor's decision.

**Checks to complete:**
- [ ] Confirm Patient and Doctor are the only external actors.
- [ ] Check the alternative flow covers a missing/unavailable slot or a Patient at the N limit.
- [ ] Open `use_case_diagram.md` and confirm GitHub renders the Mermaid diagram.
- [ ] Confirm the five diagram use cases match the table in `2_use_cases.md` / `use_cases.md`.

**Observed AI mistake:** None recorded yet. Add a specific quote/behavior, explanation, and how it was detected if a real mistake is found.

## P4–P6 — Candidate classes and diagrams

**Draft made:** Patient, Doctor, and Appointment are Explicit; TimeSlot, MedicalRecord, and ClinicSystem are Inferred. Payment and prescription features are excluded due to no requirement evidence.

**Checks to complete:**
- [ ] Confirm each class has requirement evidence.
- [ ] Check multiplicities and associations in `4_class_diagram.md` / `class_diagram.md`.
- [ ] Confirm `Pending` appointments reserve a slot, and `Declined` appointments release it.
- [ ] Check the sequence order: availability → booking validation → Pending request → Doctor decision.
- [ ] Confirm the `alt / else` branches and method names match `main.py`.
- [ ] Open the diagrams on GitHub and confirm they render.

**Observed AI mistake:** None recorded yet. Do not convert a design choice or a team change into an “AI mistake” unless there was a demonstrably incorrect AI output.

## P7 — Code and tests

**Automated checks performed while preparing this draft:** `python main.py` and `python -m unittest -v` were run in the working environment. The output from the actual run is pasted below. The team must repeat these checks after any later edits.

**Team checks to complete:**
- [ ] Run `python main.py` locally.
- [ ] Run `python -m unittest -v` locally.
- [ ] Explain to a teammate how R4 is enforced and how R5 is represented in this educational demo.
- [ ] Confirm the output below matches the team's own final run; replace it if any code was changed.

## Output of `python main.py`

```text
Doctor availability for 2026-10-30:
  2026-10-30 10:00
  2026-10-30 11:00
A001: Pending for Sara at 2026-10-30 10:00
Doctor decision: Accepted
A002: Pending for Omar at 2026-10-30 11:00
Doctor decision: Declined
A002 declined; its slot is available again: True
Sara's upcoming appointment count: 1 / 3
Authorized medical-data access: Demo medical summary
```

## Unit-test result

```text
test_authorized_doctor_can_read_medical_data (test_main.ClinicSystemTests.test_authorized_doctor_can_read_medical_data) ... ok
test_booking_starts_pending_and_reserves_slot (test_main.ClinicSystemTests.test_booking_starts_pending_and_reserves_slot) ... ok
test_declined_slot_is_released (test_main.ClinicSystemTests.test_declined_slot_is_released) ... ok
test_doctor_can_accept_request (test_main.ClinicSystemTests.test_doctor_can_accept_request) ... ok
test_double_booking_same_doctor_slot_is_rejected (test_main.ClinicSystemTests.test_double_booking_same_doctor_slot_is_rejected) ... ok
test_only_assigned_doctor_can_review (test_main.ClinicSystemTests.test_only_assigned_doctor_can_review) ... ok
test_patient_cannot_exceed_n (test_main.ClinicSystemTests.test_patient_cannot_exceed_n) ... ok
test_unauthorized_doctor_cannot_read_medical_data (test_main.ClinicSystemTests.test_unauthorized_doctor_cannot_read_medical_data) ... ok
test_view_available_slots (test_main.ClinicSystemTests.test_view_available_slots) ... ok

----------------------------------------------------------------------
Ran 9 tests in 0.001s

OK
```

## Team collaboration record

| Teammate | Student ID | Artifact reviewed | Real review comment left on a teammate's PR? | PR link |
|---|---|---|---|---|
| Omar Abdelsamad Hassan | 20240377 | Pending | Pending | Pending |
| Youssef Mohamed Saber | 20240708 | Pending | Pending | Pending |
| Ahmed Eltaher Bakry | 20240815 | Pending | Pending | Pending |
| Abdelrahman Yasser Adel | 20240814 | Pending | Pending | Pending |
