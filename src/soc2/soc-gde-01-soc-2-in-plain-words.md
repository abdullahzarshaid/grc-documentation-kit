---
id: SOC-GDE-01
title: "Guide: SOC 2 in plain words"
type: guide
framework: soc2
maps:
  - SOC 2 CC1.1
  - SOC 2 CC2.3
  - SOC 2 CC4.1
  - SOC 2 CC9.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: What a SOC 2 report is and is not, the difference between Type 1 and Type 2, the five categories, how criteria, controls and tests relate, and the parts of the process that surprise organisations the first time, written for a reader who has to run one.
---
## 1. What a SOC 2 report is

A SOC 2 report is an independent auditor's opinion on whether a service organisation's controls are suitably designed, and for a Type 2 report whether they operated effectively over a period, to meet a published set of criteria called the Trust Services Criteria. The criteria are issued by the American Institute of Certified Public Accountants. The opinion is signed by a licensed public accounting firm, not by a certification body, and it is addressed to the organisation's customers and their auditors, who use it to decide how much they can rely on the organisation's controls without testing them themselves.

Three things follow from that. SOC 2 is an attestation, not a certification: there is no certificate, no register of certified organisations and no "SOC 2 compliant" status in law. The report is the deliverable, and it is a restricted-use document shared with customers under a non-disclosure agreement, not published. And the controls are the organisation's own: the criteria say what outcome must be achieved; [Organisation] decides how, writes its controls down in SOC-REG-01, and the auditor tests those.

## 2. Type 1 and Type 2

A Type 1 report gives an opinion on the design of controls at a single date: were the controls in place and capable of meeting the criteria on that day. A Type 2 report gives an opinion on design and on operating effectiveness across a period, usually between three and twelve months, by testing samples of the controls' records from inside that period.

Customers almost always want a Type 2. A Type 1 is still useful as a milestone: it proves the control set is complete and designed well before the clock starts, and it gives sales teams something to show while the first period runs. PB-03 treats the Type 1 as the day 90 outcome and the Type 2 as what follows the observation period. An organisation that skips the Type 1 saves money and loses an early warning.

## 3. The five categories

The criteria are grouped into five categories. Security is mandatory and is made up of the common criteria, CC1 to CC9, which cover the control environment, communication, risk assessment, monitoring, control activities, logical and physical access, system operations, change management and risk mitigation including vendors. The other four are added when a service makes commitments in that area.

| Category | Criteria | Add it when |
|---|---|---|
| Security (common criteria) | CC1.1 to CC9.2 | Always. Every SOC 2 report includes it. |
| Availability | A1.1 to A1.3 | Contracts promise uptime, recovery times or capacity. |
| Processing integrity | PI1.1 to PI1.5 | The service transforms, calculates or delivers data and customers rely on the result being complete and accurate. |
| Confidentiality | C1.1, C1.2 | Customers give the organisation information they require to be protected and destroyed on terms. |
| Privacy | P1.1 to P8.1 | The organisation collects or processes personal information under its own privacy commitments, usually as a controller. |

Choose categories by the commitments [Organisation] has actually made in contracts and service descriptions, not by ambition. Every added category adds controls, evidence and testing. A processor that handles personal data on customers' instructions usually covers that through Confidentiality and the security criteria, with privacy law met through the PIMS and GDPR documents in this kit, rather than adding the Privacy category.

## 4. Criteria, controls and tests

The three words are used loosely and the confusion costs time.

- A criterion is an outcome the auditor must conclude on, for example that access is removed when no longer needed (CC6.2 in theme). The criteria are fixed and the same for every organisation.
- A control is something [Organisation] does, written as an object and a state that can be checked: "quarterly access reviews completed and signed off for every in-scope system". One criterion usually needs several controls, and one control often serves several criteria. The controls live in SOC-REG-01.
- A test is what the auditor does to a control: inspects a sample of access reviews, re-performs a calculation, observes a process, asks a person. The organisation's own version of the tests, run during the period, is SOC-PRO-01.

