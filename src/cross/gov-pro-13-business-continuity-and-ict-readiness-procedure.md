---
id: GOV-PRO-13
title: Business Continuity and ICT Readiness Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.29
  - ISO/IEC 27001:2022 Annex A 5.30
  - SOC 2 A1.2
  - SOC 2 A1.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How business impact is analysed, how continuity and ICT recovery strategies are chosen and planned, how security is maintained during a disruption, and how plans are exercised and improved.
---
## 1. Purpose

This procedure prepares [Organisation] to keep delivering its critical services, and to keep information secure, through a disruption. It sets how business impact is analysed, how strategies and plans are built, what the plans contain, how they are exercised and how lessons are applied.

## 2. Scope

It applies to all processes and systems in the management system scope (ISMS-STM-01), the people and suppliers they depend on, and the offices and remote working arrangements through which they are delivered. It covers disruptions from loss of a site, loss of a cloud provider or region, loss of a key supplier, loss of staff availability, and attacks that take systems offline.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Crisis lead (Chief Executive Officer or named deputy) | Activates plans, takes decisions beyond delegated authority, approves external communication. |
| Business continuity coordinator (Information Security Manager) | Runs this procedure, maintains the plans, schedules exercises, keeps GOV-REG-16. |
| Head of Engineering | Owns ICT readiness: recovery designs, runbooks and technical exercises. |
| Process owners and System Owners | Complete the business impact analysis, maintain their recovery runbooks, take part in exercises. |
| Communications lead | Prepares and issues internal and external messages approved by the crisis lead. |

## 4. Procedure

4.1 **Business impact analysis.** Each process owner completes GOV-TPL-07 for their process annually and when the process changes materially. The worksheet records dependencies (systems, data, people, suppliers, facilities), impact at four hours, one day, three days and one week, the maximum tolerable period of disruption, the recovery time objective, the recovery point objective and the minimum resources needed to operate. The coordinator consolidates the worksheets into a prioritised list of critical processes and systems, which the steering committee approves.

4.2 **Strategy selection.** For each critical process the coordinator and the process owner identify the options that meet the objectives (redundant infrastructure, alternative provider, manual workaround, reduced service, alternative workplace, cross-trained staff), estimate the cost and recovery time of each, and record the chosen strategy with the reason. The steering committee approves the strategies and the budget they need. A strategy that cannot meet its objective is recorded as a risk in GOV-REG-05.

4.3 **ICT readiness.** The Head of Engineering designs each critical system so that the approved strategy is achievable: redundancy across failure zones (GOV-PRO-19), backups that meet the recovery point objective (GOV-PRO-12), infrastructure definitions that can rebuild the service, and a documented recovery runbook stating the order of recovery, the people authorised to run it and the credentials they need, held under the break-glass arrangements in GOV-REG-13. Runbooks are reviewed after every change to the system under GOV-PRO-09.

4.4 **Plan content.** The business continuity plan and each recovery runbook contain: activation criteria and who may activate; roles and deputies; a contact tree held outside the primary systems; the recovery sequence and its dependencies; the minimum service to restore first; message templates for staff, customers and suppliers, and the inputs PIMS-PRO-04 needs where personal data is involved; and the point at which the plan is stood down and normal operation confirmed.

4.5 **Security during disruption.** Access control, logging, encryption and change control stay in force during recovery. Any relaxation (a shared recovery account, a temporary network opening, a manual process without logging) requires the crisis lead's approval, is recorded in the incident record with an expiry, and is reversed and verified before the incident closes.

4.6 **Activation.** A disruption is first handled as an incident under GOV-PRO-07. The incident lead recommends activation when the recovery time objective of a critical process is at risk; the crisis lead decides, and the decision and its time are recorded.

4.7 **Exercise programme.**

| Exercise | Cadence | Minimum content |
|---|---|---|
| Tabletop walkthrough of the business continuity plan | Annually | Scenario, decisions, communication, gaps found |
| Technical recovery test of each critical system | Annually, may be combined with the restore test in GOV-PRO-12 | Recovery from backups and definitions into a clean environment, time measured against the objective |
| Full exercise with relocation or remote operation | Every two years | End-to-end recovery of at least one critical service |
| New critical system | Within six months of go-live | Technical recovery test |

The coordinator sets objectives for each exercise in advance and records the outcome, the time achieved against the recovery time objective and the findings in GOV-REG-16.

4.8 **Lessons and actions.** Within ten working days of an exercise or a real disruption, the coordinator holds a review, records what worked and what did not, and raises each gap as an action in GOV-REG-03 with an owner and due date. Plans are updated within 30 days of the review.

4.9 **Maintenance.** The coordinator confirms the contact tree quarterly and reviews the plans after a change to a critical system or supplier, after an exercise or disruption, and at least annually.

## 5. Records and evidence

- Completed GOV-TPL-07 worksheets and the consolidated priority list with steering committee approval.
- GOV-REG-16 Business continuity exercise log: every exercise and activation with objectives, time achieved and findings.
- The business continuity plan and recovery runbooks with version history.
- Review records and the resulting GOV-REG-03 actions.
- Records of security relaxations approved during a disruption and their reversal.

## 6. Exceptions

A critical system may go live without a technical recovery test only under a risk acceptance in GOV-PRO-24 that fixes the test date within six months of go-live.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any activation, after an exercise that missed its objectives, and when the critical process list changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-07 Business impact analysis worksheet
- GOV-REG-16 Business continuity exercise log
- GOV-PRO-12 Backup and restore testing procedure
- GOV-PRO-19 Capacity and availability management procedure
- GOV-PRO-07 Information security incident management procedure
- PIMS-PRO-04 Personal data breach assessment and notification procedure
- GOV-REG-05 Information security risk register
- GOV-REG-03 Corrective action log
- GOV-REG-13 Privileged account register
- GOV-PRO-24 Exception and risk acceptance procedure
- ISMS-STM-01 ISMS scope statement
