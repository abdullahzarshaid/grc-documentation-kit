---
id: PB-06
title: "Playbook: running your first internal audit cycle"
type: playbook
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 9.2.1
  - ISO/IEC 27001:2022 clause 9.2.2
  - ISO/IEC 27001:2022 clause 10.2
  - SOC 2 CC4.1
  - SOC 2 CC4.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: A practical walk through the first internal audit cycle, from preparing the programme and the checklist to interviewing, sampling, writing findings in four parts, running the closing meeting, raising corrective actions and following them up, for the person who has to do it for the first time.
---
## 1. What a first cycle has to achieve

The first internal audit cycle has three jobs. It must cover every clause 4 to 10 requirement and every control declared applicable in ISMS-REG-01 before the certification audit. It must produce findings that are true, specific and written well enough for someone to act on. And it must show the corrective action loop in GOV-PRO-04 working end to end, because that loop is what the external auditor reads first.

Expect findings. A first implementation is never clean, and an internal audit report with nothing in it tells an external auditor that the audit did not look. Ten to twenty findings across a first cycle, most of them minor or observations, is normal.

The rules are in GOV-PRO-02; this playbook shows how to apply them. The same cycle serves a SOC 2 programme as the separate evaluation that CC4.1 and CC4.2 ask for.

## 2. Six things to have in place before the first audit

1. **An approved plan.** ISMS-PLN-03 names the audits, their scope, auditor, auditee and quarter, and GOV-REG-02 has one row per audit with Status Planned. An audit without a programme behind it is itself a nonconformity against clause 9.2.
2. **A competent auditor.** GOV-PRO-02 step 4.3 sets the bar. If nobody inside meets it, engage an external auditor for the first cycle and have your intended auditor shadow them. The person who runs the management system cannot audit it.
3. **An independence map.** Write down who may not audit what, using the table in ISMS-PLN-03 section 5, and record the arrangement in the Notes column of GOV-REG-02 before each audit.
4. **Three months of records.** Audits test operation, not intention. Before a control has run for a quarter you can only audit its design, and the report should say so.
5. **An evidence folder you can read.** Set it up as PB-09 describes and give the auditor read access to the whole period. Evidence requested one file at a time doubles the fieldwork.
6. **Warned auditees.** The schedule goes out at the start of the cycle under ISMS-PLN-02, and each audit plan ten working days ahead. Surprise audits produce defensive interviews and missing people.

## 3. Planning one audit

The audit plan is one page: the scope area and the systems in it; the criteria (clause numbers, control numbers and the kit documents that implement them, as listed in ISMS-PLN-03); the dates and the day-by-day timetable; the people to interview, by role; the records to have available; the ISMS-REG-04 rows you will use; and how confidential material will be handled. Send it, get the confirmation, then read every document in the criteria before day one and pre-fill the Evidence to request column of your checklist copy. Fieldwork is for seeing evidence, not for discovering what it is called.

| When | What you do |
|---|---|
| Ten working days before | Issue the plan; book rooms and calls; request read access to the systems you will inspect |
| Three working days before | Receive the confirmation; chase anyone missing |
| The day before | Read the documents; prepare the checklist copy; list the populations you will sample and request the exports |
| Day one, first twenty minutes | Opening meeting: scope, timetable, grading scale, how evidence will be shared, who to call if something cannot be found |
| Fieldwork | Interviews of forty-five to sixty minutes; evidence inspection between them; keep one third of the time free for chasing evidence |
| Last hour | Closing meeting (section 9) |
| Within ten working days | Report on GOV-TPL-01 |

Budget one to three days of fieldwork per audit and never more than four interviews in a day.

## 4. Using ISMS-REG-04

The checklist has about one hundred and thirty rows: around thirty for clauses 4.1 to 10.2 and one for each Annex A control. Each row carries a question you can answer yes or no, the evidence to ask for and the role to ask. The first three columns are fixed; the rest are yours.

Work from a copy per audit, named for the audit reference, and keep only the rows in that audit's criteria. For controls marked Not applicable in ISMS-REG-01, set Result to Not applicable and write the Statement of Applicability justification in Notes, so the row shows that you checked the exclusion rather than skipped it. Add rows for your own policy statements where the kit question does not reach them.

The question is the way in, not a script. Ask it, ask to be shown, then follow what you see. Four rules keep the completed checklist usable as a record:

