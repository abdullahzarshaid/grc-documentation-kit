---
id: GOV-TPL-05
title: Incident Report Form
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.24
  - ISO/IEC 27001:2022 Annex A 5.26
  - ISO/IEC 27001:2022 Annex A 5.28
  - SOC 2 CC7.3
  - SOC 2 CC7.4
owner: Information Security Manager
approver: Chief Executive Officer
classification: Confidential
review: Annual
summary: The single record kept for each incident from first report to closure, holding its facts, classification, actions, timeline, notifications and evidence under GOV-PRO-07.
---
## 1. How to use this form

*The first responder opens this form when the Incident Lead declares an incident under GOV-PRO-07 step 4.2, using the reference already assigned in GOV-REG-08. The Incident Lead keeps it current throughout the response. Write facts and times, not opinions; record the source of every fact in the timeline. Times use one time zone, stated once in section 2. Keep the completed form in the restricted evidence location, not in email.*

## 2. Incident identification

| Field | Entry |
|---|---|
| Incident reference | [Prefix]-[Year]-[Number] |
| Current status | Open / Contained / Resolved / Under review / Closed |
| Incident Lead | [Role] |
| Reported by | [Role or external party] |
| Reporter contact | [Contact] |
| How detected | Staff report / Monitoring alert / Supplier notice / Client report / Audit / Other |
| Date and time detected | [Date] [Time] |
| Date and time reported | [Date] [Time] |
| Date and time incident declared | [Date] [Time] |
| Time zone used in this form | [Time zone] |

## 3. Description

*Three to ten sentences: what happened, how it was discovered, what is known and what is not yet known. Update the "current state" line as the response progresses.*

| Field | Entry |
|---|---|
| What happened | |
| How it was discovered | |
| Current state | |
| Suspected cause | |

## 4. Affected assets and information

| Asset or system | Owner | Classification | Information types involved | Approximate records or individuals |
|---|---|---|---|---|
| [System name] | [Role] | Public / Internal / Confidential / Restricted | | [Number] |
| | | | | |
| | | | | |

## 5. Classification

| Field | Entry |
|---|---|
| Incident type | Malware / Phishing or social engineering / Unauthorised access / Data exposure / Lost or stolen device / Denial of service / Misconfiguration / Supplier incident / Insider misuse / Physical / Other |
| Severity (GOV-PRO-07 step 4.3) | 1 Critical / 2 High / 3 Medium / 4 Low |
| Severity changes | *Record each change with time and reason.* |
| Personal data involved | Yes / No / Under assessment |
| Privacy Officer informed at | [Date] [Time] |
| PIMS-PRO-04 started | Yes / No. *If yes, the time of awareness recorded there must match the time above.* |
| [Organisation] acts as | Controller / Processor / Both / Not applicable |
| Client-facing service affected | Yes / No |
| Supplier involved | Yes / No. *Name the GOV-REG-07 entry.* |
| AI system involved | Yes / No. *If yes, AI-PRO-03 applies.* |

## 6. Actions taken

*One row per action. Containment, eradication and recovery actions are all recorded here. Emergency changes are also recorded under GOV-PRO-09.*

| Date and time | Phase | Action | By whom | Result |
|---|---|---|---|---|
| | Containment / Eradication / Recovery | | [Role] | |
| | | | | |
| | | | | |
| | | | | |

## 7. Timeline

*A chronological record of what happened and what the team learned, including events before detection as they become known. Name the source of each entry: a log, an alert, a person, a supplier notice.*

| Date and time | Event | Source |
|---|---|---|
| | | |
| | | |
| | | |
| | | |

## 8. Notifications

*Internal escalations and every external notification. Nothing leaves [Organisation] without the executive sponsor's approval recorded here.*

| Recipient | Required by | Deadline | Approved by | Sent at | Reference |
|---|---|---|---|---|---|
| Executive sponsor | GOV-PRO-07 | | | | |
| Privacy Officer | GOV-PRO-07 step 4.4 | | | | |
| Supervisory authority | PIMS-PRO-04, GDPR-TPL-10 | | | | |
| Affected individuals | PIMS-PRO-04 | | | | |
| Clients | Contract (GOV-REG-04) | | | | |
| Controller (where processor) | Contract | | | | |
| Insurer / law enforcement / other | | | | | |

## 9. Evidence collected

*Collect before remediation alters anything. Record a hash value for every file and keep the chain of custody.*

| Item | Location | Hash value | Collected by | Date and time |
|---|---|---|---|---|
| | | | [Role] | |
| | | | | |
| | | | | |

## 10. Closure

| Closure criterion | Confirmed (Yes / No) | Note |
|---|---|---|
| Cause removed and persistence checked | | |
| Service recovered and confirmed by the system owner | | |
| All notifications complete | | |
| Evidence stored in the restricted location with hashes | | |
| GOV-REG-08 updated with times, root cause and lessons | | |
| Post-incident review required (Severity 1 or 2, or selected) | | *GOV-TPL-11 reference* |
| Corrective actions raised | | *GOV-REG-03 references* |

| Field | Entry |
|---|---|
| Date and time contained | [Date] [Time] |
| Date and time resolved | [Date] [Time] |
| Root cause (one sentence) | |
| Closed by | Incident Lead, [Date] |
