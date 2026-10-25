---
id: GOV-PRO-01
title: Document Control Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 7.5
  - ISO/IEC 27701 clause 6.5
  - SOC 2 CC2.2
  - SOC 2 CC5.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How every policy, procedure, plan and record in the management system is created, identified, approved, published, changed, retained and withdrawn.
---
## 1. Purpose

This procedure keeps the management system's documented information under control, so that staff always work from the approved version, auditors can trace every change, and withdrawn documents cannot be mistaken for current ones.

## 2. Scope

It applies to every document and record that the information security and privacy management system requires: policies, procedures, plans, statements, registers, forms and the records those forms produce. It applies in every format, including word-processed files, spreadsheets, wiki pages, tickets and exported reports.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Document owner | Writes and maintains the document, proposes changes, answers questions about it. |
| Reviewer | Checks the content for accuracy and fit with other documents before approval. |
| Approver | Authorises the document for use. A policy is approved by the role named in its control block. |
| Information Security Manager | Runs this procedure, keeps the master list (GOV-REG-01), publishes approved versions, withdraws superseded ones. |
| All staff | Use only the current version from the approved location and report errors to the owner. |

## 4. Procedure

4.1 **Identification.** The owner assigns the next free identifier from the master list in the form `[Prefix]-[Type]-[Number]`, for example `ISMS-POL-03`. The identifier never changes for the life of the document and is never reused.

4.2 **Control block.** Every document carries a control block with identifier, title, type, owner role, approver role, classification, version, effective date and next review date, and a revision history table. Registers carry the identifier and purpose in rows 2 to 9 of the workbook.

4.3 **Drafting.** The owner drafts the document in the approved template, writes a version number of `0.x` while it is a draft, and marks the status as Draft in the master list.

4.4 **Review.** At least one reviewer who did not write the document reads it and records comments. The owner resolves every comment or records why it was declined.

4.5 **Approval.** The approver confirms the document in writing, by signature or by an approval record in the document system. The owner sets the version to `1.0` for a first issue, or increments the major number for a change of meaning and the minor number for a correction that does not change meaning.

4.6 **Publication.** The Information Security Manager places the approved version in the single approved location, updates GOV-REG-01 with version, date and location, and announces the change through the channel named in the communication plan. Only the approved location is authoritative; copies elsewhere are uncontrolled.

4.7 **Change.** A change request names the document, the reason, the proposed text and the requester. Changes follow steps 4.3 to 4.6. A change that affects another document triggers a review of that document within thirty days.

4.8 **Review cycle.** Each document is reviewed on the date in its control block, at least annually, and earlier after an incident, an audit finding, a change in law or contract, or a change in the organisation that affects the document. The outcome of a review is recorded even when nothing changes.

4.9 **Withdrawal.** When a document is superseded or no longer needed, the Information Security Manager marks it Withdrawn in GOV-REG-01, removes it from the approved location, and keeps one archived copy marked as withdrawn.

4.10 **Records.** Records produced by following a document (for example a completed access review, a signed acknowledgement, an audit report) are retained for the period in the retention schedule, protected against alteration, and kept legible and retrievable.

4.11 **External documents.** Standards, laws, contracts and supplier documents that the management system relies on are listed in GOV-REG-01 with their source and version, and are not altered.

## 5. Records and evidence

- GOV-REG-01 Master list of documents and records: the index of every controlled document with status, version, owner, location and review dates.
- Approval records for every issued version.
- Review records, including reviews that resulted in no change.
- The archive of withdrawn versions.

## 6. Exceptions

A document may be issued without a separate reviewer only when the approver reviews it personally and records that fact in the revision history. No other exception applies.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding about documented information. Proposed changes follow section 4.

## 8. Related documents

- GOV-REG-01 Master list of documents and records
- GOV-POL-01 Information security and privacy governance framework
