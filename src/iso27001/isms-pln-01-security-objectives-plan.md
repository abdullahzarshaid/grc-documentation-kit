---
id: ISMS-PLN-01
title: Information security objectives and plan
type: plan
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 6.2
  - ISO/IEC 27001:2022 clause 5.2
  - ISO/IEC 27001:2022 clause 9.1
  - SOC 2 CC3.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The rules for setting measurable information security objectives, the objectives for the current period with their measures, owners and actions, and how progress is measured and reported.
---
## 1. Purpose

This plan turns the commitments in GOV-POL-03 into a small number of measurable objectives for the period, each with an owner, actions, resources and a date, so that leadership can see whether the management system is improving the outcomes it exists for.

## 2. Scope

The plan covers the whole scope in ISMS-STM-01. It is set for one financial year and tracked in GOV-REG-21.

## 3. Rules for setting objectives

3.1 Each objective is consistent with GOV-POL-03 and traceable to at least one of: a risk in GOV-REG-05, a requirement in ISMS-REG-03, a legal or contractual obligation in GOV-REG-04, or a result reported under ISMS-PRO-04.

3.2 Each objective is measurable. Before it is approved, the measure, the formula, the target, the frequency and the data source are written against it. An objective that cannot be measured is rewritten until it can be.

3.3 Each objective has an owner role, a list of actions, the resources needed, and a completion date within the period.

3.4 The steering committee approves the objectives in the month after the management review, and the Information Security Manager records them in GOV-REG-21 and communicates them under ISMS-PLN-02 to the roles that contribute to them.

3.5 Progress is reviewed quarterly by the steering committee. Each objective carries a status of Green (on target), Amber (behind but recoverable within the period) or Red (target will be missed without intervention). An objective that is Red at two consecutive reviews is raised as a nonconformity under GOV-PRO-04.

3.6 An objective may be changed during the period only by the steering committee, with the reason recorded in GOV-REG-22.

3.7 The plan holds between six and ten objectives. More than ten dilutes attention; fewer than six usually means a risk area has been left without a target.

## 4. Objectives for [Year]

The objectives below are examples of the form a complete objective takes. Replace them with [Organisation]'s own, keeping the same structure.

| No. | Objective | Measure and target | Owner | Reviewed |
|---|---|---|---|---|
| 1 | Close critical vulnerabilities inside the agreed window | Critical findings in GOV-REG-14 fixed within 7 days, divided by all critical findings closed in the quarter: 95 percent or more | Head of Engineering | Monthly |
| 2 | Complete every access review on time | Reviews recorded in GOV-REG-12 within 10 working days of quarter end, divided by reviews due: 100 percent | Information Security Manager | Quarterly |
| 3 | Make every joiner competent before they handle customer data | New starters with induction recorded in GOV-REG-09 within 10 working days of start, divided by all starters: 98 percent or more | Head of People | Quarterly |
| 4 | Prove that critical systems can be restored | Restore tests in GOV-REG-15 that met the recovery time objective, divided by tests performed: 100 percent, at least one test per critical system per quarter | Head of Engineering | Quarterly |
| 5 | Reduce susceptibility to phishing | Click rate in simulations 5 percent or lower and report rate 50 percent or higher by the final simulation of the year | Information Security Manager | Per simulation |
| 6 | Contain serious incidents quickly | Severity 1 and 2 incidents in GOV-REG-08 contained within 4 hours of detection, divided by all such incidents: 90 percent or more | Incident Lead | Quarterly |
| 7 | Keep supplier assurance current | Tier 1 suppliers in GOV-REG-07 with a review dated within the last 12 months, divided by all Tier 1 suppliers: 100 percent | Head of Operations | Quarterly |
| 8 | Close audit findings before they age | Corrective actions in GOV-REG-03 closed by their due date, divided by actions due in the quarter: 90 percent or more | Information Security Manager | Quarterly |

## 5. Actions and resources

| No. | Planned actions | Resources | Evidence of completion |
|---|---|---|---|
| 1 | Enrol every production asset in scanning; agree the patch window with product owners; add an exception route under GOV-PRO-24 | Scanning licence, [Number] engineer days per month | GOV-REG-14 trend report |
| 2 | Publish the review calendar; pre-build account exports for each system; assign a deputy reviewer per system | [Number] hours per system per quarter | GOV-REG-12 entries with evidence links |
| 3 | Add the security induction to the starter workflow; block system access until the induction record exists | Learning content, people team time | GOV-REG-09 and GOV-CHK-01 records |
| 4 | Define the critical system list with the business impact analysis; schedule tests; record results and gaps | Test environment, [Number] engineer days per quarter | GOV-REG-15 entries |
| 5 | Run a simulation each quarter with a different lure; brief managers on results; target repeat clickers with coaching | Simulation service, awareness time | Simulation reports, GOV-REG-09 |
| 6 | Run two incident exercises in the year; publish the on-call rota; pre-approve containment actions for common scenarios | Exercise time, on-call budget | GOV-REG-08 timestamps, GOV-REG-16 |
| 7 | Tier every supplier; collect assurance evidence; diarise renewals ninety days ahead | Procurement and security time | GOV-REG-07 review dates |
| 8 | Review open actions fortnightly; escalate items older than sixty days to the steering committee | Information Security Manager time | GOV-REG-03 closure dates |

## 6. Measurement and reporting

6.1 Owners extract the measure for each objective from the named register by the fifth working day after each period, using the formula written in GOV-REG-21.

6.2 The Information Security Manager compiles the values into the quarterly performance report produced under ISMS-PRO-04, assigns the Green, Amber or Red status, and adds one sentence of commentary and one sentence on the next action for every objective not Green.

6.3 The steering committee reviews the report each quarter. The year end values and the status of every objective are an input to the management review under GOV-PRO-03, which decides the objectives for the next period.

## 7. Records and evidence

- GOV-REG-21 Security objectives and measures tracker: the approved objectives, the latest values and the status history.
- Quarterly performance reports under ISMS-PRO-04.
- Steering committee minutes approving the objectives and recording quarterly reviews.
- GOV-REG-22 entries where objectives were changed or carried over.

## 8. Review and maintenance

The Information Security Manager reviews this plan annually after the management review, and within thirty days of a change to GOV-POL-03, a change of scope, or a severity 1 incident that shows an objective was missing.

## 9. Related documents

- GOV-POL-03 Information security policy
- GOV-REG-21 Security objectives and measures tracker
- ISMS-PRO-04 Monitoring, measurement, analysis and evaluation procedure
- ISMS-PLN-02 Communication plan
- GOV-PRO-03 Management review procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-REG-05 Information security risk register
- ISMS-REG-03 Interested parties and requirements register
