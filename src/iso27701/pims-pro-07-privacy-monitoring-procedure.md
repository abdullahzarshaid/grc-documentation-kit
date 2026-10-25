---
id: PIMS-PRO-07
title: Privacy control effectiveness monitoring procedure
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 5.7.1
  - ISO/IEC 27701 clause 5.7.3
  - ISO/IEC 27001:2022 clause 9.1
  - GDPR Article 24
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The measures that show whether the privacy controls work, how they are collected and graded each quarter, the structure of the quarterly privacy report, and how the results reach the management review and the corrective action process.
---
## 1. Purpose

This procedure replaces the feeling that privacy is under control with numbers that are collected the same way every quarter, graded against targets, and acted on. It gives the management review the privacy performance input it needs and gives the Privacy Officer early warning before a missed deadline becomes a regulatory matter.

## 2. Scope

It applies to every privacy procedure and register in the kit, to the ISO/IEC 27701 Annex A and Annex B controls marked applicable in ISMS-REG-01, and to the processing activities in PIMS-REG-01. It extends ISMS-PRO-04, which covers security measurement, and uses the same reporting cycle.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Owns the measure set, collects or receives the values, grades effectiveness, writes the quarterly report and presents it. |
| Processing Owners and System Owners | Provide register exports and configuration evidence by the fifth working day after quarter end. |
| Information Security Manager | Supplies security measures that bear on privacy and records control test results in ISMS-REG-02. |
| Internal Auditor | Uses the reports to focus the audit programme and tests a sample of reported values. |
| Chief Executive Officer | Receives the report, decides on resources and accepts or rejects proposed actions at the management review. |

## 4. Procedure

4.1 **The measure set.** The Privacy Officer maintains the measures below in GOV-REG-21 with their targets. Each has a defined formula, a named source register and a frequency, so that two people computing it get the same number.

| Measure | How it is calculated | Source | Target |
|---|---|---|---|
| Requests answered on time | Requests closed within the deadline divided by requests closed in the quarter | PIMS-REG-02 | 100 percent |
| Median days to close a request | Median of days from receipt to closure | PIMS-REG-02 | [Number] days or fewer |
| Requests refused or extended | Count of refusals and extensions, each with a recorded reason | PIMS-REG-02 | Every one has a Privacy Officer decision |
| Breaches assessed within 48 hours | Breaches with a decision within 48 hours of awareness divided by breaches in the quarter | PIMS-REG-03 | 100 percent |
| Authority notifications within 72 hours | Notifications sent within 72 hours divided by notifications required | PIMS-REG-03 | 100 percent |
| Breaches per quarter and trend | Count by nature and root cause against the previous four quarters | PIMS-REG-03, GOV-REG-08 | Downward or stable trend |
| Privacy training completion | People with current training divided by people in scope | GDPR-REG-05, GOV-REG-09 | 95 percent or more |
| Assessments completed before go-live | Processing activities that started with an approved assessment or a recorded screening divided by activities that started | PIMS-REG-08, PIMS-REG-01 | 100 percent |
| Assessment reviews overdue | Count of assessments past their next review date | PIMS-REG-08 | Zero |
| Processors with signed terms | Processors with terms signed divided by processors active | PIMS-REG-06 | 100 percent |
| Transfers with a current assessment | Transfers relying on contractual safeguards with an assessment within its review period divided by such transfers | PIMS-REG-05 | 100 percent |
| Retention checks passed | Categories checked with result Pass divided by categories checked | PIMS-REG-07 | 95 percent or more, no Fail older than one quarter |
| Consent withdrawals actioned in time | Withdrawals actioned within the time in PIMS-PRO-05 divided by withdrawals received | PIMS-REG-04, system exports | 100 percent |
| Notices reviewed in the last twelve months | Published notices with a recorded review within twelve months divided by notices published | PIMS-REG-04, GOV-REG-01 | 100 percent |
| Inventory rows reviewed in the last twelve months | PIMS-REG-01 rows with a review date within twelve months divided by active rows | PIMS-REG-01 | 100 percent |
| Privacy corrective actions overdue | Open GOV-REG-03 actions with a privacy source past their due date | GOV-REG-03 | Zero |

