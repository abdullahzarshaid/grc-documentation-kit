---
id: AI-POL-01
title: Acceptable Use of AI Tools Policy
type: policy
framework: ai
maps:
  - ISO/IEC 42001 clause 6.1.4
  - ISO/IEC 42001 clause 7.3
  - NIST AI RMF GOVERN
  - GDPR Article 5
  - GDPR Article 32
  - ISO/IEC 27001:2022 Annex A 5.10
  - ISO/IEC 27001:2022 Annex A 5.12
  - SOC 2 CC6.7
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The rules for staff use of generative and assistive AI tools at work, covering which tools are approved, what may never be entered into them, how output is checked, and how use is recorded and disclosed.
---
## 1. Purpose

This policy lets staff gain the benefit of AI tools without leaking information, breaching a contract or a privacy obligation, or presenting unchecked output as finished work. It sets a short list of approved tools, a shorter list of things that must never be entered, and a single accountability rule: the person who uses the output owns it.

## 2. Scope

It applies to every employee, contractor and temporary worker of [Organisation], on every device, for every tool that generates, summarises, translates, classifies or transforms text, code, images, audio or data using a trained model. This includes stand-alone assistants, features embedded in office, development, browser and meeting software, and models called through an interface by internal scripts. Development and procurement of AI systems that [Organisation] builds or sells is governed by AI-POL-02; this policy covers the use of tools by people.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Chief Executive Officer | Approves this policy and the prohibited uses in 4.8. |
| Information Security Manager | Maintains the approved tool list in AI-REG-04, assesses new tool requests with the Privacy Officer, runs the annual review and investigates reported misuse. |
| Privacy Officer | Confirms the personal data conditions for each approved tool and advises on client disclosure. |
| Line manager | Confirms that staff in their team have completed the training in 4.10 and that client contracts permit the intended use. |
| Tool owner | A named role for each approved tool: configures the tenant settings in 4.2, reviews usage and removes leavers. |
| All staff | Use only approved tools, within the approved uses and prohibited-data limits in AI-REG-04, and review every output before relying on it. |

## 4. Policy statements

4.1 **Approved tools only.** Staff use an AI tool for work only when it is listed as Approved in AI-REG-04 AI tool approval register, for the uses recorded there. A tool not on the list, or a free personal account for a tool that is on the list, is not approved. Requests for a new tool or a new use go to the Information Security Manager, who records the decision in AI-REG-04 within ten working days.

4.2 **Tenant settings.** The tool owner configures each approved tool so that prompts and outputs are not used to train the provider's models, retention of prompt history is the shortest the provider offers, access is through single sign-on with multi-factor authentication under GOV-POL-06, and administrative logs are available to the Information Security Manager. The settings are recorded in AI-REG-04 and re-checked at each review.

4.3 **Information that must never be entered.** Staff do not enter into any AI tool, including an approved one: personal data of customers, employees or any other person unless AI-REG-04 records that the tool is approved for that category and a processor agreement under PIMS-TPL-02 is in place; information classified Confidential or Restricted under GOV-PRO-16 belonging to a client, unless the client has agreed in writing; passwords, keys, tokens, certificates and connection strings; source code of [Organisation] or a client unless the tool is approved for code and the repository owner has agreed; security findings, incident details and vulnerability reports before the affected party has been notified; and information subject to legal privilege or a non-disclosure agreement that forbids third party processing.

4.4 **Personal data.** Where AI-REG-04 permits personal data in a tool, staff enter the minimum needed for the task, use anonymised or pseudonymised extracts where the task allows, and record the processing in PIMS-REG-01 through the Privacy Officer. Special category data is never entered without a documented assessment under PIMS-PRO-02.

4.5 **Output review and accountability.** The person who uses an AI output is accountable for it as if they had written it. Before output is sent to a client, published, committed to a repository, or used to make a decision about a person, the user checks it for factual accuracy, for content copied from a third party, for secrets or personal data the model may have reproduced, and for code defects or insecure patterns. Code produced with AI assistance passes the same review and testing steps as any other change under GOV-PRO-15 and GOV-PRO-09.

4.6 **Decisions about people.** No AI tool makes or materially shapes a decision about recruitment, performance, discipline, pay, credit or access to a service without a named person reviewing the output and recording the decision as their own. Any use of this kind is recorded in AI-REG-01 and assessed under AI-PRO-01 and, where personal data is involved, PIMS-PRO-02.

4.7 **Disclosure.** Where a client contract, a tender or a professional standard requires it, the engagement lead tells the client in writing which approved tools will be used on their work and for what. A client's written refusal is recorded in AI-REG-04 against the engagement and respected by everyone on it.

4.8 **Prohibited uses.** Staff do not use any AI tool to: generate content that impersonates a real person or organisation; create or test malicious code outside an authorised engagement with a signed scope; produce material that is discriminatory, harassing or unlawful; circumvent a client's or [Organisation]'s security controls; or process data in a jurisdiction that a contract or PIMS-POL-03 forbids.

4.9 **Records of use.** Where output forms part of a deliverable, a decision record or a code change, the user keeps the prompt and output, or the tool's conversation link, with the working papers for that item for the retention period in PIMS-POL-02. Tool owners export administrative usage logs quarterly and keep them under GOV-PRO-14.

4.10 **Training.** Every person completes the AI tool module under GOV-PRO-08 before first use and annually thereafter, and the completion is recorded in GOV-REG-09. The module covers this policy, the prohibited-data list, prompt injection through documents and web pages, and how to report a suspected leak.

4.11 **Reporting.** Anyone who enters information in breach of 4.3, or sees output that reveals another party's data, reports it the same working day under GOV-PRO-07. The Information Security Manager treats such a report as a potential personal data breach under PIMS-PRO-04 and follows AI-PRO-03.

4.12 **Consequences.** Breach of this policy is handled under the disciplinary process referenced in GOV-PRO-18. Entering credentials or client confidential material into an unapproved tool is treated as a serious breach.

## 5. Records and evidence

- AI-REG-04 AI tool approval register: the approved tools, uses, prohibited data, tenant settings, approver and review dates.
- AI-REG-01 AI system inventory: entries for tools used in decisions about people.
- GOV-REG-09 Training and awareness register: completion of the AI tool module.
- GOV-REG-23 Policy acknowledgement register: annual acknowledgement of this policy.
- Administrative usage logs exported under 4.9.
- Incident records under GOV-REG-08 for reports made under 4.11.

## 6. Exceptions

An exception to 4.1 or 4.3 is granted only under GOV-PRO-24, in writing, for a named person, tool, purpose and period not exceeding ninety days, and is recorded in GOV-REG-06. No exception is available for entering credentials or for the prohibited uses in 4.8.

## 7. Review and maintenance

The Information Security Manager reviews this policy annually, when a tool is added to or removed from AI-REG-04, after any incident involving an AI tool, and when a client contract or a law introduces a new condition on AI use. Changes follow GOV-PRO-01.

## 8. Related documents

- AI-POL-02 AI system development, procurement and deployment policy
- AI-PRO-01 AI risk assessment procedure
- AI-PRO-02 AI vendor and model due diligence procedure
- AI-PRO-03 AI incident and model failure handling procedure
- AI-REG-04 AI tool approval register
- GOV-POL-02 Acceptable use policy
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-PRO-23 Information transfer and data loss prevention procedure
- PIMS-PRO-02 Privacy risk and data protection impact assessment procedure
- PIMS-TPL-02 Data processing agreement template
