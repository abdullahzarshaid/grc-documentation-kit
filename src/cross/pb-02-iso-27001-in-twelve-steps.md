---
id: PB-02
title: "Playbook: ISO/IEC 27001:2022 implementation in twelve steps"
type: playbook
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 4.1
  - ISO/IEC 27001:2022 clause 5.1
  - ISO/IEC 27001:2022 clause 6.1.2
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 8.1
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 9.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: A twelve step route from the decision to certify to the certification audit, with inputs, activities, outputs, kit documents and typical duration for each step, and a 26 week timeline for an organisation of up to about one hundred people.
---
## 1. Before you start

This playbook is for the person who has been asked to get [Organisation] certified and needs an order of work. It assumes you have read PB-01, that you will use the registers in this kit, and that someone with authority has agreed to spend money and people's time. If that last point is not true, step 1 is where you make it true.

Durations assume an organisation of 20 to 100 people, one main product or service, cloud hosted, with one person spending about half their time on the programme and others contributing a few hours a week. Larger or more complex organisations should double the figures; very small ones can compress steps 5 to 7 into a fortnight. The one duration you cannot compress is step 10, because auditors need to see the system operating.

Track the work in ISMS-REG-05, which holds the tasks below with planned weeks, owners and status. Keep GOV-REG-01 from day one so that the master list grows as you go rather than being reconstructed at the end.

## 2. The twelve steps

### Step 1. Management support and charter

**Inputs.** The reason certification matters (a customer, a market, a regulator), a rough budget, the names of the people who will carry the work.

**Activities.** Write a one page business case. Agree who the Information Security Manager will be and how much of their time the programme gets. Form the steering committee with a charter, quorum and monthly cadence using GOV-POL-01. Have the Chief Executive Officer sign GOV-STM-01. Agree the target date for stage 1 and the budget for the certification body.

**Outputs.** Signed commitment statement, steering committee charter and first meeting minutes, named roles, budget line.

**Kit documents.** GOV-STM-01, GOV-POL-01, GOV-TPL-03 for the committee minutes.

**Typical duration.** Two weeks. Longer if the budget needs a board cycle; start that conversation first.

### Step 2. Scope and context

**Inputs.** The org chart, the list of products and services, the list of offices and hosting regions, current customer contracts with security clauses.

**Activities.** Run the context workshop in ISMS-PRO-01 and fill ISMS-REG-03 with the interested parties and their requirements. Draft the scope in ISMS-STM-01, including the shared responsibility split with your providers and any exclusions with reasons. Confirm the scope with the steering committee.

**Outputs.** Approved scope statement, interested parties register, issues analysis.

**Kit documents.** ISMS-PRO-01, ISMS-REG-03, ISMS-STM-01.

**Typical duration.** Two to three weeks, overlapping with step 1.

### Step 3. Gap analysis

**Inputs.** The approved scope, access to the people who run each area, the Annex A tables in ISMS-GDE-01.

**Activities.** Work through GOV-REG-28 with the owners of each domain and through the Annex A tables control by control. Mark each item as exists and evidenced, exists informally, or missing. Turn every gap into a task in ISMS-REG-05 with an owner and a planned week. Report the result to the steering committee with the three largest risks you can already see.

**Outputs.** Completed readiness questionnaire, populated project plan, a gap summary for leadership.

**Kit documents.** GOV-REG-28, PB-08, ISMS-GDE-01, ISMS-REG-05.

**Typical duration.** Two weeks.

### Step 4. Policy and governance

**Inputs.** The gap list, the kit's policy and procedure sources, the roles agreed in step 1.

**Activities.** Set up document control with GOV-PRO-01 and GOV-REG-01 first; everything else is then issued through it. Adapt and approve the top level policy GOV-POL-03, the governance framework GOV-POL-01, and the topic policies that apply (GOV-POL-02, GOV-POL-04, GOV-POL-05, GOV-POL-06). Issue the management procedures for audit, review, corrective action and exceptions (GOV-PRO-02, GOV-PRO-03, GOV-PRO-04, GOV-PRO-24). Issue the communication plan ISMS-PLN-02. Do not issue operational procedures yet; they depend on the risk assessment.

