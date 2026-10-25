---
id: GOV-TPL-07
title: Business Impact Analysis Worksheet
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.30
  - ISO/IEC 27001:2022 Annex A 5.29
  - SOC 2 A1.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The worksheet a process owner completes to record dependencies, impact over time, recovery objectives and minimum resources for one business process, feeding the continuity plan.
---
## 1. How to use this worksheet

*Complete one worksheet per business process, with the process owner and the owners of the systems it depends on present. Rate impact at each point in time on the 1 to 5 scale in section 4, using the impact definitions in GOV-PRO-05 so that continuity and risk speak the same language. Return the completed worksheet to the business continuity coordinator, who consolidates all worksheets under GOV-PRO-13. Guidance notes are in italics and are deleted from the completed copy.*

## 2. Process identification

| Field | Entry |
|---|---|
| Process name | [Process] |
| Process owner (role) | [Role] |
| Description (two sentences) | |
| Service or customers it supports | |
| Peak periods when disruption hurts most | |
| Worksheet completed by (role) | [Role] |
| Date completed | [Date] |

## 3. Dependencies

*List everything the process cannot run without, one row per dependency. "Workaround" is what you would do if the dependency failed today.*

| Dependency type | Name | Owner | Workaround | Single point of failure |
|---|---|---|---|---|
| System or application | [System name] | [Role] | | Yes / No |
| Data set | | | | |
| People or skill | | | | |
| Supplier or provider | | | | |
| Facility or equipment | | | | |
| Other process | | | | |

## 4. Impact over time

*Score each category 1 negligible, 2 minor, 3 moderate, 4 major, 5 severe, using the impact definitions in GOV-PRO-05. The highest score at each time point is the overall impact.*

| Impact category | 4 hours | 1 day | 3 days | 1 week |
|---|---|---|---|---|
| Financial (lost revenue, penalties, cost of recovery) | | | | |
| Legal, regulatory and contractual | | | | |
| Reputation and customer trust | | | | |
| Operational (other processes stopped) | | | | |
| Harm to individuals, including through personal data | | | | |
| Overall (highest score) | | | | |

## 5. Recovery objectives

*The maximum tolerable period of disruption is the point at which the overall impact reaches 4. The recovery time objective must be shorter than that. The recovery point objective is the most data you can afford to lose, expressed as time.*

| Objective | Value | Reason |
|---|---|---|
| Maximum tolerable period of disruption | [Number] hours or days | |
| Recovery time objective | [Number] hours or days | |
| Recovery point objective | [Number] minutes or hours | |
| Minimum service level during recovery (what must work first) | | |
| Priority tier (1 highest to 4 lowest) | | |

## 6. Minimum resources to operate

| Resource | Normal | Minimum during recovery | Source if the primary is lost |
|---|---|---|---|
| People (number and roles) | | | |
| Systems and access | | | |
| Data and the most recent acceptable copy | | | |
| Suppliers and services | | | |
| Workplace, equipment and connectivity | | | |
| Communication channels | | | |

## 7. Current readiness

| Question | Answer |
|---|---|
| Does a recovery runbook exist for each dependent system? | Yes / No / Partial |
| Were the data sets restore-tested in the last 12 months (GOV-REG-15)? | |
| When was this process last exercised (GOV-REG-16)? | |
| Known gaps against the objectives above | |
| Risks raised in GOV-REG-05 as a result | |

## 8. Summary row for the consolidated list

*The coordinator copies this row into the consolidated priority list.*

| Process | Recovery time objective | Recovery point objective | Maximum tolerable disruption | Owner |
|---|---|---|---|---|
| [Process] | | | | [Role] |

## 9. Sign-off

| Role | Signature | Date |
|---|---|---|
| Process owner | | [Date] |
| Business continuity coordinator | | [Date] |
| Head of Engineering, for ICT dependencies | | [Date] |

## 10. Records and review

The completed worksheet is a record under GOV-PRO-13, retained with the business continuity plan. It is reviewed annually and when the process, its systems or its suppliers change. Changes to this template follow GOV-PRO-01.

## 11. Related documents

- GOV-PRO-13 Business continuity and ICT readiness procedure
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-PRO-12 Backup and restore testing procedure
- GOV-REG-15 Backup and restore test log
- GOV-REG-16 Business continuity exercise log
- GOV-REG-05 Information security risk register
