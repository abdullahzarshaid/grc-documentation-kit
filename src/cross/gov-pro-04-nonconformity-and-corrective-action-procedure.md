---
id: GOV-PRO-04
title: Nonconformity and corrective action procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 10.1
  - ISO/IEC 27001:2022 clause 10.2
  - SOC 2 CC4.2
  - SOC 2 CC5.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] records a nonconformity, contains it, finds its root cause, corrects the cause, verifies that the correction worked, and learns from the pattern across many nonconformities.
---
## 1. Purpose

A nonconformity is any failure to meet a requirement of the management system, whether the requirement comes from a kit document, an adopted framework, a law or a contract. This procedure turns each one into a verified improvement rather than a repeated fix.

## 2. Scope

It applies to every nonconformity, whatever its source, across the information security and privacy management system. Incident response itself follows GOV-PRO-07; this procedure starts when an incident review identifies a failed or missing control.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Anyone | Raises a suspected nonconformity. |
| Information Security Manager | Logs every nonconformity in GOV-REG-03, assigns an owner, runs the monthly review, performs trend analysis, closes minor nonconformities. |
| Action owner | Contains the problem, leads the root cause analysis, implements the corrective action, provides evidence. |
| Verifier | A person other than the action owner who checks effectiveness. Usually the Internal Auditor or the Information Security Manager. |
| Executive sponsor | Closes major nonconformities and decides on actions that need resources beyond the owner's authority. |
| Privacy Officer | Co-owns nonconformities involving personal data and decides whether a breach assessment under PIMS-PRO-04 is needed. |

## 4. Procedure

4.1 **Sources.** Nonconformities arise from internal audits (GOV-PRO-02), external audits, incidents and post-incident reviews (GOV-PRO-07), management review (GOV-PRO-03), monitoring and measurement results (ISMS-PRO-04), complaints from customers or data subjects, supplier reviews, readiness assessments and staff reports. All are handled the same way.

4.2 **Raising.** The person who finds the problem completes the first part of GOV-TPL-02: what was observed, where, when, and the requirement it appears to breach. The Information Security Manager logs it in GOV-REG-03 within two working days, assigns a reference, a grade (Major, Minor, Observation or Opportunity, as defined in GOV-PRO-02) and an action owner, and sets the status to Open.

4.3 **Correction.** The action owner first contains the problem: stops the nonconforming activity, restores the control, or limits the consequences. The correction is recorded on GOV-TPL-02 with its date. For a major nonconformity the correction is in place within five working days; for a minor, within twenty.

4.4 **Deciding on corrective action.** Correction removes the symptom; corrective action removes the cause. The action owner and the Information Security Manager decide whether corrective action is needed by asking whether the problem could recur, whether it has occurred before, whether the same cause could exist elsewhere, and what the impact of recurrence would be. A major nonconformity always needs corrective action. The decision and its reasons are recorded.

4.5 **Root cause analysis.** The action owner leads the analysis with the people who do the work, using the five whys for a simple failure or a fishbone (cause and effect) diagram where several factors interact. The analysis stops at a cause the organisation can act on, not at "human error". The root cause is written on GOV-TPL-02 and in GOV-REG-03.

4.6 **Corrective action plan.** The action owner writes the plan on GOV-TPL-02: the actions, the person responsible for each, the resources needed and the due date. The due date is within thirty days of raising for a major nonconformity and within ninety days for a minor, unless the executive sponsor approves a longer period in writing. The Information Security Manager records the plan and sets the status to In progress.

4.7 **Extending the check.** Before closing the plan, the action owner checks whether the same cause exists in other systems, teams or locations, and raises a linked entry in GOV-REG-03 for each place where it does.

4.8 **Implementation.** The action owner implements the plan, attaches evidence of each completed action to GOV-TPL-02, and updates any document the change affects through GOV-PRO-01. Where the action changes a risk, the owner updates GOV-REG-05.

4.9 **Effectiveness verification.** After the corrected process has operated for at least ninety days, or for three operating cycles where the control runs less often, the verifier tests whether the nonconformity has recurred and whether the control now operates as intended. The verifier samples records from the period, interviews the people involved and inspects the configuration or output. The result (Effective or Not effective), the method, the date and the verifier's role are recorded on GOV-TPL-02 and in GOV-REG-03, and the status becomes Verified. A result of Not effective reopens the root cause analysis at 4.5.

4.10 **Closure.** The Information Security Manager closes a minor nonconformity and the executive sponsor closes a major one, in each case only after the verification is recorded as Effective. The closer signs GOV-TPL-02 and the status becomes Closed. Observations and opportunities are closed when the decision to act or not act is recorded.

4.11 **Monthly review.** The Information Security Manager reviews GOV-REG-03 monthly, chases overdue actions, and escalates any action more than thirty days overdue to the executive sponsor.

4.12 **Trend analysis.** Each quarter the Information Security Manager analyses closed and open entries by source, area, requirement and root cause category, identifies repeated causes, and reports the trends with proposed systemic actions to the steering committee and to management review.

## 5. Records and evidence

- GOV-REG-03 Corrective action log: every nonconformity from raising to closure.
- GOV-TPL-02 Corrective action request forms with evidence attached.
- Quarterly trend analysis reports.
- Updated documents and risk entries resulting from corrective actions.

## 6. Exceptions

A due date may be extended once, by the executive sponsor in writing, with the reason recorded in GOV-REG-03. The verification period in 4.9 may be shortened only where the control runs continuously and the verifier can test at least twenty-five records.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding about corrective action. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-02 Corrective action request form
- GOV-REG-03 Corrective action log
- GOV-PRO-02 Internal audit procedure
- GOV-PRO-03 Management review procedure
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-PRO-07 Information security incident management procedure
- PIMS-PRO-04 Personal data breach assessment and notification procedure
