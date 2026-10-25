---
id: AI-GDE-01
title: "Guide: AI Governance Frameworks Mapped to the Kit"
type: guide
framework: ai
maps:
  - ISO/IEC 42001 clause 4.1
  - ISO/IEC 42001 clause 6.1
  - ISO/IEC 42001 clause 8.1
  - NIST AI RMF GOVERN
  - NIST AI RMF MAP
  - NIST AI RMF MEASURE
  - NIST AI RMF MANAGE
  - GDPR Article 22
owner: Information Security Manager
approver: Head of Engineering
classification: Internal
review: Annual
summary: A short orientation to ISO/IEC 42001, the NIST AI Risk Management Framework and the EU AI Act, in plain words, with a map from each framework's requirements to the kit documents and registers that satisfy them.
---
## 1. Why three frameworks

Three public frameworks shape how an organisation is expected to govern AI, and they do different jobs. ISO/IEC 42001 is a certifiable management system standard: it tells you what a governed AI programme must contain and lets an auditor check it. The NIST AI Risk Management Framework is a voluntary method: it tells you how to think about AI risk and gives a vocabulary that regulators and customers increasingly borrow. The EU AI Act is law: it tells you which systems are banned, which carry heavy obligations and which only need transparency, and it applies to any organisation that places a system on the EU market or whose system's output is used there. An organisation that already runs the kit's security and privacy documents has most of the machinery these three need. This guide shows where each requirement lands.

## 2. ISO/IEC 42001 in plain words

ISO/IEC 42001 follows the same harmonised structure as ISO/IEC 27001: context (clause 4), leadership (5), planning (6), support (7), operation (8), performance evaluation (9) and improvement (10). The management system is about AI systems specifically, so the standard adds three things the security standard does not demand. First, an AI policy and defined objectives for responsible development and use. Second, an AI system impact assessment: not only risk to the organisation but the consequences for individuals, groups and society of the system's operation. Third, lifecycle controls: requirements for data, for evaluation, for human oversight and for what happens when a system fails, through its entire life. Its Annex A lists reference controls and Annex B explains them; Annex C lists AI-specific objectives and risk sources, and Annex D describes how the standard applies across sectors.

An organisation combining ISO/IEC 42001 with ISO/IEC 27001 runs one management system with two scopes, in the way PB-10 describes. The clauses on document control, internal audit, management review, nonconformity and competence are satisfied once, by the cross documents in the kit. What is new is the AI policy, the AI inventory, the AI impact assessment and the lifecycle procedures.

| ISO/IEC 42001 area | Kit document or register |
|---|---|
| Context, interested parties, scope (clauses 4.1 to 4.4) | ISMS-PRO-01, ISMS-STM-01 with an AI scope paragraph, ISMS-REG-03 |
| Leadership, AI policy, roles (clause 5) | GOV-POL-01, AI-POL-01, AI-POL-02, GOV-STM-01 |
| Risk assessment and treatment, AI system impact assessment (clauses 6.1.2 to 6.1.4) | AI-PRO-01, AI-REG-02, PIMS-PRO-02 for the personal data dimension, GOV-PRO-05 for scales |
| Objectives and planning (clause 6.2) | ISMS-PLN-01 with AI objectives, GOV-REG-21 |
| Resources, competence, awareness, communication, documents (clause 7) | ISMS-PRO-02, GOV-PRO-08, ISMS-PLN-02, GOV-PRO-01 |
| Operational planning, AI system lifecycle, data, third parties (clause 8) | AI-POL-02, AI-REG-01, AI-REG-03, AI-PRO-02, AI-TPL-01, GOV-PRO-15, GOV-PRO-09 |
| Monitoring, internal audit, management review (clause 9) | ISMS-PRO-04, GOV-PRO-02, GOV-PRO-03 with AI items on the agenda |
| Nonconformity, continual improvement, incidents (clause 10) | GOV-PRO-04, AI-PRO-03, GOV-REG-03 |
| Annex A controls on policies, roles, resources, impact, lifecycle, data, information for parties, use, third parties | Covered across the rows above; record applicability in a Statement of Applicability built the way ISMS-REG-01 is built |

## 3. The NIST AI Risk Management Framework in plain words

The NIST AI RMF is organised around four functions. GOVERN is the culture and structure: policies, accountability, roles, and the decision to treat AI risk as a management matter. MAP is understanding the context: what the system is for, who it affects, what could go wrong, and what the organisation's risk tolerance is. MEASURE is evaluation: choosing metrics, testing the system against them, and tracking how it performs over time, including on fairness, robustness, privacy and security. MANAGE is acting on what was measured: prioritising, treating, monitoring and responding, including planning for incidents and for retirement. The framework describes seven characteristics of trustworthy AI, from validity and safety through explainability and fairness to privacy and accountability, and asks that each be considered rather than prescribing how. A companion playbook, published separately, suggests actions per function.

| NIST AI RMF function | What it asks | Kit document or register |
|---|---|---|
| GOVERN | Policies, roles, accountability, risk tolerance, workforce competence, supply chain awareness | GOV-POL-01, AI-POL-01, AI-POL-02, GOV-PRO-08, AI-PRO-02, AI-REG-04 |
| MAP | Context, intended use, affected parties, benefits and harms, categorisation of the system | AI-REG-01, AI-POL-02 4.1 to 4.2, AI-PRO-01 4.1 to 4.2 and 4.4, PIMS-PRO-02 |
| MEASURE | Metrics, evaluation, testing for trustworthiness characteristics, tracking over time | AI-POL-02 4.6 to 4.7, AI-PRO-01 4.6, AI-REG-03, ISMS-PRO-04 |
| MANAGE | Prioritise and treat risks, monitor, respond to incidents, plan decommissioning | AI-PRO-01 4.5 to 4.8, AI-REG-02, AI-PRO-03, AI-POL-02 4.12, GOV-PRO-24 |

