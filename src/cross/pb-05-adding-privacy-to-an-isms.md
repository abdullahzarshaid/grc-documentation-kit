---
id: PB-05
title: "Playbook: adding ISO/IEC 27701 privacy management to an existing ISMS"
type: playbook
framework: cross
maps:
  - ISO/IEC 27701 clause 5.2.1
  - ISO/IEC 27701 clause 5.2.3
  - ISO/IEC 27701 clause 5.4.1.3
  - ISO/IEC 27701 Annex A
  - ISO/IEC 27701 Annex B
  - ISO/IEC 27001:2022 clause 4.3
  - ISO/IEC 27001:2022 clause 6.1.3
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How an organisation that already runs an ISO/IEC 27001 management system extends it to personal data and prepares for ISO/IEC 27701 certification, in eight steps, with the evidence an auditor will ask for and the findings that most often go wrong.
---
## 1. What you are adding, and what you are not

If you already operate an information security management system, the privacy extension is not a second system. It is the same scope decision, the same risk method, the same Statement of Applicability, the same audit programme and the same management review, each widened so that personal data and the people it describes are inside them. The work is in four places: the facts you do not yet have written down (which processing you do, in which role, on what basis), the controls you do not yet operate (rights handling, breach assessment, consent, transfers, processor terms), the documents that must say "and privacy" where they now say "security", and the evidence that all of this runs for long enough to be audited.

What you are not adding is legal compliance by certificate. ISO/IEC 27701 is a management system standard; it asks you to identify the privacy law that applies and run processes that meet it, and the auditor tests the processes. It does not certify that you comply with any particular law, and you should never say that it does. The GDPR documents in the kit, such as GDPR-GDE-01 and GDPR-REG-01, deal with the law itself; this playbook deals with the management system that carries it.

Expect the extension to take three to six months for an organisation with a working ISMS, most of it in steps 3 to 6, plus the operating period in step 7 before an audit is worth booking.

## 2. What changes in the ISMS

| Area | Before the extension | After the extension |
|---|---|---|
| Scope | ISMS-STM-01 names services, systems and locations | It also names the processing of personal data covered and the role of [Organisation] for each |
| Context and interested parties | Customers, regulators and staff in ISMS-REG-03 | Individuals whose data is processed, privacy regulators and client controllers are added with their requirements, and privacy law is in GOV-REG-04 |
| Policy | GOV-POL-03 commits to information security | PIMS-POL-01 commits to the privacy principles beside it, and GOV-POL-03 refers to it |
| Roles | Information Security Manager accountable | A Privacy Officer is named in GOV-POL-01 with independence, resources and a reporting line to the top |
| Risk | GOV-REG-05 scores impact on the organisation | GOV-PRO-05 also scores severity for individuals, PIMS-PRO-02 screens every processing activity, and PIMS-REG-08 records assessments |
| Statement of Applicability | ISMS-REG-01 covers the 93 controls | It also covers Annex A, Annex B or both, justified per processing role, using PIMS-GDE-01 |
| Controls | Security procedures | The privacy procedures PIMS-PRO-01 to PIMS-PRO-07, the policies PIMS-POL-02 and PIMS-POL-03 and the agreement PIMS-TPL-02, plus privacy additions to training, classification, backups, logs, test data, suppliers and incidents |
| Registers | GOV and ISMS registers | PIMS-REG-01 to PIMS-REG-08 are added and existing registers gain privacy columns |
| Competence | Security training | Privacy training for all staff and role-based training for handlers, developers and responders, recorded in GDPR-REG-05 |
| Measurement, audit and review | ISMS-PRO-04, ISMS-PLN-03, GOV-PRO-03 | PIMS-PRO-07 adds privacy measures, the audit plan adds the annexes and clause 5, and the Privacy Officer attends management review |

## 3. The eight steps

### Step 1: decide the roles and the scope

Start with PIMS-PRO-01, not with the standard. For every service you run and every data set you hold, decide whether [Organisation] is a controller, a processor or both, and write the reasoning down. Most product companies are both: controller for their own customers, employees, applicants and marketing, and processor for the data their customers put into the product. The answer decides whether Annex A, Annex B or both apply, which procedures carry the most weight, and what your contracts must say.

