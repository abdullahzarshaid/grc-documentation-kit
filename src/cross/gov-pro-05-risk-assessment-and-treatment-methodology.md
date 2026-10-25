---
id: GOV-PRO-05
title: Risk assessment and treatment methodology
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 clause 6.1.2
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 8.2
  - ISO/IEC 27001:2022 clause 8.3
  - ISO/IEC 27701 clause 5.4.1.2
  - SOC 2 CC3.1
  - SOC 2 CC3.2
  - SOC 2 CC3.3
  - SOC 2 CC3.4
  - GDPR Article 32
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The single method [Organisation] uses to value assets, identify and score information security and privacy risks, decide how to treat them, link treatment to the Statement of Applicability, and keep the results current.
---
## 1. Purpose

This methodology makes risk assessment repeatable, puts treatment decisions at the right level, and lets the Statement of Applicability trace back to the risks that justify it.

## 2. Scope

It applies to every risk to the confidentiality, integrity or availability of information within the scope in ISMS-STM-01, including risks from suppliers, cloud services and AI systems. Risks to individuals follow PIMS-PRO-02; AI threats use the AI-PRO-01 catalogue with these scales.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves the criteria and appetite; accepts Critical risks. |
| Executive sponsor | Accepts High risks; approves the risk treatment plan. |
| Information Security Manager | Owns this methodology and GOV-REG-05, facilitates assessments, consolidates the treatment plan, maintains ISMS-REG-01. |
| Risk owner | Manager with authority over the asset or process; decides treatment, accepts Low risks, keeps entries current. |
| Asset owner | Values the asset; supplies the facts on threats, vulnerabilities and controls. |
| Privacy Officer | Joins every assessment involving personal data; links results to PIMS-REG-08. |

## 4. Procedure

4.1 **Criteria and appetite.** The Chief Executive Officer approves the scales, bands and authorities below as the risk criteria. The appetite: no risk stays High or Critical without an approved treatment plan or a time-limited acceptance under GOV-PRO-24; Medium risks are treated where the cost is proportionate.

4.2 **Asset valuation.** The asset owner rates each asset in GOV-REG-10 from 1 to 3 on confidentiality, integrity, availability, legal consequence and reputational consequence. The highest rating is the asset value.

| Rating | Meaning |
|---|---|
| 1 | Inconvenience absorbed within normal operations. |
| 2 | Measurable harm: lost working time, a contractual complaint, a correctable legal exposure, local reputational damage. |
| 3 | Serious harm: regulatory action, loss of a major customer, harm to individuals, public loss of trust. |

4.3 **Identifying risks.** The Information Security Manager runs a workshop with each area's asset owners at least annually. For each asset or process the group considers seven threat categories (environmental events, technical failure, human error, insider misuse, external attack, supplier failure, legal or contractual change) and six vulnerability categories (technical weakness, missing or weak control, process gap, skill or awareness gap, physical exposure, contractual gap).

4.4 **Scenario method.** Each risk is a scenario, not a category. The group imagines the incident, asks how it would be detected and by whom, then works back to the causes and the controls that would have prevented it. In GOV-REG-05 the scenario reads: a named threat exploits a named vulnerability on a named asset, with a stated consequence. Each scenario has one owner.

4.5 **Likelihood.** The group rates the likelihood within twelve months, with the controls operating today.

| Level | Name | Definition |
|---|---|---|
| 1 | Rare | No known occurrence in the sector; needs an exceptional combination of events. |
| 2 | Unlikely | Seen in comparable organisations; not expected here within five years. |
| 3 | Possible | Could occur within one to five years; precursors seen. |
| 4 | Likely | Expected within the year; happened here or at a close peer in the last three years. |
| 5 | Almost certain | Expected more than once a year, or already occurring. |

4.6 **Impact.** The group rates the worst credible consequence, considering the asset value and the five dimensions in 4.2.

| Level | Name | Definition |
|---|---|---|
| 1 | Negligible | Absorbed within the day; no external party affected; cost below [Number]. |
| 2 | Minor | Disruption under one day; a few individuals or one customer affected; no notification. |
| 3 | Moderate | Disruption of one to three days; a notifiable breach or contractual breach possible; cost up to [Number]. |
| 4 | Major | Disruption over three days; regulatory notification; loss of a key customer; significant harm to individuals. |
| 5 | Severe | Threatens the viability of a service or the organisation; enforcement action; serious harm to many individuals. |

