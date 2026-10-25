---
id: PIMS-GDE-01
title: "Guide: ISO/IEC 27701 Annex A (controller) and Annex B (processor) controls and where the kit covers each"
type: guide
framework: iso27701
maps:
  - ISO/IEC 27701 Annex A
  - ISO/IEC 27701 Annex B
  - ISO/IEC 27701 clause 5.4.1.3
owner: Privacy Officer
approver: Privacy Officer
classification: Internal
review: Annual
summary: A reading aid that lists every control in Annex A and Annex B of ISO/IEC 27701 with a short theme in plain words and the kit documents that implement it, and explains how the clause 5 and clause 6 extensions change an existing ISMS, for use when extending the Statement of Applicability.
---
## 1. How to use this guide

ISO/IEC 27701 does not stand alone. It extends an information security management system built on ISO/IEC 27001 and ISO/IEC 27002 so that it also manages personal data, and it calls the result a privacy information management system. The 2019 edition has four working parts. Clause 5 adds privacy requirements to each ISO/IEC 27001 clause, mostly by saying that wherever the security standard says information security, you read information security and privacy, and by requiring you to decide whether you act as a controller, a processor, or both. Clause 6 adds privacy guidance to the ISO/IEC 27002 controls, for example on training, classification, backups, logs, test data, suppliers and incidents. Clause 7 gives guidance for controllers and clause 8 for processors. Annex A lists the controller controls and Annex B the processor controls; these two annexes are normative, which means your Statement of Applicability must cover them in the same way it covers the ISO/IEC 27001 Annex A controls.

Which annex applies depends on the role decision under PIMS-PRO-01. A pure controller applies Annex A; a pure processor applies Annex B; an organisation that is both, which is most product companies, applies both, and the justification column of ISMS-REG-01 says for which processing activities each applies.

The tables below give each control number a theme written in this kit's own words. The themes are a memory aid, not the standard's titles; read the standard itself for the requirement. The third column names the kit documents that implement the control, the first being the primary one. Use the tables in three places:

1. **ISMS-REG-01 Statement of Applicability.** Add the Annex A and Annex B rows under the ISO/IEC 27001 rows, decide Applicable Yes or No for each, justify, set the implementation status, and copy the kit IDs you actually use.
2. **ISMS-REG-02 Control implementation tracker.** Add the same rows with owner, evidence, test method and the effectiveness grade from PIMS-PRO-07.
3. **Gap analysis in step 5 of PB-05.** Walk the tables with the Processing Owners and mark what exists, what exists informally and what does not exist.

## 2. Annex A: controls for controllers