**Outputs.** Approved and published policies and management procedures, master list showing their versions, acknowledgement records starting in GOV-REG-23.

**Kit documents.** GOV-PRO-01, GOV-REG-01, GOV-POL-03, GOV-POL-01, GOV-POL-02, GOV-POL-04, GOV-POL-05, GOV-POL-06, GOV-PRO-02, GOV-PRO-03, GOV-PRO-04, GOV-PRO-24, ISMS-PLN-02.

**Typical duration.** Four to five weeks, running alongside steps 5 and 6.

### Step 5. Competence and awareness

**Inputs.** The roles table, the headcount list, any existing training.

**Activities.** Complete the competence matrix in ISMS-PRO-02 and assess the people in security roles against it. Plan the gap closing actions. Set up GOV-REG-09 and schedule the all staff awareness session under GOV-PRO-08; run it before step 10 begins so that the acknowledgement records exist when operation starts. Identify who will be the internal auditor and arrange their training or an external auditor now, because step 11 is closer than it looks.

**Outputs.** Assessed competence matrix, training plan, first awareness session delivered and recorded, internal auditor named.

**Kit documents.** ISMS-PRO-02, GOV-PRO-08, GOV-REG-09, GOV-TPL-10, GOV-REG-23.

**Typical duration.** Three to four weeks, overlapping.

### Step 6. Assets

**Inputs.** Exports from the identity provider, device management, cloud accounts and the finance asset list.

**Activities.** Build GOV-REG-10 with every information asset in scope, an owner and a classification using GOV-PRO-16. Build GOV-REG-24 for hardware and software with end of support dates. Build GOV-REG-07 with every supplier and a provisional tier. Build GOV-REG-25 for data flows across the scope boundary. These four registers are the raw material for the risk assessment; a risk assessment without them produces generic risks.

**Outputs.** Four populated registers, reconciled against the source exports.

**Kit documents.** GOV-PRO-16, GOV-REG-10, GOV-REG-24, GOV-REG-07, GOV-REG-25.

**Typical duration.** Three to four weeks, overlapping with steps 4 and 5.

### Step 7. Risk method

**Inputs.** The gap summary, the steering committee's view of appetite, GOV-PRO-05 as the starting text.

**Activities.** Adapt GOV-PRO-05: confirm the scales, the matrix bands, who may accept risk in each band, and the review triggers. Approve it at the steering committee. Set up GOV-REG-05 and GOV-REG-06. Brief the risk owners on the scenario method so that the workshop in step 8 is productive.

**Outputs.** Approved risk methodology, empty risk and acceptance registers, briefed risk owners.

**Kit documents.** GOV-PRO-05, GOV-REG-05, GOV-REG-06, GOV-TPL-06.

**Typical duration.** One to two weeks.

### Step 8. Risk assessment

**Inputs.** The asset registers, the issues analysis, incident history, the briefed risk owners.

**Activities.** Run risk workshops by area (product and infrastructure, people and access, suppliers and cloud, offices and devices, corporate systems). For each asset group imagine the incident, how it would be detected and by whom, then the causes and the existing controls. Score raw risk, agree treatment options, and record each risk in GOV-REG-05 with its owner. Have each owner confirm their rows. Present the heat map and the risks above appetite to the steering committee.

**Outputs.** Populated risk register with raw scores and treatment decisions, committee minute accepting the assessment.

**Kit documents.** GOV-PRO-05, GOV-REG-05.

**Typical duration.** Three to four weeks including owner confirmation.

### Step 9. Treatment and Statement of Applicability

**Inputs.** The risk register, the Annex A tables, the gap list.

**Activities.** For each risk above appetite, define treatment actions with an owner and date and record them against the risk. Complete ISMS-REG-01 for all 93 controls: Applicable, justification, status, implementing documents. Make sure every control referenced by a treatment is Applicable, and every Not applicable has a reason tied to a risk or a scope fact. Load the treatment actions and the Planned or Partial controls into ISMS-REG-02 as implementation tasks. Now issue the operational procedures that the applicable controls need (GOV-PRO-06 to GOV-PRO-23, GOV-PRO-25 to GOV-PRO-27 as applicable) and the operational planning procedure ISMS-PRO-03. Set the objectives in ISMS-PLN-01 and the measures in ISMS-PRO-04.

