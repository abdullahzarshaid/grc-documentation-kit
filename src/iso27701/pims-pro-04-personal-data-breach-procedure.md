---
id: PIMS-PRO-04
title: Personal data breach assessment and notification procedure
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 6.13.1.1
  - ISO/IEC 27701 clause 6.13.1.5
  - ISO/IEC 27701 Annex B 8.2.5
  - GDPR Article 33
  - GDPR Article 34
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: "What happens from the moment an incident is found to involve personal data: the 72 hour clock, the assessment of risk to individuals, the decision whether to notify the supervisory authority and the individuals, the processor duty to tell the controller, and the record kept whether or not anyone is notified."
---
## 1. Purpose

This procedure turns an incident involving personal data into a documented assessment and, where required, a notification made within the legal deadline, so that individuals can protect themselves, the authority is told what the law requires, and [Organisation] can show its reasoning afterwards.

## 2. Scope

It applies to every breach of security leading to the accidental or unlawful destruction, loss, alteration, unauthorised disclosure of, or access to, personal data that [Organisation] holds as controller or processor, including breaches at a processor or sub-processor. It runs alongside GOV-PRO-07, which handles the technical response; this procedure handles the assessment, the notification decisions and the privacy record.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Incident Lead | Informs the Privacy Officer the moment personal data is suspected to be involved and records the time of awareness. |
| Privacy Officer | Runs this procedure, assesses the risk to individuals, drafts notifications, keeps PIMS-REG-03 and is the contact point for the authority. |
| Legal adviser | Confirms the notification duties in each jurisdiction and reviews the wording of notifications. |
| Chief Executive Officer | Approves notification to individuals and any public statement; is informed of every notification to an authority before it is sent. |
| Processing Owner and System Owners | Supply the facts about the data, the individuals and the systems, within the times below. |
| Communications lead | Prepares the channels for notifying individuals and handles enquiries, under GOV-PRO-07. |

## 4. Procedure

4.1 **Trigger and time of awareness.** GOV-PRO-07 step 4.4 triggers this procedure. The Incident Lead records the time at which [Organisation] became aware, meaning the time at which a person in [Organisation] had a reasonable degree of certainty that a breach of personal data had occurred, not the time the investigation finished. For a breach reported by a processor, awareness is the time the processor's report is received. The 72 hour clock runs from this time, including outside working hours.

4.2 **Register entry.** Within two hours of the trigger the Privacy Officer opens an entry in PIMS-REG-03 with the GOV-REG-08 reference, the time of awareness and the 72 hour deadline, and sets the status to Under assessment.

4.3 **Facts within 24 hours.** The Privacy Officer obtains from the Incident Lead and the Processing Owner, within 24 hours of awareness: what happened and how; whether the breach affects confidentiality, integrity, availability or several; the categories and approximate number of individuals and of records; whether special categories, financial data, credentials or children's data are involved; whether the data was encrypted or pseudonymised and whether the keys are safe; who received or could access the data and whether it has been recovered; whether the breach is ongoing; and which processing activities in PIMS-REG-01 are affected. Facts not yet known are recorded as unknown with the time they are expected.

4.4 **Role check.** For each affected data set the Privacy Officer confirms from PIMS-REG-01 whether [Organisation] is controller or processor. A single incident can put [Organisation] in both roles for different data; each role follows its own path below.

4.5 **Processor path.** Where [Organisation] is a processor, the Privacy Officer notifies each affected controller without undue delay and in any case within the time in the agreement, or within 24 hours of awareness where no time is agreed, using the contact in PIMS-REG-06 or the contract. The notification gives the facts known, states what is still being established, and promises updates at the agreed cadence. [Organisation] does not notify the authority or the individuals for the controller's data unless the controller instructs it in writing, and gives the controller the assistance it needs to meet its own deadline.

4.6 **Risk assessment to individuals.** Where [Organisation] is a controller, the Privacy Officer assesses the risk to the individuals using the likelihood and severity scales in PIMS-PRO-02 step 4.8, considering: the type of breach; the nature, sensitivity and volume of the data; how easily individuals can be identified; the severity of the consequences (identity theft, fraud, financial loss, discrimination, reputational damage, physical harm, distress, loss of control); whether the individuals are vulnerable; the number affected; the nature of the recipient, if known; and the measures already in place, such as encryption with uncompromised keys, or taken since, such as recovery of the data before it was read. The outcome is one of three: risk unlikely, risk likely, high risk likely.

