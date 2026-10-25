---
id: SOC-PRO-01
title: Control testing and sampling procedure
type: procedure
framework: soc2
maps:
  - SOC 2 CC4.1
  - SOC 2 CC4.2
  - ISO/IEC 27001:2022 clause 9.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] tests its own SOC 2 controls before and during an examination period, with defined populations, sample sizes by frequency, deviation handling and workpapers that an external auditor can re-perform.
---
## 1. Purpose

This procedure sets how the controls in SOC-REG-01 are tested by [Organisation] itself, so that a control that has stopped operating is found and repaired months before the external auditor finds it, and so that every test leaves a workpaper the auditor can rely on and re-perform.

## 2. Scope

Every control listed in SOC-REG-01 Trust Services Criteria control matrix with a status of Operating or Tested, for every system inside the boundary described in SOC-TPL-01. It covers manual controls, controls a system performs on a schedule and controls that run on every transaction. It does not replace the internal audit programme in GOV-PRO-02, which examines the management system as a whole; the two share their findings through GOV-REG-03.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the testing plan, assigns testers, approves sample sizes, classifies deviations, reports results. |
| Control owner | Operates the control, produces the population on request, responds to deviations and fixes causes. |
| Tester | A person independent of the control's operation who defines the population, selects the sample, performs the test and writes the workpaper. |
| Internal Auditor | Reviews a sample of workpapers each quarter for quality and independence. |
| Steering committee | Receives the quarterly testing summary and decides on unresolved deviations. |

## 4. Procedure

4.1 **Testing plan.** At the start of each examination period, and at least annually, the Information Security Manager lists every control in SOC-REG-01 with its frequency, owner, the quarter in which it will be tested and the assigned tester. Every control is tested at least once per period. A control with a deviation in the previous period, a linked risk rated High or Critical in GOV-REG-05, or a change during the period is tested twice.

4.2 **Population definition.** Before selecting anything, the tester writes down the population: what one occurrence of the control looks like (one access review, one change ticket, one backup job, one new starter), the system of record that holds the occurrences, the date range, and the total count. The control owner produces the population as a system export that carries an identifier and a date for every item. A hand-typed list or a filtered screen view is not accepted; the tester records the refusal and requests the export.

4.3 **Population completeness.** The tester checks the population against an independent source before sampling: the leaver list against the people system, change tickets against the deployment log, new accounts against the identity provider's creation events. A difference above 2 percent of items, or any missing item that should have triggered the control, is a deviation under 4.8 before testing begins.

4.4 **Sample sizes.** The tester selects at least the number of items in the table below. Where the population is smaller than the sample size, the tester tests every item.

| Control frequency | Typical items in a twelve month period | Minimum sample |
|---|---|---|
| Annual | 1 | 1 |
| Semi-annual | 2 | 2 |
| Quarterly | 4 | 2 |
| Monthly | 12 | 3 |
| Weekly | 52 | 5 |
| Daily | 250 or more | 20 |
| Many times a day, or on every event, performed by a person | More than 250 | 25 |
| Performed by a system on every event | Not counted | 1 item, plus inspection of the configuration and of the change records for it |

For an event-driven control (a joiner, a leaver, an incident, a change) the row is chosen by how many events occurred in the period. For a shorter period the typical counts fall but the minimum samples stay.

4.5 **Selection method.** The tester selects items at random by a method that can be repeated from the recorded inputs, for example a seeded random number list applied to the exported row numbers. Where the period is long, the tester spreads the sample so that every quarter is represented. The tester records the method, the seed or formula and the selected identifiers. The control owner never chooses the items and does not see the selection until evidence is requested.

4.6 **Test methods and attributes.** The tester applies at least one of: inspection of a record the control produced, re-performance of the control on the selected item, observation of the control being performed, or inquiry of the operator. Inquiry on its own is never sufficient; it is paired with inspection or re-performance. Each test states the attributes checked, for example: reviewer named, review dated inside the quarter, every account dispositioned, removals actioned within five working days, sign-off by the System Owner.

4.7 **Performing the test.** For every selected item the tester records the identifier, the date, each attribute checked and a result of Pass or Fail, with a reference to the evidence file named as PB-09 describes. Evidence is taken from the system of record by the tester or in the tester's presence. Evidence forwarded by the control owner without the tester seeing its source is marked To confirm until the source is shown.

4.8 **Deviations.** Any item that fails an attribute is a deviation. The tester records it the same day with the item, the attribute, the facts observed and the control owner's explanation. The Information Security Manager classifies it within five working days as one of the following.

- Isolated: one item, a cause that applies only to that item, no effect on others. The tester doubles the sample from the same population; if no further deviation appears, the control is reported as operating with one noted exception.
- Systemic: more than one item, or a cause that could affect other items (a step nobody owns, a tool change, a person who left). The control is reported as not operating effectively for the period of the cause, and a corrective action is raised in GOV-REG-03 under GOV-PRO-04.
- Design gap: the control as written cannot meet the criterion even when performed perfectly. SOC-REG-01 is updated with a redesigned control and its start date, and the gap is reported to the steering committee.

4.9 **Remediation and retest.** The control owner implements the corrective action by the date in GOV-REG-03. The tester retests after at least one full operating cycle of the control has completed following the fix, using a fresh sample drawn from occurrences after the fix date. A control fixed and retested inside the period is reported with both results and both dates.

4.10 **Workpaper.** Every test produces one workpaper containing: control identifier and text from SOC-REG-01, criteria served, period tested, population definition and count, completeness check, selection method and sample, attributes tested, results per item, deviations and their classification, conclusion, tester name and date, reviewer name and date. Workpapers are stored in the evidence folder area for audit and review, hashed as PB-09 describes and retained with the period's evidence.

4.11 **Quality review.** Each quarter the Internal Auditor reviews at least [Number] workpapers, checking that the tester was independent, that the population came from a system of record, that the sample was random and recorded, and that the conclusion follows from the results. Findings about testing quality become corrective actions in GOV-REG-03.

4.12 **Reporting.** The Information Security Manager reports to the steering committee quarterly: controls tested, controls passed, open deviations by classification, retests due, and controls not yet tested in the period. The period-end summary is an input to management review under GOV-PRO-03 and is given to the external auditor on request as evidence for CC4.1 and CC4.2.

## 5. Records and evidence

- The testing plan for each period.
- SOC-REG-01 with Status and Test method completed for every control.
- One workpaper per test, with the population export, the selection record and the evidence files.
- Deviation records and their corrective actions in GOV-REG-03.
- Quarterly testing summaries and the Internal Auditor's quality reviews.

## 6. Exceptions

A control may be tested by its own operator only where no independent person has the knowledge to test it; the Information Security Manager records the reason and the Internal Auditor re-performs that test in the quarterly quality review. A sample size may be reduced only with the written agreement of the Information Security Manager, recorded in the workpaper with the reason. No exception permits the control owner to choose the sample.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after each external examination (to adopt the auditor's population and sample expectations where they differ), and when the control set in SOC-REG-01 changes materially. Changes follow GOV-PRO-01.

## 8. Related documents

- SOC-REG-01 Trust Services Criteria control matrix
- SOC-REG-02 Evidence calendar
- SOC-TPL-01 System description template
- GOV-PRO-02 Internal audit procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-REG-03 Corrective action log
- PB-09 Playbook: evidence management that survives an audit
- SOC-GDE-01 Guide: SOC 2 in plain words
