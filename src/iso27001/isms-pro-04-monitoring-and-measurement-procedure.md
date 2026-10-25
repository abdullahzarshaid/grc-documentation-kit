---
id: ISMS-PRO-04
title: Monitoring, measurement, analysis and evaluation procedure
type: procedure
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 9.1
  - ISO/IEC 27001:2022 clause 6.2
  - ISO/IEC 27001:2022 Annex A 5.36
  - SOC 2 CC4.1
  - SOC 2 CC4.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: What [Organisation] measures about its controls and its management system, how and how often the data is collected, who analyses it, how control effectiveness is tested, and how results reach the steering committee and the management review.
---
## 1. Purpose

This procedure produces the evidence that the management system works: a fixed set of measures with formulas and targets, a test of every applicable control at least once a year, and a quarterly report that tells leadership where performance is below target and what is being done about it.

## 2. Scope

It applies to every process in the inventory of ISMS-PRO-03, every applicable control in ISMS-REG-01, and every objective in ISMS-PLN-01, across the scope in ISMS-STM-01.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the measurement set, compiles the quarterly report, plans control testing, presents results. |
| Process owner | Extracts the measures for their process by the due date, explains variances, proposes actions. |
| System Owner | Provides configuration and record extracts for control tests on their system. |
| Internal Auditor | Performs or witnesses the tests marked for independent testing; may not test a control they operate. |
| Steering committee | Reviews the quarterly report, decides on actions for Red items, confirms targets for the next year. |

## 4. Procedure

4.1 **Measurement set.** The measures below are collected for every period. Each is defined by a formula, a target, a frequency and the register it is drawn from, so that two people would compute the same value.

| Measure | Formula | Target | Frequency and source |
|---|---|---|---|
| Critical vulnerability closure | Critical findings fixed within 7 days divided by critical findings closed in the period | 95 percent or more | Monthly, GOV-REG-14 |
| Patch currency | In-scope hosts patched within their cycle divided by in-scope hosts | 98 percent or more | Monthly, GOV-REG-24 and GOV-REG-14 |
| Access review completion | Reviews completed within 10 working days of quarter end divided by reviews due | 100 percent | Quarterly, GOV-REG-12 |
| Leaver access removal | Leavers with all access removed within one working day divided by leavers | 98 percent or more | Monthly, GOV-CHK-01 records and GOV-REG-12 |
| Training currency | Staff with induction and a refresher within the last 12 months divided by headcount | 98 percent or more | Quarterly, GOV-REG-09 |
| Phishing susceptibility | Recipients who clicked divided by recipients, and recipients who reported divided by recipients | 5 percent or lower; 50 percent or higher | Per simulation, simulation report |
| Incident containment time | Median hours from detection to containment for severity 1 and 2 incidents | 4 hours or less | Quarterly, GOV-REG-08 |
| Restore test success | Restore tests that met the recovery time objective divided by tests performed | 100 percent | Quarterly, GOV-REG-15 |
| Change success | Changes completed without rollback or incident divided by changes completed | 97 percent or more | Monthly, GOV-REG-11 |
| Corrective action timeliness | Actions closed by their due date divided by actions due in the period | 90 percent or more | Quarterly, GOV-REG-03 |
| Risk treatment progress | Treatment actions completed by their due date divided by actions due in the period | 85 percent or more | Quarterly, GOV-REG-05 |
| Supplier review currency | Tier 1 suppliers reviewed within the last 12 months divided by Tier 1 suppliers | 100 percent | Quarterly, GOV-REG-07 |

4.2 **Data collection.** By the fifth working day after each period the process owner extracts the value from the named register, keeps the extract (export or filtered view with its date), and enters the value and the extract location in GOV-REG-21. A value that cannot be computed because the register is incomplete is recorded as missing, not estimated.

4.3 **Control effectiveness testing.** At the start of each year the Information Security Manager plans a test of every control marked Implemented in ISMS-REG-01 and records the plan in ISMS-REG-02: the test method, the sample, the tester and the quarter. Methods are inspection of configuration, sampling of records, re-performance of the control, interview, and observation. Controls that protect restricted information or privileged access are tested by someone who does not operate them. The tester records the result as Pass or Fail with the evidence reference and the date. A Fail is raised under GOV-PRO-04 within five working days.

4.4 **Sampling rule.** For a control that runs daily or more often, the tester examines at least 25 instances spread across the year; weekly, at least 10; monthly, at least 3; quarterly or less often, every instance. A single exception in the sample is a Fail unless the process owner shows it was detected and corrected by the process itself at the time.

4.5 **Analysis.** The Information Security Manager compares each value with its target and with the previous four periods, assigns Green (at or better than target), Amber (within 10 percent of target or a single miss after four Greens) or Red (below that), and writes one sentence of cause and one of action for every Amber and Red. Trends matter as much as single values: three consecutive periods moving away from target is reported as Amber even if still above target.

4.6 **Quarterly report.** Within fifteen working days of quarter end the Information Security Manager issues the quarterly performance report containing: the measurement table with status, the objectives from ISMS-PLN-01 with status, control test results from ISMS-REG-02 (tests planned, performed, passed, failed), open nonconformities from GOV-REG-03 by age, and the actions proposed. The steering committee reviews it at its next meeting and the decisions are minuted.

4.7 **Annual evaluation.** The year's four reports, the full year control test results and the trend of every measure are an input to the management review under GOV-PRO-03. The review confirms or changes the measures and targets for the next year, and the Information Security Manager updates this procedure and GOV-REG-21 within thirty days.

4.8 **Data quality.** Every reported value can be traced to a dated extract. If a formula or source changes, the change is recorded in GOV-REG-21 and values before the change are not compared with values after it without a note.

## 5. Records and evidence

- GOV-REG-21 Security objectives and measures tracker: values, extracts and status for every measure and objective.
- ISMS-REG-02 Control implementation tracker: the test plan and the result of every control test.
- Quarterly performance reports and the steering committee minutes that reviewed them.
- Dated extracts from the source registers.
- Nonconformities raised in GOV-REG-03 from failed tests or Red measures.

## 6. Exceptions

A measure may be suspended for at most two periods when its source register is being rebuilt, with the reason recorded in GOV-REG-21 and reported in the quarterly report. No control marked Implemented may go untested for more than twelve months.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually after the management review, and within thirty days of a change to ISMS-PLN-01 or to the process inventory in ISMS-PRO-03. Changes follow GOV-PRO-01.

## 8. Related documents

- ISMS-PLN-01 Information security objectives and plan
- GOV-REG-21 Security objectives and measures tracker
- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- ISMS-PRO-03 Operational planning and control procedure
- GOV-PRO-03 Management review procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-02 Internal audit procedure
