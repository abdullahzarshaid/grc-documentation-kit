---
id: ISMS-GDE-01
title: "Guide: the 93 Annex A controls and where the kit covers each"
type: guide
framework: iso27001
maps:
  - ISO/IEC 27001:2022 Annex A
  - ISO/IEC 27001:2022 clause 6.1.3
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: A reading aid that lists every Annex A control number of ISO/IEC 27001:2022 with a short theme in plain words and the kit documents that implement it, for use when building the Statement of Applicability and the control tracker.
---
## 1. How to use this guide

Annex A of ISO/IEC 27001:2022 lists 93 reference controls in four groups: organisational (5.1 to 5.37), people (6.1 to 6.8), physical (7.1 to 7.14) and technological (8.1 to 8.34). The standard requires you to compare the controls you chose from your risk treatment with this list, confirm that nothing necessary was missed, and record in a Statement of Applicability which controls apply, why, and whether they are implemented.

The tables below give each control number a theme written in this kit's own words. The themes are a memory aid, not the standard's titles; when you need the authoritative text, read the standard itself. The third column names the kit documents that implement the control. Where several documents are listed, the first is the primary one and the others supply records or related rules.

Use the tables in three places:

1. **ISMS-REG-01 Statement of Applicability.** The control numbers and themes are prefilled there. For each row decide Applicable Yes or No, write a justification in one or two sentences, set the implementation status, and copy the kit IDs you actually use into the implementing documents column.
2. **ISMS-REG-02 Control implementation tracker.** The same 93 rows carry the owner, the evidence, the test method and the last test result for each applicable control. ISMS-PRO-04 explains how controls are tested.
3. **Gap analysis in step 3 of PB-02.** Walk the tables with the people who run each area and mark what exists, what exists informally and what does not exist.

Three rules save time at audit. First, a control marked Not applicable needs a justification that an auditor can accept: either no risk in GOV-REG-05 needs it and no requirement in ISMS-REG-03 demands it, or the activity it governs does not happen at all in the scope (for example in-house development where no software is developed). "We use the cloud" is not by itself a justification for excluding the physical controls; it moves most of them to the provider and leaves offices, home working and devices with you. Second, every applicable control needs an owner and evidence that it operates, not only a document. Third, the justification should name the risk or requirement it satisfies, so that when the risk changes the Statement of Applicability can be re-checked.

The 2022 edition also attaches attributes to each control (control type, security property, cybersecurity concept, operational capability, security domain). The kit does not reproduce them. If you want to filter controls by, for example, detective versus preventive, add an attribute column to ISMS-REG-01 and populate it from your own copy of the standard.

## 2. Organisational controls (5.1 to 5.37)

