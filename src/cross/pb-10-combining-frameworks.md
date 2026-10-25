---
id: PB-10
title: "Playbook: one control set, several certifications"
type: playbook
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 4.2
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27701 clause 5.4.1.3
  - SOC 2 CC4.1
  - GDPR Article 24
  - GDPR Article 32
  - NIST CSF 2.0 GV.OC
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How to run one set of controls, one set of registers and one evidence folder so that ISO/IEC 27001, ISO/IEC 27701, SOC 2, the GDPR and NIST CSF 2.0 are served together through the crosswalk GOV-REG-27, with a plain account of where the frameworks genuinely differ and what cannot be shared between them.
---
## 1. The idea

An organisation that reviews access quarterly does one piece of work. ISO/IEC 27001 calls it an Annex A control, SOC 2 calls it a control activity under two criteria, the GDPR calls it a technical and organisational measure, and NIST CSF 2.0 calls it a subcategory outcome. The work, the record and the evidence are the same. Everything that differs is how each framework asks about them.

So the kit holds one control set, described in its procedures and declared in ISMS-REG-01, and GOV-REG-27 records for each control which criteria, articles and categories it serves. Registers carry framework tags rather than being duplicated. Evidence is collected once, to the strictest standard any framework imposes, and filed once. The audits, attestations and inspections then read from the same system, and the cost of the second and third framework is mostly the parts that cannot be shared, which section 7 lists.

## 2. What each framework is

| Framework | What it is | Who checks and what you get |
|---|---|---|
| ISO/IEC 27001:2022 | A management system standard: requirements for how you govern security (clauses 4 to 10) plus a reference list of controls (Annex A) you compare your own choice against | An accredited certification body audits and issues a certificate for a three year cycle with annual surveillance |
| ISO/IEC 27701 | An extension to ISO/IEC 27001 that adds privacy requirements and controller and processor controls; it cannot be certified on its own | The same certification body extends the certificate scope |
| SOC 2 | An attestation framework: you write a system description and state your controls, and a licensed accountancy firm tests them against the Trust Services Criteria | A report with the auditor's opinion, either at a point in time (Type 1) or over a period, usually six to twelve months (Type 2) |
| GDPR | Law: obligations on controllers and processors of personal data about individuals in the European Union, enforced by supervisory authorities and courts | No certificate in normal practice; the test is whether you can demonstrate compliance when asked, and the consequence of failure is enforcement |
| NIST CSF 2.0 | A voluntary framework of outcomes in six functions, used to describe current and target posture and to talk to boards and partners | Self-assessed, or assessed by a consultant; produces profiles and tiers, not a certificate |

## 3. Where they genuinely differ

Treating the frameworks as interchangeable is the mistake that costs most. They differ on five dimensions, and each difference changes what an assessor will accept.

| Dimension | Management system (ISO/IEC 27001 and 27701) | Attestation (SOC 2) | Law (GDPR) | Framework (NIST CSF 2.0) |
|---|---|---|---|---|
| What is assessed | The system: scope, risk, objectives, review, audit, improvement, and the controls it chose | The controls you stated in your description, and whether they met the criteria | Each processing activity: lawful, transparent, limited, secure, demonstrable | Outcomes achieved, measured against a target profile |
| Who decides the controls | You, from your risk assessment, checked against Annex A and justified in the Statement of Applicability | You, against the criteria; the auditor tests what you claim | The law sets the obligations; you choose the measures and must justify them | You, through the profile you set |
| Time dimension | A point of certification, then a cycle; records must show the system has operated | A defined period; every control must have operated throughout it, and the sample is drawn from the period | Always; an obligation applies at the moment it applies, with fixed clocks for notification and rights | A snapshot, repeated when you choose |
| What failure looks like | Nonconformities that must be closed before the certificate is issued or kept | Exceptions written into the report, which readers see | Complaints, investigations, orders and fines | A gap between current and target profile |
| Scope language | A scope statement naming locations, services and systems | A system description naming services, components, boundaries and subservice organisations | The processing activities in your records of processing | The organisation or the part you chose to profile |

