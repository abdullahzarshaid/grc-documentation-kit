---
id: PIMS-PRO-06
title: Privacy by design and by default procedure
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 7.4.1
  - ISO/IEC 27701 clause 7.4.2
  - ISO/IEC 27701 clause 7.4.3
  - ISO/IEC 27701 clause 7.4.4
  - ISO/IEC 27701 clause 7.4.5
  - ISO/IEC 27701 clause 7.4.6
  - ISO/IEC 27701 clause 7.4.9
  - ISO/IEC 27701 clause 8.4.1
  - ISO/IEC 27701 Annex A 7.4.1
  - ISO/IEC 27701 Annex A 7.4.2
  - ISO/IEC 27701 Annex A 7.4.4
  - ISO/IEC 27701 Annex B 8.4.1
  - GDPR Article 25
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The checklist that every product, feature, system and procurement involving personal data passes through the development and purchasing lifecycle, so that minimisation, protective defaults, access limits, retention, transparency, security and rights support are built in rather than added later.
---
## 1. Purpose

This procedure puts privacy decisions at the points where they are cheap: in the backlog, the design review, the supplier selection and the go-live gate. It turns the principles in PIMS-POL-01 into checks with evidence, and makes the most protective setting the one an individual gets without doing anything.

## 2. Scope

It applies to every new product, feature, system, integration, report, internal tool and AI feature that processes personal data, to every significant change to one, and to every procurement of a service that will process personal data, whether [Organisation] is controller or processor. It works alongside GOV-PRO-15 for development, GOV-PRO-06 for suppliers, GOV-PRO-09 for changes and PB-07 for the go-live gate.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Product Owner or Processing Owner | Raises the privacy requirements at the start, completes the checklist with the team and owns the evidence. |
| Head of Engineering and System Owner | Design and build to the checklist, verify defaults by test, and keep test environments free of production personal data. |
| Privacy Officer | Reviews the checklist at each gate, decides To confirm items, screens for an impact assessment under PIMS-PRO-02 and records the review. |
| Supplier owner | Applies the procurement path for a service that processes personal data. |
| Information Security Manager | Confirms the security checks against the Statement of Applicability. |

## 4. Procedure

4.1 **Entry points.** The procedure starts when: a product or feature involving personal data enters the backlog; a change request under GOV-TPL-08 answers Yes to personal data processing changed; a supplier is proposed under GOV-PRO-06 for a service that processes personal data; an AI feature or tool is proposed under AI-POL-02; or an existing system is found processing personal data without a record. The Product Owner opens a privacy review record with the project reference and the PIMS-REG-01 processing ID, new or existing.

4.2 **Privacy requirements.** At the same time as the security requirements in GOV-PRO-15 step 4.1, the Product Owner writes privacy requirements as backlog items with acceptance criteria: which data items are needed and why, the retention period and deletion mechanism, which settings are on by default, how individuals are informed, how each right is supported, and who may access what. The Privacy Officer screens the processing under PIMS-PRO-02 step 4.1 at this point.

4.3 **The checklist.** The team completes the checklist below at design and again before go-live, attaching evidence for each check. Each check is Verified, To confirm (with owner and date), Not implemented or Not applicable (with reason).

| Area | Checks | Evidence |
|---|---|---|
| Minimisation | Each data item is traced to a purpose; optional fields are marked optional; free text fields are limited where structured data suffices; identifiers are pseudonymised where the purpose allows; data is aggregated or anonymised for analytics. | Data dictionary with purpose per field; schema review record |
| Defaults | The most protective option is active without user action; optional sharing, profiling, marketing and public visibility are off until the individual turns them on; location, contacts and device permissions are requested only when needed and explained; settings are reversible. | Screenshots of a fresh account; configuration export; test case results |
| Access | Access to personal data is by role and least privilege under GOV-PRO-10; administrative access to personal data is logged; support staff see only what the case needs; bulk export is restricted and logged. | Role matrix; log sample; GOV-REG-12 review |
| Retention | Retention and deletion are configured per PIMS-REG-07; deletion covers derived data, caches, search indexes and processor copies; temporary files and exports are removed on a schedule; backups expire within their cycle. | Configuration export; deletion test result; PIMS-REG-07 row |
| Transparency | The notice covers the processing and is shown at collection; in-product explanations exist where data use would surprise; changes to the notice are versioned under PIMS-PRO-05. | Notice version reference; screenshots of the collection point |
| Security | Data is encrypted in transit and at rest under GOV-PRO-20; environments are separated and test environments hold no production personal data; secrets are managed under GOV-PRO-15; logging under GOV-PRO-14 does not capture personal data it does not need; transfers use an approved channel under GOV-PRO-23. | ISMS-REG-01 references; configuration evidence; test data confirmation |
| Rights support | The system can find all data about one individual, export it in a machine-readable format, correct it, delete it, restrict it and suppress marketing, each within the times in PIMS-PRO-03; automated decisions can be reviewed by a person. | Demonstration record of each function; PIMS-PRO-03 reference |
| Accuracy | Data is validated at entry; individuals can correct their own data; stale data is flagged or expired; sources of data not from the individual are recorded. | Validation rules; correction flow test |

