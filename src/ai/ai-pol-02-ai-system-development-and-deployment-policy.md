---
id: AI-POL-02
title: AI System Development, Procurement and Deployment Policy
type: policy
framework: ai
maps:
  - ISO/IEC 42001 clause 6.1
  - ISO/IEC 42001 clause 8.1
  - ISO/IEC 42001 clause 8.2
  - ISO/IEC 42001 clause 8.4
  - NIST AI RMF MAP
  - NIST AI RMF MEASURE
  - NIST AI RMF MANAGE
  - GDPR Article 22
  - GDPR Article 25
  - ISO/IEC 27001:2022 Annex A 8.25
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The lifecycle rules for any AI system [Organisation] builds, buys or embeds in a product or service, from risk classification through data governance, human oversight, evaluation and logging to incident handling and decommissioning.
---
## 1. Purpose

This policy sets the conditions under which an AI system may be developed, procured, deployed and retired, so that every system has a known risk class, an owner, a tested behaviour, a person who can intervene, and a record of what it did. It applies the same lifecycle gates whether the model is trained in house, fine-tuned, called from a vendor service or bought inside a product.

## 2. Scope

It applies to every system that uses a trained model to produce predictions, content, recommendations, classifications or decisions, and that [Organisation] operates, sells, embeds in a product, or runs on behalf of a client. It covers internal tools built by staff on a vendor model, product features, autonomous agents that call tools, and vendor services integrated into a workflow. Personal use of assistive tools by staff is governed by AI-POL-01.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves deployment of any system classed High in 4.2 and any system that makes decisions about people. |
| Head of Engineering | Owns this policy, the lifecycle gates and the evaluation standard. |
| System Owner | Accountable for one AI system: its entry in AI-REG-01, its risk assessment, its evaluation results, its monitoring and its decommissioning. |
| Information Security Manager | Runs AI-PRO-01 with the System Owner and confirms the security controls at each gate. |
| Privacy Officer | Decides whether a DPIA is required under PIMS-PRO-02 and signs off data governance in 4.4. |
| Internal Auditor | Tests a sample of systems against this policy each year. |

## 4. Policy statements

4.1 **Inventory.** No AI system is used in production, or exposed to clients or the public, until the System Owner has recorded it in AI-REG-01 AI system inventory with its purpose, model and provider, hosting location, inputs, outputs, personal data flag and risk class.