| Control | Theme | Kit documents |
|---|---|---|
| 5.1 | Policy framework and approval | GOV-POL-03, GOV-PRO-01 |
| 5.2 | Assigned security roles | GOV-POL-01 |
| 5.3 | Conflicting duties separated | GOV-POL-01, GOV-PRO-10 |
| 5.4 | Leadership enforcement of rules | GOV-STM-01, GOV-POL-01, GOV-PRO-18 |
| 5.5 | Regulator and authority liaison | GOV-PRO-25, GOV-PRO-07, ISMS-PLN-02 |
| 5.6 | Specialist community contacts | GOV-PRO-27, ISMS-PLN-02 |
| 5.7 | Threat information gathering | GOV-PRO-27 |
| 5.8 | Security built into projects | PB-07, GOV-PRO-15, ISMS-PRO-03 |
| 5.9 | Asset and owner inventory | GOV-PRO-16, GOV-REG-10, GOV-REG-24 |
| 5.10 | Rules for using assets | GOV-POL-02, GOV-PRO-16 |
| 5.11 | Returning assets on exit | GOV-PRO-16, GOV-CHK-01 |
| 5.12 | Sensitivity grading scheme | GOV-PRO-16 |
| 5.13 | Marking by sensitivity | GOV-PRO-16 |
| 5.14 | Safe information movement | GOV-PRO-23, GOV-REG-25 |
| 5.15 | Access rules by need | GOV-PRO-10 |
| 5.16 | Identity lifecycle control | GOV-PRO-10 |
| 5.17 | Credential issue and care | GOV-POL-06, GOV-PRO-10 |
| 5.18 | Access grant and review | GOV-PRO-10, GOV-TPL-09, GOV-REG-12 |
| 5.19 | Supplier security governance | GOV-PRO-06, GOV-REG-07 |
| 5.20 | Security terms in contracts | GOV-PRO-06, PIMS-TPL-02 |
| 5.21 | Technology supply chain depth | GOV-PRO-06, GOV-PRO-15 |
| 5.22 | Supplier performance monitoring | GOV-PRO-06, GOV-REG-07, SOC-PRO-02 |
| 5.23 | Cloud service lifecycle | GOV-PRO-26 |
| 5.24 | Incident response readiness | GOV-PRO-07 |
| 5.25 | Event triage decisions | GOV-PRO-07, GOV-TPL-05 |
| 5.26 | Incident handling execution | GOV-PRO-07, GOV-REG-08 |
| 5.27 | Lessons from incidents | GOV-PRO-07, GOV-TPL-11 |
| 5.28 | Evidence preservation | GOV-PRO-07, PB-09 |
| 5.29 | Controls kept through disruption | GOV-PRO-13 |
| 5.30 | Technology continuity readiness | GOV-PRO-13, GOV-TPL-07, GOV-REG-16 |
| 5.31 | Legal duties identified | GOV-PRO-25, GOV-REG-04 |
| 5.32 | Respecting licences and copyright | GOV-PRO-25, GOV-PRO-15 |
| 5.33 | Records kept safe | GOV-PRO-25, GOV-PRO-01, PIMS-POL-02 |
| 5.34 | Personal data safeguards | PIMS-POL-01, GDPR-POL-01, GOV-PRO-25 |
| 5.35 | Impartial programme review | GOV-PRO-02, GOV-PRO-25 |
| 5.36 | Policy compliance checks | ISMS-PRO-04, GOV-PRO-02 |
| 5.37 | Operating steps written down | GOV-PRO-01, ISMS-PRO-03 |

## 3. People controls (6.1 to 6.8)

| Control | Theme | Kit documents |
|---|---|---|
| 6.1 | Pre-employment checks | GOV-PRO-18 |
| 6.2 | Employment security clauses | GOV-PRO-18 |
| 6.3 | Staff awareness and skills | GOV-PRO-08, ISMS-PRO-02, GOV-REG-09 |
| 6.4 | Consequences for breaches | GOV-PRO-18, GOV-POL-03 |
| 6.5 | Duties after leaving | GOV-PRO-18, GOV-CHK-01 |
| 6.6 | Secrecy undertakings signed | GOV-PRO-18, GOV-PRO-06 |
| 6.7 | Working away from office | GOV-POL-05, GOV-PRO-22 |
| 6.8 | Staff event reporting | GOV-PRO-07, GOV-POL-02 |

## 4. Physical controls (7.1 to 7.14)

| Control | Theme | Kit documents |
|---|---|---|
| 7.1 | Protected area boundaries | GOV-PRO-17 |
| 7.2 | Entry control and visitors | GOV-PRO-17, GOV-REG-19 |
| 7.3 | Room and facility protection | GOV-PRO-17 |
| 7.4 | Premises surveillance | GOV-PRO-17 |
| 7.5 | Protection from hazards | GOV-PRO-17 |
| 7.6 | Conduct in secure areas | GOV-PRO-17 |
| 7.7 | Tidy desks and locked screens | GOV-POL-04 |
| 7.8 | Placing equipment safely | GOV-PRO-17 |
| 7.9 | Assets taken off site | GOV-PRO-17, GOV-POL-05 |
| 7.10 | Media handling lifecycle | GOV-PRO-16, GOV-REG-20 |
| 7.11 | Power and support services | GOV-PRO-17 |
| 7.12 | Cable protection | GOV-PRO-17 |
| 7.13 | Equipment upkeep | GOV-PRO-17 |
| 7.14 | Wiping before disposal | GOV-PRO-16, GOV-REG-20 |

## 5. Technological controls (8.1 to 8.34)

