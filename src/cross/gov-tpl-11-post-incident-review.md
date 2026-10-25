---
id: GOV-TPL-11
title: Post-Incident Review Template
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.27
  - ISO/IEC 27001:2022 clause 10.1
  - SOC 2 CC7.5
  - SOC 2 CC4.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The structured review held within ten working days of closing a significant incident, recording the timeline, what worked, what did not, the root cause, the measured response times and the actions that follow.
---
## 1. How to use this template

*The Incident Lead chairs the review within ten working days of closure for every Severity 1 and Severity 2 incident, and for any Severity 3 incident selected under GOV-PRO-07 step 4.11. Invite the technical lead, the system owner, the Privacy Officer where personal data was involved, and anyone whose decision appears in the timeline. The purpose is to improve controls, not to assign blame; write what the organisation will change, not who was at fault. Complete sections 2 to 5 before the meeting from GOV-TPL-05, and sections 6 to 11 during and after it.*

## 2. Review details

| Field | Entry |
|---|---|
| Incident reference | [Prefix]-[Year]-[Number] |
| Incident type and severity | |
| Date closed | [Date] |
| Date of review | [Date] |
| Held within ten working days of closure | Yes / No. *If no, state the reason.* |
| Chair | Incident Lead, [Role] |
| Attendees | [Roles] |
| Personal data breach | Yes / No. *If yes, PIMS-REG-03 reference.* |

## 3. Summary of the incident

*Three to five sentences a reader outside the response team can follow: what happened, how it was found, what the impact was, how it was resolved.*

## 4. Timeline

*Copy the agreed timeline from GOV-TPL-05 and mark where time was lost. The phase column lets the review see how long each stage took.*

| Date and time | Event | Phase | Delay or gap noted |
|---|---|---|---|
| | | Occurrence | |
| | | Detection | |
| | | Reporting | |
| | | Triage | |
| | | Containment | |
| | | Eradication | |
| | | Recovery | |
| | | Notification | |
| | | Closure | |

## 5. Metrics

*Targets come from GOV-PRO-07 step 4.3 for the severity assigned. Record the value in hours, or in days for the review itself.*

| Metric | Measured from and to | Value | Target | Met (Yes / No) |
|---|---|---|---|---|
| Time to detect | Occurrence to detection | | | |
| Time to report | Detection to report | | One hour | |
| Time to triage | Report to severity assigned | | One hour | |
| Time to contain | Detection to containment | | | |
| Time to recover | Detection to service restored | | Recovery time objective | |
| Time to notify authority (if required) | Awareness to notification | | 72 hours | |
| Time to notify clients (if required) | Awareness to notification | | Contract | |
| Review held | Closure to review | | Ten working days | |

## 6. What worked

*List the controls, decisions and people that limited the impact. These are candidates for positive observations in the next internal audit and for keeping when budgets are reviewed.*

- 
- 
- 

## 7. What did not work

*List the control failures, delays, missing information and decisions that would be made differently. Be specific: "the alert fired but was routed to an unmonitored mailbox" rather than "monitoring was weak".*

- 
- 
- 

## 8. Root cause analysis

| Field | Entry |
|---|---|
| Method used | Five whys / Cause and effect diagram / Other |
| Direct cause | *The technical or human action that produced the incident.* |
| Contributing causes | *Conditions that made it possible or made it worse.* |
| Root cause | *The underlying reason the direct cause could occur, usually a missing, weak or unfollowed control.* |
| Why existing controls did not prevent it | |
| Why existing controls did not detect it sooner | |
| Was the risk in GOV-REG-05 before the incident | Yes, rated [Band] / No |

## 9. Actions

*Every action needs an owner and a date and is raised in GOV-REG-03 under GOV-PRO-04 so that it is tracked to closure and its effectiveness verified. Corrections fix this incident; corrective actions remove the root cause; improvements reduce impact or response time.*

| Action | Type | Owner | Due | GOV-REG-03 reference |
|---|---|---|---|---|
| | Correction / Corrective action / Improvement | [Role] | [Date] | |
| | | | | |
| | | | | |
| | | | | |

## 10. Updates required

| Record or document | Update needed (Yes / No) | Owner | Done |
|---|---|---|---|
| GOV-REG-05 Information security risk register | | | |
| ISMS-REG-01 Statement of Applicability or control status | | | |
| GOV-REG-07 Supplier register | | | |
| GOV-REG-14 Vulnerability register | | | |
| Policies or procedures (name them) | | | |
| Awareness content under GOV-PRO-08 | | | |
| Monitoring rules under GOV-PRO-14 | | | |
| Continuity plans under GOV-PRO-13 | | | |

## 11. Sign-off

| Role | Confirmation | Date |
|---|---|---|
| Incident Lead | Review complete and actions raised | [Date] |
| Information Security Manager | Actions accepted into GOV-REG-03 | [Date] |
| Privacy Officer (where personal data involved) | Breach record complete | [Date] |
| Executive sponsor (Severity 1) | Reviewed | [Date] |
