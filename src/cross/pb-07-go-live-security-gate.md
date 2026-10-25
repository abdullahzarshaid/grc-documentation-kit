---
id: PB-07
title: "Playbook: The Go-Live Security and Privacy Gate for a Software Project"
type: playbook
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
summary: How to run a short, evidence-based gate before a new system or major release goes to production, so that what the management system promises is true of the system being launched.
---
## 1. Why a gate exists even in a certified organisation

A management system describes how the organisation works. A project is where the organisation does something new. Between the two there is drift. The certificate says that a set of controls exists and was sampled; it does not say that the system your team built last quarter has multi-factor authentication on its administrative console, or that its backups have ever been restored. Projects are built under deadline pressure by people who did not write the policies. Cloud defaults are permissive. Items marked "after launch" are forgotten once launch happens. Internal audit samples after the fact, so by the time it looks, the system has carried real data for months with the gap in place.

The gate is the point where the control set meets the new system before it carries real data, real users and real contractual promises. It is also the cheapest moment to fix anything, because nothing depends on the system yet.

A gate is short. The submitting team spends one to two days spread over two weeks; the reviewer spends two to three days. If a gate takes longer than that, either the project is not ready or the checklist has grown beyond the must-prove areas. Resist adding checks. Everything that is not a must-prove item belongs in the secure development lifecycle under GOV-PRO-15, where it is cheaper to catch.

## 2. The two-step model: the team submits, compliance verifies

The gate has two steps and two parties. The project team knows the system; the reviewer is independent of it. Neither does the other's job.

**Step 1, submission.** Two weeks before the planned go-live, the project lead receives a copy of GOV-REG-29 for the system. For each of the 30 checks the team sets a status, writes an evidence reference that points to a file in the evidence folder (built as PB-09 describes), and names an owner. The team may set three statuses: To confirm (evidence attached, awaiting verification), Not implemented (the control is absent and a ticket exists) or Not applicable (with the reason in Notes). The team never sets Verified. Verified is the reviewer's word.

**Step 2, verification.** The reviewer, normally the Information Security Manager or a delegate who has not worked on the project, opens every evidence reference and, wherever possible, observes the control directly using a read-only account provisioned for the gate. The reviewer sets each row to Verified, leaves it at To confirm with a note saying exactly what evidence would suffice, sets it to Not implemented, or agrees Not applicable. The reviewer never fixes anything. A reviewer who configures a setting to make a check pass has stopped being a reviewer.

**Blockers first.** The order of work follows the Blocker column, in both steps. The team completes the 22 blocking checks before the 8 others. The reviewer opens the blockers on the day of submission and tells the project lead the same day if any blocker is Not implemented or has no evidence. Nobody waits until the end of the review to learn that go-live is at risk.

## 3. The must-prove areas

GOV-REG-29 groups its checks into ten areas. Each area has a question the reviewer must be able to answer with evidence, not with a conversation.

| Area | What must be shown | Where it is recorded |
|---|---|---|
| Scope and residency | The exact accounts, subscriptions or tenants that make up the system, the regions where data rests and is processed, and that these match what clients and privacy notices were told | GOV-REG-10, ISMS-STM-01, GOV-REG-04 |
| External processing | Every third party that receives data from the system, including analytics, email, error reporting, support, payment and AI services, each approved for its tier with a contract that permits the use | GOV-REG-07, PIMS-REG-06, AI-REG-01 |
| Data flow | A current diagram of stores, interfaces and endpoints with a classification per flow, and test environments that hold no production personal data | GOV-REG-25, GDPR-REG-02 |
| Access | Named accounts through the central identity provider, multi-factor authentication on every administrative path, an approved administrator list, a link to the leaver process and a first access review scheduled | GOV-REG-13, GOV-REG-12, GOV-PRO-10 |
| Network | The complete list of internet-facing endpoints, each intended and authenticated, with management interfaces and data stores unreachable from the internet | GOV-CHK-02, GOV-PRO-21 |
| Encryption | Current transport protocols, encryption at rest on every store including backups and snapshots, and keys and secrets held in a managed vault and absent from code | GOV-REG-18, GOV-PRO-20 |
| Logging | Authentication, privilege use, administrative actions, changes and restricted data access logged to a central store the system's administrators cannot alter, with alerts tested | GOV-PRO-14 |
| Backups | Backups configured at the agreed frequency in a separate account or location, a restore performed within the last 90 days, and recovery objectives the configuration meets | GOV-REG-15, GOV-TPL-07 |
| Contractual | The security and availability commitments made to clients for this system, each mapped to a control, plus licence compliance and supplier service levels | GOV-REG-04, GOV-REG-24 |
| Privacy | A completed impact assessment or a screening record showing none is needed, a processing inventory entry, an accurate notice, configured retention and the ability to fulfil rights requests | PIMS-REG-08, PIMS-REG-01, PIMS-REG-07 |

## 4. Status vocabulary

The gate uses four statuses and no others. "In progress", "Partially" and "Planned" are not statuses: a partially implemented control is Not implemented with a note.

| Status | Definition | Who may set it |
|---|---|---|
| Verified | The reviewer saw the control operating in the named environment on the recorded date, and the evidence reference points to proof that would satisfy an auditor without the reviewer present | Reviewer only |
| To confirm | Evidence is missing or insufficient. The row has an owner and a due date. It is an unknown, not a gap | Team or reviewer |
| Not implemented | The control is absent, shown by evidence of its absence, with a ticket, an owner and a due date | Team or reviewer |
| Not applicable | The check does not apply to this system, the reason is written in Notes, and the reviewer has agreed. On a blocking check the reviewer's agreement is written in Notes as well | Team proposes, reviewer agrees |

