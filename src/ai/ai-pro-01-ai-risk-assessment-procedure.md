---
id: AI-PRO-01
title: AI Risk Assessment Procedure
type: procedure
framework: ai
maps:
  - ISO/IEC 42001 clause 6.1.2
  - ISO/IEC 42001 clause 6.1.3
  - ISO/IEC 42001 clause 8.2
  - NIST AI RMF MAP
  - NIST AI RMF MEASURE
  - ISO/IEC 27001:2022 clause 6.1.2
  - GDPR Article 35
owner: Information Security Manager
approver: Head of Engineering
classification: Internal
review: Annual
summary: How the risks of an AI system are identified from a standard threat catalogue, scored on the organisation's risk scale with an added impact-on-people rating, treated, tested and recorded in the AI risk register.
---
## 1. Purpose

This procedure produces, for every AI system in AI-REG-01, a set of scored risks with controls and tests that the System Owner can show at the Design and Pre-release gates of AI-POL-02. It uses the same likelihood and impact scales as GOV-PRO-05 so that AI risks sit in the same appetite and escalation path as every other risk, and adds one rating that the general method lacks: the impact on people.

## 2. Scope

It applies to every system recorded or proposed for AI-REG-01, at first design, before each release that passes the Change gate, after any AI incident, and at least annually. It covers systems built in house and vendor services integrated into a workflow. It does not replace the information security risk assessment of the hosting platform, which stays in GOV-REG-05.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| System Owner | Requests the assessment, supplies the system description, owns the resulting risks and treatments. |
| Information Security Manager | Facilitates the assessment, applies the catalogue, confirms scores, records the register entries. |
| Privacy Officer | Rates impact on people, decides whether a DPIA under PIMS-PRO-02 is needed and links it. |
| Head of Engineering | Approves treatment plans and accepts Medium risks with the System Owner. |
| Engineering lead for the system | Designs and runs the tests in 4.6 and records results in AI-REG-03. |

## 4. Procedure

4.1 **Describe the system.** The System Owner provides the AI-REG-01 entry plus: the model and version, who can send inputs (staff, clients, the public, other systems), what the model can read (documents, web pages, databases), what it can do (text only, or actions through tools, with the tool list), how output is used (shown to a person, acted on automatically), and the data in prompts, retrieval and training.

4.2 **Apply the threat catalogue.** The Information Security Manager walks the catalogue below with the System Owner and the engineering lead. Each row that applies becomes one risk scenario in AI-REG-02, written as: a named actor or failure uses a named weakness in the system, with the consequence. Rows that do not apply are recorded as not applicable with a one-line reason. The catalogue draws on the public OWASP Top 10 for LLM Applications and MITRE ATLAS; both are consulted for new techniques at each annual review.

| Threat | What it looks like | Controls to consider | Test |
|---|---|---|---|
| Data leakage through prompts | Staff or users paste confidential or personal data into a tool that retains it, trains on it or shows it to another tenant. | AI-POL-01 limits, tenant settings with training opt-out and short retention, data loss prevention under GOV-PRO-23, redaction before send. | Submit a marked test string and confirm it cannot be retrieved later or by another account. |
| Direct prompt injection | A user crafts input that overrides the system instructions, extracts them, or unlocks prohibited behaviour. | Separate system and user content, constrain output format, limit what the system can reveal, reject instructions in user fields. | Run the agreed injection set and record the rate at which instructions are overridden. |
| Indirect prompt injection | Instructions hidden in a document, web page, email or record the model reads cause it to act against the user. | Treat retrieved content as untrusted, strip or flag instruction-like text, require confirmation for actions, restrict retrieval sources. | Plant instructions in a retrieved item and confirm the model does not follow them. |
| Insecure output handling | Model output is executed, rendered or passed to another system without validation, enabling script injection, command execution or query injection. | Encode and validate output as untrusted input, never execute it directly, use allow-lists for generated commands. | Prompt the model to emit markup, commands and queries and confirm downstream components neutralise them. |
| Training data poisoning | Manipulated training, fine-tuning or retrieval data introduces backdoors, bias or false facts. | Approved data sources under AI-POL-02 4.4, integrity checks, provenance records, held-out evaluation sets. | Compare behaviour on canary cases before and after each data change. |
| Model theft and extraction | Weights, prompts or decision boundaries are copied by insiders, through the interface, or by repeated querying. | Access control under GOV-PRO-10, rate limits, watermarking where available, weights stored as a Restricted asset. | Review access logs for bulk queries; confirm weights are not readable by non-owners. |
| Supply chain of models and plugins | A pre-trained model, library, dataset or plugin contains malicious code, undisclosed data use or a vulnerability. | AI-PRO-02 due diligence, pinned versions, signature verification, vulnerability tracking under GOV-PRO-11. | Verify provenance and version pins; scan dependencies before release. |
| Excessive agency | An agent has more tools, permissions or autonomy than the task needs and takes a harmful action. | Minimum tool list, read-only by default, human confirmation for irreversible actions, spending and rate limits, kill switch. | Attempt out-of-scope actions through the agent and confirm they are refused or require approval. |
| Over-reliance | People accept output without review, so errors reach clients, code or decisions. | Output review duty in AI-POL-01 4.5, confidence or source display, mandatory human decision for affected people. | Sample deliverables for review evidence; test whether reviewers catch planted errors. |
| Bias and harmful output | Output discriminates, defames, misleads or is unsafe for the audience. | Evaluation across relevant groups, content filters, refusal rules, user reporting route. | Run the bias and safety evaluation set; record failure rate per category. |
| Denial of service by expensive inputs | Very long, recursive or adversarial inputs exhaust tokens, budget or capacity. | Input length limits, timeouts, per-user quotas, cost alerts, capacity plan under GOV-PRO-19. | Send maximal inputs at rate and confirm limits trigger before cost or availability is affected. |
| Privacy inference | The model reveals or infers personal data about individuals from training data, retrieval or context, including re-identification. | Minimisation, pseudonymisation, retrieval scoping by user permission, membership inference testing, DPIA. | Query for known individuals in training data; confirm retrieval respects the caller's permissions. |

