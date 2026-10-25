---
id: SOC-PRO-02
title: Subservice organisation and vendor assurance report review procedure
type: procedure
framework: soc2
maps:
  - SOC 2 CC9.2
  - SOC 2 CC3.4
  - ISO/IEC 27001:2022 Annex A 5.22
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] obtains, reviews and acts on the SOC and equivalent assurance reports of its subservice organisations and critical vendors, including bridge letters, exceptions and the complementary user entity controls those reports place on [Organisation].
---
## 1. Purpose

A subservice organisation operates controls that [Organisation]'s own service commitments depend on: hosting, identity, payment, email delivery, support tooling. This procedure makes sure those controls have been examined by somebody, that [Organisation] reads the result rather than filing it, and that the user entity controls each report expects of [Organisation] are actually in place.

## 2. Scope

Every supplier in GOV-REG-07 that is a subservice organisation named in SOC-TPL-01, every Tier 1 supplier, and any other supplier whose failure would cause [Organisation] to miss a service commitment. Assurance reports covered are SOC 1, SOC 2 and SOC 3 reports, ISO/IEC 27001 certificates with their Statement of Applicability, and other independent attestation reports a supplier offers in their place.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the procedure, performs or assigns the review, keeps the review record, decides on exceptions. |
| Supplier relationship owner | Requests reports and bridge letters, chases overdue items, holds the contract. |
| System Owner | Confirms which supplier services and locations [Organisation] uses, maps complementary user entity controls to [Organisation] controls. |
| Privacy Officer | Reviews reports for suppliers that process personal data, together with PIMS-REG-06. |
| Steering committee | Decides on continued use of a supplier with an unresolved adverse result. |

## 4. Procedure

4.1 **Identify.** When a supplier is onboarded under GOV-PRO-06, and at each annual review, the Information Security Manager marks in GOV-REG-07 whether it is a subservice organisation (its controls are necessary for [Organisation] to meet a criterion) or a vendor, and records the assurance type expected: SOC 2 Type 2, SOC 1 Type 2, ISO/IEC 27001 certificate, or questionnaire only.

4.2 **Request.** The supplier relationship owner requests the current report within 30 days of onboarding and then annually, no later than 60 days after the supplier's expected report date. The request names the services and locations [Organisation] uses so that the supplier sends the report that covers them. Reports are stored in the evidence folder area for suppliers, classified Confidential, and used only as the supplier's terms permit.

4.3 **Coverage check.** Before reading the detail, the reviewer confirms four things and records each: the report type (Type 2 is required for a subservice organisation; a Type 1 is accepted only for a supplier in its first year); the period covered; that the services, systems and locations [Organisation] uses are inside the report's scope; and that the categories match the dependency (a hosting provider must cover Security and Availability, for example). A report that fails any check is treated as absent and step 4.9 applies.

4.4 **Bridge letter.** Where the report period ended more than three months before the review date, or more than three months before the end of [Organisation]'s own examination period, the supplier relationship owner obtains a bridge letter in which the supplier states whether its controls have changed and whether it knows of any failures since the period end. A gap of more than twelve months without a new report is escalated to the steering committee.

4.5 **Opinion and exceptions.** The reviewer reads the auditor's opinion first. A qualified, adverse or disclaimed opinion is escalated to the Information Security Manager the same day. The reviewer then lists every exception in the testing section with: the control, the exception, the supplier's management response, and whether the control is one [Organisation] depends on. For each dependent exception the reviewer decides whether [Organisation]'s own controls compensate; if they do not, the reviewer raises a risk in GOV-REG-05 and a corrective action in GOV-REG-03.

4.6 **Complementary user entity controls.** The reviewer extracts the complementary user entity controls the report lists and, with the System Owner, maps each to a control in SOC-REG-01, recording the mapping in the review record. Each unmapped user entity control is a gap: it is assigned an owner and a due date of no more than 60 days, because the supplier's assurance does not hold without it.

4.7 **The supplier's own subservice organisations.** The reviewer notes the supplier's carved-out subservice organisations and whether any of them hold [Organisation] data. Those that do are added to GOV-REG-07 as fourth parties with the supplier as relationship owner, and the supplier's monitoring of them is noted in the review record.

4.8 **Review record.** For every report the reviewer completes a record with: supplier, report type and period, auditor, opinion, scope match, categories, exceptions and their disposition, user entity control mapping, bridge letter status, overall conclusion (Acceptable, Acceptable with actions, Not acceptable), reviewer and date. GOV-REG-07 is updated with the assurance type, last review date, next review date and status.

4.9 **No report available.** Where a subservice organisation cannot provide an assurance report, the Information Security Manager obtains instead a completed GOV-TPL-04 questionnaire, an independent penetration test summary dated within twelve months, and a contractual right to audit or to receive security information; records the supplier as unattested in GOV-REG-07; and raises a risk in GOV-REG-05 for the steering committee to accept or treat. For [Organisation]'s own report, an unattested subservice organisation is disclosed in SOC-TPL-01 and discussed with the external auditor before the period begins.

4.10 **Carve-out or inclusive.** For each subservice organisation the Information Security Manager records in SOC-TPL-01 whether [Organisation] uses the carve-out method (the supplier's controls are excluded from [Organisation]'s report and the complementary subservice organisation controls [Organisation] relies on are listed) or the inclusive method (the supplier's controls are examined within [Organisation]'s report, which needs the supplier's written agreement and participation). The carve-out method is the default.

4.11 **Actions and follow up.** Actions from 4.5 and 4.6 are tracked in GOV-REG-03 and reported at the quarterly supplier review. A supplier whose conclusion is Not acceptable at two consecutive reviews is referred to the steering committee for a decision on exit under GOV-PRO-06.

## 5. Records and evidence

- GOV-REG-07 Supplier register with assurance type, last and next review dates and status.
- The supplier assurance reports and bridge letters in the evidence folder.
- One review record per report, including the complementary user entity control mapping.
- Risks in GOV-REG-05 and corrective actions in GOV-REG-03 arising from exceptions or gaps.
- Steering committee minutes for escalations.

## 6. Exceptions

A Tier 1 supplier that is not a subservice organisation may be accepted on an ISO/IEC 27001 certificate and Statement of Applicability without a SOC report where the Information Security Manager records that no [Organisation] criterion depends on the supplier's controls. No exception removes the requirement to map complementary user entity controls where a report lists them.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any supplier incident, and when a new subservice organisation is added to the system boundary. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-07 Supplier register
- GOV-TPL-04 Supplier security and privacy questionnaire
- SOC-TPL-01 System description template
- SOC-REG-01 Trust Services Criteria control matrix
- SOC-GDE-01 Guide: SOC 2 in plain words
- PIMS-REG-06 Processor and sub-processor register