The auditor's report lists the controls and the tests side by side with the results. If a control is written vaguely ("access is managed appropriately") there is nothing to test, and the auditor will either rewrite it with you or report it as not testable.

## 5. Points of focus

Each criterion comes with points of focus: considerations that illustrate what the criterion is getting at. They are not requirements and the auditor does not issue an opinion on each one. Use them in two ways. When writing controls, read the points of focus for a criterion and check that the control set covers the themes they raise; a theme with no control is a gap to explain. When a point of focus does not apply (a cloud-only organisation and physical data centres, for example), say so in SOC-REG-01 so the auditor does not ask.

## 6. The audit period

For a Type 2, evidence must come from inside the period. A control that started operating in month four of a twelve month period is reported as operating for nine months, and the auditor's opinion will say so. A control that has no records for a month, because the person who ran it was on leave and nobody covered, is a gap in that month whether or not anything went wrong.

Periods run consecutively: the next report's period starts the day after the previous one ended, so that a customer reading two reports sees no uncovered time. Between the period end and the report's issue, and between reports, customers may ask for a bridge letter, a short statement from management that nothing material has changed. SOC-PRO-02 explains the same letter from the other side, when [Organisation] receives one from a supplier.

Most organisations choose a first period of three to six months to get a report into customers' hands, then move to twelve month periods aligned to the financial year.

## 7. Sampling

The auditor does not test every occurrence of a control. For each control they define the population, every occurrence in the period, and select a sample whose size depends on how often the control runs. Monthly controls might see three items tested, weekly five, daily twenty or more; the auditor's own table governs, and SOC-PRO-01 section 4.4 gives [Organisation]'s internal equivalent.

Two practical consequences. The auditor chooses the items, not the organisation, so there is no value in preparing beautiful examples; prepare complete populations as system exports instead. And a population must be complete: if the leaver list from the people system shows fourteen leavers and the identity provider shows sixteen accounts disabled, the auditor will ask about the two, and the answer had better be in a record.

## 8. Exceptions

An exception is a tested item that did not meet the control: a leaver whose access was removed in nine days instead of five, a change ticket with no approval. The auditor reports every exception with management's response. One isolated exception with a documented cause and a fix rarely affects the opinion. A pattern of exceptions in one control may lead the auditor to conclude the control did not operate effectively, which appears in the opinion as a qualification: the opinion holds except for that control and the criteria it serves. Customers read qualifications closely.

Handle an exception the way SOC-PRO-01 section 4.8 describes: classify it, find the cause, fix it, and show the fix operating. An exception found by [Organisation] in its own testing and corrected before the auditor arrives is reported as a corrected deviation; the same exception found first by the auditor is a surprise. Both are better than a hidden one, which becomes a question of integrity rather than of control.

## 9. The report's sections

A SOC 2 report has a fixed shape, and knowing it helps both in writing [Organisation]'s own and in reading a supplier's.

| Section | Written by | Contains |
|---|---|---|
| Independent auditor's report | The auditor | The opinion, the scope, the period, the categories, the responsibilities of each party, any qualifications. |
| Management's assertion | [Organisation] | A signed statement that the description is fair and the controls were designed and operated effectively. |
| System description | [Organisation] | What the service is, its components, boundaries, commitments, changes and incidents in the period, subservice organisations and complementary user entity controls. SOC-TPL-01 is the template. |
| Criteria, controls, tests and results | The auditor, from [Organisation]'s control list | One row per control: the criteria it serves, the control text, the auditor's test, the result including exceptions. |
| Other information | [Organisation] | Anything management wants to add, such as responses to exceptions or future plans. The auditor does not opine on it. |

Readers go to the opinion first, then the exceptions, then the complementary user entity controls. Write the description knowing that.

## 10. Complementary user entity controls