Two consequences follow. First, a SOC 2 auditor cannot accept the ISO certificate as evidence of operation, because the certificate says nothing about the period or the sample; and an ISO auditor cannot accept a SOC 2 report as proof of a management system, because the report never looked for one. Second, the GDPR is not a control set. Security controls satisfy one article; the lawful basis, the notices, the records of processing, the rights process and the breach clock are obligations no security framework will give you.

## 4. How GOV-REG-27 works

GOV-REG-27 has one row for each of the 93 Annex A controls, carrying the theme in the kit's own words, the SOC 2 criteria the control contributes to, the GDPR articles it helps satisfy, the NIST CSF 2.0 categories whose outcomes it supports, the kit documents that implement it, a note, and a status for your own review of the mapping.

Read a row from left to right as a chain of questions. Take the control for access grant and review. The theme reminds you what the control is. The SOC 2 column says that this one piece of work contributes to the criteria on user registration and removal and on role-based access with periodic review. The GDPR column says it is one of the measures that answer the security obligation. The CSF column points at the identity and access category. The kit column names GOV-PRO-10, GOV-TPL-09 and GOV-REG-12 as the procedure, the form and the record. The same evidence folder entry, a dated access review export with the reviewer's decisions, is what all four assessors will be shown.

Four rules govern the register:

1. **Mapping is partial, and the notes say where.** A criterion listed against a control means the control contributes to it, not that it satisfies it alone. Most SOC 2 criteria draw on several controls and on the management system clauses as well.
2. **A mapping is never evidence.** The crosswalk tells you which evidence to show to whom. The assessor then tests it to their own rules.
3. **"none" means none.** Where a framework has no requirement a control serves, the cell says so. Do not fill the gap with the nearest sounding criterion; an assessor will read it as not understanding their framework.
4. **The register is reviewed annually and when any framework changes edition.** Set the Status column to To review for every row at that point and confirm each mapping before resetting it to Confirmed.

The clause 4 to 10 requirements of ISO/IEC 27001 are not in the crosswalk because they have no Annex A number. Their SOC 2 relatives are the CC1 to CC5 criteria and the criteria on monitoring; ISMS-GDE-02 lists the mandatory items and SOC-GDE-03 maps the criteria to the kit.

## 5. The tag approach: one register, framework tags

Never keep two risk registers, two corrective action logs or two audit programmes. Add a Frameworks column to each shared register and fill it with tags: ISO27001, ISO27701, SOC2, GDPR, CSF. The registers that take tags are GOV-REG-05 for risks, ISMS-REG-02 for controls, GOV-REG-03 for corrective actions, GOV-REG-02 for audits, GOV-REG-04 for obligations and the evidence index in each area of the evidence folder.

Tags come from GOV-REG-27 and from GOV-REG-04, never from memory. A control row in ISMS-REG-02 inherits the tags of its crosswalk row. A risk inherits the tags of the controls that treat it. A corrective action inherits the tags of the control or clause it was raised against. An audit in GOV-REG-02 lists the tags of the criteria it covered.

What the tags buy you:

- A filter. When the SOC 2 auditor sends the request list, filter every register on SOC2 and you have the population they will sample from. When the certification auditor arrives, filter on ISO27001.
- One audit programme. ISMS-PLN-03 already covers every applicable control; the SOC 2 criteria ride on the same audits through the tags, and GOV-PRO-02 names them as criteria.
- One corrective action loop. A SOC 2 exception, an ISO nonconformity and a GDPR gap all become GOV-REG-03 rows and are closed the same way.
- One steering report. The quarterly report under ISMS-PRO-04 shows measures by tag, so the committee sees the SOC 2 period and the ISO cycle in the same table.

The frequency rule: a control is operated and tested at the strictest frequency any tagged framework needs, and only once. If the SOC 2 period needs quarterly evidence of a control that ISO would accept annually, it is quarterly, and the ISO auditor receives four records instead of one.

## 6. Evidence reuse

The same artefact answers a different question for each assessor. Collect it so that it answers all of them.