Then revise ISMS-STM-01 so that it names the processing of personal data that is inside the scope and the role for each. A scope that says "all processing" is honest only if the inventory in step 3 supports it. Record the two decisions in GOV-REG-01 as a scope change and have the approver sign it.

**Inputs:** service list, contracts, ISMS-STM-01. **Outputs:** role decisions in PIMS-REG-01, revised ISMS-STM-01. **Duration:** two weeks.

### Step 2: appoint the Privacy Officer and change governance

Name the Privacy Officer in GOV-POL-01 with the responsibilities in PIMS-POL-01: independence in how the role performs its tasks, direct access to the Chief Executive Officer, a seat at the steering committee and at management review, and the resources to run the procedures. Decide whether the role is a formal data protection officer under the law in GOV-REG-04; the kit uses one role name for both cases. Approve PIMS-POL-01, add it to the mandatory policies list in GOV-POL-03, communicate it under ISMS-PLN-02 and collect acknowledgements in GOV-REG-23.

Update ISMS-REG-03 with the new interested parties and their requirements, and GOV-REG-04 with the privacy law and the client contract clauses that apply. These two registers are what the auditor reads first to see whether you know what you are being measured against.

**Outputs:** approved PIMS-POL-01, updated GOV-POL-01, ISMS-REG-03, GOV-REG-04. **Duration:** two weeks, in parallel with step 1.

### Step 3: build the processing inventory

PIMS-REG-01 is the foundation that every other privacy control refers to. Build it with the workshop method in GDPR-PRO-01: one session per function, listing every activity in which personal data is used, with purpose, lawful basis, data items, individuals, recipients, transfers, retention and the systems involved. Map the flows in GDPR-REG-02 and GOV-REG-25 at the same time. Give every row a Processing Owner, not a department.

Three traps. First, internal processing (HR, recruitment, access logs, monitoring, building access) is forgotten because the privacy conversation starts with customers. Second, processors and sub-processors are listed from memory rather than from GOV-REG-07, so a tool someone signed up for last year is missed. Third, retention is written as "as long as necessary", which PIMS-POL-02 forbids; put a period and a trigger in every row even if the first value is a best estimate marked for review.

**Outputs:** PIMS-REG-01 complete, GDPR-REG-02, PIMS-REG-06 and PIMS-REG-05 populated, PIMS-REG-07 drafted. **Duration:** four to six weeks.

### Step 4: extend the risk assessment to individuals

Your risk method already exists in GOV-PRO-05. The extension is to assess, for every processing activity, the harm to the individuals as well as to [Organisation], using the severity scale in PIMS-PRO-02 step 4.8, and to screen every activity for a full assessment under PIMS-PRO-02 step 4.1. Record screening outcomes in PIMS-REG-08 even when the answer is "not required", because the auditor will ask how you know an assessment was not needed. Complete a full assessment on PIMS-TPL-01 for every activity that triggers one, and carry every medium or higher residual risk into GOV-REG-05 with a cross-reference.

Do not run a separate privacy risk register. One register with a column for harm to individuals keeps the treatment plan, the acceptances and the review cycle in one place, which is what clause 5 of the standard expects.

**Outputs:** PIMS-REG-08 with every activity screened, completed assessments, GOV-REG-05 extended. **Duration:** three to four weeks.

### Step 5: extend the Statement of Applicability

Add the Annex A and Annex B rows to ISMS-REG-01 using the tables in PIMS-GDE-01. For each row decide Applicable Yes or No, write a justification that names the processing role and the risk or requirement, set the implementation status honestly, and name the kit documents you use. A processor-only organisation marks Annex A not applicable with that reason; a controller-only organisation does the same for Annex B; an organisation that is both applies both and says for which activities.

Walk the clause 5 and clause 6 table in section 4 of PIMS-GDE-01 at the same time and list the existing documents that need "and privacy" added: the training content, the classification scheme, the backup and logging procedures, the test data rules, the supplier procedure and the incident procedure. Raise a GOV-REG-03 action for each.

