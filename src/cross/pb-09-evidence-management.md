---
id: PB-09
title: "Playbook: Evidence Management That Survives an Audit"
type: playbook
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 7.5.3
  - ISO/IEC 27001:2022 clause 9.2
  - SOC 2 CC4.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How to collect, name, protect and present the evidence that proves controls operate, so that an auditor, a reviewer or an investigator can rely on it without the person who collected it in the room.
---
## 1. What evidence is for

Evidence is the proof that a control operated at a point in time. Three audiences depend on it. The auditor, internal or external, who tests a control by sampling its records. The reviewer at a gate or a readiness assessment, who must set a status without taking anyone's word for it. And the organisation itself after an incident, when it has to show what was configured, who had access and when a change was made. To all three, a control without evidence is a control that did not operate. That is not cynicism; it is the only position a person can take who was not there.

Good evidence shares five properties. It is dated by the system that produced it. It shows where it came from: the account, the environment, the tenant or region. It is complete rather than illustrative: a population rather than one example. It is unaltered, and you can show that it is. And it is findable by someone other than the person who filed it.

## 2. The no-assumption rule

Every unknown becomes To confirm, plus an owner, plus a due date.

Never write "assumed", "should be", "probably", "I believe" or "as far as we know" in a register, a review or a report. If you did not see it, it is To confirm. This applies in GOV-REG-28, in GOV-REG-29, in ISMS-REG-02, in audit preparation and in every incident timeline. The reason is practical. An assumption converts into an audit finding at the worst possible moment; a To confirm row converts into a task today. The two cost the same to write and behave completely differently afterwards.

The rule has a corollary. A To confirm row that passes its due date is escalated to the sponsor or the Information Security Manager, not quietly extended. Extended unknowns are assumptions wearing a different label.

## 3. The evidence folder structure

One root folder per period: the audit cycle year for the management system, or one per project for a gate. Under the root, numbered areas. The first ten match the ten domains of GOV-REG-28 so that a readiness assessment, an internal audit and an external audit all file in the same place.

| Area | Holds |
|---|---|
| 01 Governance | Steering minutes, management review packs and minutes, objectives reports, policy approvals |
| 02 Scope and context | Scope statement, context analysis, interested parties, legal register extracts |
| 03 Risk | Risk assessment exports, treatment plans, acceptances and exceptions, Statement of Applicability |
| 04 Policies and documents | Approved versions, review records, acknowledgement exports |
| 05 People | Screening confirmations, training completion exports, induction records, leaver checklists |
| 06 Access | Access request approvals, access review exports, privileged account lists, multi-factor settings |
| 07 Assets and data | Asset register exports, classification records, processing inventory, retention checks, disposal records |
| 08 Technology and cloud | Configuration exports, vulnerability scan exports, change tickets, backup and restore records, log retention settings |
| 09 Suppliers | Questionnaires, certificates, assurance reports, contracts, review notes, exit confirmations |
| 10 Incidents and continuity | Incident records, post-incident reviews, breach assessments, exercise records, continuity plans and test results |
| 11 Audit and review | Internal audit plans and reports, corrective action records, external audit correspondence |
| 12 Projects and gates | One subfolder per gate with its GOV-REG-29 copy, evidence and GOV-TPL-12 note |

Inside each area, split by system or by control only when volume demands it. Every area carries two files: an index, which is a simple table of file name, what it proves, which control or question it serves, the date collected and who collected it; and a hash list, described in section 7. The folder is classified Confidential, because evidence routinely contains names, account identifiers and configuration detail. Read access is for reviewers and auditors, write access for collectors, and nobody deletes except the Information Security Manager under the retention schedule.

## 4. File naming

Name every file as date, system, area, what, joined with underscores and in lower case:

```
YYYYMMDD_system_area_what.ext
YYYYMMDD_identityprovider_access_mfa-policy-export.csv
YYYYMMDD_backupservice_backups_restore-test-result.pdf
YYYYMMDD_cloudaccount_logging_retention-setting-01.png
```

The date is the date the evidence was collected, not the date it was filed, and it comes first so that a folder sorts into a timeline. The system is one word that anyone in the organisation would recognise. The area matches the folder. The "what" says what the file proves in two or three words. Add a two digit sequence number when several screenshots make up one proof. Never use "final", "new", "latest", "v2" or a person's name in a file name; the index records who collected it, and the date already says which is latest.

## 5. What a screenshot must show

A screenshot is admissible only when it answers four questions without the collector present: who was logged in, where, when, and what is being shown.

- **Account.** The signed-in user is visible, usually in the top corner of the console. An auditor needs to know the setting was read with an account entitled to see the whole picture.
- **Environment.** The tenant, subscription, account identifier or region is visible, or the navigation path makes it unambiguous. Production and staging consoles look identical; the identifier is the only difference.
- **Date and time.** The operating system clock or the page's own timestamp is in the frame. A file's modification date is not enough, because files are copied.
- **The whole window.** Include the address bar or the navigation path and the page title. A cropped widget proves nothing about where it came from.
- **One fact per image.** If a proof needs three settings, take three numbered screenshots, not one scrolled composite.
- **Masking.** Mask secrets, keys, passwords and personal data of individuals who are not needed for the proof, with a solid block so that the masking is obvious. Never blur, never crop to hide, never edit anything else.

A screenshot that fails any of these is To confirm until retaken.

## 6. Exports over screenshots

Where the system can export, export. A system export is complete where a screenshot is a sample; it is dated and attributed by the system; it can be filtered, counted and reconciled; and it is far harder to fabricate. Auditors sample from populations, so give them populations.

