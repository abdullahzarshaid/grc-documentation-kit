---
id: HIPAA-GDE-01
title: "Guide: HIPAA in plain words"
type: guide
framework: hipaa
maps:
  - HIPAA 45 CFR 160
  - HIPAA 45 CFR 164
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: What HIPAA covers, who must comply, the rules it sets and the ideas that shape the Security Rule, written for a team new to it. Read the regulation and HHS guidance for the authoritative detail.
---
## 1. What HIPAA is

HIPAA is United States federal law that protects health information. Its rules are enforced by the Department of Health and Human Services through its Office for Civil Rights. The parts that matter in day-to-day work are the Privacy Rule, the Security Rule, the Breach Notification Rule and the Enforcement Rule, all in 45 CFR Parts 160 and 164. This guide explains them in plain words; the authoritative text is the regulation itself.

## 2. Who must comply

Two kinds of organisation are bound by HIPAA. A covered entity is a health plan, a health care clearinghouse, or a health care provider that transmits health information electronically for certain transactions. A business associate is an organisation that creates, receives, maintains or transmits protected health information on behalf of a covered entity, for example a cloud host, a billing service or a software vendor. A business associate's own subcontractors that handle the information are also bound. If you build or run software that handles health information for a covered entity, you are almost certainly a business associate.

## 3. The information it protects

Protected health information, or PHI, is individually identifiable health information held or transmitted in any form. When it is in electronic form it is called ePHI, and the Security Rule applies to it specifically. Information that has been de-identified under the standard in the Privacy Rule is no longer PHI.

## 4. The four rules

4.1 **The Privacy Rule** governs how PHI may be used and disclosed. Its central ideas are the minimum necessary principle, the individual's rights over their own information, and the requirement to give a notice of privacy practices. See HIPAA-POL-01.

4.2 **The Security Rule** requires administrative, physical and technical safeguards for ePHI, to protect its confidentiality, integrity and availability. See HIPAA-POL-02 and the safeguard matrix in HIPAA-REG-01.

4.3 **The Breach Notification Rule** requires notification to the affected individuals, to HHS, and in larger breaches to the media, when unsecured PHI is breached. See HIPAA-PRO-02.

4.4 **The Enforcement Rule** sets out how HHS investigates and penalises non-compliance. The practical message is that documented, good-faith safeguards and a real risk analysis matter when something goes wrong.

## 5. Required and addressable

The Security Rule is deliberately flexible. Each implementation specification is marked either required or addressable. A required specification must be implemented. An addressable specification is not optional in the ordinary sense: you must assess whether it is reasonable and appropriate in your environment, and then either implement it, or document why it is not reasonable and implement an equivalent alternative measure. Addressable never means "ignore"; it means "decide and record".

## 6. The security risk analysis is the foundation

The one activity that everything else rests on is the security risk analysis required by the Security Rule. It identifies where ePHI lives, the threats and vulnerabilities to it, and the risks that result, and it drives the risk management decisions that follow. An organisation cannot show it meets the Security Rule without it. See HIPAA-PRO-01.

## 7. How HIPAA sits with the rest of the kit

Most of what the Security Rule asks for is general good security practice that the kit already provides: access control, encryption, logging, incident response, contingency planning, workforce training, risk management and vendor management. The HIPAA set adds the HIPAA-specific pieces, the privacy obligations, the business associate agreement, the breach rule and the safeguard mapping, and points each safeguard at the kit document that implements it. HIPAA-GDE-02 is that map.

## 8. Related documents

- HIPAA-POL-01 HIPAA privacy policy
- HIPAA-POL-02 HIPAA security policy
- HIPAA-PRO-01 Security risk analysis procedure
- HIPAA-PRO-02 HIPAA breach notification procedure
- HIPAA-TPL-01 Business associate agreement
- HIPAA-GDE-02 HIPAA Security Rule mapped to the kit
- HIPAA-REG-01 HIPAA Security Rule safeguard matrix
