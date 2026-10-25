---
id: AI-PRO-02
title: AI Vendor and Model Due Diligence Procedure
type: procedure
framework: ai
maps:
  - ISO/IEC 42001 clause 8.4
  - ISO/IEC 42001 clause 6.1.2
  - NIST AI RMF MAP
  - GDPR Article 28
  - ISO/IEC 27001:2022 Annex A 5.19
  - ISO/IEC 27001:2022 Annex A 5.20
  - SOC 2 CC9.2
owner: Information Security Manager
approver: Head of Engineering
classification: Internal
review: Annual
summary: How a vendor AI service, hosted model or pre-trained model is assessed before it is approved for staff use or integrated into a system, what the vendor must answer and evidence, and how the decision is recorded.
---
## 1. Purpose

This procedure answers the questions that matter before a model or AI service touches [Organisation]'s data: whether the vendor trains on customer inputs, how long prompts and outputs are kept and where, who else processes them, how the service is secured, and what evidence exists that the model behaves as claimed. It produces a documented decision that AI-POL-01 and AI-POL-02 require before approval.

## 2. Scope

It applies to every hosted AI service, interface to a model, embedded AI feature in a product [Organisation] already uses, and pre-trained or open-weight model downloaded for internal use, whether paid or free. It runs alongside GOV-PRO-06, which covers the vendor's general security; this procedure adds the model-specific questions. A new version of an approved model from the same vendor is re-assessed only for the questions whose answers could change (section 4.8).

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Requester | Describes the intended use, data involved and users, and names the business owner. |
| Information Security Manager | Runs the assessment, sends AI-TPL-01, reviews answers and evidence, records the decision. |
| Privacy Officer | Reviews personal data, retention, location, sub-processor and contract answers; confirms processor terms under PIMS-TPL-02. |
| Head of Engineering | Reviews evaluation evidence and integration security for systems under AI-POL-02; approves or rejects. |
| Legal or contracts role | Reviews terms of use, licence of model weights, liability and intellectual property clauses. |
| Tool owner or System Owner | Implements the approved configuration and owns the ongoing review. |

## 4. Procedure

4.1 **Request.** The requester submits the intended use, the categories of data that will be sent to the service (none, internal, client confidential, personal, special category), who will use it, whether output will be acted on automatically, and the expected volume. The Information Security Manager assigns a tier: Tier 1 where no personal or confidential data is sent and output is reviewed by a person; Tier 2 where confidential or personal data is sent or output is acted on automatically; Tier 3 where special category data, decisions about people, or a High class system under AI-POL-02 is involved.

4.2 **Gather.** The Information Security Manager obtains the vendor's published documentation on data use, retention, security and model behaviour, and sends AI-TPL-01 AI vendor and model questionnaire to the vendor for Tier 2 and Tier 3. For Tier 1, published documentation may answer the questionnaire if the Information Security Manager completes it from those sources and records the source for each answer. GOV-TPL-04 is sent in parallel where the vendor is not already in GOV-REG-07.

4.3 **Review the answers.** The reviewers named in section 3 each check their questions in AI-TPL-01 and record a verdict per question: Acceptable, Acceptable with condition, or Blocking. The following are Blocking for Tier 2 and Tier 3 unless an exception is approved under section 6: customer inputs used to train the vendor's models without an opt-out that [Organisation] can enforce; prompt or output retention that cannot be set to thirty days or less or that is not stated; processing locations or sub-processors that cannot be named; no processor agreement where personal data is sent; no independent security assurance report or equivalent evidence; no statement of the model's intended use, limitations and known failure modes.

4.4 **Verify.** For Tier 2 and Tier 3 the Information Security Manager verifies the key answers rather than accepting them: confirms the training opt-out and retention settings in the actual tenant or contract, reads the processor terms, reads the assurance report under SOC-PRO-02, and runs a short technical check that the service refuses a planted secret on retrieval and applies the stated rate and length limits. Results are recorded against the questionnaire.

4.5 **Risk assess.** For a service that becomes part of a system, the Information Security Manager runs AI-PRO-01 with the questionnaire as input. For a staff tool, the supply chain, data leakage and privacy inference rows of the AI-PRO-01 catalogue are assessed and recorded in AI-REG-02.

4.6 **Decide.** The Head of Engineering (for systems) or the Information Security Manager with the Privacy Officer (for staff tools) records one decision: Approved, Approved with conditions (listed, with an owner and date), or Rejected. Tier 3 decisions are also approved by the Chief Executive Officer. The decision, tier, approved uses, prohibited data and required configuration are written to AI-REG-04 for a tool, and to AI-REG-01 and GOV-REG-07 for a system component. Where personal data is processed the vendor is also entered in PIMS-REG-06 with the processor agreement reference.

4.7 **Configure.** The tool owner or System Owner applies the approved configuration (training opt-out, retention, single sign-on, logging, allowed regions, rate limits) before first use and records a screenshot or export of the settings with the AI-REG-04 or AI-REG-01 entry.

4.8 **Re-assess.** The Information Security Manager repeats 4.2 to 4.6 annually for Tier 2 and Tier 3 and every two years for Tier 1, and sooner when the vendor changes its terms, data use, sub-processors or model version in a way that changes an answer, when an incident involves the vendor, or when a contract or law adds a requirement. A model version change within an approved service is re-assessed on questions 4 to 7 and 24 to 30 of AI-TPL-01 only, unless the answers reveal a wider change.

4.9 **Exit.** When a service is withdrawn or rejected after use, the Information Security Manager obtains the vendor's confirmation of deletion of retained prompts, outputs and any fine-tuned artefacts, records it in AI-REG-04 or AI-REG-01, and revokes credentials under GOV-PRO-10.

## 5. Records and evidence

- Completed AI-TPL-01 questionnaires with per-question verdicts and verification notes.
- AI-REG-04 AI tool approval register: decision, tier, conditions, configuration evidence, review dates for staff tools.
- AI-REG-01 AI system inventory and GOV-REG-07 Supplier register: entries for vendor models used in systems.
- PIMS-REG-06 Processor and sub-processor register: vendors processing personal data, with agreement references.
- AI-REG-02 AI risk register: supply chain and leakage risks for each approved vendor.
- Deletion confirmations on exit.

## 6. Exceptions

A Blocking answer in 4.3 is overridden only by GOV-PRO-24 with a written risk acceptance by the Head of Engineering, limited to ninety days and to a stated use, recorded in GOV-REG-06. The absence of processor terms where personal data is sent cannot be excepted.

## 7. Review and maintenance

The Information Security Manager reviews this procedure and AI-TPL-01 annually, after any incident involving a vendor AI service, and when a law or client contract introduces a new vendor obligation. Changes follow GOV-PRO-01.

## 8. Related documents

- AI-TPL-01 AI vendor and model questionnaire
- AI-POL-01 Acceptable use of AI tools policy
- AI-POL-02 AI system development, procurement and deployment policy
- AI-PRO-01 AI risk assessment procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-TPL-04 Supplier security and privacy questionnaire
- SOC-PRO-02 Subservice organisation and vendor assurance report review procedure
- PIMS-TPL-02 Data processing agreement template
- PIMS-POL-03 International transfer policy