| Control | Theme | Kit documents |
|---|---|---|
| A.7.2.1 | Purpose identified and recorded before processing | PIMS-REG-01, GDPR-PRO-01 |
| A.7.2.2 | Lawful basis determined and recorded | PIMS-REG-01, PIMS-PRO-05, GDPR-TPL-07 |
| A.7.2.3 | Deciding when and how consent is needed | PIMS-PRO-05 |
| A.7.2.4 | Obtaining and recording consent | PIMS-PRO-05, PIMS-REG-04, GDPR-TPL-06 |
| A.7.2.5 | Privacy impact assessment | PIMS-PRO-02, PIMS-TPL-01, PIMS-REG-08 |
| A.7.2.6 | Written contracts with processors | PIMS-TPL-02, GOV-PRO-06, PIMS-REG-06 |
| A.7.2.7 | Joint controller arrangements | PIMS-PRO-01 |
| A.7.2.8 | Records of processing | PIMS-REG-01, GDPR-PRO-01 |
| A.7.3.1 | Working out the duties owed to individuals | PIMS-PRO-03, GOV-REG-04, GOV-PRO-25 |
| A.7.3.2 | Deciding what individuals must be told | PIMS-PRO-05, GDPR-TPL-01 |
| A.7.3.3 | Giving individuals the information | PIMS-PRO-05, GDPR-TPL-01, GDPR-TPL-02, GDPR-TPL-03, GDPR-TPL-04 |
| A.7.3.4 | Changing or withdrawing consent | PIMS-PRO-05, PIMS-REG-04 |
| A.7.3.5 | Objecting to processing | PIMS-PRO-03, GDPR-TPL-07 |
| A.7.3.6 | Access, correction and erasure | PIMS-PRO-03, PIMS-REG-02, GDPR-TPL-05 |
| A.7.3.7 | Telling third parties about corrections and erasures | PIMS-PRO-03 |
| A.7.3.8 | Providing a copy of the data | PIMS-PRO-03, GDPR-TPL-05 |
| A.7.3.9 | Handling requests within set times | PIMS-PRO-03, PIMS-REG-02 |
| A.7.3.10 | Decisions made by automated means | PIMS-PRO-03, PIMS-PRO-02, AI-POL-02 |
| A.7.4.1 | Collecting only what is needed | PIMS-PRO-06 |
| A.7.4.2 | Processing only what the purpose needs | PIMS-PRO-06, PIMS-POL-01 |
| A.7.4.3 | Accuracy and quality of data | PIMS-PRO-06, PIMS-PRO-03 |
| A.7.4.4 | Minimisation objectives set and measured | PIMS-PRO-06, PIMS-PRO-07, ISMS-PLN-01 |
| A.7.4.5 | De-identification or deletion when the purpose ends | PIMS-POL-02, PIMS-PRO-06 |
| A.7.4.6 | Temporary files removed | PIMS-PRO-06, PIMS-POL-02 |
| A.7.4.7 | Retention limited and justified | PIMS-POL-02, PIMS-REG-07 |
| A.7.4.8 | Secure disposal | PIMS-POL-02, GOV-PRO-16, GOV-REG-20 |
| A.7.4.9 | Controls on transmission of data | GOV-PRO-23, GOV-PRO-20 |
| A.7.5.1 | Basis for transfers between countries | PIMS-POL-03, PIMS-REG-05 |
| A.7.5.2 | Permitted destination countries recorded | PIMS-POL-03, PIMS-REG-05, GDPR-TPL-08 |
| A.7.5.3 | Records of transfers | PIMS-REG-05, GDPR-REG-02 |
| A.7.5.4 | Records of disclosures to third parties | PIMS-REG-01, PIMS-PRO-03, GOV-PRO-25 |

## 3. Annex B: controls for processors

| Control | Theme | Kit documents |
|---|---|---|
| B.8.2.1 | Written agreement with the customer | PIMS-TPL-02, GOV-PRO-06 |
| B.8.2.2 | No processing for the processor's own purposes | PIMS-TPL-02, PIMS-PRO-01 |
| B.8.2.3 | No use for marketing or advertising without consent | PIMS-TPL-02, PIMS-PRO-05 |
| B.8.2.4 | Flagging instructions that would break the law | PIMS-TPL-02, PIMS-PRO-01 |
| B.8.2.5 | Helping the customer meet its own obligations | PIMS-TPL-02, PIMS-PRO-03, PIMS-PRO-04, PIMS-PRO-02 |
| B.8.2.6 | Processor's own records of processing | PIMS-REG-01 |
| B.8.3.1 | Supporting the customer's duties to individuals | PIMS-PRO-03, PIMS-TPL-02 |
| B.8.4.1 | Temporary files removed | PIMS-PRO-06, PIMS-POL-02 |
| B.8.4.2 | Return, transfer or disposal at the end of service | PIMS-TPL-02, PIMS-POL-02 |
| B.8.4.3 | Controls on transmission of data | GOV-PRO-23, GOV-PRO-20 |
| B.8.5.1 | Basis for transfers between countries | PIMS-POL-03, PIMS-REG-05 |
| B.8.5.2 | Permitted destination countries recorded | PIMS-POL-03, PIMS-REG-05 |
| B.8.5.3 | Records of disclosures to third parties | PIMS-REG-05, PIMS-REG-01 |
| B.8.5.4 | Telling the customer about disclosure requests | PIMS-POL-03, GOV-PRO-25 |
| B.8.5.5 | Legally binding disclosures handled lawfully | PIMS-POL-03, GOV-PRO-25 |
| B.8.5.6 | Sub-processors disclosed to the customer | PIMS-REG-06, PIMS-TPL-02 |
| B.8.5.7 | Engaging a sub-processor only with authorisation and terms | GOV-PRO-06, PIMS-REG-06, PIMS-TPL-02 |
| B.8.5.8 | Notifying changes of sub-processor | PIMS-REG-06, ISMS-PLN-02, PIMS-TPL-02 |

