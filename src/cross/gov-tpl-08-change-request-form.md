---
id: GOV-TPL-08
title: Change Request Form
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.32
  - SOC 2 CC8.1
owner: Head of Engineering
approver: Information Security Manager
classification: Internal
review: Annual
summary: The form, or the field set for a change ticket, that records a change from request through assessment, approval, implementation and post-implementation review under GOV-PRO-09.
---
## 1. How to use this form

*One form per change. Where a change tracking system is used, its ticket must carry every field below and this form is the fallback. Fields marked with an asterisk are mandatory before approval. Attach test evidence and the rollback plan rather than summarising them. Record the completed form's reference in GOV-REG-11.*

## 2. Request

| Field | Entry |
|---|---|
| Change reference * | [Number] |
| Date raised * | [Date] |
| Requester (name and role) * | |
| Change type * | Standard / Normal / Emergency |
| Standard change catalogue entry, if Standard | |
| Title * | |
| Description of the change * | *State what will be different afterwards.* |
| Reason and expected benefit * | |
| Systems, services and components affected * | *Use the names in GOV-REG-24.* |
| Data classification touched * | Public / Internal / Confidential / Restricted |
| Security-relevant * | Yes / No, *per GOV-PRO-09 section 4.3* |
| Related references | *Incident, GOV-REG-14 finding, risk, project or supplier notice* |

## 3. Risk and impact assessment

| Field | Entry |
|---|---|
| Users or customers affected (number and type) * | |
| Expected downtime or degradation * | |
| Reversibility * | Easy / Possible with effort / Not reversible |
| Dependencies and other changes in the same window | |
| Security controls affected and how * | |
| Personal data processing changed | Yes / No, *refer to PIMS-PRO-06 if Yes* |
| Risk rating * | Low / Medium / High |
| Assessment completed by (role) | |

## 4. Test evidence

| Field | Entry |
|---|---|
| Test environment | |
| Test plan reference * | |
| Tests performed and results * | *Attach output and state pass or fail per test.* |
| Tester, not the implementer * | |
| Peer review of configuration or code (reference) * | |
| Residual issues accepted, and by whom | |

## 5. Rollback plan

| Field | Entry |
|---|---|
| Rollback trigger (success criteria not met by what time) * | |
| Rollback steps * | |
| Time needed to roll back * | |
| Backup or snapshot taken before the change (reference) * | |
| Rollback tested * | Yes / No |
| Person authorised to call rollback * | |

## 6. Communication and scheduling

| Field | Entry |
|---|---|
| Proposed window (start and end) * | |
| Within a published maintenance window | Yes / No |
| Who is notified, when and how | |
| Customer notice required by contract | Yes / No |
| Service desk briefed | Yes / No |

## 7. Approvals

*Approval authority follows the rating table in GOV-PRO-09 section 4.4. The approver is never the implementer.*

| Approver role | Name | Decision | Conditions | Date |
|---|---|---|---|---|
| System Owner | | Approved / Rejected / More information | | |
| Head of Engineering (Medium and High) | | | | |
| Information Security Manager (security-relevant) | | | | |
| Change advisory group (High) | | | | |

## 8. Implementation record

| Field | Entry |
|---|---|
| Implementer | |
| Actual start | |
| Actual end | |
| Steps followed as approved | Yes / No, *describe any deviation and who approved it* |
| Result | Successful / Rolled back / Partially implemented / Failed |
| Verification performed after the change | |
| Documentation updated (GOV-REG-24, GOV-REG-25, diagrams, runbooks) | |
| Emergency change: retrospective record completed within two working days | Yes / No / Not applicable |

## 9. Post-implementation review

| Field | Entry |
|---|---|
| Review date (within five working days for High and emergency) | |
| Reviewer (System Owner) | |
| Purpose achieved | Yes / Partly / No |
| Incidents or problems caused | |
| Lessons and process improvements | |
| Corrective action raised (GOV-REG-03 reference) | |
| Change closed in GOV-REG-11 on | [Date] |

## 10. Records and review

The completed form is a record under GOV-PRO-09, retained for at least three years and indexed in GOV-REG-11. This template is reviewed annually with GOV-PRO-09 and whenever the change tracking system changes. Changes to this template follow GOV-PRO-01.

## 11. Related documents

- GOV-PRO-09 Change management procedure
- GOV-REG-11 Change log
- GOV-REG-24 Software and hardware inventory
- GOV-REG-25 Data flow and interface inventory
- GOV-REG-14 Vulnerability register
- GOV-REG-03 Corrective action log
- PIMS-PRO-06 Privacy by design and by default procedure
