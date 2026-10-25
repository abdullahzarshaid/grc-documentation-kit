---
id: SOC-GDE-02
title: "Guide: the auditor's request list and how to answer it from the kit"
type: guide
framework: soc2
maps:
  - SOC 2 CC4.1
  - SOC 2 CC2.1
  - SOC 2 CC6.1
  - SOC 2 CC7.2
  - SOC 2 CC8.1
  - SOC 2 CC9.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The evidence requests a SOC 2 auditor typically issues, grouped by the team that produces each one, with the kit register or document that holds the answer and the form the answer should take.
---
## 1. How the request list works

A few weeks before fieldwork the auditor sends a request list: one line per item of evidence, each tied to one or more controls in SOC-REG-01, with a due date. The list is long, the dates are short, and the items land on five or six different teams. Organisations that struggle are not short of controls; they are short of a person who knows which team holds each answer and what form it should take.

This guide groups the typical requests by the owner who produces them. For each request it names the criteria, the kit register or document that holds the answer, and how to deliver it. Read it with PB-09, which sets the evidence rules that apply to every item: dated system exports over screenshots, complete populations over examples, file names that say what the file proves, and a To confirm status for anything not yet seen.

Four rules apply to every request.

1. Deliver populations, not examples. The auditor samples; [Organisation] supplies the whole list with identifiers and dates and lets the auditor choose.
2. Deliver evidence from inside the period. A record dated after the period end proves nothing about the period, however good it is.
3. Deliver the system of record's own export. A spreadsheet typed from memory is not evidence of anything except memory.
4. Deliver through one channel, with one person tracking status per item. The Information Security Manager owns the list; the teams below own the items.

## 2. People team

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| List of all employees and contractors at period start, joiners and leavers during the period, with dates | CC1.4, CC6.2, CC6.3 | People system; GOV-CHK-01 | Export with start and end dates; this is the population for onboarding and offboarding samples |
| Evidence of background screening for sampled joiners | CC1.1, CC1.4 | GOV-PRO-18; GOV-REG-23 | Screening completion record per sampled person, dated before start |
| Signed terms with confidentiality and security obligations for sampled joiners | CC1.1, CC1.5 | GOV-PRO-18 | Signed agreement or acknowledgement record naming the version |
| Code of conduct or acceptable use acknowledgement for all staff | CC1.1, CC2.2 | GOV-POL-02; GOV-REG-23 | Export of acknowledgements with policy version and date |
| Security awareness training completion for all staff in the period | CC1.4, CC2.2 | GOV-PRO-08; GOV-REG-09 | Completion export with names and dates; new starters within the induction window |
| Role-based training for developers and administrators | CC1.4 | GOV-PRO-08; GOV-REG-09; GOV-TPL-10 | Session records and attendance |
| Performance review or accountability evidence for control owners | CC1.5 | GOV-POL-01; GOV-PRO-18 | Role descriptions with control responsibilities; review completion export |
| Organisation chart and role descriptions for security roles | CC1.3 | GOV-POL-01 | Current chart dated inside the period |
| Offboarding checklist for sampled leavers | CC6.2, CC6.3 | GOV-CHK-01 | Completed checklist per leaver with dates |
| Disciplinary process and any cases in the period | CC1.1, CC1.5 | GOV-PRO-18 | Procedure plus a count of cases; details only if the auditor asks |

## 3. Engineering

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| List of all production changes in the period | CC8.1 | GOV-REG-11; deployment log | Export of change tickets and of deployments, reconciled to each other |
| For sampled changes: request, approval, test evidence, deployment record, post-implementation review | CC8.1 | GOV-PRO-09; GOV-TPL-08 | Ticket export plus pipeline records per sampled change |
| Emergency changes in the period with retrospective approval | CC8.1 | GOV-PRO-09; GOV-REG-11 | Filtered export with approver and date |
| Secure development lifecycle: peer review, static and dependency analysis, secrets scanning | CC8.1, CC7.1 | GOV-PRO-15 | Repository settings export showing review required; scan results for sampled changes |
| Separation of development, test and production, and who can deploy | CC8.1, CC6.3 | GOV-PRO-15; GOV-PRO-10 | Environment list; export of deployment permissions |
| Infrastructure as code or configuration baseline and drift checks | CC5.2, CC7.1 | GOV-CHK-02 | Baseline document plus drift report for the period |
| Processing specifications for in-scope services | PI1.1 | SOC-POL-01; SOC-TPL-01 | Approved specification with version history |
| Input validation rules and quarantine records | PI1.2 | SOC-PRO-03 | Catalogue extract; quarantine export for the period |
| Daily reconciliation records | PI1.3 | SOC-PRO-03 | Export of reconciliations with preparer and reviewer; this is a daily population |
| Output completeness, accuracy and delivery records | PI1.4 | SOC-PRO-04 | Job monitor export; delivery logs; sample verification records |
| Storage integrity verification and reissue records | PI1.5 | SOC-PRO-04 | Verification results; processing error log |
| Open source licence check for the period | CC2.3 | GOV-PRO-15 | Licence scan output |

