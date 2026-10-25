---
id: ISMS-PLN-03
title: Annual internal audit plan
type: plan
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 9.2.1
  - ISO/IEC 27001:2022 clause 9.2.2
  - ISO/IEC 27001:2022 Annex A 5.35
  - SOC 2 CC4.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The schedule of internal audits for one year of the audit cycle, giving for each audit the scope area, the clauses and controls covered, the auditor, the auditee, the timing and the method, together with the coverage rule that proves every clause and every applicable control is audited within the cycle and the statement of auditor independence.
---
## 1. Purpose

This plan turns the audit programme in GOV-PRO-02 into a dated schedule for year [Number] of the [Number]-year cycle. It tells auditees when to expect an audit and what will be examined, tells auditors what they are responsible for, and gives the Chief Executive Officer and the external auditor a single page that shows the whole management system is independently checked.

## 2. Scope and criteria

The plan covers the management system described in ISMS-STM-01. The criteria for every audit are the clause 4 to 10 requirements of ISO/IEC 27001:2022, the Annex A controls declared applicable in ISMS-REG-01, the SOC 2 criteria tagged to those controls in GOV-REG-27 where a SOC 2 report is in scope, and the policies, procedures and registers of [Organisation] as listed in GOV-REG-01. Where ISO/IEC 27701 has been adopted, the privacy extensions audited in each area are those tagged in the Statement of Applicability.

## 3. The cycle and this year's position

The audit cycle is [Number] years, matching the certification cycle. Year 1 of the cycle, and the year before a first certification audit, covers every clause and every applicable control. In later years the clause 4 to 10 requirements are audited every year, controls that meet any of the annual triggers in section 4 are audited every year, and the remaining controls are spread across the cycle so that none goes unaudited for more than [Number] years.

This plan is for year [Number]. The programme in section 6 is written for a year in which everything is covered; when a later year rotates controls, the rows are kept and the clauses and controls column is reduced, with the reconciliation in section 4 proving that nothing falls out of the cycle.

## 4. Coverage rule

4.1 Every clause 4 to 10 requirement is audited every year. Audits IA-01 and IA-10 carry this coverage between them.

4.2 Every control marked Applicable in ISMS-REG-01 is audited at least once within the cycle, and every control that meets one of the following triggers is audited every year: it treats a risk rated High or Critical in GOV-REG-05; a major nonconformity against it is open or was closed within the last twelve months; an incident in GOV-REG-08 involved it within the last twelve months; or the system or process it protects changed significantly during the year.

4.3 At the end of each year the Information Security Manager reconciles the Criteria column of every audit marked Reported or Closed in GOV-REG-02 against the applicable controls in ISMS-REG-01 and against clauses 4.1 to 10.2. Any item not covered is scheduled in the first quarter of the next year's plan. No clause and no applicable control may remain unaudited when the cycle ends.

4.4 A control added to ISMS-REG-01 during the year, or changed from Not applicable to Applicable, is added to the next audit whose scope area fits, and in any case audited within twelve months of the change.

4.5 Coverage is recorded in GOV-REG-02, not in this plan. This plan states the intention; the register proves the outcome.

## 5. Independence statement

5.1 No auditor audits work they performed, managed or designed, or an area where they hold a control owner role in ISMS-REG-02. The Internal Auditor does not report to the Information Security Manager for the purpose of audit work and is not directed by the auditee on what to examine.

5.2 The Information Security Manager owns the management system and therefore does not audit any clause 4 to 10 requirement, nor any control whose owner column in ISMS-REG-02 names that role.

5.3 The Internal Auditor performs or witnesses control tests under ISMS-PRO-04 during the year. Audit IA-10, which examines performance evaluation and improvement, is therefore assigned to a second auditor: a trained person from a department outside the security function, or an external auditor engaged for the purpose.

5.4 Where no independent internal person is available for an area, the Information Security Manager engages an external auditor before the audit's planned quarter and records the arrangement in GOV-REG-02.

5.5 Independence is confirmed in writing for each audit in the Notes column of GOV-REG-02 before fieldwork begins, naming the auditor role and the reason the auditor is independent of the area.

| Role | May not audit |
|---|---|
| Information Security Manager | Any clause 4 to 10 requirement; any control owned by that role; incident management; supplier security; awareness and training |
| Internal Auditor | Controls the Internal Auditor tested under ISMS-PRO-04 in the same year; the internal audit process itself; measurement and reporting under clause 9.1 |
| Head of Engineering and System Owners | Any technological control they operate; change, development and configuration records they approved |
| Privacy Officer | Personal data safeguards and breach handling where the Privacy Officer runs the process |

## 6. Programme by quarter

