---
id: AI-PRO-03
title: AI Incident and Model Failure Handling Procedure
type: procedure
framework: ai
maps:
  - ISO/IEC 42001 clause 8.3
  - ISO/IEC 42001 clause 10.1
  - NIST AI RMF MANAGE
  - ISO/IEC 27001:2022 Annex A 5.24
  - ISO/IEC 27001:2022 Annex A 5.26
  - GDPR Article 33
  - GDPR Article 34
  - SOC 2 CC7.4
owner: Information Security Manager
approver: Head of Engineering
classification: Internal
review: Annual
summary: How an event involving an AI system or tool, such as harmful output, data leakage, model drift or abuse, is recognised, contained, rolled back, investigated and disclosed, and how it connects to the security incident and personal data breach procedures.
---
## 1. Purpose

AI systems fail in ways the general incident procedure does not describe: a model gives a harmful answer to one person, leaks a document to another, drifts quietly until its decisions are wrong, or is manipulated into acting outside its purpose. This procedure names those event types, gives each a first response, and routes the event into GOV-PRO-07 and PIMS-PRO-04 so that one timeline, one register and one set of notifications cover it.

## 2. Scope

It applies to every system in AI-REG-01 and every tool in AI-REG-04, whether the event is reported by a user, a client, a member of the public, a vendor, monitoring under AI-POL-02 4.7, or an evaluation run. It covers events in production and in pilots with external exposure.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Any person | Reports a suspected AI event the same working day through the route in GOV-PRO-07. |
| Incident lead (role assigned under GOV-PRO-07) | Runs the response, keeps the timeline, decides containment with the System Owner. |
| System Owner or tool owner | Executes pause, rollback and configuration changes; supplies logs and the AI-REG-03 history. |
| Information Security Manager | Classifies the event, links it to GOV-REG-08, owns the post-incident review. |
| Privacy Officer | Assesses personal data impact under PIMS-PRO-04 and leads notifications to authorities and individuals. |
| Head of Engineering | Approves re-release after a rollback and any change to evaluation thresholds. |
| Engagement lead or account role | Handles disclosure to the affected client. |

## 4. Procedure

4.1 **Recognise and classify.** The Information Security Manager classifies the event within four working hours of the report as one or more of the types below, records it in GOV-REG-08 with the type and the AI-REG-01 or AI-REG-04 reference, and assigns the severity under GOV-PRO-07.

| Type | Examples | First response |
|---|---|---|
| Harmful or wrong output | Discriminatory, defamatory, unsafe or materially false output reached a user, a client or a decision; a decision about a person was shaped by a wrong output. | Capture the prompt, output and model version; stop the use case or add a human review step; identify affected people. |
| Leakage | Confidential, client or personal data entered into a tool in breach of AI-POL-01; output revealed another tenant's or person's data; system instructions or retrieval content exposed. | Delete the item at the provider where possible and record the request; revoke the affected session; identify data categories and subjects. |
| Drift or degradation | Accuracy, refusal rate, error rate or bias measure crosses the threshold set in AI-REG-03; outputs changed after a provider model update. | Pause or roll back to the last evaluated version; re-run the evaluation set; freeze dependent decisions until results are known. |
| Abuse and manipulation | Prompt injection succeeded; an agent took an unauthorised action; the service was used for a prohibited purpose; denial of service through expensive inputs. | Disable the affected tool or permission; block the source; preserve logs; check for actions that must be reversed. |
| Supply chain | Vendor incident, terms change, sub-processor breach, or a vulnerable or malicious model, library or plugin. | Suspend the integration; obtain the vendor's statement; check AI-REG-04 and AI-REG-01 for every dependent use. |

4.2 **Contain.** The System Owner applies the first response within the time stated for the system in AI-REG-01 and never later than one working day. Where a kill switch, feature flag or version pin exists under AI-POL-02 4.5, it is used before any slower measure. Containment actions and their times go in the GOV-PRO-07 timeline.

4.3 **Assess personal data impact.** Where personal data may have been entered, exposed, inferred or used in a decision, the Privacy Officer runs PIMS-PRO-04 from the moment of classification. The seventy-two hour clock for a notifiable breach runs from awareness of the event, not from the end of the AI investigation.

4.4 **Investigate.** The incident lead establishes from the logs required by AI-POL-02 4.7: which inputs produced the event, which model version and prompt template were live, which tools or data sources the model reached, how many users or records were affected, and whether the AI-PRO-01 risk register predicted the scenario. Where a vendor service is involved, the Information Security Manager requests the vendor's incident report through the channel recorded in AI-TPL-01 question 23.

4.5 **Roll back and recover.** The System Owner restores the last version whose evaluation passed, reverses any actions an agent took that can be reversed, corrects or withdraws decisions about people that were based on the wrong output, and records the rollback in AI-REG-03 with the reason. A system stays paused until the Head of Engineering approves re-release on the basis of a repeated evaluation under AI-POL-02 4.6 that covers the failure case.

4.6 **Disclose.** The engagement lead tells an affected client in writing within the period the contract sets, or within two working days where it sets none, what happened, what data or output was involved, what has been done and what the client should do. Individuals affected by a wrong decision are told how it was corrected and how to contest it. Public statements are approved by the Chief Executive Officer. Where the system is High class under AI-POL-02 and a law requires a report to an authority, the Privacy Officer or the legal role files it within the statutory period and records it in GOV-REG-08.

4.7 **Review and correct.** Within ten working days of closure the Information Security Manager completes a post-incident review under GOV-TPL-11, updates AI-REG-02 with the new or re-scored risk, raises corrective actions in GOV-REG-03 under GOV-PRO-04, and adds the failure case to the system's evaluation set in AI-REG-03 so that it is tested before every future release. Where a staff tool caused a leak, AI-REG-04 is updated with any new prohibited data or configuration.

4.8 **Learn across systems.** Quarterly, the Information Security Manager reviews all AI events in GOV-REG-08 for patterns, reports them to the steering committee under GOV-POL-01, and proposes changes to AI-POL-01, AI-POL-02 or the AI-PRO-01 catalogue.

## 5. Records and evidence

- GOV-REG-08 Incident register: every AI event with type, system reference, severity, personal data flag and status.
- Incident timelines and GOV-TPL-05 Incident report form entries.
- PIMS-REG-03 Personal data breach register: AI events that involved personal data.
- AI-REG-03 AI change and evaluation log: rollbacks, re-evaluations and added test cases.
- AI-REG-02 AI risk register: re-scored or new risks.
- GOV-REG-03 Corrective action log: actions from the post-incident review.
- Client and authority notifications and vendor incident reports.

## 6. Exceptions

A system that is paused under 4.2 may be re-enabled before the full re-evaluation only for a Minimal class system with no personal data and no client exposure, on the written decision of the Head of Engineering recorded in the timeline. No exception applies to 4.3 or to disclosure obligations under contract or law.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after every Major or Critical AI event, and when GOV-PRO-07 or PIMS-PRO-04 changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-07 Information security incident management procedure
- PIMS-PRO-04 Personal data breach assessment and notification procedure
- GOV-TPL-05 Incident report form
- GOV-TPL-11 Post-incident review template
- GOV-PRO-04 Nonconformity and corrective action procedure
- AI-POL-01 Acceptable use of AI tools policy
- AI-POL-02 AI system development, procurement and deployment policy
- AI-PRO-01 AI risk assessment procedure
- AI-PRO-02 AI vendor and model due diligence procedure