| Artefact | ISO asks | SOC 2 asks | GDPR asks | CSF asks |
|---|---|---|---|---|
| Quarterly access review export with decisions, GOV-REG-12 | Does the control exist, apply, and operate as the procedure says | Did it operate every quarter of the period; sample two and trace the removals | Is access to personal data limited to those who need it, and can you show it | Is the identity and access outcome achieved and improving |
| Change ticket export, GOV-REG-11 | Are changes controlled per the procedure, including emergency changes | For a sample of twenty-five changes across the period, were approval and testing recorded before deployment | Were changes to processing assessed for privacy impact where needed | Is platform change managed as an outcome |
| Incident record and post-incident review, GOV-REG-08 and GOV-TPL-11 | Was the incident process followed and were lessons fed to improvement | Was each incident in the period evaluated, responded to and communicated | Was the breach assessed within the notification clock and documented even when not notified | Were detection, response and recovery outcomes met |
| Training completion export, GOV-REG-09 | Is competence and awareness evidenced for the roles | Did every person in the period complete the training the policy requires | Were staff handling personal data made aware of their obligations | Is the awareness outcome achieved |

The collection rules in PB-09 already meet the strictest reader. Three additions matter when frameworks combine. Date coverage: SOC 2 samples are drawn across the whole period, so evidence that exists only for the month before the ISO audit fails the SOC 2 test; collect on the control's own rhythm, every time. Population exports: SOC 2 auditors sample from populations they choose, so keep the full export, not the items you think are interesting. Retention: keep evidence for the longest of the ISO cycle, the SOC 2 period plus the next period, and any contract term in GOV-REG-04.

## 7. What cannot be shared

Some artefacts belong to one framework and have no equivalent in another. Budget for them separately and do not try to make one document do two jobs.

- **The SOC 2 system description and the management assertion.** Written in the form SOC-TPL-01 sets out, signed by management, and read word for word by the auditor and by every customer who receives the report. ISMS-STM-01 is a source for it, not a substitute.
- **The SOC 2 auditor's own tests.** You cannot hand the attestation firm your internal audit and expect it to be relied on. Your internal audit is evidence of monitoring under the criteria; their tests are theirs.
- **The mandatory ISO records.** The scope statement, the risk assessment method and results, the Statement of Applicability, the objectives, the management review minutes and the internal audit records are required by clauses 4 to 10. SOC 2 does not ask for a Statement of Applicability and the GDPR does not ask for a management review; neither excuses you from producing them for the certificate.
- **The ISO/IEC 27701 layer.** The controller or processor role decision under PIMS-PRO-01, the applicability of the Annex A and Annex B controls, and the privacy extensions to risk and to the Statement of Applicability. PB-05 covers adding them.
- **The GDPR obligations that are not controls.** The lawful basis for each processing activity, the records of processing in PIMS-REG-01, impact assessments under PIMS-PRO-02, the notices from GDPR-TPL-01 to GDPR-TPL-04, the rights process under PIMS-PRO-03, the breach clock under PIMS-PRO-04, processor terms from PIMS-TPL-02 and transfer mechanisms under PIMS-POL-03. A certificate and a clean SOC 2 report together leave every one of these untouched.
- **The CSF profile.** Current and target profiles and the tier are a separate exercise in describing posture; they reuse the evidence but are not produced by any audit.
- **The assessors and their rules.** A certification body works under accreditation rules; an attestation firm under professional standards; a supervisory authority under the law. None of them will adopt another's sampling, period or conclusion.
- **The words you may use.** "Certified to ISO/IEC 27001" needs a certificate with the scope wording from ISMS-STM-01. A SOC 2 report is "has obtained a SOC 2 Type 2 report for the period", never "SOC 2 certified". Nothing is "GDPR certified" unless an approved certification scheme says so. ISMS-PLN-02 section 3 holds the safe wording.

## 8. Adding a framework to a set you already run