## 4. The EU AI Act in plain words

The EU AI Act is a regulation that applies obligations according to the risk a system poses. Four tiers matter in practice. Prohibited practices are banned outright: examples in the Act include manipulative techniques that cause harm, exploitation of vulnerable groups, social scoring by public authorities, and most real-time remote biometric identification in public spaces. High-risk systems are those used as safety components of regulated products, or those in the listed areas such as biometrics, critical infrastructure, education, employment, access to essential services, law enforcement, migration and justice; these carry obligations on risk management, data governance, technical documentation, logging, transparency to deployers, human oversight, accuracy, robustness and cybersecurity, plus conformity assessment and registration. Limited-risk systems carry transparency duties: people must know they are dealing with an AI system, and synthetic content must be marked. Minimal-risk systems carry no new obligations, and voluntary codes are encouraged. General-purpose AI models carry their own documentation and copyright obligations, with extra duties where a model is classed as posing systemic risk.

The Act distinguishes roles. A provider develops a system or model and places it on the market; a deployer uses a system under its own authority; importers and distributors have narrower duties. Most organisations using this kit are deployers of vendor systems and, for anything they build and sell, providers. A deployer of a high-risk system must use it according to the provider's instructions, keep the logs it generates, assign human oversight to competent people, inform affected workers and individuals, and in some cases complete a fundamental rights impact assessment. Obligations apply in phases over several years from entry into force, with prohibitions first and high-risk duties later; the current timetable is on the public text linked from the resources page.

| EU AI Act obligation (deployer and provider) | Kit document or register |
|---|---|
| Identify the risk class of each system; never build or procure a prohibited practice | AI-POL-02 4.2, AI-REG-01 |
| Risk management system across the lifecycle (high-risk) | AI-PRO-01, AI-REG-02, AI-POL-02 4.3 |
| Data governance for training, validation and test data (high-risk) | AI-POL-02 4.4, AI-REG-03 |
| Technical documentation and record keeping, automatic logging (high-risk) | AI-POL-02 4.7, AI-REG-03, GOV-PRO-14 |
| Human oversight by competent persons | AI-POL-02 4.5, GOV-PRO-08 |
| Accuracy, robustness and cybersecurity | AI-POL-02 4.6 and 4.8, GOV-PRO-15, GOV-PRO-11 |
| Transparency to users and marking of synthetic content | AI-POL-02 4.10, AI-POL-01 4.7 |
| Fundamental rights and data protection impact assessment where required | PIMS-PRO-02, PIMS-TPL-01, AI-PRO-01 4.4 |
| Provider instructions followed, logs kept, vendor obligations understood (deployer) | AI-PRO-02, AI-TPL-01 question 30, GOV-REG-07 |
| Serious incident reporting | AI-PRO-03 4.6, GOV-REG-08 |
| Inform workers and affected individuals; route to contest decisions | AI-POL-01 4.6, AI-POL-02 4.5, PIMS-PRO-03 |

## 5. Where the frameworks overlap with GDPR

Any AI system that processes personal data is already inside the GDPR and ISO/IEC 27701 documents. Three points carry most of the weight. Article 22 limits decisions based solely on automated processing that have legal or similarly significant effects, which is why AI-POL-01 4.6 and AI-POL-02 4.5 require a human decision maker and a route to contest. Article 35 requires a data protection impact assessment for high-risk processing, which for an AI system is run under PIMS-PRO-02 and recorded in PIMS-REG-08, with AI-PRO-01 supplying the AI-specific risks. Article 28 governs the vendor relationship, which is why AI-PRO-02 and AI-TPL-01 insist on processor terms before personal data reaches a model. Privacy by design under Article 25 is applied to AI systems through PIMS-PRO-06 at the Design gate.

## 6. A minimum AI governance set

An organisation that wants a defensible position without a full ISO/IEC 42001 programme needs the following, in this order: AI-REG-04 populated with every tool staff use and AI-POL-01 issued and acknowledged; AI-REG-01 populated with every system that uses a model, each with a class and an owner; AI-PRO-01 run on every system that affects people or handles personal or client data, with results in AI-REG-02; AI-PRO-02 run on every vendor whose model receives data; and AI-PRO-03 adopted so that the first failure is handled on a procedure rather than improvised. AI-POL-02 and the full gate model follow when the organisation builds or sells AI systems. Every item above produces a register row or a signed record, which is what any of the three frameworks will ask to see.

## 7. Related documents

- AI-POL-01 Acceptable use of AI tools policy
- AI-POL-02 AI system development, procurement and deployment policy
- AI-PRO-01 AI risk assessment procedure
- AI-PRO-02 AI vendor and model due diligence procedure
- AI-PRO-03 AI incident and model failure handling procedure
- AI-TPL-01 AI vendor and model questionnaire
- PB-10 Playbook: one control set, several certifications
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- GDPR-GDE-02 Guide: GDPR articles mapped to kit documents and registers