4.2 **Collection.** By the fifth working day after each quarter end, owners send the register exports and evidence named in the source column. The Privacy Officer computes each value, records it in GOV-REG-21 with the date and the export used, and files the exports under the evidence rules in PB-09 so that the Internal Auditor can recompute any value.

4.3 **Sampling.** Each quarter the Privacy Officer samples, in addition to the measures: five closed requests from PIMS-REG-02 for correctness of the response; every breach entry for the quality of the risk assessment; three processing activities from PIMS-REG-01 for a match between the notice, the inventory row and the system; and one withdrawal tested end to end. Sample results are recorded with the report.

4.4 **Control effectiveness grades.** For each applicable Annex A and Annex B control in ISMS-REG-01, the Privacy Officer records in ISMS-REG-02 a grade from the measures and samples that bear on it: Effective, the measures are at target and the sample found no exception; Largely effective, one measure is below target or one sample exception was found, with an action open; Partly effective, two or more measures are below target, a sample found a repeated exception, or any statutory deadline was missed; Not effective, the control is not operating or the exceptions are systemic. Partly effective and Not effective raise a corrective action in GOV-REG-03 within ten working days.

4.5 **The quarterly privacy report.** The Privacy Officer issues the report by the fifteenth working day after quarter end, with these sections: 1 Overall grade and the three things management must know; 2 Measures against targets with the trend over four quarters; 3 Breaches and incidents involving personal data, notifications made and lessons; 4 Requests from individuals, complaints and authority contact; 5 Assessments completed, overdue and the significant changes in processing; 6 Processors, sub-processor changes and transfers; 7 Training and awareness; 8 Audit findings, corrective actions and their status; 9 Risks changed in GOV-REG-05 and decisions required from management. The overall grade uses the scale in step 4.4 applied to the programme as a whole.

4.6 **Distribution and action.** The report goes to the Chief Executive Officer, the Information Security Manager and the steering committee under GOV-POL-01, and forms the privacy input to the management review under GOV-PRO-03, where decisions on resources and improvements are minuted in GOV-TPL-03 and tracked in GOV-REG-22.

4.7 **Annual consolidation.** The fourth quarter report includes the year's trend for every measure, the effectiveness grade for every applicable control, the outcome of the annual notice check under PIMS-PRO-05 and the annual retention sampling under PIMS-POL-02, and proposes targets for the following year for approval at the management review.

4.8 **Changing the measure set.** A measure is added, changed or retired by the Privacy Officer with the Information Security Manager's agreement, recorded in GOV-REG-21 with the reason, and never within a quarter already being reported, so that trends stay comparable.

## 5. Records and evidence

- GOV-REG-21 Security objectives and measures tracker: the privacy measures, their targets and each quarter's values.
- Quarterly privacy reports with the register exports and sample records behind them.
- ISMS-REG-02 Control implementation tracker: effectiveness grades for Annex A and Annex B controls.
- GOV-REG-03 Corrective action log entries raised from the grades.
- GOV-TPL-03 Management review minutes recording the privacy input and decisions.

## 6. Exceptions

A measure whose source register holds no items in the quarter is reported as Not applicable for that quarter with the reason, not as 100 percent. No other exception applies.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually at the fourth quarter consolidation, after a management review that changed the measure set, and after an audit finding about performance evaluation. Changes follow GOV-PRO-01.

## 8. Related documents

- ISMS-PRO-04 Monitoring, measurement, analysis and evaluation procedure
- GOV-REG-21 Security objectives and measures tracker
- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- GOV-PRO-03 Management review procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-REG-03 Corrective action log
- PB-09 Playbook: evidence management that survives an audit
- PIMS-POL-01 Privacy information management policy