| Control | Theme | Kit documents |
|---|---|---|
| 8.1 | User device protection | GOV-PRO-22 |
| 8.2 | Elevated privileges limited | GOV-PRO-10, GOV-REG-13 |
| 8.3 | Information access limits | GOV-PRO-10, GOV-PRO-16 |
| 8.4 | Source code safeguarding | GOV-PRO-15, GOV-PRO-10 |
| 8.5 | Strong authentication methods | GOV-POL-06 |
| 8.6 | Capacity forecasting | GOV-PRO-19, GOV-REG-17 |
| 8.7 | Malicious code defence | GOV-PRO-22 |
| 8.8 | Vulnerability handling | GOV-PRO-11, GOV-REG-14 |
| 8.9 | Hardened configuration baselines | GOV-CHK-02, GOV-PRO-22, GOV-PRO-26 |
| 8.10 | Deleting unneeded information | PIMS-POL-02, GOV-PRO-16 |
| 8.11 | Masking sensitive values | GOV-PRO-15, PIMS-PRO-06 |
| 8.12 | Stopping data exfiltration | GOV-PRO-23 |
| 8.13 | Backup copies and tests | GOV-PRO-12, GOV-REG-15 |
| 8.14 | Resilience through redundancy | GOV-PRO-19, GOV-PRO-13 |
| 8.15 | Event log capture | GOV-PRO-14 |
| 8.16 | Anomaly monitoring | GOV-PRO-14 |
| 8.17 | Synchronised clocks | GOV-PRO-14 |
| 8.18 | Powerful utilities controlled | GOV-PRO-10, GOV-CHK-02 |
| 8.19 | Controlled software installs | GOV-PRO-22, GOV-PRO-09 |
| 8.20 | Network protection | GOV-PRO-21 |
| 8.21 | Network service assurance | GOV-PRO-21, GOV-PRO-06 |
| 8.22 | Network segmentation | GOV-PRO-21 |
| 8.23 | Filtering web destinations | GOV-PRO-21 |
| 8.24 | Cryptography and keys | GOV-PRO-20, GOV-REG-18 |
| 8.25 | Security across development | GOV-PRO-15 |
| 8.26 | Security needs of applications | GOV-PRO-15, PB-07 |
| 8.27 | Secure design principles | GOV-PRO-15 |
| 8.28 | Safe coding rules | GOV-PRO-15 |
| 8.29 | Security testing before release | GOV-PRO-15, PB-07 |
| 8.30 | Overseeing external developers | GOV-PRO-15, GOV-PRO-06 |
| 8.31 | Environment separation | GOV-PRO-15 |
| 8.32 | Controlled changes | GOV-PRO-09, GOV-TPL-08, GOV-REG-11 |
| 8.33 | Test data protection | GOV-PRO-15 |
| 8.34 | Audit test safeguards | GOV-PRO-02, GOV-PRO-09 |

## 6. Controls that most often need attention

Experience of first certifications points to the same handful of controls where a document exists but the evidence does not. Check these first:

- **5.9 and 7.10.** The asset inventory is often a spreadsheet nobody reconciles. GOV-PRO-16 sets a quarterly reconciliation; keep the dated export.
- **5.18.** Access reviews are promised quarterly and performed once. GOV-REG-12 should show four dated entries per system per year, each with the account list that was reviewed.
- **5.22.** Supplier reviews stop after onboarding. GOV-REG-07 needs a review date within twelve months for every Tier 1 supplier.
- **6.3.** Training records show attendance but not currency. GOV-REG-09 should let you compute, for any date, who is overdue.
- **8.8.** Severity windows are written but not measured. GOV-REG-14 should produce the closure measure in ISMS-PRO-04 without manual work.
- **8.13.** Backups run; restores are never tested. GOV-REG-15 needs a test per critical system per quarter with the time taken.
- **8.15 and 8.16.** Logs exist; nobody looks at them. GOV-PRO-14 defines a review cadence; keep the review notes and the alert tickets.
- **8.32.** Emergency changes bypass the record. GOV-REG-11 should hold every production change, including the emergency ones with their retrospective approval.

## 7. Where the kit leaves decisions to you

The kit cannot decide applicability for you. Controls 7.1 to 7.14 depend on whether you have offices, server rooms or only laptops and a provider; GOV-PRO-17 explains what remains for a cloud only organisation. Controls 8.4, 8.25 to 8.31 and 8.33 apply only where software is developed or materially configured in house. Control 8.30 applies only where development is outsourced. Control 5.23 applies to almost everyone. Record every decision, and its reason, in ISMS-REG-01.

## 8. Related documents

- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- GOV-PRO-05 Risk assessment and treatment methodology
- ISMS-PRO-04 Monitoring, measurement, analysis and evaluation procedure
- ISMS-GDE-02 Guide to mandatory documented information and records
- GOV-REG-27 Framework crosswalk