- One row, one conclusion. If a control conforms on one system and fails on another, split the row.
- No blank rows. Every row ends as Conforms, Minor, Major, Observation or Not applicable.
- Conforms needs evidence. Write the file names you saw, named as PB-09 requires, in Evidence seen; never write "seen" or "discussed".
- Notes hold the population, the sample size, how the sample was chosen and the exact words of any statement you rely on.

File the completed copy in area 11 of the evidence folder with the report. A checklist with evidence beside every row is what persuades an external auditor that the cycle was real.

## 5. Interviewing

Interview the role holders named in the plan, and at least two staff you choose on the day for the awareness questions under clause 7.3. Say at the start that you are auditing the process, not the person.

| Type | Purpose | Example |
|---|---|---|
| Open | Get the person to describe the process in their own words | Walk me through what happens from the day someone resigns to the day their access is gone |
| Probing | Test a detail or a boundary | What happens when the line manager is on leave that week |
| Show me | Convert a statement into evidence | Open the record for the most recent leaver and show me the removal date |
| Closing | Find what the person already knows is weak | If you could fix one thing about this process, what would it be |

Three habits matter. Separate what should happen from what did happen: "we usually" is answered with "show me the last one". Do not lead; "you do review access quarterly, don't you" produces a yes and no evidence. Write down the exact words of any statement a finding may rest on, with the role and the time, so the closing meeting discusses what was said rather than what was remembered.

When the answer is "someone else handles that", note the role and follow it the same day. When nobody can say, the row becomes To confirm with an owner and a due date, as PB-09 section 2 requires; if it is still unconfirmed when you write the report, it is a finding.

## 6. Sampling: how many and which

The minimum sample sizes are set in GOV-PRO-02 step 4.6 and are not negotiable downwards.

| Control frequency | Minimum sample | Typical population |
|---|---|---|
| Annual | 1 | Management review, risk assessment, policy review, supplier annual review |
| Quarterly | 2 | Access reviews per system, restore tests, steering committee minutes |
| Monthly | 3 | Vulnerability scan cycles, metrics reports, change log exports |
| Weekly | 5 | Backup verification, alert review notes |
| Daily or continuous | 25 | Change tickets, access grants, alert triage, leaver removals |
| Any | Whole population | Where the population is smaller than the minimum |

How you choose matters as much as how many. Get the full population first, as a system export covering the audit period, and choose the items yourself: spread them across the period and include the cases most likely to break the control, such as an emergency change, a leaver with privileged access or a Tier 1 supplier. Never accept items the auditee has picked.

Sample from the system of record, not from the register. For access grants that means accounts created in the identity provider, traced back to GOV-TPL-09 forms; for changes it means deployments or tickets, traced to GOV-REG-11; for leavers it means the leaver list from the Head of People, traced to GOV-CHK-01 and to the account disable dates. A difference between the register and the system is itself a finding against the register.

When a sample contains one exception, double the sample. When it contains a second, stop: the control is failing systematically, which is the definition of a major nonconformity in GOV-PRO-02 step 4.7. Record population, selection method, items and exceptions in Notes; GOV-TPL-01 asks for the same facts in the method section.

## 7. Writing a finding in four parts

A finding is four sentences in a fixed order. Anything else is an opinion.

1. **Requirement.** What the criteria require, cited by clause or control number and by the section of your own document that implements it. Quote your own document, never the standard.
2. **Evidence.** What you saw: the files, the counts, the dates, the system, the sample.
3. **Gap.** The difference between the two, in one sentence.
4. **Grade.** Major, minor, observation or opportunity, using GOV-PRO-02 step 4.7.

Three examples:

*Minor.* GOV-PRO-10 section 4 requires a quarterly access review of every Restricted system, recorded in GOV-REG-12. GOV-REG-12 holds two reviews for [System name] in the last four quarters, dated in the first and third quarters, and none for the second or fourth. Two of the four required reviews were not performed. Minor nonconformity.

*Major.* GOV-PRO-12 section 4 requires a restore test for every critical system each quarter, recorded in GOV-REG-15 with the time taken. GOV-REG-15 contains no restore test entries for the audit period; the Head of Engineering stated that backups are monitored but restores have not been attempted since the service was set up. The control is not operating for any critical system. Major nonconformity.

*Observation.* GOV-PRO-01 section 4.5 requires an acknowledgement to name the document version acknowledged. GOV-REG-23 records acknowledgements of GOV-POL-02 but the version column is empty for the twenty entries made before the current version was issued. It cannot be shown which version those staff acknowledged; the current version is being acknowledged correctly. Observation.

