---
id: HIPAA-PRO-01
title: Security risk analysis procedure
type: procedure
framework: hipaa
maps:
  - HIPAA 45 CFR 164.308
  - HIPAA 45 CFR 164.306
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] performs the security risk analysis the HIPAA Security Rule requires, finding where electronic protected health information lives, the threats and vulnerabilities to it, and the resulting risks, and feeding the risk management decisions that follow.
---
## 1. Purpose

This procedure performs the security risk analysis required by the HIPAA Security Rule. It is the foundation of the Security Rule programme: without it, [Organisation] cannot show that its safeguards are reasonable and appropriate. It identifies the risks to electronic protected health information so that they can be managed.

## 2. Scope

It covers all electronic protected health information that [Organisation] creates, receives, maintains or transmits, wherever it is held, including in systems operated by business associates on [Organisation]'s behalf.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Runs the analysis, records the results and proposes risk treatment. |
| System and process owners | Describe where electronic protected health information flows and the controls in place. |
| Chief Executive Officer | Accepts residual risk above the appetite. |

## 4. Procedure

4.1 **Scope the information.** Identify every place electronic protected health information is created, received, maintained or transmitted: applications, databases, file stores, endpoints, backups, logs, email and the systems of business associates. Record them as assets in the asset register (GOV-REG-10) and flag those holding electronic protected health information.

4.2 **Identify threats and vulnerabilities.** For each place, identify the reasonably anticipated threats, both human and environmental, and the vulnerabilities that a threat could exploit. Use incident history, vulnerability scans, audit findings and known threat sources.

4.3 **Assess current controls.** Record the safeguards already in place for each place, from the safeguard matrix (HIPAA-REG-01) and the kit procedures.

4.4 **Determine likelihood and impact.** Using the risk methodology (GOV-PRO-05), judge the likelihood that a threat exploits a vulnerability and the impact on the confidentiality, integrity and availability of the information, and on the individuals it concerns.

4.5 **Determine the level of risk.** Combine likelihood and impact into a risk level, and record each risk in the risk register (GOV-REG-05), linked to the place and the safeguard it concerns.

4.6 **Decide risk management.** For each risk above the appetite, decide the treatment: additional safeguards, acceptance with a recorded reason, avoidance or transfer. Record the decision, the owner and the due date. For an addressable implementation specification, record in the safeguard matrix whether it is reasonable and appropriate and what is implemented.

4.7 **Record and approve.** Produce the risk analysis record, listing the information locations, threats, vulnerabilities, current controls, risk levels and treatment decisions. The Chief Executive Officer accepts any residual risk above the appetite.

4.8 **Review.** Review and update the analysis at least annually, and after a security incident, a significant change to the systems or facilities that handle electronic protected health information, or a change in the threats.

## 5. Records and evidence

- The security risk analysis record and its dated versions.
- The risk register entries for electronic protected health information (GOV-REG-05).
- The safeguard matrix status (HIPAA-REG-01).
- Residual risk acceptances.

## 6. Exceptions

No part of the analysis is waived. If a place cannot be assessed in time, it is recorded as an open item with an owner and a due date, not omitted.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any change to the risk methodology it relies on.

## 8. Related documents

- HIPAA-POL-02 HIPAA security policy
- HIPAA-REG-01 HIPAA Security Rule safeguard matrix
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
