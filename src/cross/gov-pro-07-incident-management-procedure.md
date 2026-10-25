---
id: GOV-PRO-07
title: Information Security Incident Management Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.24
  - ISO/IEC 27001:2022 Annex A 5.25
  - ISO/IEC 27001:2022 Annex A 5.26
  - ISO/IEC 27001:2022 Annex A 5.27
  - ISO/IEC 27001:2022 Annex A 5.28
  - ISO/IEC 27001:2022 Annex A 6.8
  - SOC 2 CC7.3
  - SOC 2 CC7.4
  - SOC 2 CC7.5
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How security events are reported, triaged, graded, contained, investigated, recovered from, communicated and reviewed, and when a personal data breach process is started alongside.
---
## 1. Purpose

This procedure gets every security event reported quickly, graded consistently and handled by named roles, so that harm is limited, evidence survives, notification duties are met on time and each incident makes the next one less likely.

## 2. Scope

It covers every event and incident affecting the confidentiality, integrity or availability of [Organisation]'s information, systems, services or people, wherever it occurs, including suspected incidents, near misses and incidents reported by clients or suppliers. Where personal data is involved PIMS-PRO-04 runs alongside this procedure. Where an AI system is involved AI-PRO-03 applies in addition.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| All staff and contractors | Report events within one hour of noticing, preserve what they see, do not investigate or discuss outside the response team. |
| First responder [Role] | Logs the report in GOV-REG-08, triages within one hour, escalates to the Incident Lead. |
| Incident Lead | The Information Security Manager or a named delegate. Declares the incident, sets severity, directs the response, keeps the record, decides closure, chairs the review. |
| Technical lead | Contains, collects evidence, eradicates and recovers, with system owners. |
| Communications lead | Drafts internal updates and external statements and holds the single approved version. |
| Privacy Officer and legal adviser | Decide regulatory, contractual and data subject notifications, set evidence preservation requirements, liaise with authorities. |
| Executive sponsor | The Chief Executive Officer or delegate. Approves external communication and decisions that stop a service or involve law enforcement. |

## 4. Procedure

4.1 **Reporting.** Staff report through [Channel], published in GOV-POL-02 and at induction, within one hour of noticing an event. External parties use the contact published under GOV-PRO-27. Suppliers report within their contracted time. The first responder records every report in GOV-REG-08 with a reference in the form [Prefix]-[Year]-[Number], the reporter, the times detected and reported, and the affected assets.

4.2 **Triage.** Within one hour the Incident Lead decides whether the report is a false positive (closed with the reason recorded), an event to monitor, or an incident. For an incident the Incident Lead assigns a severity from the matrix, opens a GOV-TPL-05 report and names the response team.

4.3 **Severity matrix.** Severity is raised as soon as the facts suggest it and lowered only on evidence.

| Severity | Definition | Examples | Response targets |
|---|---|---|---|
| 1 Critical | Confirmed compromise, loss or outage affecting Restricted information or a client-facing production service, a likely regulatory notification, or an attacker still active | Ransomware on production, exfiltration of client data, compromised privileged account | Lead engaged within 15 minutes, executive sponsor informed within one hour, updates every two hours |
| 2 High | Confirmed incident affecting Confidential information or one internal service, limited to few systems or individuals | Standard account takeover, malware on one endpoint, personal data sent to the wrong recipient | Lead within one hour, sponsor informed within four hours, daily updates |
| 3 Medium | Confirmed incident with limited impact and no exposure of personal or confidential information outside [Organisation] | Lost encrypted laptop, phishing click with no credentials entered, policy breach without exposure | Lead within four hours, working hours response, closed within ten working days |
| 4 Low | Event that did not become an incident, or a near miss | Blocked phishing campaign, vulnerability found before exploitation | Recorded and trended monthly |

4.4 **Personal data breach trigger.** When an incident involves personal data, through loss, destruction, alteration, unauthorised disclosure or unauthorised access, the Incident Lead informs the Privacy Officer immediately and records the time [Organisation] became aware. PIMS-PRO-04 starts at that time, including the 72 hour assessment clock and, where [Organisation] is a processor, notification to the controller without undue delay.