An unknown on a blocker is treated as a gap when the verdict is decided. That rule is what keeps To confirm honest: it is a work item with a date, not a place to park an awkward question.

## 5. The gap evidence rule

A screenshot of the absence plus a ticket is a valid answer.

The gate measures truth, not perfection. A team that shows the reviewer the backup configuration page with no schedule on it, together with a ticket that names an owner and a date, has given a complete and honest answer. The reviewer marks the row Not implemented and moves to the next check. The review is not blocked by the gap; production use is blocked, if the check is a blocker. Those are different things, and keeping them separate is what makes teams tell the truth.

Without this rule, teams hide gaps as To confirm, delay submission to buy time, or argue about scope. With it, the fastest route through the gate is to state every gap plainly on day one. Evidence of absence follows the same rules as evidence of presence in PB-09: the account, environment and date are visible, and an export is preferred to a screenshot where one exists.

The verdict then follows the decision table mechanically. Nobody has to negotiate it.

## 6. Running the gate: a two-week timeline

| Day | Who | What happens |
|---|---|---|
| 0 | Project lead, Information Security Manager | The go-live change is raised with GOV-TPL-08 under GOV-PRO-09. The reviewer is named. The evidence folder is created with the PB-09 structure. Read-only reviewer accounts are requested with GOV-TPL-09 and listed in the access list |
| 1 to 5 | Project team | Step 1. Blockers first. Each check gets a status, an evidence file and an owner. Gaps get tickets |
| 5 | Project lead, reviewer | Submission. The reviewer opens every blocker the same day and reports any Not implemented or unevidenced blocker to the project lead immediately |
| 6 to 9 | Reviewer, project team | Step 2. The reviewer verifies, sending questions to the team in one batch per day. The team may close To confirm rows during this window |
| 10 | Reviewer, signatories | The reviewer writes GOV-TPL-12. A thirty minute sign-off meeting is held. Conditions are entered in GOV-REG-03. Reviewer accounts are removed and the removal is recorded |
| Go-live plus [Number] days | Information Security Manager | Conditions fall due. A missed condition is a nonconformity under GOV-PRO-04 |

For a system that processes personal data the Privacy Officer joins on day 6 for the privacy area and signs the verdict note.

## 7. The verdict decision table

| Blocking checks | Non-blocking checks | Verdict |
|---|---|---|
| All Verified, or Not applicable with the reviewer's written agreement | All Verified or Not applicable | Approved |
| All Verified | One or more To confirm or Not implemented, each with an owner, a ticket and a due date within [Number] days (30 is the recommended maximum) | Approved with conditions |
| All Verified | Any To confirm or Not implemented without an owner or a date | Stop until the rows are complete, usually a one day fix |
| Any To confirm | Any | Stop. An unknown on a blocker is a gap |
| Any Not implemented | Any | Stop |
| Any Not applicable without the reviewer's agreement | Any | Stop |

There is no override by seniority. If management decides to launch despite a Stop, that decision is a risk acceptance under GOV-PRO-24 by the authority for the risk band, recorded in GOV-REG-06, and the verdict note still reads Stop with the acceptance reference beside it. The gate records what is true; management records what it decided. Both records survive, and an auditor reading them later sees an organisation that knew what it was doing.

## 8. Outputs

A completed gate leaves these behind:

1. The completed GOV-REG-29 copy for the system, dated and kept. The next major release of the same system starts from it and re-verifies only what changed.
2. The signed GOV-TPL-12 verdict note.
3. The evidence folder, with the evidence footer described in PB-09 on the verdict note.
4. The access list of reviewer accounts and the confirmation of their removal.
5. Conditions entered as actions in GOV-REG-03 with owners and dates.
6. Register updates made during the gate: the system in GOV-REG-10, its interfaces in GOV-REG-25, any new supplier in GOV-REG-07, new or changed risks in GOV-REG-05, the processing entry in PIMS-REG-01 and the assessment in PIMS-REG-08, and evidence references against the relevant controls in ISMS-REG-02.
7. The go-live change in GOV-REG-11 referencing the verdict note.
8. Gate metrics for GOV-REG-21: gates run, verdicts by type, blockers found at submission, and days from submission to verdict.

## 9. Patterns that cause a Stop, and where to catch them earlier

| Pattern seen at the gate | Where it should have been caught |
|---|---|
| Multi-factor authentication enforced for staff but not for the break-glass account or the vendor support account | Design review under GOV-PRO-15; GOV-POL-06 |
| Backups configured, never restored | GOV-PRO-12 quarterly test, scheduled at project start |
| Logs stored in the same account the system administrators control | Architecture review; GOV-PRO-14 |
| "Test data" that is a copy of production personal data | GOV-PRO-15 test data rules; PIMS-PRO-06 |
| An analytics, error reporting or AI service added in the final sprint with no supplier entry | GOV-PRO-06 at the moment the dependency is added |
| Secrets present in repository history even after removal from the current code | GOV-PRO-15 secrets scanning |
| "A DPIA is not needed" decided by the developer rather than screened under PIMS-PRO-02 | Project kick-off; PIMS-PRO-02 screening triggers |
| Data resting in a region nobody chose because a managed service defaulted there | GOV-PRO-26 region and residency decision at account creation |

Each of these is a design-time control that the gate merely confirms. A team that runs GOV-CHK-02 and the GOV-PRO-15 checks during the build arrives at the gate with nothing to hide and leaves in a day.

## 10. Related documents

- GOV-REG-29 Go-live gate checklist
- GOV-TPL-12 Readiness verdict note
- PB-09 Playbook: evidence management that survives an audit
- GOV-PRO-09 Change management procedure
- GOV-TPL-08 Change request form
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-26 Cloud services security procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-PRO-06 Privacy by design and by default procedure
- GOV-CHK-02 Secure configuration baseline checklist
