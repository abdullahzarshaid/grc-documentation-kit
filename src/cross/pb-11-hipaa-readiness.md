---
id: PB-11
title: "Playbook: HIPAA readiness for a small team"
type: playbook
framework: cross
maps:
  - HIPAA 45 CFR 164.308
  - HIPAA 45 CFR 164.404
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The order of work for a covered entity or business associate to meet the HIPAA Security, Privacy and Breach Notification Rules, built on the kit's existing controls.
---
## 1. Purpose

This playbook takes a small team that handles protected health information to the point where it can show it meets HIPAA. Most of the work is the kit's ordinary security and privacy controls applied to health data; the HIPAA set adds the pieces that are specific to the law.

## 2. First, know your role

Decide whether you are a covered entity, a business associate, or both. A covered entity is a health plan, clearinghouse or provider that transmits health data electronically. A business associate handles protected health information on behalf of a covered entity. The duties overlap heavily, but the Privacy Rule obligations are heavier for a covered entity, and a business associate works under a business associate agreement. HIPAA-GDE-01 explains the distinction.

## 3. The steps

3.1 **Appoint the officials.** Name the security official and the privacy official (one person may hold both in a small team). This is a required Security Rule standard.

3.2 **Find the health data.** List every place electronic protected health information is created, received, maintained or transmitted, in the asset register (GOV-REG-10). You cannot protect or assess what you have not located.

3.3 **Run the security risk analysis.** Perform the analysis required by the Security Rule (HIPAA-PRO-01), feeding the risk register (GOV-REG-05). This is the foundation; everything else flows from it, and no other step substitutes for it.

3.4 **Work the safeguard matrix.** Open HIPAA-REG-01. For each required specification, confirm the kit control that implements it is in place. For each addressable specification, record whether it is reasonable and appropriate, and implement it or an equivalent alternative, or document why neither is required. Encryption of health data at rest and in transit is almost always the reasonable measure.

3.5 **Adopt the policies.** Issue the HIPAA security policy (HIPAA-POL-02) and, if you are a covered entity, the privacy policy (HIPAA-POL-01) and a notice of privacy practices.

3.6 **Govern business associates.** Put a business associate agreement (HIPAA-TPL-01) in place with every vendor that handles protected health information, and record them in HIPAA-REG-02. If you are a business associate, make sure your own subcontractors are bound.

3.7 **Prepare for a breach.** Adopt the breach notification procedure (HIPAA-PRO-02). Know the sixty-day clock, the four-factor risk assessment, and when HHS and the media must be told. Open the breach register (HIPAA-REG-03).

3.8 **Honour individual rights.** Where you are a covered entity, stand up the process for access, amendment, accounting of disclosures, restrictions and confidential communications (HIPAA-POL-01), reusing the rights process in PIMS-PRO-03.

3.9 **Train and document.** Train the workforce, keep the documentation for six years, and review it as things change. The Documentation standard is required.

3.10 **Evaluate.** Periodically evaluate your safeguards against the rule through internal audit (GOV-PRO-02), and update the risk analysis after any significant change or incident.

## 4. What HIPAA does not change

HIPAA does not ask for a different security programme. Access control, encryption, logging, incident response, backups, continuity, training, vendor management and risk management are the kit's existing controls. Point them at protected health information, add the business associate agreement, the breach rule and the required-versus-addressable judgement, and keep the documentation. That is HIPAA readiness.

## 5. Related documents

- HIPAA-GDE-01 HIPAA in plain words
- HIPAA-GDE-02 HIPAA Security Rule mapped to the kit
- HIPAA-PRO-01 Security risk analysis procedure
- HIPAA-REG-01 HIPAA Security Rule safeguard matrix
- HIPAA-TPL-01 Business associate agreement
- PB-09 Evidence management
