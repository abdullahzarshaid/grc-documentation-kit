---
id: ISMS-GDE-03
title: "Guide: the certification journey from decision to recertification"
type: guide
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 4.3
  - ISO/IEC 27001:2022 clause 6.1.3
  - ISO/IEC 27001:2022 clause 9.2
  - ISO/IEC 27001:2022 clause 9.3
  - ISO/IEC 27001:2022 clause 10.2
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: Walks through every stage of an ISO/IEC 27001 certification, from the business case to the three year recertification, with what each stage demands, the findings that most often derail it, and how to choose a certification body.
---
## 1. What certification is and is not

Certification is an independent, accredited body's confirmation that your management system conforms to ISO/IEC 27001:2022 and is operating. It is not a statement that you are secure, that no incident will happen, or that every control works perfectly. It says that you have a system that identifies risk, treats it, checks itself and improves. A certificate lasts three years, with surveillance audits in between, and the scope wording on it is the only thing a customer can rely on.

The journey below assumes you are implementing with this kit. PB-02 gives the twelve implementation steps; this guide covers what happens around them and after them.

## 2. Stage by stage

### 2.1 Decision and business case

Someone has to decide that certification is worth the cost, and that decision has to be made by the people who will fund it. Write the case in one page: which customers or markets require it, what it costs (certification body fees, internal time, tooling, possibly external support), what it saves (shorter security questionnaires, fewer bespoke audits, lower insurance friction), and the earliest realistic date. Get the Chief Executive Officer to sign GOV-STM-01 at this point, not at the end. A certificate pursued without that signature stalls at the first budget conversation.

### 2.2 Scope

Decide what the certificate will cover. A narrow scope (one product, one location) is quicker to certify and harder to sell; a wide scope is the reverse. The wording goes into ISMS-STM-01 and later onto the certificate. Two tests: would a customer reading the certificate conclude that the service they buy is covered, and can you honestly include every system that touches that service? Scopes that exclude the support team, the identity provider or the build pipeline do not survive a careful customer or a careful auditor.

### 2.3 Gap analysis

Compare what exists with clauses 4 to 10 and with the Annex A tables in ISMS-GDE-01. Record three states: exists and evidenced, exists informally, does not exist. GOV-REG-28 is built for this. The output is the task list in ISMS-REG-05 with owners and weeks. Resist the urge to write policies before the gap analysis is finished; the gap analysis tells you which policies you actually need.

### 2.4 Risk assessment

Run GOV-PRO-05 across the scope. The method must be written before the first assessment, and the first assessment must be complete before the Statement of Applicability. Auditors read risk registers closely: they expect risks that reflect your business (your data, your providers, your people), not a generic list, and they expect the treatment column to point to real controls and real tasks.

### 2.5 Statement of Applicability

Complete ISMS-REG-01. Every one of the 93 controls gets a decision and a reason. The Statement of Applicability is the document most referenced during stage 2, because the auditor uses it as the sampling frame. Its version number appears in your scope wording and in the audit report; change control it strictly.

### 2.6 Implementation

Work through ISMS-REG-05. Policies and procedures are approved under GOV-PRO-01, controls are implemented and evidenced in ISMS-REG-02, registers start to fill. The common mistake is to treat this as a writing exercise. A procedure that has never been followed is worth nothing at audit; a control that has been operating for three months with records is worth everything.

### 2.7 Operating evidence

Certification bodies expect to see the management system operating, not only designed. Plan for at least three months of operation before stage 2, during which the following have all happened at least once: an access review, a vulnerability cycle with closures, a change through change management, a backup restore test, an incident or an incident exercise, awareness training with records, a supplier review, a risk review, a quarterly performance report under ISMS-PRO-04, and a steering committee meeting with minutes. Some bodies accept less for a very small organisation; none accept zero.

### 2.8 Internal audit

Clause 9.2 requires an internal audit covering the whole system before certification. Use GOV-PRO-02 and the checklist ISMS-REG-04. The auditor must be independent of the areas audited; in a small organisation that usually means an external person or a trained colleague from an unrelated function. The audit must produce findings. An internal audit report with no findings is itself a finding, because no first implementation is clean. Record the corrective actions in GOV-REG-03 and close or at least plan every one before stage 2.

### 2.9 Management review

Clause 9.3 requires a management review with the inputs listed in GOV-PRO-03, minuted with GOV-TPL-03. It must happen after the internal audit and before stage 2, because audit results are a mandatory input. Keep it real: a review in which leadership only receives information, and decides nothing, reads as a formality. Decisions about resources, objectives and improvements are what the auditor looks for in the minutes.

### 2.10 Stage 1 audit

The certification body's auditor reviews your documented information and your readiness, usually over one or two days and often remotely. They check the scope, the policy, the risk method and results, the Statement of Applicability, the audit and review evidence, and whether the system has operated long enough. Stage 1 produces a list of concerns, any of which could become a nonconformity at stage 2 if not addressed. Run GOV-CHK-03 four weeks before stage 1 and fix what it shows.

### 2.11 Stage 2 audit

