---
id: AI-TPL-01
title: AI Vendor and Model Questionnaire
type: template
framework: ai
maps:
  - ISO/IEC 42001 clause 8.4
  - GDPR Article 28
  - ISO/IEC 27001:2022 Annex A 5.19
  - SOC 2 CC9.2
owner: Information Security Manager
approver: Head of Engineering
classification: Internal
review: Annual
summary: The thirty questions sent to a vendor of an AI service or model under AI-PRO-02, with columns for the vendor's answer, the evidence supplied, and the reviewer's verdict.
---
## 1. How to use this questionnaire

*Send sections 2 to 8 to the vendor with the cover details completed. Ask for an answer to every question and a piece of evidence for each: a contract clause, a documentation page, a configuration screenshot, a report or a signed statement. Do not accept "yes" without evidence for Tier 2 and Tier 3 assessments under AI-PRO-02. The reviewer completes the verdict column (Acceptable, Acceptable with condition, Blocking) and the verification note after the vendor returns the form. File the completed form with the AI-REG-04 or AI-REG-01 entry.*

| Field | Entry |
|---|---|
| Vendor | [Vendor name as recorded in GOV-REG-07] |
| Service or model | [Service name, model name and version] |
| Requested by | [Role] |
| Intended use | [One or two sentences] |
| Data categories to be sent | [None, Internal, Client confidential, Personal, Special category] |
| Tier under AI-PRO-02 | [1, 2 or 3] |
| Date sent and date returned | [Date], [Date] |

## 2. Use of customer data for training

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 1 | Are inputs, prompts, uploaded files or outputs from our account used to train, fine-tune or otherwise improve your models or any third party's models? | | |
| 2 | If such use is possible, is there an opt-out, is it enforceable at the account or contract level rather than per user, and is it on by default for business accounts? | | |
| 3 | Are our inputs or outputs ever reviewed by your staff or contractors, and under what conditions (for example abuse monitoring)? How are reviewers vetted and bound? | | |
| 4 | Which model versions are offered, how are version changes announced, and can we pin a version for a stated period? | | |

## 3. Retention of prompts, files and outputs

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 5 | How long are prompts, uploaded files, conversation history and outputs retained on your systems by default, and what is the shortest retention we can configure? | | |
| 6 | Can we delete individual items, a user's history or the whole account's data on demand, and how long until deletion is complete across backups? | | |
| 7 | Are any derived artefacts kept after deletion (embeddings, logs, abuse records, fine-tuned weights), for how long, and for what purpose? | | |
| 8 | What is deleted, and confirmed in writing, when the contract ends? | | |

## 4. Location and transfers

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 9 | In which countries or regions are inputs processed and stored, including inference, logging and backups? Can processing be restricted to a region we choose? | | |
| 10 | Which legal mechanisms cover transfers of personal data outside the region in which we contract (for example standard contractual clauses or an adequacy decision)? | | |
| 11 | Can government or law enforcement access to our data be requested in any processing location, and what is your policy for notifying us? | | |

## 5. Sub-processors and supply chain

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 12 | List every sub-processor that may receive our inputs or outputs, including the underlying model provider and hosting provider, with location and role. | | |
| 13 | How are we notified of sub-processor changes, with how much notice, and can we object? | | |
| 14 | For the model itself: who trained it, what is its licence, and what is publicly stated about its training data sources and cut-off? | | |
| 15 | For plugins, tools, connectors or extensions available in the service: are they vetted, can we restrict which ones our users may enable, and are third party plugins bound by the same terms as you? | | |

## 6. Security

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 16 | Which independent assurance do you hold for the service (for example an attestation report or a management system certificate), what is the scope and period, and may we have the report? | | |
| 17 | How is tenant isolation implemented so that one customer's prompts, files, retrieval indexes and fine-tuned models cannot be reached by another? | | |
| 18 | Which authentication options are supported (single sign-on, multi-factor, service credentials), and can administrators enforce them for all users? | | |
| 19 | Which administrative and audit logs are available to us (user activity, data exports, configuration changes), for how long, and in what format? | | |
| 20 | Is data encrypted in transit and at rest, who holds the keys, and can we supply our own? | | |
| 21 | How are vulnerabilities in the service and in the model handled: disclosure route, patch timescales, and how customers are told? | | |
| 22 | What controls exist against prompt injection, retrieval of other customers' data, and extraction of system instructions, and how were they tested? | | |
| 23 | Within what time are customers notified of a security incident or personal data breach affecting their data, and through which channel? | | |

## 7. Model behaviour and evaluation evidence

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 24 | What is the model's intended use, and which uses do you state as out of scope or unsupported? | | |
| 25 | What documentation describes the model's known limitations, failure modes and the groups or languages on which performance is weaker? | | |
| 26 | Which evaluations have been performed for accuracy, robustness to adversarial input, bias and harmful output, by whom, and may we see the results? | | |
| 27 | Which content safety controls operate on inputs and outputs, can we adjust them, and are refusals and filtered events visible to us? | | |
| 28 | Can we export our prompts, outputs and configuration in a usable format so that we can move to another provider? | | |

## 8. Contract and compliance

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 29 | Do you offer processor terms that meet the requirements of GDPR Article 28, including instructions, confidentiality, assistance with data subject rights and audit rights, and will you sign ours (PIMS-TPL-02) if yours are not adequate? | | |
| 30 | Which obligations under the EU AI Act or comparable laws do you take on as provider of the model or system, and which do you pass to us as deployer? Where is this stated in the contract? | | |

## 9. Reviewer assessment

*Completed by [Organisation] after return. One row per question with a verdict; the Blocking conditions are listed in AI-PRO-02 4.3.*

| No. | Verdict | Verification performed | Reviewer (role) |
|---|---|---|---|
| 1 to 4 | | | |
| 5 to 8 | | | |
| 9 to 11 | | | |
| 12 to 15 | | | |
| 16 to 23 | | | |
| 24 to 28 | | | |
| 29 to 30 | | | |

| Decision | Entry |
|---|---|
| Decision (Approved, Approved with conditions, Rejected) | |
| Conditions, owner and due date | |
| Required configuration before first use | |
| Approver (role) and date | [Role], [Date] |
| Register entry | [AI-REG-04 or AI-REG-01 reference] |
| Next review date | [Date] |

## 10. Related documents

- AI-PRO-02 AI vendor and model due diligence procedure
- AI-POL-01 Acceptable use of AI tools policy
- AI-POL-02 AI system development, procurement and deployment policy
- GOV-TPL-04 Supplier security and privacy questionnaire
- PIMS-TPL-02 Data processing agreement template
