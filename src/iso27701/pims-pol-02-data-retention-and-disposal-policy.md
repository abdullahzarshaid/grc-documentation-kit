---
id: PIMS-POL-02
title: Data retention and disposal policy
type: policy
framework: iso27701
maps:
  - ISO/IEC 27701 clause 7.4.7
  - ISO/IEC 27701 clause 7.4.8
  - ISO/IEC 27701 clause 7.4.5
  - ISO/IEC 27701 Annex A 7.4.7
  - ISO/IEC 27701 Annex A 7.4.8
  - ISO/IEC 27701 Annex B 8.4.2
  - ISO/IEC 27001:2022 Annex A 5.33
  - ISO/IEC 27001:2022 Annex A 8.10
  - GDPR Article 5
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The rules that decide how long each category of information is kept, what starts the clock, how it is disposed of, how legal holds suspend disposal, and how backups and logs are treated, with the schedule itself held in PIMS-REG-07.
---
## 1. Purpose

This policy keeps information for as long as it is needed and no longer. Over-retention increases the harm of every breach, makes requests from individuals harder to answer and breaks the storage limitation principle; under-retention loses records that the law, a contract or a dispute requires.

## 2. Scope

It applies to all information that [Organisation] holds, in every system, backup, archive, log, mailbox, device, paper file and supplier service, with particular rules for personal data. Where [Organisation] is a processor, the client's instructions and the agreement take precedence over the schedule, and the policy governs what happens at the end of the service.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Owns this policy and PIMS-REG-07, approves every period and its justification, imposes and lifts legal holds with the legal adviser. |
| Processing Owner | Proposes the period and trigger for each category they own and confirms the quarterly check. |
| System Owner | Configures retention and deletion in their system, runs manual disposal where configuration is impossible, and records the result. |
| Information Security Manager | Sets the retention of security logs and backups under GOV-PRO-14 and GOV-PRO-12 and supplies the disposal methods for media under GOV-PRO-16. |
| Legal adviser | Confirms statutory periods and limitation periods recorded in GOV-REG-04. |

## 4. Policy statements

4.1 **The schedule.** Every category of information is listed in PIMS-REG-07 with its systems, its retention period, the trigger that starts the period, the reason for the period, the disposal method and the owner. A category not in the schedule is added within thirty days of being found, and until then is treated as held for the default in 4.3.

4.2 **Justified periods.** Each period is justified by one of: a statutory retention requirement, a contractual requirement, the limitation period for legal claims, or a documented operational need, in that order of preference. The justification names the source in GOV-REG-04 where it is legal or contractual. "We might need it" is not a justification.

4.3 **Default period.** Personal data with no entry in the schedule is deleted [Number] months after the purpose for which it was collected ends, and at most twelve months after.

4.4 **Triggers.** Periods run from a defined event (end of contract, last activity, decision date, end of employment, financial year end, closure of a case, creation of the record), never from an undefined "when no longer needed". The trigger is recorded in the system where possible.

4.5 **Configured disposal.** Where a system can enforce retention, the System Owner configures it and records where. Where it cannot, the System Owner runs a disposal at least quarterly and records the run. The Privacy Officer samples each category at least annually and records Pass, Fail or To confirm in PIMS-REG-07.

4.6 **Disposal methods.** Personal data is disposed of by secure deletion, by irreversible anonymisation, or by return to the controller or individual. Paper is cross-cut shredded or placed in confidential waste. Media and devices are wiped or destroyed under GOV-PRO-16 and recorded in GOV-REG-20. Deleting a reference, a link or an index entry while the data remains is not disposal.

4.7 **Anonymisation.** Data counts as disposed of by anonymisation only when no party, using means reasonably likely to be used, can re-identify the individuals, and the Privacy Officer has recorded the assessment. Pseudonymised data remains personal data and stays in the schedule.

4.8 **Copies and derived data.** Disposal covers every copy: primary stores, replicas, exports, reports, caches, temporary files, search indexes, analytics data sets, test environments and data held by processors. The Processing Owner lists the locations from GOV-REG-25 and PIMS-REG-06 and confirms each.