Do not write names, solutions or "the team failed to", and do not pad the gap sentence with how serious you think it is; the grade says that.

## 8. Grading well

Grade the control, not the effort of the people running it, and not the ease of the fix. A ten minute fix to a control that has not operated all year is still a major nonconformity. Several minor findings with the same cause are one major, written once with the examples as evidence. An observation is evidence of weakness without a breached requirement; an opportunity for improvement is a better way of doing something that already conforms, and should be rare in a first cycle, because most of what looks like an opportunity is a weakness you have not finished investigating. When the auditee disputes a grade, record the disagreement and refer it to the executive sponsor as GOV-PRO-02 step 4.8 provides.

## 9. The closing meeting

Thirty to forty-five minutes, on the last day of fieldwork, with the auditee and the people who gave the main evidence.

1. Thank the people who took part, and restate the scope and the grading scale.
2. Read every finding aloud in its four parts. For each, ask one question: is the evidence correct. Correct the facts if they are wrong; do not debate the grade.
3. State the positive observations: controls that worked well and the evidence that showed it. They go in the report and are the part the auditee will remember.
4. Record any disagreement in the auditee's own words.
5. State the next steps and dates: the report within ten working days, corrective action responses within ten working days of it (five for a major), re-audit of any major within ninety days.

No finding is raised after the closing meeting. Anything you discover while writing the report goes into the next audit of that area or, if serious, into a short additional audit agreed with the Information Security Manager.

## 10. The report and corrective actions

Write the report on GOV-TPL-01 within ten working days and send it to the auditee, the Information Security Manager and the executive sponsor. Enter the finding counts by grade and the report reference in GOV-REG-02 and set the audit to Reported. End the report with the evidence footer from PB-09 section 10.

The auditee raises one GOV-TPL-02 for each major and minor nonconformity and the Information Security Manager logs them in GOV-REG-03. Three responses arrive in every first cycle and none is a corrective action: "we retrained the person", "we updated the document" and "we reminded everyone". Each is a correction at best. Send them back with the question GOV-PRO-04 asks: why did the process allow this, and what change to the process stops it happening to the next person. The answer is usually a missing trigger, a missing owner or a missing record, and the corrective action is to add it. Observations and opportunities are logged with a decision to act or not act; not acting is acceptable when the reason is written down.

## 11. Follow-up and closing the cycle

Closure needs evidence that the changed process has operated, not a promise that it will: for a quarterly control, at least one review performed under the new process; for a daily control, a sample of items after the change date. Verify it yourself, record the result in GOV-REG-03, and re-audit any major within ninety days of the report. Set an audit to Closed in GOV-REG-02 only when every nonconformity it raised is Verified or Closed.

At the end of the year, reconcile coverage as ISMS-PLN-03 section 4.3 requires: every clause 4.1 to 10.2 and every applicable control in ISMS-REG-01 must appear in the criteria of an audit that was Reported or Closed, and anything missing goes into the first quarter of the next plan. Summarise the cycle for the steering committee each quarter and for the management review under GOV-PRO-03: audits done against plan, findings by grade, open and overdue corrective actions, and the controls that failed most often. Write next year's ISMS-PLN-03 from what you learned, and keep the whole folder for the external auditor: plan, completed checklist, evidence index, report, corrective action forms and closure evidence.

## 12. Ten mistakes first cycles make

1. Auditing documents instead of operation, and reporting a conforming system that has no records.
2. Letting the Information Security Manager audit the management system they run.
3. Accepting samples chosen by the auditee.
4. Writing "seen" in the evidence column.
5. Grading down because the fix is easy, or because the person was helpful.
6. Writing findings as advice rather than as requirement, evidence, gap and grade.
7. Copying the standard's wording into the requirement sentence.
8. Accepting "retrained the person" as a corrective action.
9. Closing a finding on a promise or a document change, with no evidence of operation.
10. Running the whole cycle in the last month before certification, so that nothing can be closed in time.

## 13. Related documents

- GOV-PRO-02 Internal audit procedure
- ISMS-PLN-03 Annual internal audit plan
- ISMS-REG-04 Internal audit checklist
- GOV-REG-02 Audit programme and findings
- GOV-TPL-01 Internal audit report template
- GOV-TPL-02 Corrective action request form
- GOV-REG-03 Corrective action log
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-03 Management review procedure
- ISMS-REG-01 Statement of Applicability
- PB-09 Playbook: evidence management that survives an audit
- GOV-CHK-03 Pre-audit readiness checklist