**Outputs.** Risk treatment plan, Statement of Applicability version 1.0, control tracker with tasks, approved operational procedures, approved objectives and measures.

**Kit documents.** ISMS-REG-01, ISMS-REG-02, ISMS-PRO-03, ISMS-PLN-01, ISMS-PRO-04, GOV-REG-21, the operational procedures above.

**Typical duration.** Three to four weeks for the Statement of Applicability and procedures; the treatment actions themselves continue into step 10.

### Step 10. Operate and measure

**Inputs.** Approved procedures, the control tracker, the measurement set.

**Activities.** Run the system. Implement the treatment actions and attach evidence in ISMS-REG-02. Perform the recurring events at least once each: access review (GOV-REG-12), vulnerability cycle (GOV-REG-14), changes through GOV-PRO-09 (GOV-REG-11), restore test (GOV-REG-15), supplier review (GOV-REG-07), an incident exercise (GOV-REG-16, GOV-REG-08), awareness refresher where due, quarterly performance report under ISMS-PRO-04, monthly operations review under ISMS-PRO-03, steering committee meetings with minutes. Book the certification body during this step; lead times are long. Use PB-09 to organise the evidence so that nothing has to be hunted for in step 12.

**Outputs.** At least one complete cycle of every recurring control with records; one quarterly report; a booked stage 1 date.

**Kit documents.** ISMS-PRO-03, ISMS-PRO-04, ISMS-REG-02, PB-09, all operational registers.

**Typical duration.** Twelve weeks minimum. This is the floor set by the need for operating evidence, not a target.

### Step 11. Internal audit and management review

**Inputs.** Three months of records, the trained or contracted internal auditor, the audit programme in ISMS-PLN-03.

**Activities.** Run the full system internal audit under GOV-PRO-02 with ISMS-REG-04, covering clauses 4 to 10 and every applicable control, with an auditor independent of each area. Record findings in GOV-REG-02, raise corrective actions in GOV-REG-03 using GOV-TPL-02, and close or plan all of them. Then hold the management review under GOV-PRO-03 with every mandatory input, minute it with GOV-TPL-03, and track the decisions in GOV-REG-22. Run GOV-CHK-03 and fix what it shows.

**Outputs.** Internal audit report, corrective action log with root causes, management review minutes with decisions, readiness checklist result.

**Kit documents.** GOV-PRO-02, ISMS-PLN-03, ISMS-REG-04, GOV-TPL-01, GOV-TPL-02, GOV-REG-02, GOV-REG-03, GOV-PRO-03, GOV-TPL-03, GOV-REG-22, GOV-CHK-03, PB-06.

**Typical duration.** Three to four weeks, including the time to close findings.

### Step 12. Certification

**Inputs.** Everything above, the booked dates, a room or a call line, the evidence folders.

**Activities.** Stage 1: present the documented system, answer the readiness questions, receive the concerns list and address each within the time the auditor sets. Stage 2: make the right people available, provide records from the registers, walk the auditor through configurations and offices, and record every finding in GOV-REG-03 as it is raised. After stage 2 submit the corrective action plans, obtain the certificate, update ISMS-PLN-02 external communications with the scope wording, and move the system onto its annual calendar as described in ISMS-GDE-03.

**Outputs.** Stage 1 report and responses, stage 2 report, corrective action plans accepted, certificate, surveillance dates in the calendar.

**Kit documents.** ISMS-GDE-03, GOV-REG-03, ISMS-PLN-02, ISMS-STM-01.

**Typical duration.** Stage 1 and stage 2 are usually four to eight weeks apart, and the certificate follows stage 2 by four to eight weeks.

## 3. The 26 week timeline

The table shows one workable arrangement. Steps overlap deliberately; the steering committee meets monthly throughout. Week numbers match the planned start and end weeks prefilled in ISMS-REG-05.

