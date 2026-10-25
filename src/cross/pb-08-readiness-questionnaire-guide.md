---
id: PB-08
title: "Playbook: Running a Readiness Assessment with the Questionnaire"
type: playbook
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 4.1
  - ISO/IEC 27001:2022 clause 9.1
  - SOC 2 CC4.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How to run the 60 question readiness questionnaire in GOV-REG-28, score it, read the result honestly and turn every gap into an owned action.
---
## 1. What the questionnaire is, and what it is not

GOV-REG-28 holds 60 questions in ten domains, six per domain. It measures two things at once: how much of a working security and privacy programme exists, and how much of it can be proved. Each question comes with a sentence on why it matters, so that the person answering understands what the question is for rather than guessing what the asker wants to hear.

It is not an audit. An audit samples records against the clauses of a standard; ISMS-REG-04 does that. It is not a legal gap assessment; GDPR-REG-01 does that for the GDPR. It is not a certification and produces nothing you can show a client as one. It is a structured conversation with evidence attached, and its output is a scored picture of where you stand and a list of actions.

Use it at four moments: at the start, as the baseline before PB-02, PB-03 or PB-04; three months before an external audit, alongside GOV-CHK-03; when a client or a board asks how mature the programme is; and once a year, so that the trend is visible.

## 2. Before you start

Four decisions, made by the executive sponsor and the Information Security Manager before anyone answers a question.

**Scope.** The whole organisation, or one business unit, or one service. If a scope statement already exists in ISMS-STM-01, use the same boundary so that the result is comparable with the audit.

**Roles.** A coordinator, usually the Information Security Manager, who runs the sessions and keeps the register. A reviewer for each domain who did not answer it. An executive sponsor who will receive the result and own the action list. Nobody scores their own domain; that rule is what makes the result worth reading.

**Time.** Two to three weeks elapsed. Each respondent spends about a day, split across a preparation hour, a ninety minute session and the time to find evidence. The coordinator spends four to five days.

**The copy.** Take a dated copy of GOV-REG-28 for this assessment. Never answer in the master. The dated copies are the trend.

## 3. The ten domains and who answers

| Domain | Typical respondent | Typical reviewer |
|---|---|---|
| Governance | Chief Executive Officer or executive sponsor | Internal Auditor |
| Scope and context | Information Security Manager | Internal Auditor |
| Risk | Information Security Manager and risk owners | Internal Auditor |
| Policies and documents | Information Security Manager and document owners | Internal Auditor |
| People | Head of human resources [Role] | Information Security Manager |
| Access | Head of Engineering or head of IT [Role] | Information Security Manager |
| Assets and data | System owners and the Privacy Officer | Information Security Manager |
| Technology and cloud | Head of Engineering | Information Security Manager |
| Suppliers | Procurement [Role] and supplier owners | Privacy Officer |
| Incidents and continuity | Information Security Manager and operations lead [Role] | Internal Auditor |

Where the same person holds several roles, which is normal in a small organisation, the reviewer for that person's domains must be someone else, even an external adviser or a board member. The respondent answers; the reviewer sets maturity and status.

## 4. The three answer types

Every question is prefilled with a suggested answer type. The type says what kind of thing counts as an answer.

**Policy.** Point to the approved document that states the rule: its identifier, version and approval date. "Yes, we have a policy" is not an answer; "GOV-POL-06 version 1.0, approved [Date], acknowledged by all staff in GOV-REG-23" is. A Policy answer earns maturity 3 only when there is also evidence that the rule is followed, so a Policy question often needs a register or proof reference as well.

**Register.** Point to the rows of the kit register that hold the record: for example, the access review rows in GOV-REG-12 for the last two quarters. The register must be live, with dated entries and named owners. A register that is still the blank template is a maturity 0 answer with good intentions.

**Proof.** Attach an artefact that shows the control operating: a system export, a screenshot that meets the rules in PB-09, a signed record, a closed ticket, a test result. One artefact per question is enough if it is the right one.

The respondent may propose a different type where a better form of answer exists; the reviewer decides. Three things are never an answer whatever the type: a sentence with no reference ("we do this"), a plan ("we will do this next quarter"), and the name of a product on its own.

## 5. Scoring: maturity 0 to 3

The reviewer scores each question after seeing the answer and the evidence.

| Maturity | Meaning | What the reviewer saw |
|---|---|---|
| 0 | Nothing in place, or the respondent does not know | No document, no record, no artefact |
| 1 | Done informally or occasionally, without a document or record, or with a document nobody follows | A verbal account, a draft, a stale record |
| 2 | Documented and performed, but the records are incomplete, irregular or not independently checked | An approved document and a partly filled register |
| 3 | Documented, performed at the stated frequency, records complete, verified by the reviewer | Document, live register and proof, all consistent |

The Status column carries the reviewer's confidence in the score. Verified means the reviewer saw the evidence and the maturity is final. To confirm means evidence was requested, an owner and due date are set, and the maturity is provisional. Not implemented means the maturity is 0 or 1 and an action is needed. Not applicable means the reviewer agrees the question does not apply, and the row leaves the arithmetic.

The arithmetic is deliberately simple. The Score column in GOV-REG-28 divides maturity by three for every applicable row. A domain percentage is the average Score across the domain's applicable rows, which is the same as the sum of maturity divided by three times the number of applicable questions. The overall percentage is the average of the ten domain percentages, so that every domain weighs the same however many rows were excluded. Report one more number beside the percentages: the count of Verified rows out of 60, the proof ratio. It separates "we have it" from "we can prove it", and auditors live on the second.