Each audit is identified as IA-[Year]-[Number]. Timing is given in weeks of the quarter so that the plan can be re-dated each year without rewriting; the agreed dates are entered in GOV-REG-02 when the audit plan is issued. Method follows GOV-PRO-02 step 4.6: document review, interview, observation and sampling of records chosen by the auditor from the full population.

### Quarter 1

| Audit | Scope area | Clauses and controls | Auditor and auditee | Timing and method |
|---|---|---|---|---|
| IA-[Year]-01 | Management system foundations: context, leadership, planning, support, documented information | Clauses 4.1 to 7.5 | Internal Auditor; auditees Information Security Manager and Chief Executive Officer | Weeks 3 to 4; document review of ISMS-STM-01, ISMS-REG-03, GOV-PRO-05, GOV-REG-05, ISMS-REG-01, ISMS-PLN-01 and GOV-REG-01; interviews with top management; sampling of documents against their control blocks |
| IA-[Year]-02 | Governance, policy, legal and compliance controls | Annex A 5.1 to 5.8 and 5.31 to 5.37 | Internal Auditor; auditees Information Security Manager and Privacy Officer | Weeks 7 to 8; document review; sampling of GOV-REG-04 obligations, GOV-REG-23 acknowledgements and project gate records under PB-07; interviews with two line managers |

### Quarter 2

| Audit | Scope area | Clauses and controls | Auditor and auditee | Timing and method |
|---|---|---|---|---|
| IA-[Year]-03 | People security, competence and awareness | Annex A 6.1 to 6.8; clause 7.2 and 7.3 records | Internal Auditor; auditees Head of People and line managers | Weeks 2 to 3; sampling of starters, movers and leavers against GOV-CHK-01 and GOV-REG-09; interviews with staff chosen by the auditor on the day |
| IA-[Year]-04 | Identity, access, privileged access and cryptography | Annex A 5.15 to 5.18, 8.2 to 8.5, 8.18 and 8.24 | Internal Auditor; auditees System Owners and Head of Engineering | Weeks 6 to 7; inspection of identity provider exports and settings; sampling of GOV-TPL-09 requests, GOV-REG-12 reviews, GOV-REG-13 privileged accounts and GOV-REG-18 keys and certificates |
| IA-[Year]-05 | Assets, classification, information transfer and deletion | Annex A 5.9 to 5.14, 7.10, 7.14 and 8.10 to 8.12 | Internal Auditor; auditees Asset owners and Privacy Officer | Weeks 10 to 11; reconciliation of GOV-REG-10 and GOV-REG-24 against the environment; sampling of GOV-REG-20 disposals, GOV-REG-25 interfaces and PIMS-REG-07 retention checks; observation of labelling |

### Quarter 3

| Audit | Scope area | Clauses and controls | Auditor and auditee | Timing and method |
|---|---|---|---|---|
| IA-[Year]-06 | Suppliers, cloud services and outsourced development | Annex A 5.19 to 5.23, 8.21 and 8.30 | Internal Auditor; auditees Head of Operations and Head of Engineering | Weeks 2 to 3; sampling of GOV-REG-07 by tier; review of contracts and assurance reports under SOC-PRO-02; inspection of the must-prove evidence for one cloud service under GOV-PRO-26 |
| IA-[Year]-07 | Technology operations: endpoints, configuration, malware, vulnerabilities, logging, backup, capacity and network | Annex A 8.1, 8.6 to 8.9, 8.13 to 8.17, 8.19, 8.20, 8.22 and 8.23 | Internal Auditor; auditees Head of Engineering and System Owners | Weeks 6 to 8; technical inspection against GOV-CHK-02; sampling of GOV-REG-14 findings past due, GOV-REG-15 restore tests, GOV-REG-17 capacity records, log retention settings and firewall rule reviews |
| IA-[Year]-08 | Secure development, change management and test protection | Annex A 5.8, 8.25 to 8.29 and 8.31 to 8.34 | Internal Auditor; auditee Head of Engineering | Weeks 10 to 11; sampling of releases and GOV-REG-11 changes including emergency changes; inspection of pipelines, environment separation and test data; review of security test results |

### Quarter 4

| Audit | Scope area | Clauses and controls | Auditor and auditee | Timing and method |
|---|---|---|---|---|
| IA-[Year]-09 | Incident management, continuity and physical security | Annex A 5.24 to 5.30, 7.1 to 7.9 and 7.11 to 7.13 | Internal Auditor; auditees Head of Operations, Incident Lead and Facilities Manager | Weeks 2 to 3; sampling of GOV-REG-08 incidents with their GOV-TPL-05 and GOV-TPL-11 records; review of GOV-TPL-07 and GOV-REG-16 exercises; walk-through of one site against GOV-PRO-17 |
| IA-[Year]-10 | Operation, performance evaluation, improvement, and verification of every finding open from IA-01 to IA-09 | Clauses 8.1 to 10.2; Annex A 5.35 and 5.36 | Second auditor independent of the Internal Auditor (section 5.3); auditees Information Security Manager and Internal Auditor | Weeks 6 to 7, completed before the management review; document review; re-performance of two measures from ISMS-PRO-04; verification of closure evidence in GOV-REG-03 |

