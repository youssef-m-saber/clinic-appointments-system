# Clinic Appointments — Team Project

An educational Doctor Appointment Booking System based strictly on the supplied `TASK Updated(1).md` requirements and workflow instructions.

## Requirements and selected N

The original R1–R7 wording is preserved in `1_requirements.md` and `requirements.txt`. The team-selected value is **N = 3 upcoming appointments per patient**. Confirm that all team members agree on this choice and keep N consistent in the documents, `main.py`, and tests.

For counting, future `Pending` and `Accepted` appointments count toward N; `Declined` appointments do not. This interpretation prevents a patient from creating several pending requests beyond the limit.

## Team members and collaboration status

| Student ID | Name | Branch | Pull Request |
|---|---|---|---|
| 20240377 | Omar Abdelsamad Hassan | Pending | Pending |
| 20240708 | Youssef Mohamed Saber | youssef | https://github.com/youssef-m-saber/clinic-appointments-system/pull/1 |
| 20240815 | Ahmed Eltaher Bakry | Pending | Pending |
| 20240814 | Abdelrahman Yasser Adel | Abdelrahman | Pending |

**N:** 3

Conflict Drill: Youssef Mohamed Saber

## Required deliverables

- `1_requirements.md` — P1 classification, original R1–R7 wording and N decision.
- `2_use_cases.md` — use-case table, flows and Mermaid use case diagram.
- `3_candidate_classes.md` — evidence and Explicit/Inferred/Rejected decisions.
- `4_class_diagram.md` — Mermaid class diagram.
- `5_sequence_diagram.md` — Mermaid sequence diagram with `alt / else`.
- `main.py` — runnable Python implementation.
- `6_ai_journal.md` — review checklist, actual run output and team review table.

The additional filenames requested in the task are also included: `requirements.txt`, `use_cases.md`, `use_case_diagram.md`, `class_diagram.md`, and `sequence_diagram.md`. The Dockerfile is not included because it is only required for a team of five; the supplied task says teams of 2–4 can ignore Docker.

## Run locally

Requires Python 3.10+ and no external packages.

```bash
python main.py
python -m unittest -v
```

## Current validation result

- `python main.py`: exit code 0.
- Unit tests: exit code 0.
- Tests run: 9.

The CI workflow in `.github/workflows/check.yml` runs the application and unit tests on pushes and pull requests. GitHub Actions does not automatically prove the diagrams are logically correct, so the team must inspect the rendered diagrams as well.

## Important scope limitations

- This is a command-line in-memory teaching demo; data resets each run.
- R5 is demonstrated with a simple `authorizedStaff` flag. There is no real login, database permission system, encryption, or audit logging.
- R6's 2-second target has not been load-tested in a production-like environment.
- R7 is a design constraint for a future responsive mobile interface; this command-line demo does not provide a mobile UI.

## Team GitHub workflow

1. Create a new public GitHub repository and set its visibility to Public. The teaching assistant confirmed that no template or board is available, so upload these project files to the new repository.
2. Invite each teammate as a collaborator.
3. Each member updates the `Conflict Drill` line on their own branch and opens a PR.
4. Review another member's PR with a specific, useful comment.
5. Merge the first PR, resolve the intentional conflict in the next PR while preserving every name, and repeat until all members' PRs are merged.
6. Each member then contributes their assigned deliverable on their own branch and through a PR.
7. Check the Actions tab and confirm the check is green.

**Before submission:** replace the pending branch/PR entries with the real values, complete and verify the Conflict Drill, verify the selected N, check the diagrams on GitHub, repeat the program/tests after any changes, and add only AI mistakes that the team actually observed.


