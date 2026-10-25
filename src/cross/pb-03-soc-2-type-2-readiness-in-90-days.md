---
id: PB-03
title: "Playbook: SOC 2 Type 2 readiness in 90 days"
type: playbook
framework: cross
maps:
  - SOC 2 CC4.1
  - SOC 2 CC1.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How to get a small organisation ready for a SOC 2 Type 2 examination in about ninety days, then run the observation period the auditor samples.
---
## 1. Purpose

This playbook takes a team with little formal structure to the point where a SOC 2 Type 2 examination can begin. It explains the difference between design and operation, the ninety days of preparation, and the observation period that follows, which is where the real evidence is made.

## 2. What SOC 2 is, in one paragraph

SOC 2 is a report, not a certificate, written by a licensed accounting firm against the Trust Services Criteria. A Type 1 report says the controls are suitably designed at a point in time. A Type 2 report says they also operated over a period, usually three to twelve months. Security is always in scope; availability, confidentiality, processing integrity and privacy are added only if you commit to them. The report reader, often a customer's security team, drives the scope.

## 3. Roles

| Role | In this effort |
|---|---|
| Project owner | Runs the readiness work and the evidence calendar. |
| Chief Executive Officer | Owns commitments, approves policies, chairs governance. |
| Engineering and operations leads | Produce technical evidence and fix technical gaps. |
| People lead | Produces onboarding, training and background-check evidence. |
| Auditor | The accounting firm, engaged once design is in place. |

## 4. The phases

4.1 **Scope and categories (about days 0 to 10).** Decide which Trust Services categories the report covers, based on what customers ask for. Define the system: the product, the people, the locations, the technology and the supporting corporate systems. Draft the system description with SOC-TPL-01.

4.2 **Gap assessment (about days 10 to 25).** Fill the readiness checklist (SOC-REG-03) and map every criterion to a control in the matrix (SOC-REG-01). Each gap becomes a corrective action in GOV-REG-03 with an owner and a date.

4.3 **Remediation (about days 25 to 60).** Close the gaps. Adopt the policies and procedures the criteria need, turn on the technical controls, and make sure each control has a named owner and a place where its evidence lands.

4.4 **Evidence collection begins (about days 60 to 90).** Start the evidence calendar (SOC-REG-02). From here on, every recurring control must produce evidence for every occurrence. This is the habit the Type 2 period depends on.

4.5 **The observation period (three to twelve months).** The controls operate and produce evidence continuously. Access reviews, vulnerability scans, change approvals, backups and training all run on their cadence, and each occurrence is kept. A Type 1 report at the ninety-day mark is an optional milestone that proves design while the period runs.

4.6 **Audit fieldwork and report.** The auditor samples the period, holds walkthroughs, inspects evidence and writes the report. Gaps found here are expensive, which is why the evidence calendar matters more than any single document.

## 5. The evidence calendar is the backbone

The single most useful tool is the recurring-events calendar (SOC-REG-02): the daily, weekly, monthly, quarterly and annual control events, each with an owner and the evidence it produces. A common monthly discipline is to spot-check one-twelfth of the controls, so that the whole set is reviewed once a year outside the audit.

## 6. What good evidence looks like

Evidence is a system export, a ticket, an approval or a dated screenshot, named as PB-09 describes, showing who did what and when. A blank template is not evidence. An empty register is not evidence. Back-dating is never evidence. If a control did not run, record that it did not and open a corrective action.

## 7. Common gaps to expect

Governance and HR evidence (board minutes, job descriptions, background checks, training records), a complete system description, a populated vendor inventory with assurance, and proof that recurring technical controls actually ran. Start these early; they take the longest to produce.

## 8. Related documents

- SOC-GDE-01 SOC 2 in plain words
- SOC-TPL-01 System description template
- SOC-REG-01 Trust Services Criteria control matrix
- SOC-REG-02 Evidence calendar
- SOC-REG-03 Readiness checklist
- PB-08 Running a readiness assessment
- PB-09 Evidence management