Some criteria can only be met if the customer does its part: manages its own users in the service, keeps its own credentials secret, reviews the reports the service sends. The description lists these as complementary user entity controls. They are honest statements of shared responsibility, not disclaimers, and the auditor will check that each one is genuinely needed for a criterion.

The same mechanism applies in reverse. Every supplier report [Organisation] relies on lists user entity controls that [Organisation] must operate. SOC-PRO-02 section 4.6 maps each of them to a control in SOC-REG-01, because a supplier's assurance does not hold if the organisation ignores its side.

## 11. Subservice organisations

A subservice organisation is a supplier whose controls are necessary for [Organisation] to meet a criterion: typically the hosting provider, sometimes the identity provider, payment processor or managed security service. The description must name them and say how they are treated.

Under the carve-out method, the default, the supplier's controls are excluded from [Organisation]'s report. The description names the supplier, the services used, the criteria that depend on them, and the complementary subservice organisation controls that [Organisation] assumes the supplier operates. [Organisation] then monitors the supplier by reviewing its own SOC report under SOC-PRO-02. Under the inclusive method the supplier's controls are tested inside [Organisation]'s report, which needs the supplier's agreement, participation and its own management assertion; it is rare outside closely held group companies.

A supplier that is merely a vendor, whose failure would not by itself cause a criterion to fail, is handled under GOV-PRO-06 and CC9.2 and does not need to be in the description.

## 12. Who the auditor is

The opinion must be signed by a licensed public accounting firm that is independent of [Organisation] and subject to peer review of its attestation practice. The same firm cannot design the controls and then audit them; a firm that offers both services separates the teams and will say so in its engagement letter. A readiness consultant who helps write controls is not the auditor, and the auditor will test what the consultant wrote exactly as hard as anything else.

When choosing, ask: how many SOC 2 examinations the firm issued in the last year for organisations of [Organisation]'s size and technology; who will do the fieldwork and how senior they are; the firm's sample size table; whether evidence is collected through a portal or by request list; how exceptions are communicated and when; the timeline from period end to issued report; and the total cost for the readiness review, the Type 1 and the Type 2. Price varies with the number of categories, systems, locations and controls, and with how organised the evidence is. A tidy evidence folder built as PB-09 describes is the single largest cost reducer.

## 13. Common misunderstandings

| Belief | What is true |
|---|---|
| "We are SOC 2 certified." | There is no certification. [Organisation] has a SOC 2 report for a period, with an opinion that may be qualified. Say "we have a SOC 2 Type 2 report covering [period]". |
| "The auditor will tell us what controls to have." | The auditor tests the controls [Organisation] wrote. Readiness help is separate from the audit. |
| "Policies are evidence." | A policy proves a rule exists. Only records prove the rule was followed. |
| "We can fix it before the audit." | For a Type 2, a control fixed in month ten operated for two months. The period is the period. |
| "One exception fails the report." | One isolated, explained, corrected exception rarely affects the opinion. A pattern does. |
| "Our hosting provider's report covers us." | It covers the provider's controls. [Organisation]'s own access, change, incident and vendor controls are still tested, and the provider's user entity controls become [Organisation]'s controls. |
| "Privacy category means GDPR." | The Privacy criteria are a separate set of commitments. GDPR obligations are met through PIMS-POL-01, GDPR-POL-01 and their procedures whether or not the Privacy category is in scope. |
| "A screenshot is enough." | A screenshot that shows account, environment and date may be. A system export of the whole population is always better. |

## 14. Where to go next

Read PB-03 for the ninety day plan to the start of the observation period. Use SOC-REG-01 to write the control matrix, SOC-REG-03 to measure readiness, SOC-REG-02 to schedule the recurring evidence, SOC-TPL-01 to draft the description, SOC-PRO-01 to test the controls before the auditor does, SOC-PRO-02 for supplier reports, and SOC-GDE-02 for what the auditor will ask for and where in the kit each answer lives. SOC-GDE-03 maps every criterion to the kit documents that serve it.
