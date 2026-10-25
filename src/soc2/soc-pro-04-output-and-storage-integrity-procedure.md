---
id: SOC-PRO-04
title: Output distribution and storage integrity procedure
type: procedure
framework: soc2
maps:
  - SOC 2 PI1.4
  - SOC 2 PI1.5
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How outputs of an in-scope service are checked for completeness and accuracy, delivered on time to authorised recipients only, corrected when wrong, and how inputs, items in processing and outputs are stored so that alteration or loss is prevented or detected.
---
## 1. Purpose

This procedure puts SOC-POL-01 statements 4.7 to 4.9 into practice. It defines the catalogue of outputs, the checks an output passes before release, the controls on who receives it and how, the handling of corrections, and the integrity controls over every store that holds processing data.

## 2. Scope

All outputs of services whose processing integrity category is in the report scope: files, reports, interface responses, notifications and data feeds to customers or other systems. It also covers every data store holding inputs, items in processing or outputs for those services, including temporary and queue storage.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| System Owner | Keeps the output catalogue and recipient lists, approves recipient changes, reviews monthly measures. |
| Operations team | Monitors delivery schedules, performs completeness and accuracy checks, handles failed deliveries and reissues. |
| Developer | Implements generation checks, checksums and delivery monitoring as specified. |
| Customer authorised contact | Requests recipient changes in writing and acknowledges deliveries where the specification requires. |
| Information Security Manager | Tests the controls under SOC-PRO-01. |

## 4. Procedure

4.1 **Output catalogue.** The System Owner keeps, within the processing specification, a catalogue of every output: name, content, recipients, channel, format, schedule and deadline, completeness and accuracy checks, retention period and store. A new output is catalogued before it goes live.

4.2 **Completeness checks.** At generation the system computes the record count and, for numeric values, the control total of each output, and compares them to the items processed for that run. A checksum of each output file is computed at generation and delivered with the file or published where the recipient can verify it. Sequenced outputs carry a sequence number so that a missing delivery is visible to the recipient.

4.3 **Accuracy checks.** The system applies automated assertions to each output before release: totals balance to inputs, mandatory fields present, no empty values where the specification forbids them, values inside expected ranges. For an output carrying financial values or customer-visible figures, a member of the operations team who did not generate it verifies a sample of [Number] items against source data each run, or each day for continuous outputs, and records the result.

4.4 **Timeliness.** Every scheduled output is registered in the job monitor with its deadline. The monitor alerts the operations team if the output has not been delivered [Number] minutes before the deadline. A missed deadline is recorded with cause and, where a customer commitment is missed, handled as an incident under GOV-PRO-07.

4.5 **Authorised recipients.** The System Owner keeps a recipient list for each output, naming the accounts, addresses or endpoints and the customer or team each belongs to. Delivery goes only to listed recipients, only by the catalogued channel, and over encrypted transport under GOV-PRO-23 and GOV-PRO-20. The recipient list is reviewed quarterly with the access reviews in GOV-REG-12 and the review is recorded.

4.6 **Recipient changes.** A change to a recipient list requires a written request from the customer authorised contact or the internal owner, verification of the requester's identity by a method independent of the request, and approval by the System Owner. The change is recorded with request, approver and date.

4.7 **Delivery confirmation.** The system records each delivery with time, recipient and result. Where the specification requires acknowledgement, the recipient's acknowledgement or the channel's delivery receipt is captured. A failed delivery is retried as the specification states and then escalated to the operations team within [Number] minutes.

4.8 **Corrections and reissue.** An output found to be wrong is reissued with a version marker and a note of what changed. The original is retained unaltered. The recipient is told what changed, why, and which version to use. The cause is entered in the processing error log and, where systemic, raised under GOV-PRO-04.

4.9 **Storage integrity.** Every store holding inputs, items in processing or outputs has access restricted under GOV-PRO-10 to the service identities and roles the specification names. Where the platform offers versioning, write-once retention or object locking, the System Owner enables it for output stores. Each stored object carries a checksum computed on write.

4.10 **Integrity verification.** The operations team verifies stored checksums on a schedule: monthly for a random sample of at least [Number] objects per store, and in full before any migration and after any restore. A mismatch is an incident under GOV-PRO-07 and the affected objects are restored from backup under GOV-PRO-12.

4.11 **Retention and disposal.** Stored processing data is kept for the period in PIMS-REG-07 and then deleted by the method PIMS-POL-02 names, with the deletion recorded. A legal hold under GOV-PRO-25 suspends deletion for the objects it names.

4.12 **Backup and capacity.** Processing stores are backed up under GOV-PRO-12, and the quarterly restore test includes verifying the checksum of at least one restored output. Capacity thresholds for processing stores are monitored under GOV-PRO-19 and a failed write raises an alert.

4.13 **Monitoring.** The System Owner reviews monthly: outputs delivered late, completeness or accuracy check failures, failed deliveries, reissues, recipient changes, integrity verification results and disposal actions.

## 5. Records and evidence

- The output catalogue and recipient lists, with quarterly review records.
- Generation check results, checksums and sequence records per run.
- Sample accuracy verification records.
- Job monitor alerts and delivery logs with acknowledgements.
- Recipient change requests and approvals.
- Reissue records and the processing error log.
- Integrity verification results, disposal records and restore test results.

## 6. Exceptions

An output may be delivered to an unlisted recipient only in an incident, on the written instruction of the System Owner, with the delivery recorded and the recipient list corrected within one working day. No exception permits alteration of an original output after release.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any processing incident or integrity failure, and when an output or store is added or changed. Changes follow GOV-PRO-01.

## 8. Related documents

- SOC-POL-01 Processing integrity policy
- SOC-PRO-03 Input validation and reconciliation procedure
- GOV-PRO-23 Information transfer and data loss prevention procedure
- GOV-PRO-20 Cryptography and key management procedure
- GOV-PRO-12 Backup and restore testing procedure
- GOV-PRO-19 Capacity and availability management procedure
- PIMS-POL-02 Data retention and disposal policy
- PIMS-REG-07 Retention schedule
- SOC-REG-01 Trust Services Criteria control matrix