## 4. IT and operations

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| List of in-scope systems and their owners | CC6.1, CC5.2 | GOV-REG-10; GOV-REG-24 | Asset register export; must match SOC-TPL-01 section 4 |
| User lists for every in-scope system at period start and end | CC6.1, CC6.2, CC6.3 | GOV-PRO-10 | Export per system with role and last sign-in |
| Access requests and approvals for sampled new accounts | CC6.2 | GOV-TPL-09; ticketing | Approved request per sampled account, dated before provisioning |
| Removal of access for sampled leavers within the policy window | CC6.2, CC6.3 | GOV-PRO-10; GOV-CHK-01 | Identity provider disable event with timestamp per leaver |
| Quarterly access reviews for the period | CC6.2, CC6.3 | GOV-REG-12 | Review export per quarter with reviewer, decisions and removals actioned |
| Privileged account inventory and multi-factor status | CC6.1, CC6.3 | GOV-REG-13; GOV-POL-06 | Export; configuration export of the multi-factor policy |
| Authentication configuration: password rules, lockout, session timeout | CC6.1 | GOV-POL-06 | Configuration export per system with date |
| Encryption in transit and at rest settings | CC6.1, CC6.7 | GOV-PRO-20; GOV-REG-18 | Configuration exports; certificate inventory |
| Network and firewall rules, remote access configuration | CC6.6 | GOV-PRO-21 | Rule export with last review date |
| Endpoint management: encryption, malware protection, update status | CC6.8, CC7.1 | GOV-PRO-22; GOV-CHK-02 | Device compliance export covering all devices |
| Vulnerability scans for the period and remediation within SLA | CC7.1 | GOV-PRO-11; GOV-REG-14 | Scan exports per cycle; register showing found, due and fixed dates |
| Penetration test report and remediation tracking | CC7.1, CC4.1 | GOV-PRO-11; GOV-REG-14 | Report summary; register rows for findings |
| Logging configuration, retention and clock synchronisation | CC7.2 | GOV-PRO-14 | Configuration exports; a query result for a known event |
| Alerts raised and triaged in the period | CC7.2, CC7.3 | GOV-PRO-14 | Alert export with triage outcome; population for sampling |
| Backup job history and restore tests | A1.2, A1.3 | GOV-PRO-12; GOV-REG-15 | Job history export for the period; restore test records per quarter |
| Capacity and availability monitoring and uptime for the period | A1.1 | GOV-PRO-19; GOV-REG-17 | Monitoring export; uptime figures against the commitment |
| Continuity plan and exercise results | A1.3, CC9.1 | GOV-PRO-13; GOV-REG-16 | Plan version; exercise record with lessons and actions |
| Physical access records and visitor logs for premises | CC6.4 | GOV-PRO-17; GOV-REG-19 | Access list export; visitor log for the period |
| Media and equipment disposal records | CC6.5, C1.2 | GOV-REG-20 | Disposal log with certificates where a third party destroyed media |
| Data deletion at contract end for sampled customers | C1.2, P4.3 | PIMS-POL-02; PIMS-REG-07 | Deletion record per sampled customer with date and method |

## 5. Policy owner (Information Security Manager)

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| All policies and procedures in force during the period with approval dates | CC5.3, CC2.2 | GOV-REG-01; GOV-PRO-01 | Master list export; approved versions |
| Evidence of annual policy review | CC5.3 | GOV-REG-01 | Review records, including no-change reviews |
| System description and management's assertion | CC2.3 | SOC-TPL-01 | Approved current version |
| Control matrix | CC5.1 | SOC-REG-01 | Current version with owner, frequency and evidence per control |
| Internal control testing results for the period | CC4.1, CC4.2 | SOC-PRO-01 | Workpapers and the quarterly summaries |
| Internal audit plan, reports and corrective actions | CC4.1, CC4.2 | GOV-PRO-02; GOV-REG-02; GOV-TPL-01 | Plan; reports; GOV-REG-03 export |
| Steering committee minutes for the period | CC1.2, CC2.2 | GOV-POL-01 | Minutes per meeting with attendance and decisions |
| Management review minutes | CC1.2, CC4.1 | GOV-PRO-03; GOV-TPL-03; GOV-REG-22 | Minutes and action tracker |
| Security objectives and measures reporting | CC3.1, CC2.1 | GOV-REG-21; ISMS-PRO-04 | Register export with values per period |
| Incident register and sampled incident records | CC7.3, CC7.4, CC7.5 | GOV-REG-08; GOV-TPL-05; GOV-TPL-11 | Register export; report and post-incident review per sampled incident |
| Communication to customers of commitments, changes and incidents | CC2.3 | ISMS-PLN-02 | Examples of each channel used in the period |
| Vulnerability disclosure channel and reports received | CC2.3, CC7.1 | GOV-PRO-27 | Channel description; log of reports and responses |
| Legal and contractual obligations register | CC2.3, CC1.1 | GOV-REG-04 | Register export with review dates |
| Exceptions and risk acceptances in force | CC5.1, CC3.2 | GOV-REG-06; GOV-TPL-06 | Register export; approvals for sampled items |
| Confidential information inventory and classification handling | C1.1 | GOV-PRO-16; GOV-REG-10 | Register export with classification |

