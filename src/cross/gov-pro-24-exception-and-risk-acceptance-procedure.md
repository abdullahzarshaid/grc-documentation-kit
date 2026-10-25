---
id: GOV-PRO-24
title: Exception and risk acceptance procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 8.3
  - SOC 2 CC3.2
  - SOC 2 CC5.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How a deviation from a policy or control, or the acceptance of a risk above appetite, is requested, assessed, limited in time, approved by the right authority, recorded and reviewed before it expires.
---
## 1. Purpose

Controls sometimes cannot be applied as written, and some risks cannot be treated at once. This procedure makes every such case visible, time-limited and owned, so that an exception is a recorded decision rather than a quiet gap.

## 2. Scope

It applies to any request to deviate from a policy, procedure or control in the management system, and to any acceptance of a residual risk in the High or Critical band under GOV-PRO-05. It does not cover changes to the documents themselves, which follow GOV-PRO-01, or changes to systems, which follow GOV-PRO-09.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Requester | The manager responsible for the system or process. Completes GOV-TPL-06, implements compensating controls, closes or renews before expiry. |
| Information Security Manager | Assesses the request, rates the risk, records it in GOV-REG-06, runs the expiry review, approves Low and Medium band requests. |
| Privacy Officer | Co-assesses any request involving personal data. |
| Executive sponsor | Approves High band requests. |
| Chief Executive Officer | Approves Critical band requests. |
| Internal Auditor | Samples GOV-REG-06 at each audit for expired or unreviewed entries. |

## 4. Procedure

4.1 **When an exception is required.** A requester raises an exception before a control is bypassed, a policy statement is not followed, or a High or Critical risk is left untreated. A deviation discovered after the fact is logged as a nonconformity under GOV-PRO-04 and may then be regularised through this procedure.

4.2 **Request.** The requester completes GOV-TPL-06 with the requirement being deviated from, the systems and data affected, the business reason, the compensating controls proposed, the duration requested and the plan for returning to full conformity. A request without a return plan is accepted only as a risk acceptance, not as an exception.

4.3 **Assessment.** Within five working days the Information Security Manager, with the Privacy Officer where personal data is involved, rates the risk using the scales in GOV-PRO-05 twice: once as it would stand without the compensating controls and once with them in place. Both bands are recorded on the form. The Information Security Manager also checks whether the deviation breaches an obligation in GOV-REG-04 or a customer commitment, in which case the request is refused unless the customer or regulator has agreed in writing.

4.4 **Compensating controls.** The requester implements the compensating controls and shows evidence that they operate before approval is given. A compensating control must reduce the band of the risk; a control that merely detects the problem after the fact is recorded as such and does not count as a band reduction unless detection leads to a response within a defined time.

4.5 **Time limit.** An exception or acceptance is granted for a fixed period of no more than twelve months. A Critical band acceptance is granted for no more than ninety days. There is no automatic renewal.

4.6 **Approval.** The authority for the band after compensating controls approves or refuses the request in writing on GOV-TPL-06.

| Band after compensating controls | Approver |
|---|---|
| Low | Information Security Manager |
| Medium | Information Security Manager and the requester's head of function |
| High | Executive sponsor |
| Critical | Chief Executive Officer |

4.7 **Register entry.** On approval the Information Security Manager enters the exception in GOV-REG-06 with its reference, type, linked risk ID, bands before and after, approver, approval date, duration and expiry date, and sets the status to Active. The linked entry in GOV-REG-05 is updated to show the acceptance and the review date. The requester informs the owners of the affected controls.

4.8 **Expiry review.** Thirty days before expiry the Information Security Manager notifies the requester. The requester then does one of three things: closes the exception because the control is now implemented, with evidence; submits a new request under 4.2 with a fresh assessment; or escalates to the approver with the reason the return plan has slipped. An exception that reaches its expiry date without one of these outcomes is set to Expired, reported to the steering committee at its next meeting, and treated as a nonconformity under GOV-PRO-04.

4.9 **Early review.** An active exception is reassessed before expiry when the affected system changes materially, an incident touches it, or a related audit finding is raised.

4.10 **Quarterly reporting.** The Information Security Manager reports the number of active, expiring and expired exceptions by band to the steering committee each quarter and to management review.

## 5. Records and evidence

- GOV-TPL-06 Risk acceptance and exception forms, signed by the approver.
- GOV-REG-06 Risk acceptance and exception register, showing status and expiry for every entry.
- Evidence that compensating controls operate.
- Steering committee minutes recording expired exceptions.

## 6. Exceptions

This procedure has no exceptions. An urgent operational need is handled as an emergency change under GOV-PRO-09, followed by a request under 4.2 within five working days.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding about exceptions or risk acceptance. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-06 Risk acceptance and exception form
- GOV-REG-06 Risk acceptance and exception register
- GOV-REG-05 Information security risk register
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-09 Change management procedure
- GOV-REG-04 Legal, regulatory and contractual register