**Outputs:** ISMS-REG-01 extended, ISMS-REG-02 extended, a gap list in GOV-REG-03. **Duration:** two weeks.

### Step 6: implement the privacy procedures

Issue and operate, in this order, because each depends on the one before: PIMS-PRO-05 (consent and notices, so that what you tell people matches PIMS-REG-01); PIMS-POL-02 and PIMS-REG-07 (retention, configured in systems); PIMS-PRO-03 and PIMS-REG-02 (rights handling, with GDPR-TPL-05 letters ready); PIMS-PRO-04 and PIMS-REG-03 (breach assessment, wired into GOV-PRO-07 step 4.4, with GDPR-TPL-10 ready); PIMS-TPL-02 and PIMS-REG-06 (processor terms, signed with every processor and offered to every client); PIMS-POL-03 and PIMS-REG-05 (transfers, with GDPR-TPL-08 assessments for every transfer that relies on contractual safeguards); PIMS-PRO-06 (privacy by design, wired into GOV-PRO-15 and PB-07). Close the "and privacy" gaps from step 5 under GOV-PRO-01.

Then train. All staff get the privacy module under GOV-PRO-08; request handlers, developers, support staff and incident responders get role-based sessions; record everything in GDPR-REG-05. A procedure nobody has been trained on is a document, not a control.

**Outputs:** every PIMS procedure issued and acknowledged, registers live, training records. **Duration:** six to ten weeks.

### Step 7: operate and collect evidence

Run the extended system for at least three months before the audit, and preferably through one full quarter of PIMS-PRO-07 reporting. The auditor wants to see processes that have happened, not processes that could happen: requests received and answered on time in PIMS-REG-02, a breach exercise or a real event assessed under PIMS-PRO-04, assessments approved before go-live in PIMS-REG-08, retention checks with results in PIMS-REG-07, processor terms signed and sub-processor notices sent, and a quarterly report presented at management review.

File the evidence under PB-09 so that every register row points to an artefact. If no request or breach has occurred, run a tabletop exercise of each and keep the record; an exercise is evidence that the procedure works, silence is not.

**Outputs:** one quarter of records across every register, one PIMS-PRO-07 report, management review minutes in GOV-TPL-03 covering privacy. **Duration:** three months minimum.

### Step 8: audit, review and certify

Extend ISMS-PLN-03 so that clause 5, the clause 6 additions and every applicable annex control are audited within the cycle, and add privacy questions to ISMS-REG-04. Run the internal audit under GOV-PRO-02 with an auditor who did not build the extension, raise findings in GOV-REG-03 and close them with verified effectiveness. Hold a management review under GOV-PRO-03 with the privacy report as an input and minute the decisions.

Certification follows the path in ISMS-GDE-03: the privacy extension is audited either with the next ISO/IEC 27001 surveillance or recertification visit, or as a separate extension audit, and the certification body decides which edition of ISO/IEC 27701 it audits against, so confirm the numbering with them before the Statement of Applicability is final (PIMS-GDE-01 section 5).

**Outputs:** audit report in GOV-TPL-01, closed findings, management review minutes, certification audit booked. **Duration:** six to eight weeks.

## 4. The evidence an auditor asks for

