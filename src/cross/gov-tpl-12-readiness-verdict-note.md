---
id: GOV-TPL-12
title: Readiness Verdict Note
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 8.1
  - ISO/IEC 27001:2022 Annex A 5.8
  - ISO/IEC 27001:2022 Annex A 8.32
  - SOC 2 CC8.1
  - GDPR Article 25
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The one page record that closes a go-live security and privacy gate, stating the verdict, the reasons, what was verified, what remains open and who signed.
---
## 1. How to use this note

*The reviewer writes this note at the end of the gate described in PB-07, after the GOV-REG-29 checklist for the system is complete. Keep it to one page. A reader who sees nothing else must understand whether the system may go to production, under what conditions, and what evidence the verdict rests on. File it in the evidence folder and reference it in GOV-REG-11 against the go-live change.*

## 2. Project and environment

| Field | Entry |
|---|---|
| Project or system | [System name] |
| Environment reviewed | Production / Pre-production configured identically to production |
| Review reference | [Reference] |
| Checklist used | GOV-REG-29 copy dated [Date] |
| Evidence folder | [Location] |
| Submitting team lead | [Role] |
| Reviewer | [Role] |
| Review period | [Date] to [Date] |
| Planned go-live | [Date] |

## 3. Verdict

*Select one. The decision table in PB-07 section 7 determines which applies.*

| Verdict | Meaning | Selected |
|---|---|---|
| Approved | Every blocker is Verified and every other check is Verified or agreed Not applicable. Production use may begin. | |
| Approved with conditions | Every blocker is Verified. One or more non-blocking checks are To confirm or Not implemented, each with an owner, a ticket and a due date within [Number] days. Production use may begin and the conditions are tracked in GOV-REG-03. | |
| Stop | At least one blocker is not Verified, or a blocker was marked Not applicable without the reviewer's agreement. Production use may not begin until the blocker is Verified and this note is reissued. | |

## 4. Reasons

*Three to six sentences. State the facts that drove the verdict and cite the evidence references from GOV-REG-29. Name any open blocker.*

1. 
2. 
3. 

## 5. Verified areas

| Area | Status | Evidence reference | Note |
|---|---|---|---|
| Scope and residency | Verified / To confirm / Not implemented / Not applicable | | |
| External processing | | | |
| Data flow | | | |
| Access | | | |
| Network | | | |
| Encryption | | | |
| Logging | | | |
| Backups | | | |
| Contractual | | | |
| Privacy | | | |

## 6. Open items

*Every check that is not Verified. An open blocker means the verdict is Stop.*

| GOV-REG-29 row | Blocker | Owner | Due | Condition for production use | GOV-REG-03 reference |
|---|---|---|---|---|---|
| | Yes / No | [Role] | [Date] | | |
| | | | | | |
| | | | | | |

## 7. Access list reference

*The reviewer used read-only accounts to verify the evidence. Record where the list of those accounts is held and confirm their removal, so that the gate itself leaves no standing access behind.*

| Field | Entry |
|---|---|
| Access list location | [Location] |
| Accounts used by the reviewer | [Number] |
| All reviewer access removed on | [Date], confirmed by [Role] |

## 8. Signatures

| Role | Statement | Name and date |
|---|---|---|
| Reviewer | The checks were verified as recorded and the verdict follows the decision table. | [Name], [Date] |
| Submitting team lead (Head of Engineering or delegate) | The evidence submitted is complete and accurate and the open items are accepted with their dates. | [Name], [Date] |
| Information Security Manager | The verdict is accepted and the conditions are entered in GOV-REG-03. | [Name], [Date] |
| Privacy Officer (where personal data is processed) | The privacy checks are verified. | [Name], [Date] |
| System owner | The residual risk recorded in GOV-REG-05 is accepted. | [Name], [Date] |
