---
id: PIMS-TPL-01
title: Data protection impact assessment template
type: template
framework: iso27701
maps:
  - GDPR Article 35
  - ISO/IEC 27701 clause 7.2.5
  - ISO/IEC 27701 Annex A 7.2.5
owner: Privacy Officer
approver: Privacy Officer
classification: Confidential
review: Annual
summary: The form used under PIMS-PRO-02 to screen a processing activity, describe it, test its necessity, record consultation, score the risks to individuals before and after measures, and obtain approval of the residual risk.
---
*Guidance notes are in italics. One assessment per processing activity or project. The reference is assigned by the Privacy Officer from PIMS-REG-08. Complete section 1 at concept stage; the remaining sections only when section 1 results in "assessment required". Write for a reader who was not in the project: an auditor or the supervisory authority may read this document.*

## 1. Screening

| Field | Entry |
|---|---|
| **Assessment reference** | [DPIA ID from PIMS-REG-08] |
| **Processing activity** | [Name], PIMS-REG-01 reference [Processing ID] |
| **Project or system** | [System name] |
| **Processing Owner** | [Name], [Role] |
| **Date of screening** | [Date] |
| **Role of [Organisation]** | [Controller, Joint controller, Processor], decided under PIMS-PRO-01 |

| Trigger | Applies? | Justification |
|---|---|---|
| 1. Evaluation, scoring or profiling of individuals | [Yes or No] | |
| 2. Automated decisions with legal or similarly significant effect | [Yes or No] | |
| 3. Systematic monitoring, tracking or surveillance | [Yes or No] | |
| 4. Special categories, criminal offence data or highly personal data | [Yes or No] | |
| 5. Large scale processing | [Yes or No] | |
| 6. Matching or combining data sets | [Yes or No] | |
| 7. Vulnerable individuals or individuals with little choice | [Yes or No] | |
| 8. New or innovative technology, including AI features | [Yes or No] | |
| 9. Could deny a service, benefit or access, or cause discrimination | [Yes or No] | |
| 10. Data obtained without the individuals' involvement | [Yes or No] | |
| 11. Transfer outside the region of establishment | [Yes or No] | |
| 12. Listed by the supervisory authority as requiring an assessment | [Yes or No] | |

| Field | Entry |
|---|---|
| **Screening outcome** | [Assessment required, Assessment not required] |
| **Reasons** | *Apply the rule in PIMS-PRO-02 step 4.2. If not required, state why the risk is low and which review under PIMS-PRO-06 still applies.* |
| **Decided by** | Privacy Officer, [Date] |

## 2. Description of the processing

*Describe what will actually happen to the data. Reference a data flow in GOV-REG-25 or GDPR-REG-02 rather than drawing a new one here.*

| Aspect | Description |
|---|---|
| **Purposes** | *Each purpose in one sentence, and the benefit to [Organisation], to the individuals and to any third party.* |
| **Nature** | *How data is collected, used, stored, shared and deleted. Who has access. Which processors and systems are involved.* |
| **Data items** | *List each field or category. Mark special categories and identifiers.* |
| **Individuals** | *Who they are, approximately how many, and the relationship to [Organisation].* |
| **Scale and duration** | *Volume, frequency, retention period from PIMS-REG-07, and geographical extent.* |
| **Context** | *What individuals would reasonably expect. Prior complaints or concerns about similar processing. Any imbalance of power. Novelty of the technology.* |
| **Recipients and transfers** | *Internal teams, processors (PIMS-REG-06 references), other controllers, and any destination outside the region with its PIMS-REG-05 reference.* |
| **Technology** | *Systems, hosting, any machine learning or AI component (AI-REG-01 reference), any tracking technology (GDPR-REG-04 reference).* |

## 3. Necessity and proportionality

| Question | Answer |
|---|---|
| **Lawful basis** | *The basis for each purpose; for legitimate interests attach GDPR-TPL-07; for consent describe the capture under PIMS-PRO-05.* |
| **Does the processing achieve the purpose?** | *Evidence that it works, not an assumption.* |
| **Is there a less intrusive way?** | *Alternatives considered: less data, aggregated or pseudonymised data, shorter retention, opt-in design. Why each was rejected.* |
| **Minimisation** | *Which data items were removed during design. Why each remaining item is needed.* |
| **Accuracy** | *How data is kept accurate and how errors are corrected.* |
| **Retention** | *Period, trigger and how deletion is configured, with the PIMS-REG-07 reference.* |
| **Transparency** | *Which notice tells individuals, when they see it, and what changed in it for this processing.* |
| **Rights** | *How access, rectification, erasure, restriction, portability and objection are supported in the system, and how automated decisions can be contested.* |
| **Processors** | *Terms signed based on PIMS-TPL-02 and the PIMS-REG-06 references.* |
| **International transfers** | *Mechanism and transfer impact assessment reference under PIMS-POL-03.* |

## 4. Consultation

| Who | When and how | What they said | Response |
|---|---|---|---|
| Privacy Officer | | | |
| Information Security Manager | | | |
| Individuals or their representatives | *Or the reason it was not practicable.* | | |
| Processors | | | |
| Legal adviser | | | |
| Others, for example works council | | | |

## 5. Risks to individuals

*Write each risk from the individual's point of view. Score likelihood 1 to 5 and severity 1 to 5 as defined in PIMS-PRO-02 step 4.8. Score is likelihood multiplied by severity. Bands: 1 to 4 low, 5 to 9 medium, 10 to 15 high, 16 to 25 critical.*

| ID | Risk to individuals and its source | Likelihood | Severity | Score and band |
|---|---|---|---|---|
| R1 | | | | |
| R2 | | | | |
| R3 | | | | |
| R4 | | | | |

## 6. Measures and residual risk

*One row per risk at medium or above. Each measure has an owner and a due date and exists as a backlog item, a configuration, a contract clause or a procedure. A measure not yet in place is To confirm until evidence is attached.*

| ID | Measures, owner and status | Residual likelihood | Residual severity | Residual score and band |
|---|---|---|---|---|
| R1 | | | | |
| R2 | | | | |
| R3 | | | | |
| R4 | | | | |

| Field | Entry |
|---|---|
| **Highest residual band** | [Low, Medium, High, Critical] |
| **GOV-REG-05 references** | *For every medium or higher residual risk.* |
| **Prior consultation required?** | [Yes or No]. *Yes when a high residual risk cannot be reduced further; see PIMS-PRO-02 step 4.11.* |

## 7. Approval and sign-off

| Field | Entry |
|---|---|
| **Privacy Officer's advice** | *Proceed, proceed with conditions, or do not proceed, with reasons. Conditions are listed with owners and dates.* |
| **Advice accepted?** | [Yes or No]. *If No, the reasons for departing from the advice are recorded here and reported at the next management review.* |
| **Approver** | *Processing Owner for low or medium residual; Chief Executive Officer for high residual.* [Name], [Role] |
| **Decision** | [Approved, Approved with conditions, Not approved] |
| **Date** | [Date] |
| **Signature** | [Signature] |
| **PIMS-REG-08 status set to** | [Approved, Prior consultation, Rejected] |

## 8. Review log

| Date | Reviewer | Trigger | Outcome |
|---|---|---|---|
| [Date] | [Role] | [Scheduled, Change, Breach, Complaint, Guidance] | *No change, or a summary of what changed and which sections were updated.* |

## 9. Related documents

- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-REG-08 DPIA register
- PIMS-REG-01 Personal data processing inventory
- PIMS-PRO-06 Privacy by design and by default procedure
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
- GDPR-TPL-07 Legitimate interests assessment template
- GDPR-TPL-08 Transfer impact assessment template
