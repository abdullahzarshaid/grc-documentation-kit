---
id: ISMS-PRO-03
title: Operational planning and control procedure
type: procedure
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 8.1
  - ISO/IEC 27001:2022 clause 6.3
  - ISO/IEC 27001:2022 clause 6.1.3
  - SOC 2 CC5.1
  - SOC 2 CC5.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How the processes that deliver the management system's controls are planned, given operating criteria, implemented from the risk treatment plan, kept under control when they change, and governed when another organisation performs them.
---
## 1. Purpose

This procedure connects the plans of the management system (the risk treatment plan, the objectives, the policies) to day to day operation. It defines which processes exist, what each must achieve, how a control agreed in the Statement of Applicability becomes something that actually runs, how planned and unplanned changes are handled, and how processes performed by suppliers stay under [Organisation]'s control.

## 2. Scope

It applies to every operational process that implements a control in ISMS-REG-01 or an action in GOV-REG-05, whether performed by staff, contractors or an external provider, across the whole scope in ISMS-STM-01.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Keeps the process inventory in step 4.1, tracks implementation of treatments, chairs the monthly operations review. |
| Process owner | Named for each process in the inventory; runs the process to its criteria, keeps its records, reports its measures. |
| System Owner | Confirms that controls on their system are implemented and operating; approves changes to it under GOV-PRO-09. |
| Head of Operations | Governs processes performed by suppliers under GOV-PRO-06 and GOV-PRO-26. |
| Steering committee | Approves planned changes to the management system and accepts residual risk after unplanned changes. |

## 4. Procedure

4.1 **Process inventory.** The Information Security Manager maintains the inventory below. Every process has a governing document, operating criteria (the measurable conditions that show it is working) and the records that prove it ran.

| Process | Governing document | Operating criteria | Records |
|---|---|---|---|
| Risk assessment and treatment | GOV-PRO-05 | Full assessment annually and on triggers; every risk above appetite has a treatment with owner and date | GOV-REG-05, GOV-REG-06 |
| Access management | GOV-PRO-10 | Joiner access within one working day of approval; leaver removal within one working day; quarterly reviews on every in-scope system | GOV-REG-12, GOV-REG-13 |
| Change management | GOV-PRO-09 | No production change without approval, test evidence and rollback plan; emergency changes reviewed within five working days | GOV-REG-11 |
| Vulnerability and patch management | GOV-PRO-11 | Findings fixed within the severity window; exceptions approved under GOV-PRO-24 | GOV-REG-14 |
| Backup and restore | GOV-PRO-12 | Backups complete to schedule; restore test per critical system each quarter | GOV-REG-15 |
| Logging and monitoring | GOV-PRO-14 | Required events logged on every in-scope system; alerts triaged within the set time; logs retained for the set period | Alert tickets, log retention evidence |
| Incident management | GOV-PRO-07 | Response within the severity time; review within ten working days | GOV-REG-08, GOV-TPL-11 |
| Supplier management | GOV-PRO-06 | Every supplier tiered; due diligence before use; annual review of Tier 1 | GOV-REG-07 |
| Secure development | GOV-PRO-15 | Peer review and security tests before release; no secrets in code; environments separated | Release approvals, pipeline results |
| Awareness and competence | GOV-PRO-08, ISMS-PRO-02 | Induction within ten working days; annual refresher; competence assessed annually | GOV-REG-09, GOV-REG-23 |
| Business continuity | GOV-PRO-13 | Business impact analysis current; plans exercised to the cadence set | GOV-REG-16 |
| Asset management | GOV-PRO-16 | Every asset has an owner and a classification; inventory reconciled quarterly | GOV-REG-10, GOV-REG-24 |

4.2 **Setting criteria.** When a process is created or its governing document changes, the process owner proposes the operating criteria and the Information Security Manager confirms that each criterion can be measured from the process's own records. Criteria that cannot be measured are rewritten before the document is approved under GOV-PRO-01.

4.3 **Implementing treatments.** Each treatment action in GOV-REG-05, and each control marked Planned or Partial in ISMS-REG-01, is given a task with an owner and a due date in ISMS-REG-02. The owner implements it, attaches evidence that it operates (configuration export, record sample, screenshot showing account and date), and the Information Security Manager updates the status in ISMS-REG-01 and ISMS-REG-02. A control is not marked Implemented until evidence of operation exists.

4.4 **Planned changes to the management system.** A change to scope, policy, process, organisation structure or principal technology that affects how a control operates is proposed in writing with its purpose, the controls affected, the resources needed, and the responsibilities that move. The Information Security Manager assesses the effect on GOV-REG-05 and ISMS-REG-01; the steering committee approves; the affected documents are updated under GOV-PRO-01 before the change takes effect. Technical changes to systems follow GOV-PRO-09 in addition.

4.5 **Unintended changes.** When a change has happened without this review (for example a provider alters a service, a team adopts a new tool, a control stops operating), the person who notices reports it as an event under GOV-PRO-07. The Information Security Manager reviews the consequences within five working days, records any new or changed risk in GOV-REG-05, and raises a nonconformity under GOV-PRO-04 if a control failed.

4.6 **Externally provided processes.** Where a supplier performs a process in the inventory, or part of one, the Head of Operations records it in GOV-REG-07 with the process name, the contract clause that requires the operating criteria, the evidence the supplier must provide and how often, and the person who reviews that evidence. Cloud services are governed under GOV-PRO-26 and the shared responsibility split in ISMS-STM-01. A supplier's failure to meet a criterion is handled as a nonconformity against the supplier under GOV-PRO-06.

4.7 **Documented information from operation.** Each process keeps the records named in the inventory for the retention period in the retention schedule, in a form that shows who did what and when. Records are controlled under GOV-PRO-01.

4.8 **Monthly operations review.** The Information Security Manager meets the process owners each month, checks each process against its criteria using the latest records, lists breaches of criteria, and agrees corrections. Breaches that repeat for two months, or that affect a critical system, go to GOV-PRO-04. The review note is filed and feeds the quarterly report under ISMS-PRO-04.

## 5. Records and evidence

- The process inventory in step 4.1, dated at each revision.
- ISMS-REG-02 Control implementation tracker: implementation tasks, evidence and status for every applicable control.
- ISMS-REG-01 Statement of Applicability with implementation status.
- Change proposals and steering committee approvals for planned changes.
- Monthly operations review notes.
- GOV-REG-07 entries for processes performed by suppliers, with the evidence received.

## 6. Exceptions

A treatment or control may operate without the evidence in step 4.3 for at most thirty days after implementation while the first records accumulate. No process may operate without a named owner.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding against clause 8.1 or 6.3. Changes follow GOV-PRO-01.

## 8. Related documents

- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
- GOV-PRO-09 Change management procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-PRO-26 Cloud services security procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- ISMS-PRO-04 Monitoring, measurement, analysis and evaluation procedure
- GOV-PRO-01 Document control procedure