4.7 **Decision table.** The Privacy Officer applies the table within 48 hours of awareness and records the decision, the reasoning and the legal adviser's confirmation in PIMS-REG-03.

| Outcome | Supervisory authority | Individuals | Record |
|---|---|---|---|
| Risk to individuals unlikely | Not notified; reasoning recorded | Not notified | PIMS-REG-03 entry with facts, effects, measures and the reasons for not notifying |
| Risk likely | Notified within 72 hours of awareness | Not required; may be informed where it helps them | PIMS-REG-03 entry plus the notification and any authority correspondence |
| High risk likely | Notified within 72 hours of awareness | Notified without undue delay, unless an exemption in step 4.9 applies | PIMS-REG-03 entry plus both notifications, the exemption reasoning if used, and enquiries received |

4.8 **Notification to the authority.** The Privacy Officer completes GDPR-TPL-10 with the nature of the breach, the categories and approximate numbers of individuals and records, the contact point, the likely consequences and the measures taken or proposed, informs the Chief Executive Officer, and submits it through the authority's published channel within 72 hours of awareness. Where the facts are incomplete, the notification is made in phases: the initial notification within 72 hours with what is known, and further information as soon as it is available. A notification made after 72 hours states the reasons for the delay. Where individuals in more than one jurisdiction are affected, the legal adviser identifies the lead authority and any further authorities from GOV-REG-04.

4.9 **Notification to individuals.** Where high risk is likely, the Privacy Officer drafts a notice in plain language stating what happened, the contact point, the likely consequences, the measures [Organisation] has taken and the steps individuals can take to protect themselves. The Chief Executive Officer approves it and the communications lead sends it directly to each individual by the most reliable channel available. Direct notification may be replaced by a public communication only where the Privacy Officer records that one of these applies: the data was made unintelligible to any unauthorised person, for example by encryption with keys not compromised; measures taken since mean the high risk is no longer likely to materialise; or individual contact would involve disproportionate effort. The authority may require notification even where [Organisation] decided against it.

4.10 **Other notifications.** The Privacy Officer and legal adviser check GOV-REG-07 for clients with contractual notification rights, GOV-REG-04 for other regulators and sector obligations, the insurance policy for its notification time, and decide with the Incident Lead whether law enforcement is informed. Each is recorded in PIMS-REG-03.

4.11 **Record keeping.** Every breach, notified or not, is recorded in PIMS-REG-03 with the facts, the effects, the measures taken, the assessment outcome and the reasoning behind each decision. The record is retained for the period in PIMS-REG-07 and is available to the authority on request.

4.12 **Review and corrective action.** The post-incident review under GOV-PRO-07, using GOV-TPL-11, includes the Privacy Officer and covers whether the time of awareness was set correctly, whether the deadlines were met and whether the notifications were adequate. Corrective actions go to GOV-REG-03; the affected risks in GOV-REG-05 and any assessment in PIMS-REG-08 are updated within thirty days.

4.13 **Timeline summary.** From awareness: register entry within 2 hours; facts within 24 hours; processor notification to controller within the agreed time or 24 hours; decision within 48 hours; authority notification within 72 hours; individuals without undue delay once high risk is established; post-incident review within ten working days of closure.

## 5. Records and evidence

- PIMS-REG-03 Personal data breach register: one entry per breach with the times, the assessment, the decisions and their reasoning.
- GOV-REG-08 Incident register entry and GOV-TPL-05 incident report for the technical response.
- Completed GDPR-TPL-10 forms, authority acknowledgements and correspondence.
- Notices sent to individuals and controllers, with the approval record and the distribution evidence.
- GOV-TPL-11 post-incident review and GOV-REG-03 corrective actions.

## 6. Exceptions

No exception applies to the deadlines. Where a deadline is missed, the reasons are recorded in PIMS-REG-03 and in the notification itself, and the miss is reported at the next management review.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after every breach notified to an authority, after an annual breach exercise run with GOV-PRO-13, and after a change in notification law or authority guidance. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-07 Information security incident management procedure
- GOV-REG-08 Incident register
- GOV-TPL-05 Incident report form
- GOV-TPL-11 Post-incident review template
- GDPR-TPL-10 Personal data breach notification form
- PIMS-REG-03 Personal data breach register
- PIMS-REG-01 Personal data processing inventory
- PIMS-REG-06 Processor and sub-processor register
- PIMS-TPL-02 Data processing agreement template
- ISMS-PLN-02 Communication plan
