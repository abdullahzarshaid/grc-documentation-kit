---
id: ISMS-GDE-02
title: "Guide: mandatory documented information and records for ISO/IEC 27001:2022"
type: guide
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 4.3
  - ISO/IEC 27001:2022 clause 5.2
  - ISO/IEC 27001:2022 clause 6.1.2
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 6.2
  - ISO/IEC 27001:2022 clause 7.2
  - ISO/IEC 27001:2022 clause 7.5
  - ISO/IEC 27001:2022 clause 8.1
  - ISO/IEC 27001:2022 clause 8.2
  - ISO/IEC 27001:2022 clause 8.3
  - ISO/IEC 27001:2022 clause 9.1
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 9.3
  - ISO/IEC 27001:2022 clause 10.2
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: Lists the documents and records that ISO/IEC 27001:2022 explicitly requires, the kit item that satisfies each, and the further documents that are not required by name but that auditors expect and that make the system run.
---
## 1. Two kinds of documented information

The standard uses one term, documented information, for two things that behave differently. **Documents** say what you intend to do: the scope, the policy, the risk method, the objectives. They are approved, versioned and reviewed. **Records** show what you did: an audit report, a risk assessment result, a management review minute, a training record. They are created by running a process and are not edited afterwards. GOV-PRO-01 controls both.

The standard names a short list of items that must exist. Everything else is at your discretion, with one condition: you must keep whatever documented information you yourself decide is needed for the management system to work. In practice, an auditor who finds a process running well without a procedure will accept it; an auditor who finds a process running inconsistently will ask for the procedure that should have prevented it. The discretionary table in section 4 lists what experience says is worth having.

## 2. Documents the standard requires by name

| Clause | What must exist, in plain words | Kit item |
|---|---|---|
| 4.3 | A written scope of the management system, stating boundaries and applicability | ISMS-STM-01 |
| 5.2 | A written information security policy, approved, communicated and available | GOV-POL-03 |
| 6.1.2 | A defined and documented risk assessment process with criteria for acceptance and for performing assessments | GOV-PRO-05 |
| 6.1.3 | A documented risk treatment process, a risk treatment plan, and the Statement of Applicability with justification for inclusion and exclusion and the implementation status of each control | GOV-PRO-05, GOV-REG-05, ISMS-REG-01 |
| 6.2 | The information security objectives, kept as documented information | ISMS-PLN-01, GOV-REG-21 |
| 7.5.1 | The documented information required by the standard plus what the organisation determines necessary | This guide, GOV-REG-01 |
| 8.1 | Documented information to the extent needed to have confidence that operational processes ran as planned | ISMS-PRO-03 and the process documents it lists |

## 3. Records the standard requires by name

| Clause | What must be retained, in plain words | Kit item that produces it |
|---|---|---|
| 7.2 | Evidence of competence of people doing work that affects security performance | GOV-REG-09, GOV-TPL-10, ISMS-PRO-02 |
| 8.1 | Evidence that operational processes were carried out as planned | Process records named in ISMS-PRO-03 (for example GOV-REG-11, GOV-REG-12, GOV-REG-14, GOV-REG-15) |
| 8.2 | Results of each information security risk assessment | GOV-REG-05 (dated assessment entries) |
| 8.3 | Results of information security risk treatment | GOV-REG-05 (treatment columns), GOV-REG-06, ISMS-REG-02 |
| 9.1 | Evidence of monitoring and measurement results | GOV-REG-21, quarterly reports under ISMS-PRO-04, ISMS-REG-02 test results |
| 9.2.2 | Evidence of the audit programme and of each audit result | GOV-REG-02, ISMS-PLN-03, GOV-TPL-01, ISMS-REG-04 |
| 9.3.3 | Evidence of the results of management reviews | GOV-TPL-03, GOV-REG-22 |
| 10.2 | Evidence of the nature of nonconformities, actions taken, and results of corrective action | GOV-REG-03, GOV-TPL-02 |

Annex A adds its own documentation expectations where a control is applicable, for example topic specific policies (5.1), rules for acceptable use (5.10), supplier agreements (5.20), incident records (5.26 and 5.28), legal requirements (5.31), operating procedures (5.37), confidentiality agreements (6.6), logs (8.15), change records (8.32) and secure development rules (8.25 to 8.28). ISMS-GDE-01 maps each of these to the kit document that provides it.

## 4. Discretionary documents and why they earn their place

| Kit item | Why it is worth having |
|---|---|
| ISMS-PRO-01 and ISMS-REG-03 | Clause 4.1 and 4.2 require you to determine issues and interested parties; they do not require a document. Without one, every audit begins with the same hour of questions and no two answers match. |
| GOV-POL-01 | Roles and authorities must be assigned and communicated (5.3). A governance document with a roles table and committee charter is the fastest proof. |
| ISMS-PLN-02 | Clause 7.4 asks you to determine what, when, with whom and how to communicate. A one page plan answers all four at once. |
| GOV-PRO-01 and GOV-REG-01 | Clause 7.5 requires control of documented information; a procedure plus a master list is how organisations of every size do it. |
| ISMS-PRO-04 | Clause 9.1 requires you to determine what to monitor and measure, by what methods and when. Writing it down is the only way to get the same measure twice. |
| GOV-PRO-02 | Clause 9.2 requires an audit programme and audits; a procedure sets independence, grading and reporting rules that stay stable when auditors change. |
| GOV-PRO-03 | Clause 9.3 lists mandatory inputs and outputs; a procedure with an agenda stops them being forgotten. |
| GOV-PRO-04 | Clause 10.2 requires reaction, evaluation, action and review; a procedure sets root cause methods and closure authority. |
| ISMS-REG-02 | Not required by name, but the simplest way to show the 6.1.3 and 9.1 evidence per control. |
| GOV-CHK-03 | A readiness checklist four weeks before an external audit is the cheapest insurance against a stage 1 surprise. |
| Topic policies (GOV-POL-02, GOV-POL-04, GOV-POL-05, GOV-POL-06) | Annex A 5.1 expects topic specific policies where the risks need them; these four cover the topics every organisation has. |
| Operational procedures (GOV-PRO-06 to GOV-PRO-27) | Each implements a group of Annex A controls; they are discretionary only in the sense that you could run the control without writing it down. |

## 5. What auditors look for in each item

- **A control block** on every document (identifier, owner, approver, version, dates) and a revision history that matches GOV-REG-01.
- **Approval evidence** for the policy, the scope and the risk method: a signature, an approval record or a minute.
- **Dates that make sense.** The risk assessment precedes the Statement of Applicability, which precedes the treatment plan; the internal audit and the management review both precede the stage 2 audit.
- **Records that are not editable after the fact**, or that carry a change history if they are.
- **Consistency.** The scope in ISMS-STM-01, the asset list in GOV-REG-10, the systems in GOV-REG-24 and the risks in GOV-REG-05 describe the same organisation. A system that appears in one and not the others is the first question an auditor asks.
- **Currency.** Every document within its review date; every register with entries from the current period.

## 6. Building your master list

Create GOV-REG-01 before anything else and add every item in sections 2 to 4 as a row with status Draft. As each document is approved, change the status and record the version and location. The master list is then both your project plan and your proof of clause 7.5. ISMS-REG-05 holds the implementation tasks that produce each item; PB-02 gives the order.

## 7. Related documents

- GOV-PRO-01 Document control procedure
- GOV-REG-01 Master list of documents and records
- ISMS-GDE-01 Guide to the 93 Annex A controls
- ISMS-GDE-03 Guide to the certification journey
- ISMS-REG-05 Implementation project plan
- GOV-CHK-03 Pre-audit readiness checklist