| Control | Prefer this export | Not this |
|---|---|---|
| Access review | The full user and role list for the system as a dated file, with the reviewer's decisions beside each row in GOV-REG-12 | A screenshot of the first page of users |
| Change management | The change ticket export for the audit period | Three example tickets chosen by the team |
| Backup | The job history export showing every run and result for the period | A screenshot of a green status tile |
| Training | The completion export from the training record with names and dates, filed against GOV-REG-09 | An email saying everyone finished |
| Vulnerability management | The scan result export with severities and dates, reconciled to GOV-REG-14 | A dashboard summary |
| Logging | The retention configuration export and a log query result for a known event | A screenshot of a log viewer |

Screenshots remain right for settings pages with no export and for events that are visual by nature, such as an alert arriving in the monitored channel.

## 7. Integrity: hashing and protection

Compute a hash value, using a current algorithm such as SHA-256, for every file at the moment of collection. Record it in the area's hash list with the file name, the collector and the date. Keep a copy of every hash list in a location the collectors cannot modify: the evidence index held by the Information Security Manager, or storage with a write-once setting. Re-verify the hashes before an audit and after any migration of the folder, and record that the verification was done.

This answers two questions before they are asked. From an auditor: how do you know this file was not altered after the fact. From an investigator after an incident: is this the configuration that was in place on that date. In both cases the answer is a hash list in a place the person who filed the evidence could not reach.

## 8. Retention and access

Keep evidence for at least one full certification cycle, three years for ISO/IEC 27001, or for the SOC 2 examination period plus the following examination, whichever is longer. Where client contracts require longer, GOV-REG-04 holds the period. Evidence that contains personal data follows PIMS-POL-02 and the schedule in PIMS-REG-07 as well: export only the columns the proof needs, and when the retention period ends, delete the evidence and record the deletion in the area index.

Review who has access to the evidence folder quarterly, as part of the access reviews in GOV-REG-12. Auditors receive read access to the period under audit for the duration of the audit, and that access is removed and recorded when the audit closes, exactly as reviewer accounts are removed after a gate under PB-07.

## 9. What auditors reject

Each of these has cost an organisation a finding. None of them is about the control; all of them are about the evidence.

1. Undated screenshots, or screenshots whose only date is the file's modification time.
2. Screenshots that show neither the account nor the environment, so that production cannot be distinguished from staging.
3. Cropped images with no page context.
4. A policy document offered as proof that the control operates. A policy proves the rule exists; a record proves it was followed.
5. Evidence from outside the audit period, however good.
6. A single example where a population was requested, or examples chosen by the team rather than sampled by the auditor.
7. Evidence produced during the audit for a control that should have operated months earlier. The evidence may be genuine; the control was not operating.
8. A file whose creation date contradicts its content.
9. Exports that have been opened and saved in a spreadsheet application, losing the original format and gaining an edit history.
10. A ticket closed with no record of what was done or who verified it.
11. A register that is still the blank template, or has entries that stop three months ago.
12. A signed acknowledgement that does not say which version of which policy was acknowledged, or when.
13. An email that says "confirmed" with nothing attached.

If you recognise one of your own files in this list, mark its row To confirm today and collect it properly. It costs an hour now and a finding later.

## 10. The evidence footer

Every artefact that draws a conclusion ends with three lines. Audit reports, review minutes, risk assessments, gate verdict notes, readiness results, supplier assessments and post-incident reviews all qualify.

```
Evidence used: [file names or index references the conclusions rest on]
Evidence missing: [items that were To confirm when this was written, each with owner and due date]
Owner: [the role that holds this artefact and will update it]
```

The footer does two things. It lets a reader separate what the author saw from what the author believed, which is the difference between a finding and an opinion. And it turns every artefact into the to-do list for the next cycle, because the missing evidence is written down where the next person will look. An artefact with an empty "Evidence missing" line is making a strong claim; the author should be sure it is true.

## 11. Building the habit: evidence by frequency

Evidence collected on the day a control runs costs minutes. Evidence reconstructed before an audit costs days and is often rejected under section 9. Attach the collection to the control's own rhythm.

| Frequency | Evidence produced at the time | Filed against |
|---|---|---|
| Daily | Alert triage notes under GOV-PRO-14 | 08 Technology and cloud |
| Weekly | Vulnerability scan export, backup job history export | GOV-REG-14, GOV-REG-15 |
| Monthly | Incident metrics report, change log export, training completion export | GOV-REG-08, GOV-REG-11, GOV-REG-09 |
| Quarterly | Access review exports with decisions, restore test record, Tier 1 supplier review notes, steering committee minutes | GOV-REG-12, GOV-REG-15, GOV-REG-07, 01 Governance |
| Annually | Risk assessment export, management review minutes, internal audit report, policy acknowledgement export, continuity exercise record, supplier annual reviews | GOV-REG-05, GOV-TPL-03, GOV-TPL-01, GOV-REG-23, GOV-REG-16, GOV-REG-07 |

Organisations heading for SOC 2 keep the same rhythm in SOC-REG-02, which is the calendar form of this table. Whichever form you use, the test is the same: on any given day, could an auditor open the folder and find last month's evidence without asking anyone.

## 12. Related documents

- GOV-PRO-01 Document control procedure
- GOV-REG-28 Readiness questionnaire
- GOV-REG-29 Go-live gate checklist
- GOV-TPL-12 Readiness verdict note
- PB-07 Playbook: the go-live security and privacy gate for a software project
- PB-08 Playbook: running a readiness assessment with the questionnaire
- GOV-PRO-02 Internal audit procedure
- ISMS-REG-02 Control implementation tracker
- SOC-REG-02 Evidence calendar
- PIMS-POL-02 Data retention and disposal policy
