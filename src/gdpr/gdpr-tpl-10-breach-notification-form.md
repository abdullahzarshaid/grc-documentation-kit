---
id: GDPR-TPL-10
title: Personal data breach notification form (to the supervisory authority)
type: template
framework: gdpr
maps:
  - GDPR Article 33
  - GDPR Article 34
  - ISO/IEC 27701 clause 6.13.1.5
  - ISO/IEC 27701 Annex A 7.3.7
owner: Privacy Officer
approver: Privacy Officer
classification: Confidential
review: Annual
summary: The content the authority needs under GDPR Article 33(3), prepared under PIMS-PRO-04 so that a notification can be made within 72 hours of awareness, in phases where the facts are not yet complete, with the record kept in PIMS-REG-03 whether or not the authority is notified.
---
*Guidance notes are in italics. Most supervisory authorities provide their own online form; this template collects every fact that form will ask for, so that the Privacy Officer fills it from here rather than from memory under time pressure. The 72 hour clock starts when the organisation becomes aware that a breach has probably occurred, not when the investigation ends. Where the facts are incomplete at 72 hours, notify with what is known and mark the rest as "to follow": a phased notification is permitted; a late one needs reasons. Keep every version of this form against the PIMS-REG-03 entry. Where [Organisation] is a processor, this form is not sent to the authority; the facts are sent to the controller without undue delay and the controller notifies.*

## 1. Notifier and references

| Field | Entry |
|---|---|
| **Internal reference** | [PIMS-REG-03 reference], linked incident [GOV-REG-08 reference] |
| **Organisation** | [Organisation], [registered address], registration or reference number with the authority if any |
| **Role** | [Controller, Joint controller (name the other), Processor notifying on behalf of a controller with its authority] |
| **Contact point for the authority** | [Role, for example Data Protection Officer or Privacy Officer], [contact channel]. *A role mailbox that is monitored outside office hours.* |
| **Notification type** | [Initial, Phased update number [Number], Final] |
| **Date and time of this notification** | [Date and time] |
| **Other authorities notified** | [None, or a list where the breach affects people in several jurisdictions, with the lead authority identified] |

## 2. Timeline

| Event | Date and time | Source |
|---|---|---|
| Breach began (or is believed to have begun) | | *Log evidence, report, estimate; say which* |
| Breach ended or was contained | | |
| Organisation became aware | | *The moment a person with responsibility had reasonable certainty that personal data was compromised* |
| Processor informed the controller (if applicable) | | |
| This notification | | |

**Hours from awareness to this notification:** [Number]. **If more than 72:** *state the reasons for the delay in section 7; it is mandatory.*

## 3. Nature of the breach

| Field | Entry |
|---|---|
| **What happened** | *Plain description in three to six sentences: the system or process involved, the cause (for example misdirected message, lost device, compromised credential, misconfiguration, malicious attack, supplier breach), how it was discovered.* |
| **Type of breach** | [Confidentiality (data disclosed or accessed), Integrity (data altered), Availability (data lost or made inaccessible), or a combination] |
| **Categories of people affected** | [Customers, users, employees, applicants, children, vulnerable people, other], with any that make the risk higher |
| **Approximate number of people affected** | [Number], or [minimum] to [maximum] with the basis of the estimate; "not yet known" with the date by which it will be |
| **Categories of personal data affected** | [Identity, contact, financial, authentication credentials, location, health or other special category, criminal offence data, content, other] |
| **Approximate number of records affected** | [Number], or a range with the basis |
| **Was the data protected** | [Encrypted with keys not compromised, Pseudonymised, Hashed credentials, Plain] |
| **Is the breach ongoing** | [Yes, No, Unknown] |
| **Cross-border element** | [People in other jurisdictions affected: list; main establishment of the organisation] |

## 4. Likely consequences for the people affected

*Assess from the point of view of the people, as PIMS-PRO-04 requires. Describe the harm and its likelihood; do not minimise. This section drives the decision in section 6.*

| Field | Entry |
|---|---|
| **Possible harms** | [Identity theft or fraud, financial loss, loss of confidentiality of professional secrecy, discrimination, reputational damage, physical safety, loss of control over data, distress, other] |
| **Severity for the people** | [Low, Medium, High], with reasons |
| **Likelihood of harm** | [Low, Medium, High], with reasons, including whether the data is in the hands of a known malicious party or was recovered |
| **Overall risk to the people** | [Unlikely to result in a risk, Risk, High risk] |

## 5. Measures taken and proposed

| Field | Entry |
|---|---|
| **Containment** | *What stopped the breach and when: credentials reset, access revoked, system isolated, message recalled, device wiped remotely, supplier instructed.* |
| **Recovery** | *What restored the data or service, and whether data was recovered or confirmed deleted by the recipient.* |
| **Mitigation for the people** | *Password resets forced, monitoring offered, accounts frozen, guidance issued.* |
| **Root cause and correction** | *What will stop it recurring, with the GOV-REG-03 corrective action reference and dates.* |
| **Processor involvement** | *If a processor caused or was involved, its name, what it did, and the contractual steps taken.* |

## 6. Communication to the people affected

| Field | Entry |
|---|---|
| **Decision** | [Individuals will be informed, Individuals have been informed on [Date], Individuals will not be informed because the risk is not high, Individuals will not be informed because [the data was encrypted and the keys are safe / subsequent measures mean the high risk is no longer likely / individual contact would involve disproportionate effort and a public communication has been made]] |
| **Method and date** | [Email, letter, in-product message, public notice], [Date] |
| **Content** | *Attach the message. It must describe the breach in plain words, give the contact point, state the likely consequences and the measures taken and recommended.* |
| **Number informed** | [Number] |

## 7. Reasons for delay (where more than 72 hours after awareness)

*State the facts: for example, the breach was discovered through a third party report that took time to verify; the scope could not be established until forensic analysis was complete; the responsible person was unavailable and the escalation path failed (and what has been fixed). Do not write "due to internal processes".*

[Reasons]

## 8. Information to follow

| Item | Expected date |
|---|---|
| [Confirmed number of people affected] | [Date] |
| [Result of forensic analysis] | [Date] |
| [Outcome of communication to individuals] | [Date] |

## 9. Sign-off

| Field | Entry |
|---|---|
| **Prepared by** | [Name], [Role], [Date and time] |
| **Approved for submission by** | [Name], Privacy Officer or Data Protection Officer, [Date and time] |
| **Executive informed** | [Name], Chief Executive Officer, [Date and time] |
| **Submitted via** | [Authority's online form, email, telephone followed by written confirmation], authority reference received [Reference] |

## 10. Related documents

- PIMS-PRO-04 Personal data breach assessment and notification procedure
- PIMS-REG-03 Personal data breach register
- GOV-PRO-07 Information security incident management procedure
- GOV-TPL-05 Incident report form
- GOV-TPL-11 Post-incident review template
- GOV-REG-08 Incident register
- GOV-REG-03 Corrective action log