| Area | What is asked for | Where it is |
|---|---|---|
| Roles and scope | The role decision for each service and the scope statement that reflects it | PIMS-REG-01 reasoning notes, ISMS-STM-01, GOV-REG-01 approval |
| Governance | The Privacy Officer's appointment, reporting line and attendance at management review | GOV-POL-01, GOV-TPL-03 attendance |
| Inventory | A complete record of processing with purpose, basis, data, recipients, retention and transfers | PIMS-REG-01, GDPR-REG-02 |
| Risk | Screening of every activity, completed assessments, residual approval, risks in the register | PIMS-REG-08, PIMS-TPL-01 documents, GOV-REG-05 |
| Applicability | Annex A and Annex B rows with justification and status | ISMS-REG-01, ISMS-REG-02 |
| Transparency and consent | Notices matching the inventory, consent records, withdrawal tests | PIMS-REG-04, published notice versions in GOV-REG-01 |
| Rights | Requests logged, verified, answered on time, refusals reasoned | PIMS-REG-02, correspondence, GDPR-TPL-05 letters |
| Breaches | Time of awareness, assessment, decision, notification or reasons for none | PIMS-REG-03, GDPR-TPL-10, GOV-REG-08 |
| Processors and transfers | Signed terms, sub-processor list and notices, transfer mechanisms and assessments | PIMS-REG-06, PIMS-TPL-02 agreements, PIMS-REG-05, GDPR-TPL-08 |
| Retention | The schedule, configuration evidence, check results, disposal records | PIMS-REG-07, GOV-REG-20 |
| Design | Checklists and gate reviews for recent changes | PIMS-PRO-06 review records, GOV-REG-29 |
| Competence | Training completion for all staff and role-based sessions | GDPR-REG-05, GOV-REG-09 |
| Performance | Quarterly measures, control grades, management review input | GOV-REG-21, PIMS-PRO-07 reports, GOV-TPL-03 |
| Audit and improvement | Internal audit coverage of the extension, findings and their closure | ISMS-PLN-03, GOV-TPL-01, GOV-REG-03 |

## 5. Common findings and how to avoid them

| Finding | Why it happens | Avoid it by |
|---|---|---|
| Role not decided, or decided differently in the contract and the inventory | Sales labelled the organisation a processor to close a deal; the facts say controller | Run PIMS-PRO-01 before signature and let the legal adviser align the wording (step 4.10) |
| Scope statement silent on personal data | The ISMS scope was copied forward | Revise ISMS-STM-01 in step 1 and approve the change |
| Inventory misses internal processing | Workshops started with customers | Hold one workshop per function, including HR, finance, facilities and IT |
| Retention "as long as necessary" | Nobody wanted to commit to a number | PIMS-POL-02 statement 4.4: a period and a trigger in every row |
| Assessments missing or done after go-live | Screening was left to the developer | Screening at concept stage in PIMS-PRO-02 step 4.1, gate 3 before production |
| Statement of Applicability does not cover the annexes | The team treated the annexes as guidance | Clause 5 makes them normative; add the rows in step 5 |
| Notice does not match the inventory | Notice written by marketing, inventory by the Privacy Officer, never compared | Annual check in PIMS-PRO-05 step 4.11, and change control from register changes |
| No evidence of requests or breaches | None occurred during the operating period | Tabletop exercises with records, as step 7 says |
| Processor terms missing for small tools | The tool was free or signed up by one person | GOV-PRO-06 step 4.3 and the supplier register as the only source of truth |
| Transfers without an assessment | The clauses were signed and the assessment assumed | PIMS-POL-03 statement 4.4; PIMS-REG-05 has no mechanism column without an assessment reference |
| Training not role-based | One generic module for everyone | GOV-PRO-08 role sessions for handlers, developers, support and responders |
| Privacy Officer not independent | The role sits inside the team it must challenge | Reporting line and independence written into GOV-POL-01 in step 2 |

## 6. Related documents

- PIMS-GDE-01 Guide: ISO/IEC 27701 Annex A and Annex B controls and where the kit covers each
- PIMS-POL-01 Privacy information management policy
- PIMS-PRO-01 Determining controller and processor roles
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-PRO-07 Privacy control effectiveness monitoring procedure
- ISMS-STM-01 ISMS scope statement
- ISMS-REG-01 Statement of Applicability
- ISMS-GDE-03 Guide: the certification journey from decision to recertification
- GDPR-PRO-01 Data mapping and records of processing procedure
- GDPR-GDE-01 Guide: a GDPR operating model for a product or service team
- PB-02 Playbook: ISO/IEC 27001:2022 implementation in twelve steps
- PB-04 Playbook: GDPR operations for a product team in ten steps
- PB-09 Playbook: evidence management that survives an audit
