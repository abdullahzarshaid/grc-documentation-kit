---
id: GOV-PRO-25
title: Legal, regulatory and contractual compliance procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.31
  - ISO/IEC 27001:2022 Annex A 5.32
  - ISO/IEC 27001:2022 Annex A 5.33
  - ISO/IEC 27001:2022 Annex A 5.34
  - ISO/IEC 27001:2022 Annex A 5.35
  - ISO/IEC 27001:2022 Annex A 5.36
  - SOC 2 CC1.1
  - SOC 2 CC2.3
  - GDPR Article 24
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] identifies the laws, regulations, contracts and scheme rules that apply to its information, records them, maps each to controls and evidence, watches for change, protects intellectual property and records, and has its compliance independently reviewed.
---
## 1. Purpose

An organisation cannot show it is compliant until it can list what it must comply with. This procedure builds and maintains that list, ties every obligation to the control and the evidence that satisfies it, and makes sure someone notices when the obligations change.

## 2. Scope

It covers obligations that affect information security, privacy and the records of the organisation: data protection law, sector regulation, intellectual property and licensing law, records retention duties, employment law as it touches monitoring and screening, export and sanctions rules as they touch technology, customer and supplier contract terms, and the rules of the certification and attestation schemes the organisation has joined.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Owns this procedure and GOV-REG-04, leads identification and change monitoring, advises on personal data obligations. |
| Information Security Manager | Maps obligations to controls and evidence, raises gaps as risks or corrective actions. |
| Legal counsel (internal or external) | Confirms the interpretation of each obligation and reviews contract clauses. |
| Obligation owner | A manager named for each row of GOV-REG-04. Operates the controls and keeps the evidence. |
| Head of Engineering | Owns software licensing and open source compliance. |
| Internal Auditor | Performs the independent review in 4.9. |

## 4. Procedure

4.1 **Identify by jurisdiction.** The Privacy Officer lists every jurisdiction where the organisation is established, employs people, sells, hosts or stores data, or has customers who impose their own law by contract. For each, with legal counsel, the Privacy Officer identifies the obligations in the categories in section 2.

4.2 **Identify by role.** For each processing activity in PIMS-REG-01 the Privacy Officer records whether the organisation acts as controller, processor or both, because the obligations differ. Obligations that attach only to one role are marked accordingly in GOV-REG-04.

4.3 **Record.** Each obligation is entered in GOV-REG-04 with a reference, a plain description of what it requires, its source, the jurisdiction, whether it applies as Controller, Processor, Both or not at all, the obligation owner, and the review frequency. One row per distinct requirement, not one row per law.

4.4 **Map to controls and evidence.** The Information Security Manager names, for each row, the kit documents and the ISMS-REG-01 controls that satisfy it and the evidence that proves it, and sets the status: Compliant, Partial, Gap or Not assessed. A Gap or Partial status creates either a risk in GOV-REG-05 or a corrective action in GOV-REG-03 within ten working days, with the reference recorded in the row.

4.5 **Contracts.** Before a customer or supplier contract is signed, the Information Security Manager reviews its security, privacy and audit clauses. Commitments the organisation accepts are recorded in GOV-REG-04, and the supplier's obligations to the organisation are recorded in GOV-REG-07. A commitment the organisation cannot meet is refused or negotiated; it is never signed and left unrecorded.

4.6 **Monitor change.** The Privacy Officer subscribes to the publications of the relevant regulators, professional bodies and legal counsel, reviews GOV-REG-04 twice a year, and assesses any change in law, regulation, guidance or contract within thirty days of learning of it. A change that affects a control triggers a review of the relevant document under GOV-PRO-01 and, where needed, a risk reassessment under GOV-PRO-05.

4.7 **Intellectual property.** The organisation uses software, content and data only under a valid licence. The Head of Engineering keeps the licence inventory in GOV-REG-24 current, checks open source licences during development under GOV-PRO-15, and removes unlicensed software within ten working days of discovery. The organisation's own intellectual property is classified and handled under GOV-PRO-16, and staff and contractor agreements under GOV-PRO-18 assign rights in work product to the organisation.

4.8 **Protection of records.** Records that the law, a regulator or a contract requires are listed in the retention schedule PIMS-REG-07 with their period and trigger. The obligation owner protects them against loss, destruction, falsification and unauthorised access for that period, in a format that remains readable, and places them under legal hold when litigation or an investigation is reasonably expected. Disposal follows PIMS-POL-02.

4.9 **Independent review.** At least once a year, and after any significant change to the business, the law or the systems, the Internal Auditor or an external reviewer who is independent of the areas reviewed examines whether the approach to managing information security and privacy, and its implementation, still meets the obligations in GOV-REG-04 and the organisation's own policies. The result is reported to the executive sponsor and to management review, and findings follow GOV-PRO-04.

4.10 **Compliance with policies in each area.** Each head of function reviews, at least annually, whether their area follows the policies and procedures that apply to it, using the evidence named in those documents, and records the result. Nonconformities are raised under GOV-PRO-04.

4.11 **Personal data.** Obligations about personal data are met through PIMS-POL-01 and the procedures it names. The Privacy Officer confirms twice a year that every processing activity in PIMS-REG-01 has a lawful basis, a notice, a retention period and, where required, a DPIA in PIMS-REG-08.

4.12 **Reporting.** The Privacy Officer reports the status distribution of GOV-REG-04, open gaps and changes assessed since the last report to the steering committee quarterly and to management review.

## 5. Records and evidence

- GOV-REG-04 Legal, regulatory and contractual register, with status and evidence for every obligation.
- Contract review records and the clauses accepted.
- Change assessments with dates and outcomes.
- GOV-REG-24 Software and hardware inventory with licence information.
- Independent review reports and the resulting GOV-REG-03 entries.
- Area compliance review records from heads of function.

## 6. Exceptions

An obligation may be marked Not assessed for no more than ninety days after it is identified. A decision not to comply with an obligation is not an exception under this procedure; it is a risk accepted by the Chief Executive Officer under GOV-PRO-24 with legal advice recorded.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after any regulatory enquiry or contractual dispute about compliance, and when the organisation enters a new jurisdiction or sector. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-04 Legal, regulatory and contractual register
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-07 Supplier register
- GOV-REG-24 Software and hardware inventory
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-PRO-18 Human resources security procedure
- PIMS-POL-01 Privacy information management policy
- PIMS-POL-02 Data retention and disposal policy
- PIMS-REG-01 Personal data processing inventory
- PIMS-REG-07 Retention schedule
- PIMS-REG-08 DPIA register
- GDPR-GDE-02 Guide: GDPR articles mapped to kit documents and registers
