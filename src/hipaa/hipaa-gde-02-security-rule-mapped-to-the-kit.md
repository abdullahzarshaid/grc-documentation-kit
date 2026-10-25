---
id: HIPAA-GDE-02
title: "Guide: the HIPAA Security Rule mapped to the kit"
type: guide
framework: hipaa
maps:
  - HIPAA 45 CFR 164.308
  - HIPAA 45 CFR 164.310
  - HIPAA 45 CFR 164.312
  - HIPAA 45 CFR 164.314
  - HIPAA 45 CFR 164.316
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: Each HIPAA Security Rule standard mapped to the kit document that implements it, so a team already running the kit can see what the Security Rule adds. The full matrix, with every implementation specification and its required or addressable flag, is HIPAA-REG-01.
---
## 1. How to read this

The Security Rule groups its requirements into administrative, physical and technical safeguards, plus organisational requirements and documentation. This guide maps each standard to the kit document that implements it. The point is simple: most of the Security Rule is good security practice the kit already provides, so a team running the kit is most of the way there. The full matrix, down to each implementation specification and whether it is required or addressable, is the register HIPAA-REG-01.

## 2. Administrative safeguards (164.308)

| Standard | Theme | Kit documents |
|---|---|---|
| Security management process | Risk analysis, risk management, sanctions, activity review | HIPAA-PRO-01; GOV-PRO-05; GOV-REG-05; GOV-PRO-14 |
| Assigned security responsibility | A named security official | HIPAA-POL-02; GOV-POL-01 |
| Workforce security | Authorisation, clearance, termination | GOV-PRO-18; GOV-PRO-10; GOV-CHK-01 |
| Information access management | Access authorisation and modification | GOV-PRO-10; GOV-TPL-09 |
| Security awareness and training | Reminders, malware protection, log-in monitoring, passwords | GOV-PRO-08; GOV-PRO-22; GOV-POL-06 |
| Security incident procedures | Response and reporting | GOV-PRO-07; GOV-REG-08 |
| Contingency plan | Backup, disaster recovery, emergency mode, testing, criticality | GOV-PRO-12; GOV-PRO-13; GOV-TPL-07 |
| Evaluation | Periodic review against the rule | GOV-PRO-02; HIPAA-REG-01 |
| Business associate contracts | Written assurances | HIPAA-TPL-01; HIPAA-REG-02 |

## 3. Physical safeguards (164.310)

| Standard | Theme | Kit documents |
|---|---|---|
| Facility access controls | Contingency operations, security plan, access validation, maintenance records | GOV-PRO-17; GOV-REG-19 |
| Workstation use | Rules for how workstations are used | GOV-POL-04; GOV-POL-02 |
| Workstation security | Physical protection of workstations | GOV-PRO-17; GOV-PRO-22 |
| Device and media controls | Disposal, re-use, accountability, backup | GOV-PRO-16; GOV-REG-20 |

## 4. Technical safeguards (164.312)

| Standard | Theme | Kit documents |
|---|---|---|
| Access control | Unique user ID, emergency access, automatic logoff, encryption | GOV-PRO-10; GOV-POL-06; GOV-PRO-20 |
| Audit controls | Record and examine system activity | GOV-PRO-14 |
| Integrity | Protect information from improper alteration | GOV-PRO-20; GOV-PRO-14 |
| Person or entity authentication | Verify who is seeking access | GOV-POL-06; GOV-PRO-10 |
| Transmission security | Integrity controls and encryption in transit | GOV-PRO-23; GOV-PRO-20; GOV-PRO-21 |

## 5. Organisational requirements and documentation (164.314 and 164.316)

| Standard | Theme | Kit documents |
|---|---|---|
| Business associate arrangements | Required contract terms | HIPAA-TPL-01; GOV-PRO-06 |
| Policies and procedures | Maintain reasonable and appropriate policies | HIPAA-POL-02; GOV-PRO-01 |
| Documentation | Keep records, make them available, review and update | GOV-PRO-01; GOV-REG-01; HIPAA-REG-01 |

## 6. What HIPAA adds beyond the kit

Three things are specific to HIPAA rather than general security practice: the business associate agreement and the assurances it carries, the breach notification duties and their time limits, and the required versus addressable judgement recorded for each specification. The HIPAA set provides all three. Everything else is the kit's existing controls, applied to electronic protected health information.

## 7. Related documents

- HIPAA-POL-02 HIPAA security policy
- HIPAA-PRO-01 Security risk analysis procedure
- HIPAA-REG-01 HIPAA Security Rule safeguard matrix
- GOV-REG-27 Framework crosswalk
