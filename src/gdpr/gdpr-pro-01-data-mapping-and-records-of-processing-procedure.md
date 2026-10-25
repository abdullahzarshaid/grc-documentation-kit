---
id: GDPR-PRO-01
title: Data mapping and records of processing procedure
type: procedure
framework: gdpr
maps:
  - GDPR Article 30
  - GDPR Article 5(2)
  - ISO/IEC 27701 clause 7.2.8
  - ISO/IEC 27701 Annex A 7.2.8
  - ISO/IEC 27001:2022 Annex A 5.9
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How the organisation discovers, records and keeps current every processing activity and every flow of personal data, so that PIMS-REG-01 and GDPR-REG-02 are a true record of processing at any moment.
---
## 1. Purpose

This procedure produces and maintains the two records that every other privacy process depends on: the processing inventory in PIMS-REG-01, which is the record of processing activities that GDPR Article 30 requires, and the flow and transfer map in GDPR-REG-02, which shows where each item of personal data comes from, where it goes and under what safeguard. Without them a request cannot be answered completely, a breach cannot be scoped, a retention rule cannot be applied and a notice cannot be accurate.

## 2. Scope

It applies to every function, system, service, supplier relationship and paper process in which [Organisation] processes personal data as a controller, joint controller or processor, including trials, internal tools, analytics, backups, support tooling and features that use machine learning.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Runs the procedure, facilitates the workshops, owns both registers, decides which activities are distinct, and signs the quarterly review. |
| Head of each function | Names a function representative, confirms the completeness of the function's rows once a year. |
| Function representative | Attends the workshop for their function, supplies the facts for each activity, and reports changes within the triggers in step 4.9. |
| System Owner | Confirms the systems, storage locations, retention settings and integrations for each flow that touches their system, and keeps the GDPR-REG-02 rows for those flows current. |
| Information Security Manager | Supplies the security measures column from the Statement of Applicability and the controls in GOV-REG-25. |
| Processor customers' contacts | Where [Organisation] is a processor, supply the categories and instructions needed for the processor rows. |

## 4. Procedure

4.1 **Plan the mapping round.** The Privacy Officer schedules one workshop per function (for example product, engineering, sales and marketing, customer support, people, finance) in the first mapping round, and one per changed function in later rounds. Each workshop has a function representative, the owners of the systems that function uses, and the Privacy Officer. The invitation lists the questions in step 4.3 so that representatives arrive with answers.

4.2 **Collect the system view first.** Before the workshop the Privacy Officer exports the asset list from GOV-REG-10, the supplier list from GOV-REG-07 and the interface list from GOV-REG-25, filters each to items that hold or move personal data, and brings the filtered lists to the workshop as a prompt. A system that holds personal data and appears in no activity is a gap to resolve in the workshop, not a line to delete.

4.3 **Identify activities.** In the workshop the Privacy Officer walks through what the function does to people, in the people's own terms: who they are (customers, users, staff, applicants, contacts, visitors), what happens to them (sign-up, billing, support, marketing, recruitment, monitoring), and why. Each distinct purpose with its own data set is one activity. Two purposes that use the same data are two activities. The same purpose across several systems is one activity with several systems. The test is whether a reader of the notice would recognise it as a separate thing the organisation does with their data.

4.4 **Record each activity.** For every activity the representative supplies, and the Privacy Officer records in PIMS-REG-01: the role of [Organisation] (controller, joint controller or processor, decided under PIMS-PRO-01); the purpose; the lawful basis, and the condition where special category or criminal offence data is involved; the categories of data subjects and of data; the source; the recipients, internal and external; whether data leaves the region and the safeguard; the retention period and trigger from PIMS-REG-07; the security measures by reference; the owner; and any DPIA reference from PIMS-REG-08. A row with any of these blank is marked Incomplete in its status and given an owner and a date.

4.5 **Trace the flows.** For every activity the System Owners trace the data from entry to deletion: the system or party it enters from, each system it is stored in or passed to, each third party it is sent to, and where backups and logs containing it are kept. Each hop is one row in GDPR-REG-02 with the data items that move, the direction, whether the destination is internal or external, the country, the transfer method, the safeguard, the controls on the hop (encryption, authentication, access restriction) and the owner. The team draws the flow as a simple diagram during the workshop and files the diagram against the activity in the evidence folder described in PB-09.

