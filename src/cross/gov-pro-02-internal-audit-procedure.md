---
id: GOV-PRO-02
title: Internal audit procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 9.2.1
  - ISO/IEC 27001:2022 clause 9.2.2
  - SOC 2 CC4.1
  - SOC 2 CC4.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] plans, performs, reports and follows up internal audits of the management system so that every requirement and every applicable control is independently checked within the audit cycle.
---
## 1. Purpose

This procedure produces independent, evidence-based information about whether the management system conforms to the organisation's own documents and to the frameworks it has adopted, and whether it is effectively implemented and maintained.

## 2. Scope

It covers every internal audit of the management system: the clause 4 to 10 requirements of ISO/IEC 27001:2022, the applicable Annex A controls in ISMS-REG-01, the ISO/IEC 27701 extensions where adopted, and the SOC 2 criteria in scope. Supplier audits follow GOV-PRO-06. External certification audits are outside this procedure but are prepared for with GOV-CHK-03.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Executive sponsor | Approves the audit programme and the annual plan, receives every report, decides on disputed gradings. |
| Information Security Manager | Maintains the programme in GOV-REG-02, schedules audits, tracks corrective actions. May not audit areas they operate. |
| Internal Auditor | Plans and performs the audit, grades findings, writes the report, verifies closure. |
| Auditee (the manager of the area audited) | Provides access, people and evidence, responds to findings, owns corrective actions. |
| Steering committee | Reviews audit results quarterly and trends annually. |

## 4. Procedure

4.1 **Programme.** The Information Security Manager proposes, and the executive sponsor approves, an audit programme covering a cycle of [Number] years (three years is recommended, matching a certification cycle). The programme schedules audits so that every clause 4 to 10 requirement, every control declared applicable in ISMS-REG-01 and every SOC 2 criterion in scope is audited at least once per cycle. Areas with High or Critical risks in GOV-REG-05, open major nonconformities, recent incidents or significant change are audited at least annually. The programme is recorded in GOV-REG-02 and detailed each year in ISMS-PLN-03.

4.2 **Independence.** An auditor never audits work they performed, managed or designed. Where the organisation cannot find an independent internal auditor for an area, the Information Security Manager engages a competent person from another department or an external auditor. Independence is recorded for each audit in GOV-REG-02.

4.3 **Competence.** Before leading an audit alone, an auditor has completed training in audit technique, can explain the requirements being audited, and has taken part in at least [Number] audits under an experienced lead. The competence record is held under ISMS-PRO-02. The Internal Auditor keeps their knowledge current through at least one refresher activity a year.

4.4 **Planning.** At least ten working days before fieldwork, the Internal Auditor issues an audit plan to the auditee stating the scope, the criteria (documents, clauses, controls), the dates, the people to be interviewed, the records to be made available, and the checklist questions drawn from ISMS-REG-04. The auditee confirms availability within three working days.

4.5 **Opening meeting.** The Internal Auditor opens the audit with the auditee, confirms scope and timing, explains the grading scale in 4.7, and agrees how evidence will be shared and how confidential material will be handled.

4.6 **Evidence gathering.** The Internal Auditor collects evidence by document review, interview, observation and sampling of records, and records the source of every piece of evidence. Samples are chosen by the auditor, not the auditee, from the full population for the period under review. The minimum sample is one item for a control operating annually, two for quarterly, three for monthly, five for weekly, and twenty-five for daily or continuous controls, or the whole population where it is smaller. Evidence must show the account, system, date and person involved. A statement without evidence is recorded as unverified, not as conforming.

4.7 **Grading.** Each finding receives one grade.

| Grade | Meaning |
|---|---|
| Major nonconformity | A requirement is not implemented, a control has failed systematically, or several minor findings show the same cause. |
| Minor nonconformity | A single lapse against a requirement that does not undermine the control as a whole. |
| Observation | Evidence of a weakness that could become a nonconformity if not addressed. |
| Opportunity for improvement | A way to make a conforming process more effective or efficient. |

A nonconformity is written in four parts: the requirement, the evidence seen, the gap between them, and the grade.

4.8 **Closing meeting.** The Internal Auditor presents every finding to the auditee before leaving, confirms the facts, and records any disagreement. A disputed grading is referred to the executive sponsor, whose decision is final.

4.9 **Report.** The Internal Auditor issues the report using GOV-TPL-01 within ten working days of the closing meeting to the auditee, the Information Security Manager and the executive sponsor, and records the finding counts by grade and the report reference in GOV-REG-02.

4.10 **Corrective action.** The auditee raises a corrective action request using GOV-TPL-02 for every major and minor nonconformity, and the Information Security Manager logs it in GOV-REG-03. The auditee proposes a root cause and a plan within ten working days of the report, or within five working days for a major nonconformity. Observations and opportunities are logged with a decision to act or not act. GOV-PRO-04 governs the rest of the process.

4.11 **Follow-up.** The Internal Auditor verifies the closure evidence for each nonconformity and records the result. A major nonconformity is re-audited within ninety days of the report. An audit is marked Closed in GOV-REG-02 only when every nonconformity it raised is Verified or Closed in GOV-REG-03.

4.12 **Reporting to management.** The Information Security Manager summarises audit results, open findings and overdue actions for the steering committee each quarter and for management review under GOV-PRO-03.

## 5. Records and evidence

- GOV-REG-02 Audit programme and findings: the programme, each audit's status and finding counts.
- ISMS-PLN-03 Annual internal audit plan.
- Audit plans, completed ISMS-REG-04 checklists and evidence files for each audit.
- Audit reports on GOV-TPL-01.
- GOV-REG-03 Corrective action log and the GOV-TPL-02 forms behind it.
- Auditor competence records under ISMS-PRO-02.

## 6. Exceptions

An audit may be postponed by up to one quarter with the written approval of the executive sponsor, recorded in GOV-REG-02 with the reason. No requirement or applicable control may be left unaudited across a full cycle.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any external audit finding about internal audit, and when the scope or the adopted frameworks change. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-02 Audit programme and findings
- GOV-TPL-01 Internal audit report template
- GOV-TPL-02 Corrective action request form
- GOV-REG-03 Corrective action log
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-03 Management review procedure
- GOV-CHK-03 Pre-audit readiness checklist
- ISMS-PLN-03 Annual internal audit plan
- ISMS-REG-04 Internal audit checklist
- ISMS-PRO-02 Competence and awareness procedure
- PB-06 Playbook: running your first internal audit cycle