4.5 **Containment.** The technical lead disables accounts, revokes sessions and tokens, blocks indicators and isolates hosts, keeping them powered where memory evidence is needed. Credentials that may have been exposed are rotated. Actions that affect client service need the Incident Lead's approval. Emergency changes are recorded under GOV-PRO-09 within one working day.

4.6 **Evidence preservation.** Before any action that would alter evidence, the technical lead copies the relevant logs under GOV-PRO-14, images affected systems for Severity 1 and Severity 2, records a hash value for every collected file, keeps a chain of custody record (who, what, when, where stored) and stores everything in a restricted evidence location. Screenshots show the account, system and time. Evidence is retained until closure plus the retention period, or longer under legal hold.

4.7 **Investigation and eradication.** The technical lead establishes the entry point, the timeline, the accounts and data affected and the extent of spread, then removes the cause: malware, the unauthorised access path, or the vulnerable component, patched under GOV-PRO-11 or reconfigured. Persistence is checked before recovery: new accounts, keys, scheduled tasks, mail rules and changed permissions.

4.8 **Recovery.** Systems are restored from clean backups under GOV-PRO-12 or rebuilt, verified before return to service, and monitored more closely for [Number] days. The system owner confirms return to normal service. Where recovery exceeds the recovery time objective, GOV-PRO-13 is invoked.

4.9 **Communication.** The Incident Lead issues internal updates at the severity cadence on a need to know basis. No statement goes to clients, regulators, data subjects, media, insurers, law enforcement or suppliers without the executive sponsor's approval and review by the Privacy Officer and legal adviser. Regulatory and data subject notifications follow PIMS-PRO-04 and GDPR-TPL-10; contractual notifications follow the timelines recorded in GOV-REG-04. Every notification is logged in GOV-TPL-05 with time, recipient and content.

4.10 **Closure.** The Incident Lead closes the incident when the cause is removed, service is recovered, notifications are complete, evidence is stored, GOV-TPL-05 is complete and GOV-REG-08 holds the containment and resolution times, root cause and lessons.

4.11 **Post-incident review.** For every Severity 1 and Severity 2 incident, and any Severity 3 incident the Incident Lead selects, the Incident Lead holds a review within ten working days of closure using GOV-TPL-11. Actions are raised in GOV-REG-03 under GOV-PRO-04, GOV-REG-05 is updated, control changes go through GOV-PRO-09, and human factor findings feed GOV-PRO-08.

4.12 **Metrics.** The Information Security Manager reports monthly: events and incidents by type and severity, time to detect, report, contain and recover, the share of reviews held within ten working days, and overdue actions. The quarterly trend goes to management review under GOV-PRO-03 and to GOV-REG-21.

4.13 **Exercise.** The Incident Lead runs a tabletop exercise at least annually on a Severity 1 scenario that includes a personal data breach, records it in GOV-REG-16 and raises findings in GOV-REG-03.

## 5. Records and evidence

- GOV-REG-08 Incident register: every event and incident with times, severity, breach flag, root cause and status.
- GOV-TPL-05 Incident report form per incident, with timeline and notification log.
- GOV-TPL-11 Post-incident review per Severity 1 and Severity 2 incident.
- Evidence files with hash values and chain of custody records.
- PIMS-REG-03 for personal data breaches, GOV-REG-16 for exercises, GOV-REG-03 for actions.

## 6. Exceptions

There is no exception to reporting. Where a Severity 1 incident makes the normal approval route unavailable, the Incident Lead acts and records the approvals obtained afterwards within one working day.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after every Severity 1 incident, after each exercise, after an audit finding and after a change in notification law or client contract terms. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-05 Incident report form
- GOV-TPL-11 Post-incident review template
- GOV-REG-08 Incident register
- PIMS-PRO-04 Personal data breach assessment and notification procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-06 Supplier and third party security procedure
- AI-PRO-03 AI incident and model failure handling procedure