4.7 **Score, matrix and band.** The score is likelihood multiplied by impact: 1 to 4 Low, 5 to 9 Medium, 10 to 15 High, 16 to 25 Critical. GOV-REG-05 calculates both.

| Likelihood and impact | Impact 1 | Impact 2 | Impact 3 | Impact 4 | Impact 5 |
|---|---|---|---|---|---|
| Likelihood 5 | 5 Medium | 10 High | 15 High | 20 Critical | 25 Critical |
| Likelihood 4 | 4 Low | 8 Medium | 12 High | 16 Critical | 20 Critical |
| Likelihood 3 | 3 Low | 6 Medium | 9 Medium | 12 High | 15 High |
| Likelihood 2 | 2 Low | 4 Low | 6 Medium | 8 Medium | 10 High |
| Likelihood 1 | 1 Low | 2 Low | 3 Low | 4 Low | 5 Medium |

4.8 **Acceptance authority.** One authority per band accepts the risk or approves its treatment plan.

| Band | Authority | Condition |
|---|---|---|
| Low | Risk owner | Record the decision; review annually. |
| Medium | Information Security Manager with the risk owner | Treat where proportionate, else accept with a reason; review twice a year. |
| High | Executive sponsor | Treatment plan required; acceptance only under GOV-PRO-24, at most twelve months; review quarterly. |
| Critical | Chief Executive Officer | Treatment starts within thirty days; acceptance only under GOV-PRO-24, at most ninety days; review monthly until High or below. |

4.9 **Treatment options.** The risk owner records one option in GOV-REG-05: Modify (add or improve controls), Retain (accept at the current rating under 4.8), Avoid (stop or change the activity), or Share (insurance or contract; accountability stays with the organisation).

4.10 **Link to the Statement of Applicability.** For every Modify treatment the risk owner names the Annex A controls and implementing kit documents in the treatment plan column. The Information Security Manager marks those controls Applicable in ISMS-REG-01 with the risk IDs as justification. A control marked Not applicable may not appear in any treatment plan. Controls applicable for legal or contractual reasons alone cite GOV-REG-04.

4.11 **Raw, treated and target ratings.** Raw: likelihood and impact today, with existing controls as they actually operate. Treated: the residual values expected once the treatment is implemented and verified. Target: the band the risk owner intends to reach, within appetite. GOV-REG-05 holds both and calculates both scores; the target band is stated in the treatment plan.

4.12 **Risk treatment plan.** The Information Security Manager consolidates all Modify treatments into one plan with actions, owners, resources, due dates and residual ratings. The executive sponsor approves the plan, risk owners approve their entries, and the authority in 4.8 accepts each residual risk in writing.

4.13 **Review and triggers.** The Information Security Manager reviews GOV-REG-05 at the frequency in 4.8 and reassesses everything at least annually. Affected scenarios are reassessed within twenty working days of an incident or breach, an audit finding, a new system, supplier or processing activity, a significant change to architecture, location or organisation, a legal or contractual change, credible threat intelligence, or a DPIA result. Each assessment leaves a dated record of attendees, scenarios, ratings and decisions; superseded ratings are kept.

## 5. Records and evidence

- GOV-REG-05 Information security risk register.
- GOV-REG-06 Risk acceptance and exception register.
- ISMS-REG-01 Statement of Applicability.
- The approved risk treatment plan and workshop records.

## 6. Exceptions

No alternative scale or band may be used. A unit reporting on a corporate scale maps this scale to it in writing, approved by the Information Security Manager, without changing the ratings here.

## 7. Review and maintenance

The Information Security Manager reviews this methodology annually, after any audit finding about risk management, and when the appetite, scope or frameworks change. The Chief Executive Officer approves changes to scales, bands or authorities.

## 8. Related documents

- GOV-REG-05 Information security risk register
- GOV-REG-06 Risk acceptance and exception register
- ISMS-REG-01 Statement of Applicability
- GOV-PRO-24 Exception and risk acceptance procedure
