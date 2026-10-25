---
id: GOV-PRO-12
title: Backup and Restore Testing Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.13
  - SOC 2 A1.2
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: What is backed up, how often and for how long, how backups are protected from the events that threaten the originals, and how restores are tested so that recovery is known to work before it is needed.
---
## 1. Purpose

This procedure keeps [Organisation]'s information recoverable. It defines the scope, frequency, retention and protection of backups, and a restore testing cycle whose results are recorded, so that recovery objectives are met in practice.

## 2. Scope

It applies to all production data and the configuration needed to rebuild production services: databases, file and object storage, application configuration, infrastructure definitions, identity and access configuration, logs held for retention, source code repositories, and the administrative data of software as a service where the provider does not back it up on [Organisation]'s behalf. Personal devices and non-production environments are out of scope unless they hold the only copy of a controlled record.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| System Owner | Decides what is backed up for their system, its frequency, retention and recovery objectives, and signs off restore tests. |
| Backup administrator | Configures and monitors backup jobs, performs restores and restore tests, records results in GOV-REG-15. |
| Information Security Manager | Approves the protection design, reviews GOV-REG-15 quarterly, confirms alignment with the retention schedule. |
| Head of Engineering | Owns this procedure, provides capacity and runs the annual recovery exercise. |
| Privacy Officer | Confirms that retention and deletion of personal data in backups meet PIMS-POL-02. |

## 4. Procedure

4.1 **Backup requirements.** For every system in GOV-REG-10, the System Owner records the data sets to back up, the recovery point objective and recovery time objective from the business impact analysis (GOV-TPL-07), and the retention period from the retention schedule (PIMS-REG-07). The backup administrator designs the schedule to meet them and records the design with the system.

4.2 **Default frequency and retention.** Unless the System Owner records a stricter requirement:

| Data set | Frequency | Retention |
|---|---|---|
| Production databases | Continuous or point-in-time capable, with a daily full copy | 35 daily copies and 12 monthly copies |
| File and object storage | Daily | 90 days, with versioning where the platform supports it |
| Configuration, infrastructure definitions, identity configuration | On every change and daily | 12 months |
| Source code repositories | Daily export to a separate account | 90 days |
| Software as a service administrative data | Weekly export where the provider offers it | 12 months |

Retention never exceeds the period the retention schedule allows for the data, except under a recorded legal hold.

4.3 **Protection.** Backups are encrypted at rest with keys managed under GOV-PRO-20, stored in a separate account, subscription or physical location from the systems they protect, and at least one copy is immutable or offline for its retention period. Credentials that can delete or alter backups are separate from production administration, require multi-factor authentication, and are listed in GOV-REG-13. Backup storage is logged under GOV-PRO-14.

4.4 **Monitoring.** The backup administrator reviews job results every working day. A failed job is investigated the same day and rerun. Two consecutive failures for a data set with a recovery point objective of 24 hours or less are reported as an incident under GOV-PRO-07.

4.5 **Quarterly restore test.** Each quarter the backup administrator restores at least one data set from every system rated priority 1 or 2 in the business impact analysis, and a rotating sample of the rest so that every data set is tested at least annually. The test restores to an isolated environment; verifies integrity by record counts, checksums, application start-up and a sample of records read by the System Owner; measures the time taken against the recovery time objective; and confirms the age of the data against the recovery point objective. The result, time, verifier and defects are recorded in GOV-REG-15. A failed test raises a corrective action under GOV-PRO-04 and a retest within 30 days.

4.6 **Annual recovery exercise.** Once a year the Head of Engineering recovers a complete critical service from backups and infrastructure definitions into a clean environment, as part of the exercise programme in GOV-PRO-13. The exercise is recorded in GOV-REG-16 and GOV-REG-15.

4.7 **Operational restores.** A restore into production requires the System Owner's written request, is performed as a change under GOV-PRO-09 (emergency path during an incident), and is recorded in GOV-REG-15 with the reason. Restored data is checked for records deleted since the backup was taken; deletions required by the retention schedule or by a data subject request are re-applied within five working days.

4.8 **Personal data in backups.** Backups are listed in the retention schedule as a storage location. Personal data in a backup is deleted when the backup expires rather than by selective deletion, and privacy notices and request responses say so. The Privacy Officer confirms this annually.

4.9 **Decommissioned systems.** When a system is retired, its final backup is retained for the retention period of its data, then deleted and recorded in GOV-REG-20. Keys needed to read a retained backup are retained for the same period (GOV-REG-18).

4.10 **Supplier-held backups.** Where a provider performs backups, the System Owner obtains the provider's backup and restore commitments in the contract (GOV-PRO-06) and tests an export or restore at least annually, recording it in GOV-REG-15.

## 5. Records and evidence

- GOV-REG-15 Backup and restore test log: every restore test and operational restore with time against objective.
- Backup requirement entries per system, with the recovery objectives.
- Backup job reports and failure tickets.
- Restore requests and approvals.
- Annual recovery exercise record in GOV-REG-16.

## 6. Exceptions

A data set may be excluded from backup only when the System Owner records in GOV-REG-10 that it can be regenerated from another backed-up source within the recovery time objective. Shortened retention or a missed quarterly test requires a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after a failed restore test, after any incident involving data loss or destructive malware, when the backup platform changes, and when the retention schedule changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-15 Backup and restore test log
- GOV-TPL-07 Business impact analysis worksheet
- GOV-PRO-13 Business continuity and ICT readiness procedure
- GOV-REG-16 Business continuity exercise log
- GOV-PRO-20 Cryptography and key management procedure
- GOV-REG-18 Cryptographic key and certificate inventory
- PIMS-POL-02 Data retention and disposal policy
- PIMS-REG-07 Retention schedule
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-PRO-09 Change management procedure
- GOV-REG-20 Media and equipment disposal log
- GOV-REG-13 Privileged account register
- GOV-PRO-06 Supplier and third party security procedure