### Coverage check for this plan

| Group | Controls | Audits |
|---|---|---|
| Organisational 5.1 to 5.37 | 37 | IA-02 (5.1 to 5.8, 5.31 to 5.37); IA-05 (5.9 to 5.14); IA-04 (5.15 to 5.18); IA-06 (5.19 to 5.23); IA-09 (5.24 to 5.30); IA-10 (5.35 and 5.36 again) |
| People 6.1 to 6.8 | 8 | IA-03 |
| Physical 7.1 to 7.14 | 14 | IA-09 (7.1 to 7.9, 7.11 to 7.13); IA-05 (7.10, 7.14) |
| Technological 8.1 to 8.34 | 34 | IA-07 (8.1, 8.6 to 8.9, 8.13 to 8.17, 8.19, 8.20, 8.22, 8.23); IA-04 (8.2 to 8.5, 8.18, 8.24); IA-05 (8.10 to 8.12); IA-06 (8.21, 8.30); IA-08 (8.25 to 8.29, 8.31 to 8.34) |
| Clauses 4.1 to 10.2 | all | IA-01 (4.1 to 7.5); IA-10 (8.1 to 10.2) |

## 7. Timetable for each audit

| Point | What happens | Source |
|---|---|---|
| Ten working days before fieldwork | The auditor issues the audit plan with scope, criteria, interviewees, records required and the ISMS-REG-04 rows in play | GOV-PRO-02 step 4.4 |
| Three working days after the plan | The auditee confirms availability and names deputies | GOV-PRO-02 step 4.4 |
| Day one | Opening meeting, then fieldwork of one to three days depending on the scope area | GOV-PRO-02 step 4.5 |
| Last day of fieldwork | Closing meeting; every finding presented in four parts and the facts confirmed | GOV-PRO-02 step 4.8 |
| Ten working days after the closing meeting | Report on GOV-TPL-01 issued; counts entered in GOV-REG-02 | GOV-PRO-02 step 4.9 |
| Ten working days after the report, five for a major nonconformity | Auditee returns GOV-TPL-02 with root cause and plan; logged in GOV-REG-03 | GOV-PRO-02 step 4.10 |
| Within ninety days of the report | Major nonconformities re-audited | GOV-PRO-02 step 4.11 |

## 8. Resources

The programme needs about [Number] auditor days for the year: two days of preparation and fieldwork and one day of reporting for each audit, plus [Number] days for follow-up. Auditees should expect to give two to four hours per audit for interviews and evidence. The Internal Auditor must meet the competence requirements in GOV-PRO-02 step 4.3 before leading an audit; where the second auditor for IA-10 is external, the engagement is approved by the Chief Executive Officer in the first quarter so that availability is secured.

## 9. Changes to the plan

An audit may be moved within its quarter by agreement between the auditor and the auditee, recorded in GOV-REG-02. Moving an audit to a later quarter needs the written approval of the Chief Executive Officer under GOV-PRO-02 section 6, and no audit may be moved out of the year. A new system, supplier, site or incident of severity 1 or 2 during the year triggers a review of whether an additional audit is needed; the Information Security Manager proposes it to the steering committee within one month of the trigger.

## 10. Records and evidence

- GOV-REG-02 Audit programme and findings: one row per audit in this plan, with dates, independence note, status and finding counts.
- The audit plan issued for each audit and the completed ISMS-REG-04 checklist.
- Audit reports on GOV-TPL-01 and the corrective actions in GOV-REG-03.
- The year-end coverage reconciliation described in section 4.3, filed with the plan for the following year.

## 11. Review and maintenance

The Information Security Manager drafts the plan for the following year in the last quarter, using the coverage reconciliation, the risk register, the incident register and the findings of the current year to set which controls need annual attention. The Chief Executive Officer approves it before the year begins. The plan is also reviewed when the scope changes, when a framework is added or withdrawn, and after any external audit finding about internal audit.

## 12. Related documents

- GOV-PRO-02 Internal audit procedure
- GOV-REG-02 Audit programme and findings
- ISMS-REG-04 Internal audit checklist
- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- GOV-TPL-01 Internal audit report template
- GOV-TPL-02 Corrective action request form
- GOV-REG-03 Corrective action log
- GOV-PRO-03 Management review procedure
- GOV-REG-27 Framework crosswalk
- PB-06 Playbook: running your first internal audit cycle
