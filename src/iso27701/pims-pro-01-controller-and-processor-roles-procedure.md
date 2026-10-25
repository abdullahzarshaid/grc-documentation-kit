---
id: PIMS-PRO-01
title: Determining controller and processor roles
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 5.2.1
  - ISO/IEC 27701 clause 7.2.6
  - ISO/IEC 27701 clause 7.2.7
  - ISO/IEC 27701 clause 8.2.1
  - ISO/IEC 27701 Annex A 7.2.7
  - ISO/IEC 27701 Annex B 8.2.1
  - GDPR Article 4
  - GDPR Article 26
  - GDPR Article 28
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The test applied to every processing activity and every counterparty to decide whether [Organisation] acts as controller, joint controller or processor, how the decision is recorded, and what obligations follow from it.
---
## 1. Purpose

This procedure makes the role decision explicit and recorded, because the role decides which obligations apply: a controller answers to individuals and the supervisory authority for the whole processing, a processor answers to the controller for following instructions, and joint controllers must agree who does what. Getting the role wrong leaves obligations unowned.

## 2. Scope

It applies to every processing activity in PIMS-REG-01, every supplier that receives personal data, every client contract under which [Organisation] receives personal data, every group company arrangement and every data sharing agreement, from the first proposal until the processing ends.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Runs the test, records the decision and its reasoning, decides disputed cases with the legal adviser, and re-assesses on change. |
| Processing Owner | Supplies the facts about who decided the processing, its purpose and its means, and applies the resulting obligations. |
| Supplier owner | Raises the test for every new supplier under GOV-PRO-06 before personal data is shared. |
| Sales or account lead | Raises the test for every client contract that involves personal data before signature. |
| Legal adviser | Confirms contract wording matches the decided role. |

## 4. Procedure

4.1 **Trigger.** The Processing Owner, supplier owner or account lead asks the Privacy Officer for a role decision when a processing activity is proposed, when a supplier or client arrangement involving personal data is proposed, when the purpose or the parties of an existing activity change, and at the annual review of PIMS-REG-01. No personal data flows under a new arrangement until the decision is recorded.

4.2 **Facts gathered.** The requester provides, in writing: the parties involved, who initiated the processing, what each party gets out of it, which party chose the data items, the individuals concerned, the retention period and the recipients, which party could stop the processing, and whether any party may use the data for anything of its own.

4.3 **The decision test.** The Privacy Officer answers five questions for each party.

| Question | Points to controller | Points to processor |
|---|---|---|
| Why does the processing happen? | The party decided it should happen for its own ends | The party does it only because another party engaged it |
| Who decides the purpose? | The party sets or shares the purpose | The purpose is set entirely by the other party |
| Who decides the essential means? | The party decides which data, which individuals, how long and who receives | The party decides only technical or organisational detail within instructions |
| Does the party gain beyond a fee? | Yes, a commercial, legal or operational benefit of its own | No, it is paid for the service and nothing more |
| Could the party use the data for anything else? | Yes, or it already does | No, contract and practice forbid it |

Three or more answers in the controller column make the party a controller. A party that decides the purpose is always a controller, however the other answers fall. A party that processes only within another party's documented instructions, decides nothing essential and gains nothing beyond its fee is a processor.

4.4 **Joint controllership.** Where two or more parties are controllers of the same processing, the Privacy Officer asks whether they decided the purposes and means together, including the case where each party's decision depends on the other's so that the processing could not happen without both. If so they are joint controllers and an arrangement is required. If each party pursues its own purpose with its own means on the same data, they are independent controllers and a data sharing agreement is used instead.

4.5 **Recurring cases.** The Privacy Officer applies the test, not a label, but records the usual outcome for recurring patterns in a short table kept with this procedure: cloud hosting and software providers acting on instruction (processor); payroll providers and benefits administrators (usually processor); professional advisers, auditors and regulators using data for their own professional duties (controller); payment and banking services (usually controller); staff augmentation working under [Organisation]'s direction (part of [Organisation], not a separate party); a group company providing a shared service to other group companies (processor for that service); a client that sends personal data for [Organisation] to deliver a service (client is controller, [Organisation] is processor); a client that buys data [Organisation] collected for its own purposes (both controllers). A pattern never overrides facts that point the other way.