4.9 **Backups.** Backups are kept for the period set under GOV-PRO-12 and recorded in PIMS-REG-07, so that data deleted from a primary system leaves the backups within that period without a separate deletion. Data restored from backup during recovery that had been deleted from the primary system is deleted again within five working days of the restore.

4.10 **Logs.** Logs are kept for the period set under GOV-PRO-14 and recorded in PIMS-REG-07. Logs are personal data where they identify an individual and are disposed of on the same terms; they are not kept longer than the security purpose needs because they might one day be useful.

4.11 **Legal hold.** When litigation, an investigation, an authority enquiry or a complaint is reasonably anticipated, the Privacy Officer or the legal adviser issues a written legal hold naming the categories, systems, individuals and custodians affected. Disposal of the named information is suspended, custodians are instructed in writing, configured deletion is paused for the affected data, and the hold is reviewed every ninety days and lifted in writing. Legal holds are listed in PIMS-REG-07.

4.12 **End of a processor service.** When [Organisation] stops acting as processor for a client, it returns or deletes the client's personal data as the agreement based on PIMS-TPL-02 requires, within the time it states, and provides written confirmation of deletion. When a supplier stops processing for [Organisation], the supplier owner obtains the same confirmation under GOV-PRO-06 and records it in PIMS-REG-06.

4.13 **Requests and breaches.** Erasure requests under PIMS-PRO-03 override the schedule unless an exemption applies. Records of requests, breaches, assessments and consents are themselves in the schedule, because they prove compliance.

4.14 **Schedule examples.** The following rows illustrate the form of PIMS-REG-07. Every period is an example for [Organisation] to replace from its own obligations in GOV-REG-04; none is a legal statement.

| Category | Trigger | Period | Disposal |
|---|---|---|---|
| Customer account and contract data | End of contract | [Number] years, set by the limitation period | Secure deletion, anonymised aggregates may remain |
| Prospect and marketing contacts | Last meaningful interaction | [Number] months | Secure deletion and suppression entry kept |
| Support tickets and chat transcripts | Ticket closure | [Number] years | Secure deletion |
| Employee records | End of employment | [Number] years, set by employment and tax law | Secure deletion, paper shredded |
| Unsuccessful applicant data | Recruitment decision | [Number] months | Secure deletion |
| Payroll and tax records | End of the tax year | As set by tax law in GOV-REG-04 | Secure deletion |
| Building access and visitor logs | Entry date | [Number] months | Secure deletion |
| Security logs | Event date | Period set under GOV-PRO-14 | Automatic expiry |
| Backups | Backup creation | Period set under GOV-PRO-12 | Automatic expiry |
| Data subject request records | Request closure | [Number] years | Secure deletion |
| Personal data breach records | Breach closure | [Number] years | Secure deletion |
| Consent records | Withdrawal or end of processing | Period set by the limitation period | Secure deletion |
| Impact assessments and processing inventory | Processing ceases | Life of the processing plus [Number] years | Archive then secure deletion |

## 5. Records and evidence

- PIMS-REG-07 Retention schedule: every category with its period, trigger, configuration, check results and legal holds.
- Configuration exports showing retention settings in each system.
- Disposal run records and GOV-REG-20 Media and equipment disposal log.
- Deletion confirmations from processors and to clients.
- Legal hold notices, custodian instructions and lift notices.

## 6. Exceptions

An extension beyond the schedule for a named data set is approved by the Privacy Officer for a stated reason and a stated end date of no more than twelve months, recorded in PIMS-REG-07, and reviewed at the end date. A legal hold is not an exception; it is a suspension under 4.11.

## 7. Review and maintenance

The Privacy Officer reviews this policy and the schedule annually, after a change in statutory periods in GOV-REG-04, after a new system or processor starts holding personal data, and after a breach or request that revealed over-retention. Changes follow GOV-PRO-01.

## 8. Related documents

- PIMS-REG-07 Retention schedule
- PIMS-POL-01 Privacy information management policy
- PIMS-PRO-03 Data subject rights handling procedure
- PIMS-TPL-02 Data processing agreement template
- GOV-PRO-12 Backup and restore testing procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-REG-20 Media and equipment disposal log
- GOV-REG-04 Legal, regulatory and contractual register
- GOV-PRO-25 Legal, regulatory and contractual compliance procedure
