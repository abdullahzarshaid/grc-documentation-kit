---
id: ISMS-PRO-02
title: Competence and awareness procedure
type: procedure
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 7.2
  - ISO/IEC 27001:2022 clause 7.3
  - ISO/IEC 27001:2022 Annex A 6.3
  - SOC 2 CC1.4
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] decides what competence each security role needs, checks whether the people in those roles have it, closes gaps, keeps the records, and makes every person aware of what the management system expects of them.
---
## 1. Purpose

This procedure makes sure that the people who operate, administer, develop, audit and lead within the management system are able to do so, and that everyone else knows the rules that apply to them and why they matter. Awareness content and delivery are described in GOV-PRO-08; this procedure defines the competence requirements, the assessment and the records.

## 2. Scope

It applies to employees, contractors and temporary workers who hold any role in the competence matrix in step 4.1, and to all staff for the awareness requirements in step 4.6. Supplier personnel who administer in-scope systems are covered through the equivalence rule in step 4.7.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the competence matrix, approves training plans for security roles, keeps GOV-REG-09 complete. |
| Line manager | Maps each person to the roles they hold, assesses them against the matrix on appointment and annually, agrees gap closing actions. |
| Head of People | Runs induction scheduling, keeps employment records that show competence evidence, confirms contractor equivalence. |
| Individual | Completes assigned training by the due date and tells the line manager of any gap in knowledge needed for the role. |
| Internal Auditor | Samples competence records each audit cycle and confirms their own independence and competence before each audit. |

## 4. Procedure

4.1 **Competence matrix.** The Information Security Manager maintains the matrix below. A person who holds more than one role meets the requirements of each.

| Role | Competence required | Evidence accepted | Refresh |
|---|---|---|---|
| Information Security Manager | Working knowledge of ISO/IEC 27001:2022 clauses 4 to 10 and Annex A, risk assessment, audit practice, incident command, [Organisation]'s technology | Recognised security management certification, or three years of relevant experience plus an implementer course; annual continuing education record | Annual |
| Privacy Officer | Data protection law in the jurisdictions served, impact assessment, rights handling, breach assessment | Recognised privacy qualification or two years of relevant experience; annual legal update | Annual |
| System Owner | The system's purpose, data classification, access model, dependencies and the procedures that apply to it | Role induction completed; one access review performed under supervision | On appointment and at role change |
| Administrator with privileged access | Secure configuration, logging, patching, incident escalation for the platforms administered | Platform training or a task demonstrated under supervision; GOV-CHK-02 walkthrough signed off | Annual |
| Developer | The secure coding rules in GOV-PRO-15, threat modelling basics, secrets handling, dependency hygiene | Secure coding course completed; participation in peer review | Annual |
| Internal Auditor | Audit technique, the requirements of the standard, independence rules, report writing | Internal auditor course; one full audit shadowed before leading one | Every two years |
| Incident Lead | GOV-PRO-07, evidence preservation, communication rules, decision making under time pressure | Participation in an exercise or a real incident review within the last twelve months | Annual |
| Line manager | Joiner, mover and leaver duties, policy enforcement, how to report concerns | Manager briefing completed | Annual |
| All staff | The policies that apply to them, how to report an event, consequences of breaches | Induction within ten working days of start and annual refresher | Annual |

4.2 **Assessment.** On appointment and once a year the line manager compares the person with the row for each role held, records whether each element of competence is met, and lists gaps. The assessment is dated and kept with the training record.

4.3 **Gap closing.** For each gap the line manager and the Information Security Manager choose one or more actions: a course, mentoring or supervised practice, a temporary external specialist, or recruitment. Each action has a due date. A gap in a role with privileged access or incident authority is closed within ninety days; until then the person acts under the supervision of someone who meets the requirement.

4.4 **Verification of effectiveness.** After the action is complete the line manager confirms competence by one of: a test result, a task observed and signed off, an audit or review result, or the quality of work produced over the following quarter. The method and result are recorded; an action without a recorded verification is not counted as closed.

4.5 **Records.** The Head of People records every assessment, course, certificate, supervised task and verification in GOV-REG-09, with the session record GOV-TPL-10 where a session was delivered. Records are kept for the period of engagement plus [Number] years.

4.6 **Awareness.** Every person in scope knows the information security policy GOV-POL-03, how their work contributes to the objectives in ISMS-PLN-01, the benefit of following the controls that apply to them, how to report an event under GOV-PRO-07, and the consequences of not following the rules under GOV-PRO-18. Awareness is delivered under GOV-PRO-08 and acknowledged in GOV-REG-23.

4.7 **Contractors and supplier personnel.** Before access is granted, the engaging manager obtains evidence that the person meets the matrix row for the role, or that the supplier applies an equivalent requirement under the contract managed through GOV-PRO-06. The evidence or the contract reference is recorded in GOV-REG-09.

4.8 **Auditor competence and independence.** Before each internal audit the Information Security Manager confirms that the auditor meets the matrix row, has no responsibility for the area audited in the preceding twelve months, and has reviewed the current audit plan. Where no independent internal person exists for an area, an external auditor is engaged and the same evidence is obtained.

4.9 **Review of the matrix.** The Information Security Manager reviews the matrix annually and within thirty days of a new system, a new role, a change in law that affects the Privacy Officer, or an incident or audit finding that points to a competence gap.

## 5. Records and evidence

- GOV-REG-09 Training and awareness register: assessments, courses, verifications and due dates for every person in scope.
- GOV-TPL-10 Awareness session record and acknowledgement for each delivered session.
- GOV-REG-23 Policy acknowledgement register.
- The dated competence matrix and the annual review note.
- Auditor independence confirmations filed with each audit under GOV-PRO-02.

## 6. Exceptions

A person may be appointed to a role before meeting the matrix row only with the written agreement of the Information Security Manager, a named supervisor who meets the row, and a closing date within ninety days recorded in GOV-REG-09. No exception applies to the Internal Auditor independence rule.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding against clauses 7.2 or 7.3. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-08 Security and privacy awareness and training procedure
- GOV-REG-09 Training and awareness register
- GOV-TPL-10 Awareness session record and acknowledgement
- GOV-REG-23 Policy acknowledgement register
- GOV-PRO-02 Internal audit procedure
- GOV-PRO-18 Human resources security procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-POL-03 Information security policy
- ISMS-PLN-01 Information security objectives and plan