4.3 **Score likelihood and impact.** The group rates each scenario on the GOV-PRO-05 scales: likelihood within twelve months with current controls, 1 to 5, and impact as the worst credible consequence to [Organisation], 1 to 5. The score is the product and the band follows GOV-PRO-05 4.7: 1 to 4 Low, 5 to 9 Medium, 10 to 15 High, 16 to 25 Critical.

4.4 **Rate impact on people.** The Privacy Officer rates each scenario's impact on individuals, separately from the organisational impact, on the same 1 to 5 scale: 1 inconvenience, 2 minor distress or cost, 3 significant financial, reputational or access harm, 4 discrimination, loss of a service or right, or harm requiring recovery, 5 physical harm, loss of liberty or irreversible harm. An impact-on-people rating of 4 or 5 raises the band by one step regardless of the score, requires a DPIA under PIMS-PRO-02 where personal data is processed, and makes the system a candidate for High class under AI-POL-02 4.2.

4.5 **Treat.** The System Owner chooses Modify, Retain, Avoid or Share for each risk under GOV-PRO-05 4.9 and names the controls, the kit documents that implement them and the target band. Acceptance authority follows the GOV-PRO-05 4.8 table, applied to the raised band from 4.4. No High or Critical risk, and no risk with impact on people of 4 or 5, is accepted without GOV-PRO-24.

4.6 **Test.** For every Modify treatment, the engineering lead runs the test named in the catalogue, or a better one agreed with the Information Security Manager, before the Pre-release gate and after each Change gate. Results with pass thresholds go in AI-REG-03 and the AI-REG-02 row is updated with the residual rating.

4.7 **Record and link.** The Information Security Manager completes the AI-REG-02 rows, cross-references the AI-REG-01 system ID, the DPIA reference in PIMS-REG-08 where one exists, and any platform risks in GOV-REG-05, and reports High and Critical risks to the steering committee under GOV-POL-01.

4.8 **Review.** Each risk is reviewed at the frequency its band sets in GOV-REG-05, after any AI incident under AI-PRO-03, when the model, provider, tool list or data sources change, and annually, when the catalogue is also refreshed against the two public sources named in 4.2.

## 5. Records and evidence

- AI-REG-02 AI risk register: every scenario with scores, impact on people, treatment, owner, residual rating and review dates.
- AI-REG-03 AI change and evaluation log: test results against each treatment.
- PIMS-REG-08 DPIA register: linked assessments.
- GOV-REG-06 Risk acceptance and exception register: accepted High, Critical and people-impact risks.
- Steering committee minutes under GOV-TPL-03 showing High and Critical risks reported.

## 6. Exceptions

A system may be released with an untested treatment only for a pilot approved under AI-POL-02 section 6, with the untested risk recorded as Open in AI-REG-02 and a test date within thirty days. No exception applies to a risk with impact on people of 4 or 5.

## 7. Review and maintenance

The Information Security Manager reviews this procedure and the catalogue annually, after any AI incident, and when OWASP or MITRE publish a revised version of the sources named in 4.2. Scale or band changes are made only in GOV-PRO-05.

## 8. Related documents

- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-REG-05 Information security risk register
- GOV-PRO-24 Exception and risk acceptance procedure
- AI-POL-02 AI system development, procurement and deployment policy
- AI-PRO-02 AI vendor and model due diligence procedure
- AI-PRO-03 AI incident and model failure handling procedure
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- GOV-PRO-23 Information transfer and data loss prevention procedure