| Starting point | What you already have | What you add | Kit documents |
|---|---|---|---|
| ISO/IEC 27001 certified, adding SOC 2 | Policies, procedures, risk register, controls with evidence, internal audit, corrective actions | The system description and assertion; a control matrix stated against the criteria; a period with continuous evidence; a control testing and sampling procedure; the subservice organisation review | SOC-TPL-01, SOC-REG-01, SOC-REG-02, SOC-PRO-01, SOC-PRO-02, PB-03 |
| SOC 2 report in hand, adding ISO/IEC 27001 | Controls with period evidence, a change and incident history, vendor reviews | Scope and context, a risk method and assessment, the Statement of Applicability, objectives and measures, competence records, the internal audit cycle and the management review | ISMS-STM-01, ISMS-PRO-01, GOV-PRO-05, ISMS-REG-01, ISMS-PLN-01, ISMS-PRO-02, GOV-PRO-02, GOV-PRO-03, PB-02 |
| Either, adding the GDPR | Security measures and evidence, supplier register, incident process | The processing inventory, lawful bases, notices, rights process, breach assessment, processor terms, retention schedule, transfer assessments | PIMS-REG-01, GDPR-PRO-01, PIMS-PRO-03, PIMS-PRO-04, PIMS-TPL-02, PIMS-POL-02, GDPR-TPL-08, PB-04 |
| ISO/IEC 27001, adding ISO/IEC 27701 | The management system | Privacy scope and roles, privacy risk, Annex A and Annex B applicability, the privacy registers | PIMS-POL-01, PIMS-PRO-01, PIMS-PRO-02, PIMS-GDE-01, PB-05 |
| Any, describing posture with NIST CSF 2.0 | Everything above | A current and target profile and a tier, drawn from ISMS-REG-02 through the CSF column of GOV-REG-27 | GOV-REG-27, ISMS-REG-02 |

In every case the order is the same: tag what exists, from GOV-REG-27 and GOV-REG-04; list what the new framework needs that nothing serves; create only those items; run one calendar.

## 9. One calendar

The management system runs on a calendar, and a second framework adds events to it rather than a second calendar. ISMS-PLN-03 fixes the audits, SOC-REG-02 fixes the recurring evidence events for a SOC 2 period, and ISMS-PLN-02 fixes the communications. Put all three in one shared calendar with an owner per event. The quarterly rhythm that satisfies every framework at once is: access reviews, restore tests, Tier 1 supplier reviews, steering committee with the measures report, vulnerability closure review, privacy measures review under PIMS-PRO-07, and the audit for that quarter. The annual rhythm adds the risk assessment, the management review, the policy reviews, the awareness refresher, the continuity exercise, the crosswalk review and the SOC 2 period close.

## 10. Mistakes to avoid

1. Treating a mapping as compliance. A row in GOV-REG-27 proves nothing; the evidence behind the control does.
2. Mapping at the level of titles. Two requirements with similar names often test different things; map requirement to requirement and write the partial cases in the notes.
3. Answering a SOC 2 request with "covered by our ISO certificate". The auditor needs the period evidence, not the certificate.
4. Keeping a risk register per framework. One register, tagged, or the two will disagree in front of an auditor.
5. Keeping an evidence folder per framework. One folder, indexed by control and tagged, as PB-09 describes.
6. Writing a policy per framework. One policy per topic; the frameworks are listed in its control block.
7. Treating the GDPR as a control set and forgetting the obligations in section 7.
8. Forgetting the period. A control switched on the month before the ISO audit is a SOC 2 exception for every earlier month.
9. Claiming a certification that a crosswalk suggests you deserve. Only a certificate, a report or a scheme supports a claim.
10. Letting the crosswalk go stale when a framework changes edition.

## 11. Related documents

- GOV-REG-27 Framework crosswalk
- GOV-POL-01 Information security and privacy governance framework
- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- ISMS-GDE-01 Guide to the 93 Annex A controls
- ISMS-GDE-02 Guide to mandatory documented information and records
- SOC-GDE-03 Guide to Trust Services Criteria mapped to kit documents
- GDPR-GDE-02 Guide to GDPR articles mapped to kit documents
- PIMS-GDE-01 Guide to ISO/IEC 27701 Annex A and Annex B controls
- ISMS-PLN-03 Annual internal audit plan
- SOC-REG-02 Evidence calendar
- PB-09 Playbook: evidence management that survives an audit
- PB-02 Playbook: ISO/IEC 27001:2022 implementation in twelve steps
- PB-03 Playbook: SOC 2 Type 2 readiness in 90 days
- PB-04 Playbook: GDPR operations for a product team in ten steps
- PB-05 Playbook: adding ISO/IEC 27701 privacy management to an existing ISMS
