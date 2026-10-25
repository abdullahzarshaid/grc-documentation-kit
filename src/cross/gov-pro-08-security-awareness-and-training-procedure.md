---
id: GOV-PRO-08
title: Security and privacy awareness and training procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 7.2
  - ISO/IEC 27001:2022 clause 7.3
  - ISO/IEC 27001:2022 Annex A 6.3
  - ISO/IEC 27701 clause 6.4.2.2
  - SOC 2 CC1.4
  - SOC 2 CC2.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How every person who works for [Organisation] receives the security and privacy knowledge their role needs, from induction through annual refreshers, role-based modules and phishing simulation, and how the results are recorded and measured.
---
## 1. Purpose

This procedure sets out how [Organisation] plans, delivers, records and measures security and privacy awareness and training, so that every person understands the policies that apply to them, recognises the attacks they are most likely to face, and knows how to report a problem.

## 2. Scope

It applies to employees, contractors, temporary staff and interns who hold an account on any [Organisation] system or who handle [Organisation] information. Supplier personnel are covered through the supplier's own training obligations under GOV-PRO-06. It covers induction, the annual refresher, role-based training, phishing simulation and awareness messages.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the programme, approves content, runs the phishing simulation, keeps GOV-REG-09 and reports results to the steering committee. |
| Privacy Officer | Writes and approves the privacy modules and the role-based training for staff who handle personal data. |
| Line manager | Confirms that each new starter completes induction on time, nominates staff for role-based training and follows up overdue training. |
| Human Resources | Notifies the Information Security Manager of every starter, role change and leaver, and holds the signed acknowledgements. |
| Trainer | Delivers a session, completes GOV-TPL-10 and returns it within five working days. |
| All staff | Complete the training assigned to them by the due date and apply it. |

## 4. Procedure

4.1 **Annual plan.** Each year the Information Security Manager and the Privacy Officer write a training plan that lists every module, its audience, its delivery method, its due dates and its measure of success. The plan takes its topics from the risk register (GOV-REG-05), the incident register (GOV-REG-08), the previous year's phishing results and any audit finding about competence. The steering committee approves the plan.

4.2 **Competence matrix.** The Information Security Manager keeps a competence matrix listing each role group, the knowledge it needs, the module that provides it and the evidence of achievement, reviewed with the annual plan and when a new role group is created. ISMS-PRO-02 holds the matrix for roles with management system duties. The minimum content is:

| Role group | Mandatory modules | Frequency |
|---|---|---|
| All staff | Induction, annual refresher, phishing simulation | Induction once, refresher yearly, simulation quarterly |
| Developers | Secure coding, secrets handling, dependency hygiene | Yearly, and before the first production change |
| System administrators | Privileged access, logging, change and backup duties | Yearly, and before privileged access is granted |
| Personal data handlers | Lawful handling, data subject requests, breach recognition | Yearly, and before first access to personal data |
| Managers | Approving access, disciplinary handling, incident escalation | Yearly |
| Incident responders | Incident procedure walkthrough, evidence handling | Yearly, plus one exercise |

4.3 **Induction.** Human Resources tells the Information Security Manager about each starter before the start date. The starter completes the induction module within [Number] working days of starting, and in every case before being granted access to Confidential or Restricted information. Induction covers GOV-POL-03, GOV-POL-02, GOV-POL-06 and GOV-POL-04, classification and handling under GOV-PRO-16, recognising phishing and social engineering, reporting an incident under GOV-PRO-07, and the basics of personal data protection. The starter signs the policy acknowledgement, which Human Resources records in GOV-REG-23.

4.4 **Annual refresher.** Every person completes the refresher module within the calendar month set in the plan. It updates the induction topics with the past year's incidents, current phishing patterns and policy changes, and ends with an assessment of at least ten questions; the pass mark is [Number] per cent and a person who fails retakes the module within ten working days.

4.5 **Role-based training.** The line manager nominates staff for the role-based modules in the competence matrix. Role-based training is completed before the related access or duty is granted, and then yearly. The Privacy Officer delivers or approves the personal data modules. The Head of Engineering confirms each year that the developer and administrator modules reflect the current secure development and operational procedures.

4.6 **Phishing simulation.** The Information Security Manager runs a simulated phishing exercise at least quarterly, with a different scenario each time. Results are recorded by cohort and never used for disciplinary action on a first failure; anyone who clicked receives a short teaching page within one working day. A person who fails two consecutive simulations completes a targeted module within ten working days. The reporting rate is tracked alongside the click rate, because reporting is the behaviour the programme wants to build.

4.7 **Awareness messages.** Between formal modules the Information Security Manager issues a short awareness message at least monthly through the channel named in the communication plan: a current scam, a reminder of a rule, or a lesson from an incident with identifying details removed.

4.8 **Delivery and recording.** A trainer who delivers a live session completes GOV-TPL-10 with the content outline, attendance, assessment results and sign-off. For online modules the learning platform's completion report is the record. The Information Security Manager enters every completion, result and due date in GOV-REG-09 within five working days.

4.9 **Overdue training.** The Information Security Manager sends each line manager a list of overdue training monthly. Training more than thirty days overdue is reported to the steering committee, and the System Owner may suspend the person's access to Restricted information until the module is completed.

4.10 **Measuring effectiveness.** Each quarter the Information Security Manager reports: completion rate by module and role group, average assessment score, phishing click rate and reporting rate, the number of incidents reported by staff, and the number caused by a human error that training addresses. A measure that misses its target for two consecutive quarters raises a corrective action under GOV-PRO-04.

4.11 **Content review.** Every module is reviewed yearly, after a significant incident, after a change of law and after a change to a policy it teaches. The review date and reviewer are recorded against the module in the training plan.

## 5. Records and evidence

- GOV-REG-09 Training and awareness register: every module, person, due date, completion date and result.
- GOV-TPL-10 Awareness session record and acknowledgement: the record of each live session.
- GOV-REG-23 Policy acknowledgement register: the acknowledgements taken at induction and after policy changes.
- The approved annual training plan and competence matrix.
- Phishing simulation reports by quarter.
- The quarterly effectiveness report to the steering committee.

## 6. Exceptions

A person who cannot complete induction within the set period because of an absence completes it within [Number] working days of returning and is not granted access to Confidential or Restricted information in the meantime. A request to exempt a role group from a module is handled as a risk acceptance under GOV-PRO-24. No other exception applies.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any audit finding about competence or awareness, and after an incident whose root cause was a gap in training. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-09 Training and awareness register
- GOV-TPL-10 Awareness session record and acknowledgement
- GOV-REG-23 Policy acknowledgement register
- GOV-PRO-18 Human resources security procedure
- GOV-POL-02 Acceptable use policy
- GOV-POL-03 Information security policy
- GOV-PRO-07 Information security incident management procedure
- ISMS-PRO-02 Competence and awareness procedure
- GDPR-REG-05 Privacy training register
