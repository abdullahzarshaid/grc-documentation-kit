---
id: GOV-PRO-14
title: Logging, Monitoring and Alert Handling Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.15
  - ISO/IEC 27001:2022 Annex A 8.16
  - ISO/IEC 27001:2022 Annex A 8.17
  - SOC 2 CC7.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: Which events every system must record, how logs are synchronised, protected and retained, how alerts are triaged and reviewed, and the limits that keep monitoring proportionate to staff privacy.
---
## 1. Purpose

This procedure makes security-relevant activity visible. It defines the minimum events every system records, how logs are protected and kept, how alerts are triaged within set times, how often logs are reviewed, and the privacy limits on monitoring.

## 2. Scope

It applies to every system in GOV-REG-24 that authenticates users, holds Confidential or Restricted data, provides a network or security function, or forms part of the production environment, including cloud control planes, identity providers, endpoints and software as a service with audit log export. Logs produced by a supplier for [Organisation]'s tenancy are in scope where export is available.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the logging standard and the alert use cases, runs the review cadence, approves any monitoring that targets an individual. |
| Security analyst or on-call engineer | Triages alerts within the response times in 4.6 and escalates incidents. |
| System Owner | Connects their system's logs, maintains its event list, acts on findings. |
| Platform team | Operates the central log store, time synchronisation and retention. |
| Privacy Officer | Reviews monitoring use cases for proportionality and approves the staff notice. |

## 4. Procedure

4.1 **Minimum events.** Every in-scope system records at least the following.

| Event category | Examples |
|---|---|
| Authentication | Success and failure, multi-factor challenge results, password and token changes, account lockout |
| Privilege use | Elevation to administrator, use of break-glass accounts, run-as actions |
| Account and permission changes | Create, modify, disable, delete; group and role membership changes |
| Configuration changes | Security settings, network rules, logging settings, deployments |
| Access to Restricted data | Read, export, download, bulk query and sharing actions |
| Administrative actions | Cloud console and API calls by privileged identities, key management operations |
| Security tooling | Malware detection, scanner findings, loss prevention events, perimeter firewall denials |
| Operations | Backup job results, job failures, service start and stop |

4.2 **Log content.** Each record carries a timestamp in Coordinated Universal Time, the source system, the identity acting, the action, the object acted on, the outcome and the source address where available. Logs never contain passwords, keys, session tokens or payment card numbers, and contain personal data only where needed to identify the actor or the object.

4.3 **Clock synchronisation.** All systems synchronise to the same trusted time source. The platform team checks drift monthly and corrects any system more than one second adrift.

4.4 **Centralisation and protection.** Logs are forwarded to the central log store within fifteen minutes of generation. The store is append-only for the retention period, held in an account or tenancy separate from the systems it monitors, and readable only by the security role and auditors. Administrators of a system cannot alter or delete that system's logs in the central store. Loss of a log feed for more than one hour raises an alert.

4.5 **Retention.** Security logs are kept online and searchable for 90 days and retained for twelve months, or longer where GOV-REG-04 or a contract requires it, then deleted. Retention of logs that contain personal data is listed in PIMS-REG-07.

4.6 **Alerting and triage.** The Information Security Manager maintains a documented list of alert use cases, each with a priority and an owner. Priority 1 alerts (for example a successful login to a break-glass account, malware on a server, a mass download of Restricted data) are acknowledged within 15 minutes during supported hours and by the on-call engineer outside them; Priority 2 within four hours; Priority 3 by the next working day. The analyst records the triage outcome (true positive, benign, false positive, needs tuning) against the alert. A true positive becomes an incident under GOV-PRO-07.

4.7 **Review cadence.** The analyst clears the alert queue every working day. The Information Security Manager reviews privileged activity and break-glass use weekly, reviews alert tuning and feed health monthly, confirms quarterly that every in-scope system in GOV-REG-24 is sending logs, and reports alert volumes, triage times and coverage gaps to the Head of Engineering monthly.

4.8 **Privacy limits.** Monitoring is limited to the purposes of security, service operation and legal compliance. Staff are told what is monitored through GOV-POL-02. No individual is monitored beyond the standard use cases unless the Privacy Officer and the human resources lead approve a written request stating the legal basis, scope and duration. Access to monitoring data for an investigation is granted per case, logged and time-limited. Monitoring data is not used for performance management.

4.9 **Onboarding.** A new system is connected to the central log store, with its event list and alert use cases confirmed, before it goes live (PB-07, GOV-REG-29).

## 5. Records and evidence

- The logging standard with the event list per system.
- The alert use case list and triage records.
- Weekly privileged activity reviews, monthly tuning and feed health reviews, quarterly coverage confirmations.
- Clock drift checks.
- Approvals for targeted monitoring and investigation access.

## 6. Exceptions

A system that cannot produce an event in 4.1 is recorded with the gap and a compensating control (for example a daily configuration comparison) under a risk acceptance in GOV-PRO-24.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any incident where logs were missing or insufficient, after an audit finding, when the log platform changes, and when the law on workplace monitoring changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-07 Information security incident management procedure
- GOV-POL-02 Acceptable use policy
- GOV-REG-24 Software and hardware inventory
- GOV-REG-04 Legal, regulatory and contractual register
- PIMS-REG-07 Retention schedule
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-PRO-10 Access management procedure
- PB-07 Playbook: the go-live security and privacy gate
- GOV-REG-29 Go-live gate checklist
