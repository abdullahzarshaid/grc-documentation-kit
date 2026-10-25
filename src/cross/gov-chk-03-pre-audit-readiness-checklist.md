---
id: GOV-CHK-03
title: Pre-audit readiness checklist
type: checklist
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 4
  - ISO/IEC 27001:2022 clause 5
  - ISO/IEC 27001:2022 clause 6
  - ISO/IEC 27001:2022 clause 7
  - ISO/IEC 27001:2022 clause 8
  - ISO/IEC 27001:2022 clause 9
  - ISO/IEC 27001:2022 clause 10
  - SOC 2 CC4.1
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: Forty-nine yes or no checks, grouped by ISO/IEC 27001:2022 clause 4 to 10, that [Organisation] runs four weeks before an external audit, each naming the evidence to have ready for the auditor.
---
## 1. How to use this checklist

Run it four weeks before a stage 1, stage 2, surveillance, recertification or SOC 2 audit. The Information Security Manager assigns each check to the role that holds the evidence, collects the answers within five working days, and raises a corrective action in GOV-REG-03 for every "No" with an owner and a due date before the audit date. A "No" that cannot be fixed before the audit is disclosed to the auditor at the opening meeting rather than discovered during it. Keep the completed checklist as a record. Evidence should be exported from the system of record, show the date and the account, and be filed under the numbered area used by PB-09.

## 2. Clause 4: context and scope

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 4.1 | Internal and external issues have been analysed and the analysis was reviewed in the last twelve months. | ISMS-PRO-01 output with review date | |
| 4.2 | Interested parties and their requirements are recorded and current. | ISMS-REG-03 | |
| 4.3 | The scope statement is approved, matches the certificate scope requested, and justifies every exclusion. | ISMS-STM-01 with approval record | |
| 4.4 | Interfaces and dependencies with suppliers and cloud providers are described and match the supplier register. | ISMS-STM-01, GOV-REG-07 | |

## 3. Clause 5: leadership

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 5.1 | The information security policy is signed by the Chief Executive Officer, is the current version, and is published where staff can find it. | GOV-POL-03, GOV-REG-01 entry | |
| 5.2 | The management commitment statement is signed and current. | GOV-STM-01 | |
| 5.3 | Roles, responsibilities and authorities are assigned, communicated and match the organisation chart. | GOV-POL-01, organisation chart, role descriptions | |
| 5.4 | The steering committee has met at the cadence in its charter and the minutes show decisions. | Charter, minutes for the last four quarters | |
| 5.5 | A budget and staffing for the management system were approved for the current year. | Budget approval record | |
| 5.6 | Staff interviewed at random can say where the policy is and how to report an incident. | Awareness spot check results | |

## 4. Clause 6: planning

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 6.1 | The risk methodology is approved and its criteria (scales, bands, appetite, authorities) are defined. | GOV-PRO-05 with approval | |
| 6.2 | A full risk assessment was performed in the last twelve months and every risk has an owner. | GOV-REG-05 with dates and owners | |
| 6.3 | Every High or Critical risk has an approved treatment plan or a current acceptance. | GOV-REG-05, GOV-REG-06 | |
| 6.4 | Risk owners have approved the treatment plan and residual risks have been accepted by the right authority. | Signed treatment plan, GOV-TPL-06 forms | |
| 6.5 | The Statement of Applicability lists all 93 Annex A controls with justification and implementation status. | ISMS-REG-01 | |
| 6.6 | Every control named in a treatment plan is Applicable in the Statement of Applicability, and no Not applicable control is relied on anywhere. | Cross-check of GOV-REG-05 against ISMS-REG-01 | |
| 6.7 | Information security objectives are measurable, resourced, owned and have a plan. | ISMS-PLN-01, GOV-REG-21 | |
| 6.8 | Changes to the management system in the period were planned and recorded. | GOV-REG-01 history, GOV-REG-22 | |

