---
id: PIMS-PRO-02
title: Privacy risk and data protection impact assessment procedure
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 7.2.5
  - ISO/IEC 27701 clause 5.4.1.2
  - ISO/IEC 27701 Annex A 7.2.5
  - GDPR Article 35
  - GDPR Article 36
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How every new or changed processing activity is screened for privacy risk, when a full data protection impact assessment is required, how risks to individuals are scored and treated, who approves the residual risk, and when the supervisory authority is consulted first.
---
## 1. Purpose

This procedure finds the harm a processing activity could do to the individuals concerned before the activity starts, reduces that harm by design, and records the decision so that [Organisation] can show it considered the risk. It also satisfies the legal duty to assess, and where necessary consult the authority about, processing likely to result in a high risk.

## 2. Scope

It applies to every new processing activity, every significant change to an existing one (new purpose, new data items, new individuals, new technology, new recipient, new country), every system or feature that handles personal data, and every procurement of a service that will process personal data. It applies whether [Organisation] is controller or processor; as a processor [Organisation] assists the controller's assessment rather than approving its own.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Processing Owner | Completes the screening, drafts the assessment with the project team, implements the measures and owns the residual risk at low or medium. |
| Privacy Officer | Decides whether a full assessment is required, advises throughout, challenges the risk scoring, records the outcome in PIMS-REG-08 and prepares any consultation with the authority. |
| Information Security Manager | Supplies the security measures and links the privacy risks to GOV-REG-05. |
| Head of Engineering or System Owner | Confirms that technical measures are built and tested before go-live. |
| Chief Executive Officer | Approves residual risk rated high and decides whether to proceed to prior consultation. |

## 4. Procedure

4.1 **Screening at concept stage.** Before design approval, the Processing Owner completes section 1 of PIMS-TPL-01, answering each screening trigger Yes or No with one line of justification, and sends it to the Privacy Officer. The triggers are:

1. evaluation or scoring of individuals, including profiling and prediction of behaviour, location, health, interests or reliability;
2. decisions made about individuals by automated means that have legal or similarly significant effects;
3. systematic monitoring of individuals, including monitoring of a publicly accessible area, employee monitoring and tracking of location or online behaviour;
4. special categories of data, criminal offence data or data of a highly personal nature such as financial detail or private communications;
5. processing on a large scale, judged by the number of individuals, the volume and range of data, the duration and the geographical extent;
6. matching or combining data sets from different sources or collected for different purposes;
7. data about individuals who may be vulnerable or have little choice, including children, patients, employees and applicants;
8. use of new or innovative technology, including machine learning, biometrics, connected devices and AI features;
9. processing that could deny individuals a service, a contract, a benefit or access, or could lead to discrimination, exclusion or physical harm;
10. data obtained without the individuals' direct involvement where a notice is impractical;
11. transfer of personal data outside the region where [Organisation] is established;
12. any processing type that the supervisory authority has listed as requiring an assessment, as recorded in GOV-REG-04.

4.2 **Screening decision.** Within five working days the Privacy Officer records the outcome in PIMS-REG-08. A full assessment is required when two or more triggers apply, when trigger 2, 4 or 12 applies on its own, or when the Privacy Officer judges any single trigger to carry a high risk. A decision that no assessment is required is recorded with reasons, and the processing still passes the privacy by design review in PIMS-PRO-06.

4.3 **Stage gates.** A required assessment advances through four gates, each recorded in PIMS-REG-08: gate 1, description and necessity complete before build starts; gate 2, risks scored and measures agreed before the go-live gate in PB-07; gate 3, residual risk approved before any personal data is processed in production; gate 4, review at the interval in step 4.11. A project does not pass a gate on a promise; a measure not yet built is a To confirm item with an owner and a due date.

4.4 **Description of the processing.** The Processing Owner completes section 2 of PIMS-TPL-01: nature (how data is collected, used, stored, shared and deleted, with a data flow referenced in GOV-REG-25 or GDPR-REG-02), scope (data items, special categories, volume, individuals, retention, geography), context (relationship with the individuals, their expectations, prior concerns, technology novelty) and purposes (the benefit to [Organisation], to the individuals and to others).

4.5 **Necessity and proportionality.** The Processing Owner and the Privacy Officer record in section 3 why the purpose cannot be achieved with less data or less intrusion, the lawful basis, how each principle in PIMS-POL-01 is met, the alternatives considered and rejected, how individuals are informed and how they exercise rights, the processors involved and the transfer mechanism.