| Weeks | Steps running | Milestones | Outputs due |
|---|---|---|---|
| 1 to 2 | 1 | Commitment signed; committee formed; Information Security Manager named | GOV-STM-01, GOV-POL-01 charter, first minutes |
| 2 to 4 | 2 | Context workshop held; scope approved | ISMS-REG-03, ISMS-STM-01 |
| 4 to 6 | 3 | Gap analysis complete; project plan loaded | GOV-REG-28, ISMS-REG-05 |
| 5 to 9 | 4, 5, 6 | Document control live; policies approved; asset registers built; competence assessed | GOV-REG-01, GOV-POL-03, topic policies, GOV-REG-10, GOV-REG-24, GOV-REG-07, ISMS-PRO-02 matrix |
| 9 to 10 | 7 | Risk method approved | GOV-PRO-05, GOV-REG-05 ready |
| 10 to 13 | 8 | Risk workshops held; register confirmed by owners | GOV-REG-05 populated |
| 13 to 16 | 9 | Statement of Applicability 1.0; operational procedures issued; objectives set | ISMS-REG-01, ISMS-REG-02, ISMS-PRO-03, ISMS-PLN-01, ISMS-PRO-04 |
| 14 to 26 | 10 | System operating; certification body booked by week 16; first quarterly report by week 22 | Operational registers filling, ISMS-REG-02 evidence, quarterly report |
| 21 to 24 | 11 | Internal audit; corrective actions; management review; readiness checklist | GOV-TPL-01, GOV-REG-03, GOV-TPL-03, GOV-CHK-03 |
| 25 to 26 | 12 | Stage 1 audit; concerns addressed | Stage 1 report and responses |
| After 26 | 12 | Stage 2 audit four to eight weeks after stage 1; certificate | Stage 2 report, certificate |

If the certification body cannot offer stage 1 by week 26, keep operating; more evidence never hurts. If the organisation wants stage 2 inside the 26 weeks, the only way is to start step 10 earlier by issuing the operational procedures that do not depend on the risk assessment (access, change, vulnerability, backup) in week 9 rather than week 13, and accept that the Statement of Applicability may be revised once the assessment finishes.

## 4. Roles through the programme

| Role | Steps where they carry the work |
|---|---|
| Chief Executive Officer | 1 (commitment, budget), 2 (scope approval), 8 (risk acceptance above appetite), 11 (chairs management review), 12 (opening and closing meetings) |
| Information Security Manager | Every step; owns ISMS-REG-05 and the registers |
| Steering committee | Monthly from step 1; approves scope, policies, risk method, Statement of Applicability, objectives |
| Head of Engineering | 6 (asset exports), 8 (product and infrastructure risks), 9 and 10 (technical controls and evidence) |
| Head of People | 5 (competence and training), 6 (headcount), 10 (joiner and leaver records) |
| Head of Operations | 6 and 10 (suppliers, continuity exercise) |
| Privacy Officer | 2 (data subject and regulator requirements), 8 (privacy risks), 9 (controls 5.34 and 8.10) |
| Internal Auditor | 5 (trained), 11 (audit) |
| All staff | 5 (awareness), 10 (following the procedures), 12 (interviews) |

## 5. Signs you are off track

- Policies are being written before the gap analysis is complete. Stop and finish step 3.
- The risk register has fewer than twenty risks or none specific to your product. Rerun the step 8 workshops with the asset registers open.
- The Statement of Applicability has controls marked Implemented with no evidence in ISMS-REG-02. Change them to Partial until evidence exists.
- Week 18 has arrived and no access review, restore test or change record exists. Step 10 has not really started; push stage 1 back.
- The internal auditor also wrote the procedures. Find another auditor; the finding at stage 2 is certain otherwise.
- The management review minutes contain information and no decisions. Reconvene and decide something about resources or objectives.

## 6. Related documents

- PB-01 Playbook: start here, how to use this kit
- ISMS-REG-05 Implementation project plan
- ISMS-GDE-01 Guide to the 93 Annex A controls
- ISMS-GDE-02 Guide to mandatory documented information and records
- ISMS-GDE-03 Guide to the certification journey
- GOV-PRO-05 Risk assessment and treatment methodology
- ISMS-REG-01 Statement of Applicability
- ISMS-REG-02 Control implementation tracker
- GOV-CHK-03 Pre-audit readiness checklist
- PB-06 Playbook: running your first internal audit cycle
- PB-09 Playbook: evidence management that survives an audit
