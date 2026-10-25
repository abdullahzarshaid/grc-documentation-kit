---
id: GOV-TPL-06
title: Risk acceptance and exception form
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 8.3
  - SOC 2 CC3.2
  - SOC 2 CC5.1
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: The form used under GOV-PRO-24 to request a deviation from a policy or control, or the acceptance of a risk above appetite, showing the risk before and after compensating controls, the duration, the approver for the band and the review date.
---
*Guidance notes are in italics. One form per exception or acceptance. The Information Security Manager assigns the reference from GOV-REG-06. Approval is valid only with the signature of the approver for the band after compensating controls.*

## 1. Request

| Field | Entry |
|---|---|
| **Reference** | [Reference from GOV-REG-06] |
| **Type** | [Exception from a policy or control, Acceptance of a risk above appetite] |
| **Requested by** | [Name], [Role] |
| **Date of request** | [Date] |
| **Requirement deviated from** | *Document ID and statement or step, for example GOV-POL-06 statement 4.4, or Annex A control reference.* |
| **Linked risk** | [GOV-REG-05 risk ID], or "new risk to be created" |
| **Systems, data and processes affected** | [Text] |
| **Personal data affected** | [Yes or No]. *If Yes, the Privacy Officer co-assesses.* |
| **Customer or legal obligation affected** | [Yes or No]. *If Yes, reference the GOV-REG-04 row and attach the written agreement of the customer or regulator.* |
| **Business reason** | *Why the requirement cannot be met now. State the cost or consequence of full conformity.* |
| **Compensating controls proposed** | *Each control, who operates it, and the evidence that it is in place. Detective controls count only if they lead to a response within a stated time.* |
| **Duration requested** | [Number] months. *Maximum twelve. Maximum three for a Critical band.* |
| **Return to conformity plan** | *The actions and dates that will remove the need for the exception. A request without a plan can only be a risk acceptance.* |

## 2. Assessment

*Completed by the Information Security Manager, with the Privacy Officer where personal data is affected, within five working days, using the scales in GOV-PRO-05.*

| Field | Without compensating controls | With compensating controls |
|---|---|---|
| Likelihood (1 to 5) | [Number] | [Number] |
| Impact (1 to 5) | [Number] | [Number] |
| Score | [Number] | [Number] |
| Band | [Low, Medium, High, Critical] | [Low, Medium, High, Critical] |

| Field | Entry |
|---|---|
| **Assessor** | [Name], [Role] |
| **Assessment date** | [Date] |
| **Compensating controls verified as operating** | [Yes or No], evidence reference |
| **Assessor's recommendation** | [Approve, Approve with conditions, Refuse], with reasons |
| **Conditions** | [Text or "none"] |

## 3. Approval

*The approver is determined by the band with compensating controls: Low, Information Security Manager; Medium, Information Security Manager and the requester's head of function; High, executive sponsor; Critical, Chief Executive Officer.*

| Field | Entry |
|---|---|
| **Decision** | [Approved, Refused] |
| **Approver** | [Name], [Role] |
| **Second approver (Medium band)** | [Name], [Role] or "not required" |
| **Approval date** | [Date] |
| **Expiry date** | [Date]. *Approval date plus duration; never more than twelve months.* |
| **Review date** | [Date]. *Thirty days before expiry.* |
| **Signature** | [Signature] |

## 4. Review and closure

| Field | Entry |
|---|---|
| **Review performed by** | [Name], [Role] |
| **Review date** | [Date] |
| **Outcome** | [Closed: control implemented, Renewed: new request reference, Escalated: reason, Expired] |
| **Evidence of closure** | [Reference] |
| **GOV-REG-06 status set to** | [Closed, Expired, Active under new reference] |
| **Signature** | [Signature] |

## 5. Related documents

- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-REG-06 Risk acceptance and exception register
- GOV-REG-05 Information security risk register
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-04 Legal, regulatory and contractual register
