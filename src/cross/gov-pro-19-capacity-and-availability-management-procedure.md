---
id: GOV-PRO-19
title: Capacity and Availability Management Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.6
  - ISO/IEC 27001:2022 Annex A 8.14
  - SOC 2 A1.1
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: What is monitored, the thresholds that trigger action, how demand is forecast, how redundancy is designed and tested, and how capacity problems link to incident handling.
---
## 1. Purpose

This procedure keeps [Organisation]'s services available and performing within agreed levels, by monitoring capacity against thresholds, forecasting demand before it becomes a problem, and designing and testing redundancy for critical systems.

## 2. Scope

It applies to production systems and the shared services they depend on: compute, memory, storage, database capacity, network bandwidth, message queues, licence counts, provider quotas and rate limits, certificate validity, and the on-call capacity of the teams that operate them.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns this procedure, approves capacity investment, reviews the quarterly report. |
| System Owner | Sets the availability target and thresholds for their system, owns its forecast and its monthly entry in GOV-REG-17. |
| Platform team | Operates monitoring, responds to threshold alerts, performs scaling changes, calculates monthly availability. |
| Information Security Manager | Confirms that resilience decisions match the risk register and the continuity objectives. |

## 4. Procedure

4.1 **Targets.** The System Owner records for each production system an availability target (for example 99.9 percent measured monthly), the indicators that define the service as working (latency, error rate, throughput), and the recovery objectives from GOV-TPL-07. Targets promised to customers are taken from the contract.

4.2 **Monitoring and thresholds.** The platform team monitors every component against a warning and a critical threshold and routes critical alerts through the triage process in GOV-PRO-14. Default thresholds, which the System Owner may tighten, are:

| Metric | Warning | Critical |
|---|---|---|
| Processor utilisation, sustained 15 minutes | 70 percent | 85 percent |
| Memory utilisation | 75 percent | 90 percent |
| Storage used | 75 percent | 90 percent |
| Database connections or queue depth | 70 percent of limit | 90 percent of limit |
| Error rate against target | Half the error budget consumed | Error budget exhausted |
| Provider quota or licence count | 80 percent | 95 percent |
| Certificate validity | 30 days to expiry | 7 days to expiry |

4.3 **Forecasting.** Each month the System Owner reviews utilisation trends and business plans (customer onboarding, feature launches, seasonal peaks) and records in GOV-REG-17 the months of headroom at the current trend. Any component forecast to reach its critical threshold within six months gets an action with an owner and date. The Head of Engineering reviews a consolidated capacity report quarterly and approves procurement or architecture changes.

4.4 **Redundancy and resilience.** Critical systems, as rated in the business impact analysis, have no single point of failure within the approved strategy (GOV-PRO-13): at least two instances across separate failure zones, load balancing with health checks, replicated storage, and provider services configured for the availability tier the target needs. Failover is tested at least annually and recorded in GOV-REG-16.

4.5 **Scaling.** Where the platform supports it, automatic scaling rules are configured with upper limits that protect cost and downstream systems. Manual scaling and changes to the limits are changes under GOV-PRO-09.

4.6 **Demand management.** Public interfaces enforce rate limits and request size limits. Batch and reporting jobs run outside peak hours. Abusive traffic is blocked at the edge and the event is reported under GOV-PRO-14.

4.7 **Measurement.** The platform team calculates availability and performance against target each month from monitoring data, excluding only maintenance windows announced under GOV-PRO-09, and records the result in GOV-REG-17. A missed target triggers a review by the System Owner within ten working days, with actions recorded.

4.8 **Incident link.** A critical threshold breach that degrades service is handled as an incident under GOV-PRO-07. The post-incident review states whether capacity or resilience was a cause; resulting actions are recorded in GOV-REG-17 and, where they need investment, as a risk in GOV-REG-05.

4.9 **Reclamation.** Idle instances, unused capacity and expired licences identified in the monthly review are released through GOV-PRO-09.

## 5. Records and evidence

- GOV-REG-17 Capacity and availability log: monthly results, headroom and actions per system.
- Monitoring dashboards and alert history.
- The quarterly capacity report and the Head of Engineering's decisions.
- Failover test records in GOV-REG-16.
- Missed target reviews and their actions.

## 6. Exceptions

A system may run without redundancy only where its business impact rating is below the critical tier and the System Owner records the decision as a risk in GOV-REG-05.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any availability incident at one of the two highest severity levels, after a target is missed in two consecutive months, and when the hosting platform changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-17 Capacity and availability log
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-13 Business continuity and ICT readiness procedure
- GOV-REG-16 Business continuity exercise log
- GOV-TPL-07 Business impact analysis worksheet
- GOV-PRO-09 Change management procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-REG-05 Information security risk register
- GOV-REG-18 Cryptographic key and certificate inventory
