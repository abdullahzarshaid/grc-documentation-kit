---
id: ISMS-PRO-01
title: Context of the organisation and interested parties procedure
type: procedure
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 4.1
  - ISO/IEC 27001:2022 clause 4.2
  - ISO/IEC 27001:2022 clause 4.3
  - ISO/IEC 27701 clause 5.2.1
  - ISO/IEC 27701 clause 5.2.2
  - SOC 2 CC3.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] identifies the internal and external issues that affect its security and privacy outcomes, the parties with an interest in those outcomes and their requirements, and how the results shape the scope, risks and objectives of the management system.
---
## 1. Purpose

This procedure gives [Organisation] a repeatable way to understand the conditions it operates in, who depends on its security and privacy performance, and what those parties require, so that the scope, the risk assessment and the objectives rest on recorded facts rather than assumptions.

## 2. Scope

It applies to the whole management system described in ISMS-STM-01, every function and location within it, and the privacy extension where [Organisation] operates one. It runs at least once a year and after any trigger event in step 4.1.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Chief Executive Officer | Sponsors the analysis, confirms the issues that matter at leadership level, approves the output through the steering committee. |
| Information Security Manager | Runs the analysis, keeps ISMS-REG-03 current, carries the results into the scope, the risk register and the objectives. |
| Privacy Officer | Contributes data protection obligations and the expectations of supervisory authorities and data subjects. |
| Heads of function | Contribute the issues and parties for their area, own the requirements assigned to them, confirm the register reflects their contracts and regulators. |
| Internal Auditor | Checks each year that the register is current and that its results trace into the risk register and the objectives. |

## 4. Procedure

4.1 **Timing.** The Information Security Manager schedules the context review once a year, in the quarter before the management review, and within thirty days of any of these events: a new market or jurisdiction, a new service or product, an acquisition or divestment, a change of principal supplier, a change in applicable law, a severity 1 or 2 incident, a customer gained or lost that changes the risk profile, or a change of ownership or leadership.

4.2 **Preparation.** Five working days before the workshop the Information Security Manager circulates the current ISMS-REG-03, the previous issues analysis, a summary of GOV-REG-05 and GOV-REG-04, incident and audit trends for the period, and the security questionnaires and contract clauses received from customers since the last review.

4.3 **Internal issues.** In a workshop of at most two hours the participants answer the questions in table 1 for each category. Each issue is recorded as one sentence that states the condition and whether it helps or hinders a security or privacy outcome, with the function that owns it. An issue that cannot be stated as a condition with an effect is not recorded.

Table 1. Internal issue categories

| Category | Questions to answer |
|---|---|
| Governance and strategy | Growth plans, funding, planned products, appetite for risk, leadership changes |
| People and culture | Headcount change, skills gaps, turnover, reliance on contractors, remote working pattern |
| Technology and architecture | Legacy components, provider dependence, technical debt, planned migrations |
| Processes and maturity | Which processes are documented and followed, where work is informal |
| Information and assets | New data categories, volume growth, where restricted information concentrates |
| Resources | Budget, tooling and time available for security and privacy work |
| Past performance | Incident, audit, nonconformity and measurement trends in the period |

4.4 **External issues.** The participants repeat the method with table 2. Each issue is recorded with the source it was learned from, so that it can be re-checked at the next review.

Table 2. External issue categories

| Category | Questions to answer |
|---|---|
| Legal and regulatory | Laws, regulators and sector rules in each jurisdiction served; changes expected within eighteen months |
| Customers and market | Security demands in contracts and tenders, certifications competitors hold, customer concentration |
| Threat environment | Threat types seen against the sector, findings from GOV-PRO-27, fraud patterns seen by support and finance |
| Suppliers and technology | Provider concentration, announced provider changes, end of support dates in GOV-REG-24 |
| Economic and financial | Pricing pressure, insurance availability and conditions, currency and payment exposure |
| Social and environmental | Public expectations on privacy, physical hazards at each location, travel or access restrictions |

4.5 **Interested parties.** The participants confirm the list of interested parties using the categories in table 3, adding and removing parties as the business has changed. For each party the register records the relationship and why the party cares about [Organisation]'s performance.

Table 3. Interested party categories

| Party category | Typical requirements |
|---|---|
| Customers and their own customers | Confidentiality, availability targets, breach notification, certifications, right to audit, data location |
| Regulators and supervisory authorities | Compliance with law, timely notifications, cooperation with enquiries |
| Staff and contractors | Clear rules, usable controls, protection of their own personal data, fair monitoring |
| Owners, board and investors | Risk within appetite, protection of value, honest reporting |
| Suppliers and partners | Clear obligations, agreed interfaces, controlled access to systems |
| Data subjects | Lawful and transparent handling, rights answered on time |
| Certification bodies and auditors | Access to evidence, conformity with the standard, notice of major changes |
| Insurers | Control baselines named in policy conditions, incident notification within policy terms |

4.6 **Requirements.** For each party the Information Security Manager records every requirement in ISMS-REG-03 as one row: the party, the requirement in plain words, its type (Legal, Contractual, Voluntary commitment or Expectation), the source, the owner, how it is addressed and its priority. Whether the requirement is met through the management system is recorded explicitly; a requirement handled outside it names the function that handles it.

4.7 **Using the results.** Within twenty working days of the workshop the Information Security Manager: (a) updates ISMS-STM-01 if an issue or requirement changes the boundary; (b) raises or updates a risk in GOV-REG-05, using GOV-PRO-05, for every issue that hinders an outcome; (c) adds or updates obligations in GOV-REG-04 for every legal or contractual requirement; (d) proposes objectives for ISMS-PLN-01 where a requirement needs a measurable commitment; (e) checks ISMS-REG-01 for any control whose applicability justification depends on an issue or requirement that has changed.

4.8 **Approval.** The steering committee reviews the issues analysis and ISMS-REG-03 at its next meeting and records acceptance in its minutes. Where participants disagree about whether a requirement applies, the committee decides and the decision is minuted.

4.9 **Reporting.** A summary of the changes in context since the last review is a mandatory input to the management review under GOV-PRO-03.

## 5. Records and evidence

- ISMS-REG-03 Interested parties and requirements register, with a last reviewed date on every row.
- The completed issues analysis (tables 1 and 2), dated and controlled under GOV-PRO-01.
- The workshop attendance list and the preparation pack.
- Steering committee minutes recording acceptance.
- Entries in GOV-REG-05, GOV-REG-04 and ISMS-PLN-01 that cite the review date as their source.

## 6. Exceptions

The workshop may be replaced by a desk review by the Information Security Manager only when none of the events in step 4.1 occurred in the period and the previous review was workshop based. The substitution is recorded in ISMS-REG-03 and may not be used in two consecutive years.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually and after any audit finding against clauses 4.1 to 4.3. Changes follow GOV-PRO-01.

## 8. Related documents

- ISMS-STM-01 ISMS scope statement
- ISMS-REG-03 Interested parties and requirements register
- ISMS-PLN-01 Information security objectives and plan
- ISMS-REG-01 Statement of Applicability
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
- GOV-REG-04 Legal, regulatory and contractual register
- GOV-PRO-25 Legal, regulatory and contractual compliance procedure
- GOV-PRO-03 Management review procedure
- GOV-POL-01 Information security and privacy governance framework