The auditor tests whether the system operates as documented. Expect interviews with the Chief Executive Officer, the Information Security Manager, system owners, developers, support staff and people in the business who have no security role, sampling of records from every register, inspection of configurations, and a walk through of offices or a review of the provider's assurance where you have none. Findings are graded, usually as major nonconformity (a requirement is missing or systematically not met), minor nonconformity (an isolated lapse), observation, and opportunity for improvement. A major blocks the certificate until closed and verified; minors need an accepted corrective action plan. The certificate is issued after the body's independent review of the audit report, typically four to eight weeks after stage 2.

### 2.12 Surveillance

In each of the two years after certification the body audits a sample of the system, always including the clauses on leadership, risk, internal audit, management review and corrective action, plus a rotation through Annex A so that every applicable control is seen within the three year cycle. The evidence they want is continuity: the registers kept filling, the audits and reviews happened on schedule, actions closed, changes were controlled. Surveillance is where organisations that treated certification as a project rather than an operating system lose their certificate.

### 2.13 Recertification

Before the certificate expires the body performs a full audit comparable to stage 2, reviews the three years of performance, and issues a new certificate for a further three years. Scope changes, mergers and major incidents in the cycle are examined closely. Start preparing six months ahead; use the same readiness checklist.

## 3. Typical findings and how to avoid them

| Finding | Why it happens | How the kit prevents it |
|---|---|---|
| Scope statement does not match the systems actually in use | Scope written early and never updated | ISMS-STM-01 section 8 triggers and the thirty day update rule |
| Risk assessment is generic or has no link to treatments | Template risks copied in | GOV-PRO-05 scenario method; GOV-REG-05 treatment and SoA reference columns |
| Statement of Applicability out of date or without justifications | Treated as a one off deliverable | ISMS-REG-01 last reviewed column; ISMS-PRO-01 step 4.7(e) |
| Objectives not measurable | Written as aspirations | ISMS-PLN-01 rule 3.2 |
| Competence records missing for key roles | Training tracked, competence not | ISMS-PRO-02 matrix and assessment |
| Access reviews not performed or not evidenced | Promised quarterly, done once | GOV-PRO-10; GOV-REG-12 dated entries |
| Supplier reviews absent after onboarding | No renewal diary | GOV-REG-07 next review column; ISMS-PRO-04 measure |
| Internal audit not independent or not covering all clauses | One person does everything | GOV-PRO-02 independence rule; ISMS-PLN-03 coverage rule |
| Management review missing mandatory inputs | Agenda improvised | GOV-TPL-03 one heading per input |
| Corrective actions without root cause or effectiveness check | Fix and close | GOV-PRO-04; GOV-TPL-02 verification section |
| Backups never restored | Backup success assumed | GOV-PRO-12 quarterly test; GOV-REG-15 |
| Incident procedure untested | No incidents, no exercise | GOV-PRO-07 exercise cadence; GOV-REG-16 |
| Logs collected, never reviewed | No review cadence | GOV-PRO-14 review step and records |
| Documents without approval evidence or past review date | Document control informal | GOV-PRO-01; GOV-REG-01 |

## 4. Choosing a certification body

- **Accreditation.** Use a body accredited by the national accreditation body for ISO/IEC 27001 certification. An unaccredited certificate is not recognised by informed customers and some tenders reject it outright.
- **Sector and size fit.** Ask which clients of your size and sector they certify. A body used to large enterprises may bring expectations and day rates that do not fit a forty person company.
- **Auditor continuity and competence.** Ask whether the same lead auditor will perform stage 1, stage 2 and surveillance where possible, and what the auditor's background is in your technology. Technical scopes need auditors who can read a cloud configuration.
- **Audit days and cost.** The number of audit days is calculated from headcount and complexity by the accreditation rules, so quotes should be similar; large differences deserve a question. Ask for the full three year cost, including surveillance and travel.
- **Scheduling.** Lead times of two to four months for stage 1 are normal. Book when your internal audit is scheduled, not when it is finished.
- **Language and location.** Confirm that audits can be conducted in the languages your staff work in, and remotely where your scope allows.
- **Report quality.** Ask for a sample report. A report with specific, evidence based findings is worth more to you than a tick list.
- **Integrated audits.** If you plan ISO/IEC 27701 or other standards, a body that can audit them together saves days every year.

## 5. Keeping the certificate

After certification, the management system is a calendar. The recurring events that surveillance auditors check are: quarterly access reviews, quarterly performance reports, at least annual risk review, at least annual internal audit covering the programme in ISMS-PLN-03, at least annual management review, annual awareness refresher, annual supplier reviews, annual policy reviews, and corrective actions closed with effectiveness verified. Put every one in a shared calendar with an owner, and let GOV-REG-21 show whether each happened. A system that runs on the calendar passes surveillance without a project.

## 6. Related documents

- PB-02 Playbook: ISO/IEC 27001:2022 implementation in twelve steps
- ISMS-GDE-01 Guide to the 93 Annex A controls
- ISMS-GDE-02 Guide to mandatory documented information and records
- ISMS-REG-05 Implementation project plan
- GOV-CHK-03 Pre-audit readiness checklist
- GOV-PRO-02 Internal audit procedure
- GOV-PRO-03 Management review procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-STM-01 Top management commitment statement