4.4 **Registers updated.** Before gate 2 of PIMS-PRO-02, or before go-live where no assessment is required, the Product Owner updates PIMS-REG-01 (purpose, basis, data, retention, recipients), GOV-REG-25 and GDPR-REG-02 (flows and interfaces), PIMS-REG-06 (processors) and PIMS-REG-05 (transfers), and records any new risk in GOV-REG-05.

4.5 **Test data.** Development, test and staging environments use synthetic or irreversibly masked data. A request to use production personal data outside production is an exception under GOV-PRO-24, approved by the Privacy Officer only with the same controls as production and a deletion date of no more than thirty days.

4.6 **Procurement path.** For a supplier service, the supplier owner applies the checklist to the service as offered, using GDPR-TPL-09 and the supplier's documentation and configuration options as evidence, records the result in the supplier assessment under GOV-PRO-06, and the Privacy Officer confirms processor terms based on PIMS-TPL-02 and a transfer mechanism under PIMS-POL-03 before any personal data is sent.

4.7 **Default verification.** Before go-live the System Owner creates a fresh account or tenant, records every privacy-relevant setting at its default, and attaches the record. A default that exposes data or enables optional processing without an affirmative act is a blocker at the gate in PB-07.

4.8 **Go-live gate.** The Privacy Officer reviews the completed checklist and the register updates at the gate in PB-07. Any Not implemented check in Minimisation, Defaults, Retention or Rights support stops production use of personal data until fixed; a To confirm item needs an owner and a date within thirty days; the review and its outcome are recorded on the privacy review record.

4.9 **Operation and change.** The checklist is repeated for a significant change under GOV-PRO-09 and at the assessment review in PIMS-PRO-02. New data items added through configuration, integrations or forms without a review are treated as a nonconformity under GOV-PRO-04.

4.10 **Decommissioning.** When a system or feature is retired, the System Owner exports what the schedule requires, deletes the rest under PIMS-POL-02, obtains deletion confirmation from processors, and the Product Owner sets the PIMS-REG-01 status to Ceased with the date.

## 5. Records and evidence

- The privacy review record for each project with the completed checklist, its evidence and the Privacy Officer's gate reviews.
- Updated rows in PIMS-REG-01, PIMS-REG-05, PIMS-REG-06, PIMS-REG-07, GOV-REG-25 and GDPR-REG-02.
- Default verification records and test data confirmations.
- GOV-REG-29 go-live checklist entries and GOV-TPL-12 verdict notes for the privacy area.

## 6. Exceptions

A check may be marked Not applicable only with a reason the Privacy Officer accepts. Production personal data in a non-production environment is permitted only under step 4.5. No other exception applies.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after a breach or complaint traced to a design decision, after a change in the development lifecycle under GOV-PRO-15, and after authority guidance on privacy by design. Changes follow GOV-PRO-01.

## 8. Related documents

- PIMS-POL-01 Privacy information management policy
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-PRO-03 Data subject rights handling procedure
- PIMS-PRO-05 Consent and privacy notice management procedure
- PIMS-POL-02 Data retention and disposal policy
- PIMS-POL-03 International transfer policy
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-PRO-09 Change management procedure
- GOV-TPL-08 Change request form
- GDPR-TPL-09 Supplier GDPR assessment questionnaire
- PB-07 Playbook: the go-live security and privacy gate for a software project
- AI-POL-02 AI system development, procurement and deployment policy