4.6 **Resolve the gaps the trace exposes.** Three findings are common and each has a fixed response. A flow to a supplier not in PIMS-REG-06 goes to the Privacy Officer, who starts GOV-PRO-06 and marks the flow Under review. A flow out of the region with no safeguard goes to PIMS-POL-03 and a GDPR-TPL-08 assessment, and the flow is suspended if it carries Restricted data. An activity with no lawful basis the representative can state is suspended until the Privacy Officer records one, or records the decision to stop the activity.

4.7 **Check against the external statements.** The Privacy Officer compares the completed rows with the current privacy notices built from GDPR-TPL-01, GDPR-TPL-02 and GDPR-TPL-03, the cookie inventory in GDPR-REG-04 and the customer-facing processing descriptions. Any activity, recipient, retention period or transfer in the registers that the notices do not describe is raised to PIMS-PRO-05 for a notice change, with the processing recorded as Partial in GDPR-REG-01 until the notice is published.

4.8 **Approve the round.** The head of each function confirms in writing that the rows for their function are complete and accurate. The Privacy Officer sets the status of each confirmed row to Current, records the round date, and reports the counts (activities, incomplete rows, flows under review, transfers without safeguard) to the steering committee under GOV-POL-01.

4.9 **Triggers for an update between rounds.** A function representative or System Owner reports to the Privacy Officer within five working days, and the Privacy Officer updates the registers within ten working days, when any of the following happens: a new product feature, form or integration that collects or sends personal data; a new or changed supplier; a new purpose for existing data; a new country of storage, support or processing; a change in retention; a change in the role of [Organisation] for a customer; a merger, acquisition or new entity; a data subject request or breach that reveals an unrecorded activity. The go-live gate in PB-07 and the change procedure in GOV-PRO-09 both ask whether the registers were updated, so a feature cannot ship with an unrecorded flow.

4.10 **Quarterly review.** Each quarter the Privacy Officer samples at least ten activities, checks each against the live system (a field list, an integration configuration, a supplier console, a retention setting) and records the result. A sample that fails on a material fact (an unrecorded recipient, transfer or data category) triggers a workshop for that function within thirty days.

4.11 **Annual round.** Once a year the full set of workshops in step 4.1 is repeated. The annual round also retires activities that have stopped, with the stop date recorded and the deletion confirmed under PIMS-POL-02.

4.12 **Producing the Article 30 record.** When a supervisory authority, an auditor or a customer asks for the record of processing, the Privacy Officer exports PIMS-REG-01 filtered to the role requested (controller rows or processor rows), dated, with the version of the register, and files a copy of what was sent.

## 5. Records and evidence

- PIMS-REG-01 Personal data processing inventory, with a status and round date on every row.
- GDPR-REG-02 Data flow and transfer map, with a diagram per activity in the evidence folder.
- Workshop attendance notes and the function heads' written confirmations.
- Quarterly sample records and any workshops they triggered.
- Copies of every Article 30 export provided to an external party.
- GDPR-REG-01 rows for Article 30 updated with the evidence reference.

## 6. Exceptions

An activity may remain Incomplete for no more than sixty days while a supplier or customer supplies a fact only they hold, with the Privacy Officer's agreement noted on the row. No activity runs without a recorded lawful basis.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after an audit finding or supervisory authority enquiry about the record of processing, and after a change in the organisation's structure. Changes follow GOV-PRO-01.

## 8. Related documents

- PIMS-REG-01 Personal data processing inventory
- GDPR-REG-02 Data flow and transfer map
- PIMS-PRO-01 Determining controller and processor roles
- PIMS-PRO-05 Consent and privacy notice management procedure
- PIMS-POL-02 Data retention and disposal policy
- PIMS-POL-03 International transfer policy
- GDPR-TPL-08 Transfer impact assessment template
- GOV-PRO-06 Supplier and third party security procedure
- GOV-PRO-09 Change management procedure
- GOV-REG-10 Information asset register
- GOV-REG-25 Data flow and interface inventory
- PB-07 Playbook: the go-live security and privacy gate for a software project
- PB-09 Playbook: evidence management that survives an audit
- GDPR-GDE-01 Guide: a GDPR operating model for a product or service team