4.6 **Documenting the decision.** The Privacy Officer records in PIMS-REG-01 the role for each processing activity and, in a note on the row, the reasoning in no more than three sentences and the date. For a supplier the role is also recorded in PIMS-REG-06 and the processor terms flag in GOV-REG-07. For a client contract the role is recorded in the contract summary held by the account lead and in PIMS-REG-01.

4.7 **Consequences for [Organisation] as controller.** The Processing Owner applies the full set: a lawful basis and a notice (PIMS-PRO-05), inventory entry (PIMS-REG-01), impact assessment screening (PIMS-PRO-02), rights handling (PIMS-PRO-03), breach notification to the authority and individuals (PIMS-PRO-04), processor terms with every processor (PIMS-TPL-02), transfer mechanisms (PIMS-POL-03) and retention (PIMS-POL-02).

4.8 **Consequences for [Organisation] as processor.** The Processing Owner applies: processing only on the controller's documented instructions and flagging any instruction that appears unlawful; confidentiality commitments from staff; the security measures in the agreement; no sub-processor without the controller's authorisation and no change without notice (PIMS-REG-06); assistance with rights requests, security, breaches and assessments; notification of breaches to the controller without undue delay (PIMS-PRO-04); deletion or return at the end of the service; processor records in PIMS-REG-01; and making information available for the controller's audits. [Organisation] does not use the data for its own purposes, including product improvement, analytics or marketing, unless the agreement allows it and [Organisation] becomes a controller for that use.

4.9 **Consequences for joint controllers.** The Privacy Officer agrees a written arrangement with the other controllers that allocates the notice, the rights handling, the breach notification, the contact point for individuals and the record keeping, and makes the essence of the arrangement available to individuals through the notice. Each controller remains answerable to individuals regardless of the allocation.

4.10 **Contract alignment.** The legal adviser confirms before signature that the contract wording matches the decided role: processor terms based on PIMS-TPL-02 for a processor, a joint controller arrangement for joint controllers, a data sharing agreement for independent controllers. A contract that labels a party a processor while the facts make it a controller is corrected, not signed.

4.11 **Disputed cases.** Where the counterparty disagrees with the role decision, the Privacy Officer records both positions and the reasons, and the legal adviser decides. Until the dispute is settled, [Organisation] applies the controller obligations, which are the wider set.

4.12 **Re-assessment.** The decision is re-assessed when the purpose, the parties, the data items or the benefit to any party changes, when a processor starts using data for its own ends, and at the annual inventory review under GDPR-PRO-01. A changed decision is recorded with the date and triggers a contract review within thirty days.

## 5. Records and evidence

- PIMS-REG-01 Personal data processing inventory: the role column and the reasoning note on each row.
- PIMS-REG-06 Processor and sub-processor register and GOV-REG-07 Supplier register entries.
- Signed processor terms, joint controller arrangements and data sharing agreements.
- The recurring-case table kept with this procedure, with the date of its last review.

## 6. Exceptions

No exception applies. A processing activity without a recorded role is not started, and an existing one found without a role is assessed within five working days of discovery.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after guidance from a supervisory authority or a court decision that changes how roles are assessed, and after any dispute under step 4.11. Changes follow GOV-PRO-01.

## 8. Related documents

- PIMS-POL-01 Privacy information management policy
- PIMS-REG-01 Personal data processing inventory
- PIMS-REG-06 Processor and sub-processor register
- PIMS-TPL-02 Data processing agreement template
- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-07 Supplier register
- GDPR-PRO-01 Data mapping and records of processing procedure
- GDPR-TPL-09 Supplier GDPR assessment questionnaire