## 6. Risk owner

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| Risk assessment methodology | CC3.1, CC3.2 | GOV-PRO-05 | Approved version |
| Risk register at period start and end | CC3.2, CC3.3, CC3.4 | GOV-REG-05 | Dated exports showing scores, treatment and owners |
| Evidence that fraud risk was considered | CC3.3 | GOV-PRO-05; GOV-REG-05 | Fraud scenarios in the register; segregation of duties mapping |
| Evidence that changes were assessed for risk impact | CC3.4 | GOV-PRO-05; ISMS-PRO-01 | Risk review records triggered by changes in the period |
| Treatment plans and their completion | CC5.1 | GOV-REG-05; GOV-REG-03 | Export with due and completed dates |
| Business impact analysis and continuity risk | CC9.1 | GOV-TPL-07; GOV-PRO-13 | Completed worksheet; continuity strategy |
| Supplier register with tiers and assurance status | CC9.2 | GOV-REG-07 | Export with last and next review dates |
| Due diligence for sampled suppliers | CC9.2 | GOV-PRO-06; GOV-TPL-04 | Questionnaire or report review per sampled supplier |
| Subservice organisation SOC reports, reviews and bridge letters | CC9.2 | SOC-PRO-02 | Review record per subservice organisation with user entity control mapping |
| Contracts with security and processor terms for sampled suppliers | CC9.2 | GOV-PRO-06; PIMS-TPL-02 | Clause extract per sampled supplier |

## 7. Privacy Officer (when the Privacy category or personal data is in scope)

| Request | Criteria | Kit source | Deliver as |
|---|---|---|---|
| Privacy notices in force during the period | P1.1 | PIMS-PRO-05; GDPR-TPL-01 | Published versions with dates |
| Consent records and withdrawal handling | P2.1, P3.2 | PIMS-REG-04; GDPR-TPL-06 | Register export; sampled records |
| Processing inventory | P3.1, P4.1, P6.2 | PIMS-REG-01 | Export with purposes, bases and recipients |
| Retention schedule and deletion evidence | P4.2, P4.3 | PIMS-REG-07; PIMS-POL-02 | Schedule; deletion records for sampled categories |
| Data subject requests and response times | P5.1, P5.2, P6.7 | PIMS-REG-02; PIMS-PRO-03 | Register export; sampled request files |
| Third party disclosures and processor agreements | P6.1, P6.4, P6.5 | PIMS-REG-06; PIMS-TPL-02 | Register export; agreement per sampled processor |
| Personal data breach register and notifications | P6.3, P6.6 | PIMS-REG-03; PIMS-PRO-04 | Register export; notification records |
| Accuracy controls and complaint handling | P7.1, P8.1 | PIMS-PRO-03; PIMS-PRO-07 | Procedure; complaints log for the period |

## 8. Requests that catch organisations out

- The population reconciliation. The auditor compares the people system's leavers to the identity provider's disabled accounts, and change tickets to deployments. Reconcile both yourself before fieldwork and have an explanation for every difference.
- The quarter with no access review. A review done in month four and month nine is two reviews, not four. SOC-REG-02 exists so that this is seen in month five, not at the audit.
- The policy acknowledged before it was approved. Acknowledgement exports must name the version, and the version's approval date must precede the acknowledgement.
- The restore test that restored nothing. A backup job success export is not a restore test. GOV-REG-15 needs a restored item, a verification and a date.
- The vendor report nobody read. Having a subservice organisation's SOC report on file is not CC9.2 evidence; the SOC-PRO-02 review record is.
- The incident with no post-incident review. GOV-TPL-11 within the window in GOV-PRO-07, or the control did not operate for that incident.
- The screenshot with no date or account. Retake it as PB-09 section 5 describes.
- The control owner who is also the tester. SOC-PRO-01 section 4 requires independence; the auditor will ask who performed each internal test.

## 9. Preparing in advance

Everything in sections 2 to 7 can be produced on the day the control runs, which is what SOC-REG-02 schedules. An organisation that files the quarterly access review export on the day the review closes, the monthly vulnerability scan on the day it completes, and the change ticket export at month end, answers the request list in a week. An organisation that starts collecting when the list arrives answers it in two months and loses items to section 8. Use SOC-REG-03 to check readiness before the period starts, and keep the owner column of SOC-REG-01 current so that every request has a name on it before the auditor asks.