4.6 **Consultation.** The Privacy Officer decides who is consulted and records it in section 4: the Information Security Manager always; the individuals or their representatives, through user research, a survey, a works council or a client advisory group, unless the Privacy Officer records why that is not practicable; processors, for the measures they operate; and the legal adviser where the lawful basis or a transfer is in question. Views received, and whether they changed the design, are recorded.

4.7 **Identifying risks to individuals.** The project team lists risks from the individual's point of view, not the organisation's: loss of control over their data, unauthorised disclosure, re-identification, inaccurate data leading to a wrong decision, discrimination, financial loss, identity theft, reputational damage, physical danger, loss of a service, distress, and inability to exercise rights. Each risk names its source (an event, an actor or a design weakness).

4.8 **Scoring.** Each risk is scored on the 1 to 5 likelihood scale in GOV-PRO-05 and on a severity scale for individuals: 1 negligible (inconvenience, easily overcome); 2 limited (annoyance, minor cost, short-lived); 3 significant (real difficulty, financial loss, distress, recoverable with effort); 4 severe (lasting harm, serious financial or psychological consequence, hard to recover from); 5 critical (danger to life, irreversible harm, loss of liberty). Score is likelihood multiplied by severity, banded as in GOV-PRO-05: 1 to 4 low, 5 to 9 medium, 10 to 15 high, 16 to 25 critical.

4.9 **Measures and residual risk.** For every risk at medium or above the team records the measures that remove the source, reduce likelihood or reduce severity (less data, pseudonymisation, encryption, access limits, shorter retention, transparency, human review, opt-out, contractual terms), the owner and the date. The risk is re-scored after the measures. Every measure becomes a backlog item or a contract clause, and every medium or higher residual risk also appears in GOV-REG-05 with a cross-reference to the assessment.

4.10 **Approval of residual risk.** Residual low or medium is approved by the Processing Owner with the Privacy Officer's written agreement. Residual high is approved only by the Chief Executive Officer after written advice from the Privacy Officer, and is reviewed every six months. Residual critical is not approved; the processing is redesigned or abandoned. The approval, the approver and the date are recorded in section 7 of PIMS-TPL-01 and in PIMS-REG-08.

4.11 **Prior consultation with the supervisory authority.** Where a residual high risk cannot be reduced further, the Privacy Officer prepares a consultation containing the assessment, the roles of the parties, the purposes, the measures and the Privacy Officer's contact details, and submits it to the authority. The processing does not start until the authority responds or the period set by law expires without a response. The Chief Executive Officer decides whether to consult or to abandon the processing.

4.12 **Review.** The Processing Owner reviews a completed assessment annually where residual risk is high, every two years otherwise, and immediately when a change in step 2 occurs, a breach affects the processing, a complaint is received about it, or the law or authority guidance changes. The review outcome is recorded even when nothing changes.

4.13 **Processor assistance.** Where [Organisation] is a processor, the Processing Owner supplies the controller, within the time in the agreement, with the description of the processing, the security measures and the sub-processors involved, and implements the measures the controller's assessment requires.

## 5. Records and evidence

- PIMS-REG-08 DPIA register: every screening outcome and every assessment with its gate dates, residual rating, approver and next review.
- Completed PIMS-TPL-01 documents, stored with the project record and retained for the life of the processing plus the period in PIMS-REG-07.
- GOV-REG-05 entries for medium and higher residual risks; backlog items and contract clauses for measures.
- Consultation records and any correspondence with the supervisory authority.

## 6. Exceptions

An activity may start before gate 3 only in a declared Severity 1 or 2 incident under GOV-PRO-07 where the processing is needed to contain harm, and then only with the Privacy Officer's recorded agreement; the assessment is completed within ten working days afterwards. No other exception applies.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after any prior consultation, after new authority guidance on assessments, and after an audit finding. Changes follow GOV-PRO-01.

## 8. Related documents

- PIMS-TPL-01 Data protection impact assessment template
- PIMS-REG-08 DPIA register
- PIMS-POL-01 Privacy information management policy
- PIMS-PRO-06 Privacy by design and by default procedure
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
- GOV-REG-25 Data flow and interface inventory
- GDPR-REG-02 Data flow and transfer map
- PB-07 Playbook: the go-live security and privacy gate for a software project
- AI-PRO-01 AI risk assessment procedure