## 5. Clause 7: support

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 7.1 | Competence requirements for security and privacy roles are defined and evidence of competence is held. | ISMS-PRO-02 matrix, certificates, training records | |
| 7.2 | Everyone in scope completed induction and the annual refresher; completion rate meets the target. | GOV-REG-09 with completion report | |
| 7.3 | Everyone in scope has acknowledged the policy and the acceptable use policy. | GOV-REG-23 | |
| 7.4 | Internal and external communications about security follow the communication plan. | ISMS-PLN-02 with examples | |
| 7.5 | The master list of documents is current, every document is at an approved version, and owners and review dates are set. | GOV-REG-01 | |
| 7.6 | Withdrawn documents are removed from the live location and no uncontrolled copies are in use. | Sample of document locations | |
| 7.7 | Records are retained for the required period, protected from alteration and retrievable on request. | PIMS-REG-07, sample retrievals | |

## 6. Clause 8: operation

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 8.1 | Operational procedures are followed as written; a sample of the last three months of records shows no unexplained gaps. | Samples from access, change and incident records | |
| 8.2 | The risk treatment plan is on track and implemented controls have evidence. | Treatment plan status, control evidence | |
| 8.3 | Outsourced and cloud processes are controlled: suppliers are tiered, assessed and reviewed on schedule. | GOV-REG-07, questionnaires, review records | |
| 8.4 | Access reviews were completed on schedule and removals were actioned. | GOV-REG-12 | |
| 8.5 | Vulnerabilities are remediated within the agreed times or have an approved exception. | GOV-REG-14, GOV-REG-06 | |
| 8.6 | Backups run as scheduled and a restore test was performed and recorded in the last quarter. | GOV-REG-15 | |
| 8.7 | Incidents are recorded, classified, reviewed and closed with lessons. | GOV-REG-08, post-incident reviews | |
| 8.8 | Changes are recorded with approval, testing and rollback. | GOV-REG-11 | |
| 8.9 | Business continuity arrangements were exercised in the period. | GOV-REG-16 | |
| 8.10 | The asset inventory is current, owned and classified. | GOV-REG-10, GOV-REG-24 | |
| 8.11 | Active exceptions are within their expiry dates and reviewed. | GOV-REG-06 | |

## 7. Clause 9: performance evaluation

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 9.1 | What is monitored and measured, how, when and by whom is defined, and results are recorded. | ISMS-PRO-04, measurement records | |
| 9.2 | Objectives have been measured and the tracker shows current values and status. | GOV-REG-21 | |
| 9.3 | The internal audit programme covers every clause and every applicable control within the cycle. | GOV-REG-02, ISMS-PLN-03 | |
| 9.4 | Internal audits were performed by competent auditors independent of the area, and reports were issued. | GOV-TPL-01 reports, competence records | |
| 9.5 | Every internal audit nonconformity has a corrective action with a root cause. | GOV-REG-03 | |
| 9.6 | A management review was held in the last twelve months and every mandatory input was covered. | GOV-TPL-03 minutes | |
| 9.7 | Management review outputs are tracked and the actions are progressing. | GOV-REG-22 | |

## 8. Clause 10: improvement

| Ref | Check | Evidence to have ready | Yes or No |
|---|---|---|---|
| 10.1 | Nonconformities from every source are logged with correction, root cause and corrective action. | GOV-REG-03, GOV-TPL-02 forms | |
| 10.2 | Effectiveness of corrective actions has been verified by someone other than the action owner. | GOV-REG-03 verification entries | |
| 10.3 | Findings from the previous external audit are closed with evidence. | Previous audit report, closure evidence | |
| 10.4 | Trend analysis of nonconformities has been performed and reported. | Quarterly trend report, steering committee minutes | |
| 10.5 | The legal, regulatory and contractual register is current and every obligation has a status. | GOV-REG-04 | |
| 10.6 | Where privacy is in scope, the processing inventory is current and DPIAs exist where required. | PIMS-REG-01, PIMS-REG-08 | |

## 9. Logistics

Confirm the following before the audit date: the audit plan from the certification body has been received and the auditees in it are available; each evidence area has a named owner who can share screens; a room or call with screen sharing is booked; the previous audit report and certificate are to hand; and the Information Security Manager has walked through this checklist with the executive sponsor.

## 10. Related documents

- GOV-PRO-02 Internal audit procedure
- GOV-PRO-03 Management review procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-03 Corrective action log
- ISMS-GDE-02 Guide: mandatory documented information and records for ISO/IEC 27001:2022
- ISMS-GDE-03 Guide: the certification journey from decision to recertification
- PB-09 Playbook: evidence management that survives an audit