## 4. What clause 5 and clause 6 change in an existing ISMS

The annexes are the visible part. An auditor spends as much time on the clause 5 extensions, because they change documents the ISMS already has. The table lists the extensions most organisations have to act on and the kit document that carries the change.

| Clause | What changes, in plain words | Kit documents |
|---|---|---|
| 5.2.1 | The organisation decides and records whether it is a controller, a processor or both, and considers privacy law and contracts as part of its context | PIMS-PRO-01, ISMS-PRO-01, GOV-REG-04 |
| 5.2.2 | Individuals whose data is processed, and privacy regulators, become interested parties with requirements | ISMS-REG-03 |
| 5.2.3 | The scope statement says which processing of personal data is covered | ISMS-STM-01 |
| 5.3.2 | The security policy, or a policy beside it, commits to the protection of personal data | PIMS-POL-01, GOV-POL-03 |
| 5.3.3 | A role is accountable for privacy, with the independence and resources it needs | GOV-POL-01, PIMS-POL-01 |
| 5.4.1.2 | Risk assessment considers the harm to individuals, not only to the organisation | GOV-PRO-05, PIMS-PRO-02 |
| 5.4.1.3 | The Statement of Applicability covers Annex A and Annex B | ISMS-REG-01, this guide |
| 5.4.2 | Objectives include privacy objectives | ISMS-PLN-01, GOV-REG-21 |
| 5.5.3 and 5.5.4 | Competence and awareness cover privacy | ISMS-PRO-02, GOV-PRO-08, GDPR-REG-05 |
| 5.7.1 | Performance evaluation measures privacy controls | PIMS-PRO-07 |
| 5.7.2 and 5.7.3 | Internal audit and management review cover the privacy extension | ISMS-PLN-03, GOV-PRO-02, GOV-PRO-03 |
| 6.4.2.2 | Training covers the consequences of breaching privacy obligations | GOV-PRO-08 |
| 6.5.2 | Classification identifies personal data as a category | GOV-PRO-16 |
| 6.9.3.1 | Backups respect retention and can be restored without reviving deleted data | GOV-PRO-12, PIMS-POL-02 |
| 6.9.4 | Logs record access to personal data and are themselves protected and retention-limited | GOV-PRO-14 |
| 6.11.3 | Test data contains no live personal data without controls | GOV-PRO-15, PIMS-PRO-06 |
| 6.12.1.2 | Supplier agreements cover personal data | GOV-PRO-06, PIMS-TPL-02 |
| 6.13.1.5 | Incident response includes breach assessment and notification | PIMS-PRO-04 |
| 6.15.1.1 | Applicable privacy law is identified | GOV-PRO-25, GOV-REG-04 |

## 5. Editions and numbering

This guide uses the numbering of the 2019 edition of ISO/IEC 27701, in which the standard is an extension to ISO/IEC 27001:2013 and ISO/IEC 27002:2013 and the controller and processor controls sit in Annex A and Annex B as listed above. A later edition restructures the standard so that it can be certified on its own and renumbers its clauses and annexes; the themes above survive the restructuring, the numbers do not. Before building your Statement of Applicability, confirm with your certification body which edition it audits against, add a column to ISMS-REG-01 for that edition's numbering, and map each theme row once. The kit document IDs do not change; only the control reference in the first column does. Keep the mapping with GOV-REG-01 as an external document reference so that the next auditor can follow it.

## 6. Related documents

- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- ISMS-GDE-01 Guide: the 93 Annex A controls and where the kit covers each
- PIMS-POL-01 Privacy information management policy
- PIMS-PRO-01 Determining controller and processor roles
- PIMS-PRO-07 Privacy control effectiveness monitoring procedure
- PB-05 Playbook: adding ISO/IEC 27701 privacy management to an existing ISMS