4.2 **Risk classification.** The System Owner classifies each system before design starts, using the risk categories of the EU AI Act as the reference scale even where the Act does not apply: Prohibited (practices the Act bans, which [Organisation] never builds or procures), High (systems in the Act's listed high-risk areas, including employment, credit, education, essential services, law enforcement and safety components), Limited (systems that interact with people or generate synthetic content and carry transparency duties), and Minimal (everything else). General-purpose models used as components are recorded with their provider's obligations noted. The class is confirmed by the Information Security Manager and recorded in AI-REG-01.

4.3 **Lifecycle gates.** Every system passes four gates, each recorded in AI-REG-03: Concept (purpose, class, intended users, owner approved), Design (AI-PRO-01 risk assessment complete, data sources approved under 4.4, oversight design under 4.5 agreed), Pre-release (evaluation under 4.6 passed, logging under 4.7 verified, go-live gate PB-07 passed where a product is involved), and Change (any change to model, prompt template, training data, tools the model can call, or decision threshold re-passes the evaluation before release). High class systems also require Chief Executive Officer approval at Pre-release.

4.4 **Data governance.** For training, fine-tuning, retrieval and prompt construction, the System Owner records in AI-REG-03 the source of every dataset, its licence or legal basis, whether it contains personal data, how it was cleaned and labelled, and who approved its use. Personal data is used only with a lawful basis confirmed by the Privacy Officer and, for High class or decisions about people, a DPIA under PIMS-PRO-02 recorded in PIMS-REG-08. Client data is never used to train or fine-tune a model without the client's written agreement. Prompts, retrieved documents and outputs are classified and handled under GOV-PRO-16.

4.5 **Human oversight.** Every system has a named person who can pause it, override an output and roll back a release within the time stated in its AI-REG-01 entry. A system that affects a person's rights, access to a service, employment or finances presents its output as a recommendation to a human decision maker, who records the decision, and the person affected is told that an automated system was involved and how to contest the outcome. Agents that execute actions operate only with the permissions, tool list and spending limits approved at the Design gate.

4.6 **Evaluation.** Before release and after every Change gate, the System Owner runs the evaluation set agreed at Design: task accuracy against a held-out set, behaviour on the adversarial cases from AI-PRO-01 (prompt injection, data extraction, unsafe output, excessive agency), bias checks across the groups relevant to the use, and performance under load and malformed input. Results, the pass thresholds and the approver are recorded in AI-REG-03. A system that fails a threshold is not released.

4.7 **Logging and monitoring.** Each system logs, with a timestamp and the calling identity: inputs (or a hash where inputs are sensitive), outputs, model version, tools invoked and overrides by a human. Logs are retained under GOV-PRO-14 for at least the period in PIMS-POL-02. The System Owner reviews drift, error rates, refusal rates and user complaints monthly and records the review in AI-REG-03.

4.8 **Security.** AI systems follow GOV-PRO-15 for development, GOV-PRO-09 for change, GOV-PRO-11 for vulnerabilities in models, libraries and plugins, and GOV-PRO-26 where hosted in cloud services. Model weights, prompt templates and evaluation sets are assets in GOV-REG-10 with an owner and classification.

4.9 **Procurement.** A vendor model or AI service is used only after AI-PRO-02 due diligence, recorded in GOV-REG-07 and, where personal data is processed, in PIMS-REG-06.

4.10 **Transparency.** Users of a Limited or High class system are told they are interacting with an AI system, synthetic content is labelled where a person could mistake it for human-made, and product documentation states the system's intended use and known limitations.

4.11 **Incidents.** Harmful output, leakage, drift beyond threshold, abuse or a safety event is handled under AI-PRO-03, with GOV-PRO-07 and PIMS-PRO-04 where applicable.

4.12 **Decommissioning.** When a system is retired, the System Owner removes it from production, deletes or archives training data, logs and model artefacts under PIMS-POL-02, revokes its credentials and tool permissions, informs affected users, and marks the AI-REG-01 entry Retired with the date.

## 5. Records and evidence

- AI-REG-01 AI system inventory: one row per system with class, owner, approval and review dates.
- AI-REG-02 AI risk register: risks and treatments from AI-PRO-01.
- AI-REG-03 AI change and evaluation log: gate approvals, data approvals, evaluation results, monitoring reviews and rollbacks.
- PIMS-REG-08 DPIA register: assessments for systems processing personal data.
- GOV-REG-07 Supplier register and PIMS-REG-06 Processor and sub-processor register: vendor models and services.
- GOV-REG-29 Go-live gate checklist for product releases.

## 6. Exceptions

A gate may be bypassed only for a time-limited pilot with no client, public or decision-about-people exposure, approved in writing by the Head of Engineering and recorded in GOV-REG-06 under GOV-PRO-24 for at most ninety days. No exception is available for Prohibited practices, for 4.5 on systems affecting people, or for 4.7.

## 7. Review and maintenance

The Head of Engineering reviews this policy annually, after any AI incident, when the EU AI Act or a comparable law changes an obligation that applies to [Organisation], and when a new class of system is proposed. Changes follow GOV-PRO-01.

## 8. Related documents

- AI-POL-01 Acceptable use of AI tools policy
- AI-PRO-01 AI risk assessment procedure
- AI-PRO-02 AI vendor and model due diligence procedure
- AI-PRO-03 AI incident and model failure handling procedure
- AI-GDE-01 Guide: AI governance frameworks mapped to the kit
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-09 Change management procedure
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-PRO-06 Privacy by design and by default procedure
- PB-07 Playbook: the go-live security and privacy gate for a software project
