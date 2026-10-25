---
id: SOC-POL-01
title: Processing integrity policy
type: policy
framework: soc2
maps:
  - SOC 2 PI1.1
  - SOC 2 PI1.2
  - SOC 2 PI1.3
  - SOC 2 PI1.4
  - SOC 2 PI1.5
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The rules that keep [Organisation]'s processing complete, accurate, timely and authorised, from the moment an input arrives to the moment an output is delivered and the data is stored, and the records that prove it.
---
## 1. Purpose

Processing integrity means that [Organisation]'s systems do what they promise: inputs are accepted only when complete, accurate and authorised; processing follows the written specification; outputs reach the right people complete, correct and on time; and stored data is not silently altered or lost. This policy sets the rules the processing integrity criteria are tested against.

## 2. Scope

Every service [Organisation] provides whose processing integrity category is in the report scope, the systems inside the boundary in SOC-TPL-01, the interfaces that feed them, the outputs they deliver and the data stores that hold inputs, items in processing and outputs. It applies to automated processing and to the manual steps staff perform within it.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns the policy, approves processing specifications, resources the controls. |
| System Owner | Writes and maintains the processing specification for each service, operates the controls in SOC-PRO-03 and SOC-PRO-04, investigates failures. |
| Product or service manager | Agrees processing commitments with customers and keeps them consistent with the specification. |
| Operations team | Monitors jobs, performs reconciliations, handles rejected items and corrections. |
| Information Security Manager | Tests the controls under SOC-PRO-01 and reports results. |

## 4. Policy statements

4.1 **Specification.** Every in-scope service has a written processing specification, approved by the Head of Engineering, that defines its inputs, validation rules, processing logic in plain words, outputs, recipients, timing commitments and the data retained. The specification is controlled under GOV-PRO-01 and changes only through GOV-PRO-09.

4.2 **Commitments match the specification.** Processing commitments made to customers in contracts, service descriptions and the system description in SOC-TPL-01 are derived from the specification. The product or service manager reviews them against it at least annually and at every specification change, and records the review.

4.3 **Inputs.** A system accepts an input only after validating it against the specification's rules for format, range, referential integrity, completeness, duplication and authorisation. A rejected input is held in a quarantine with its reason, reported to the submitter within [Number] hours, and never silently discarded or silently corrected. SOC-PRO-03 governs.

4.4 **Manual inputs.** A manual input that changes customer data or a financial value is entered by one person and verified by a second before it takes effect, or is covered by a system check that the System Owner has documented as equivalent.

4.5 **Processing.** Every processing job records its start, end, items in, items out, items rejected and errors in a log kept under GOV-PRO-14. A job that fails, or whose counts fall outside the specification's tolerance, raises an alert to the operations team within [Number] minutes and is not marked complete until resolved.

4.6 **Reconciliation.** The operations team reconciles inputs received to items processed and outputs produced at least daily for each in-scope service, investigates every difference the same working day, and records the result with a preparer and a separate reviewer.

4.7 **Outputs.** Outputs are delivered complete, accurate and within the time the specification states, to the recipients and by the channel it names, over encrypted transport under GOV-PRO-23. A missed or incomplete delivery is detected by the system, not by the recipient, and is treated as an incident under GOV-PRO-07 when a customer commitment is missed. SOC-PRO-04 governs.

4.8 **Corrections.** An output found to be wrong is corrected by reissue with a version marker. The original is retained, the recipient is told what changed and why, and the cause is entered in the processing error log, with a corrective action under GOV-PRO-04 where the cause is systemic.

4.9 **Storage.** Inputs, items in processing and outputs are stored with controls that prevent and detect unauthorised alteration: access restriction under GOV-PRO-10, integrity checks under SOC-PRO-04 and backups under GOV-PRO-12. They are kept for the period in PIMS-REG-07 and are recoverable to the state at any processing step the specification requires.

4.10 **Segregation of duties.** No single person may both submit an input and approve it, both develop processing logic and deploy it to production, or both perform a reconciliation and resolve its differences without a second person's record. Where headcount makes this impossible, the compensating review is recorded in GOV-REG-06.

4.11 **Errors and incidents.** Processing errors are logged with cause, items affected, correction and date. An error that affects a customer commitment, more than [Number] items, or any financial value is an incident under GOV-PRO-07.

4.12 **Measures.** The System Owner reports monthly: inputs rejected by reason, reconciliation differences and time to resolve, outputs delivered late, corrections issued, and open processing errors. Targets are held in GOV-REG-21 and reviewed at management review under GOV-PRO-03.

## 5. Records and evidence

- Approved processing specifications per service, with their change history in GOV-REG-11.
- Input rejection and quarantine records with submitter notifications.
- Job logs and alerts under GOV-PRO-14.
- Daily reconciliation records with preparer and reviewer, and difference investigations.
- Output delivery logs, acknowledgements and reissue records.
- The processing error log and the monthly measures report.
- SOC-PRO-01 workpapers for the processing integrity controls in SOC-REG-01.

## 6. Exceptions

A service may deviate from a statement only under GOV-PRO-24, with a compensating control approved by the Head of Engineering and a duration of no more than twelve months. No exception applies to statement 4.3 (no silent discard or correction) or statement 4.8 (retention of the original output).

## 7. Review and maintenance

The Head of Engineering reviews this policy annually, after any processing incident, and when a new service enters the report scope. Changes follow GOV-PRO-01.

## 8. Related documents

- SOC-PRO-03 Input validation and reconciliation procedure
- SOC-PRO-04 Output distribution and storage integrity procedure
- SOC-TPL-01 System description template
- SOC-REG-01 Trust Services Criteria control matrix
- GOV-PRO-09 Change management procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-PRO-12 Backup and restore testing procedure
- PIMS-REG-07 Retention schedule