## 6. Running the sessions

Run one session per respondent, sixty to ninety minutes, with the register open on a shared screen.

1. The coordinator reads the question and the "why it matters" line aloud. The second line stops the conversation turning into a debate about what the question means.
2. The respondent names the answer. The coordinator records the answer type, the answer and the evidence reference in the row immediately. Nothing is written up afterwards from memory.
3. Anything without a reference becomes To confirm, with the respondent as owner and a due date inside five working days. This is the no-assumption rule from PB-09 and it applies to every row without exception.
4. Evidence is filed in the evidence folder under the numbered area that matches the domain, named as PB-09 describes, so that the reference in the register points to something that exists.
5. Within five working days of the last session the reviewer for each domain opens every reference, sets maturity and status, and writes one sentence in Reviewer notes saying what was seen or what is missing. A reviewer note that says only "OK" is not a review.
6. The coordinator closes To confirm rows as evidence arrives, and escalates any row still open after its due date to the sponsor. A To confirm row is never quietly extended.

## 7. Reading the result

| Overall percentage | Reading | What it means for the next step |
|---|---|---|
| 0 to 39 | Foundation | The programme does not yet exist in a provable form. Start at the first four steps of PB-02, or the opening phases of PB-03 or PB-04. Do not book an external audit |
| 40 to 69 | Developing | Rules exist but evidence is patchy. Concentrate on live registers and records. An internal audit now will find major nonconformities, which is useful if the organisation can hear it |
| 70 to 89 | Established | The programme operates. Close the specific gaps, run the first internal audit cycle under PB-06, and plan the external audit three to six months out |
| 90 to 100 | Audit-ready | Run GOV-CHK-03 four weeks before the certification audit or the start of the SOC 2 observation period, and keep the evidence habit |

Read the shape as well as the number. Any domain below 40 is a priority whatever the overall figure, because a certification audit fails on the weakest clause, not on the average. A high score on Policy questions beside a low proof ratio is a paper programme: the documents exist and the work does not. A domain with many To confirm rows is an ownership problem rather than a control problem, and the fix is a name beside each row, not a new procedure.

Give the sponsor three answers, not a spreadsheet: the lowest domain and why, the largest gap between what is written and what is proved, and how many rows have no owner.

## 8. Turning gaps into actions

Every row whose status is Not implemented, and every row Verified at maturity 0 or 1, becomes one action in GOV-REG-03 under GOV-PRO-04. The description is the question text plus what is missing. The source is "Readiness assessment, [Date]". The owner is the row owner. The action names the kit document that closes the gap, taken from the table below, and the due date follows priority.

| Domain | Kit documents that close the common gaps |
|---|---|
| Governance | GOV-POL-01, GOV-POL-03, GOV-PRO-03, GOV-REG-21, GOV-REG-01 |
| Scope and context | ISMS-STM-01, ISMS-PRO-01, ISMS-REG-03, GOV-PRO-25, GOV-REG-04 |
| Risk | GOV-PRO-05, GOV-REG-05, ISMS-REG-01, GOV-PRO-24, GOV-REG-06 |
| Policies and documents | GOV-PRO-01, GOV-REG-01, GOV-REG-23 |
| People | GOV-PRO-18, GOV-PRO-08, GOV-REG-09, GOV-CHK-01 |
| Access | GOV-PRO-10, GOV-POL-06, GOV-REG-12, GOV-REG-13 |
| Assets and data | GOV-PRO-16, GOV-REG-10, PIMS-REG-01, GDPR-REG-02, PIMS-POL-02, PIMS-REG-07, GOV-REG-20 |
| Technology and cloud | GOV-CHK-02, GOV-PRO-11, GOV-PRO-09, GOV-PRO-14, GOV-PRO-20, GOV-PRO-12, GOV-REG-15 |
| Suppliers | GOV-PRO-06, GOV-REG-07, GOV-TPL-04, PIMS-TPL-02 |
| Incidents and continuity | GOV-PRO-07, GOV-REG-08, PIMS-PRO-04, GOV-TPL-11, GOV-PRO-13, GOV-TPL-07, GOV-REG-16 |

Priority order: first anything that is a legal duty regardless of framework, which in practice means processor terms, the breach process and the processing inventory; then the blockers for the framework you are heading towards; then everything else from the lowest maturity upwards. The sponsor reviews the action list once, approves the dates and resources, and the list goes to the next management review under GOV-PRO-03 with the domain percentages beside it.

## 9. Repeating the assessment

Repeat annually and before each external audit. Keep every dated copy and compare domain percentages, not individual answers. Do not carry answers forward: a Proof answer older than twelve months is stale and is re-verified, and a Register answer is re-opened to check that entries continued after the last assessment. Put the overall percentage and the proof ratio into GOV-REG-21 as measures, so that the trend reaches management review without anyone having to remember to bring it.

## 10. Related documents

- GOV-REG-28 Readiness questionnaire
- GOV-REG-03 Corrective action log
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-CHK-03 Pre-audit readiness checklist
- ISMS-REG-04 Internal audit checklist
- GDPR-REG-01 GDPR gap assessment
- GOV-REG-21 Security objectives and measures tracker
- PB-09 Playbook: evidence management that survives an audit
