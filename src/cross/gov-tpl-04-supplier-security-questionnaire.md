---
id: GOV-TPL-04
title: Supplier Security and Privacy Questionnaire
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.19
  - ISO/IEC 27001:2022 Annex A 5.20
  - ISO/IEC 27701 clause 7.2.6
  - SOC 2 CC9.2
  - GDPR Article 28
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The questions a supplier answers before it is given information or access, with space for its evidence and a scoring method that produces an approval outcome under GOV-PRO-06.
---
## 1. How to use this questionnaire

*Send sections 2 and 3 to the supplier. The supplier owner sets the tier under GOV-PRO-06 step 4.1 first: Tier 1 and Tier 2 suppliers answer every question; Tier 3 suppliers answer domains 3.1, 3.3, 3.6 and 3.11 only. The supplier writes its answer in the Answer column and names the document, export or screenshot it attaches in the Evidence column. An answer without evidence scores lower than an answer with it. The reviewer completes sections 4 and 5. Questions marked with an asterisk are critical: a score of 0 on a critical question blocks approval for Tier 1 and Tier 2 until the gap is remediated or an exception is accepted under GOV-PRO-24.*

## 2. Supplier and service details

| Field | Entry |
|---|---|
| Supplier legal name | [Supplier] |
| Service to be provided | [Service] |
| Supplier owner at [Organisation] | [Role] |
| Tier assigned | [Tier] |
| Information the supplier will hold or access | [Classification and description] |
| Personal data involved | Yes / No. *If yes, section 3.10 is mandatory and processor terms are required before any data is shared.* |
| Supplier contact completing this questionnaire | [Role] |
| Date returned | [Date] |

## 3. Questions

### 3.1 Organisation and governance

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 1* | Do you have an approved information security policy, and who in your management is accountable for information security? | | |
| 2 | Do you have a named person or role responsible for data protection, and how can [Organisation] contact them? | | |
| 3 | How do you screen staff and contractors before they are given access to client information, and what confidentiality obligations do they sign? | | |
| 4 | How often do your staff complete security and privacy training, and how do you record completion? | | |

### 3.2 Certifications and independent assurance

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 5* | Which independent certifications or attestation reports do you hold that cover the service you will provide, and what is the scope and expiry of each? | | |
| 6 | When was the service last tested by an independent penetration tester, and were all high and critical findings closed? | | |
| 7 | Do you run an internal audit programme over your security controls, and how are findings tracked to closure? | | |
| 8 | Will you provide [Organisation] with renewed certificates or reports each year, and on request after a significant change? | | |

### 3.3 Access control

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 9* | Is multi-factor authentication enforced for all your staff access to systems that hold client information, including administrative and remote access? | | |
| 10* | How do you restrict your staff's access to [Organisation]'s information to those who need it for their role, and how often is that access reviewed? | | |
| 11 | How quickly is access removed when a member of your staff leaves or changes role? | | |
| 12 | How does the service separate [Organisation]'s data and users from those of your other clients? | | |
| 13 | Does the service support single sign-on from [Organisation]'s identity provider and role-based permissions that [Organisation] administers? | | |

### 3.4 Encryption

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 14* | Is all client data encrypted in transit using current protocol versions, with obsolete versions disabled? | | |
| 15* | Is all client data, including backups and snapshots, encrypted at rest? | | |
| 16 | How are encryption keys generated, stored, rotated and protected, and who can access them? | | |
| 17 | Can [Organisation] hold or control its own keys, and what happens to encrypted data when a key is revoked? | | |

### 3.5 Logging and monitoring

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 18 | Which security events do you log for the service, and for how long are logs retained? | | |
| 19 | Who reviews logs and alerts, how often, and is monitoring in place outside working hours? | | |
| 20 | Can [Organisation] obtain audit logs of actions on its own data and users, and in what format? | | |
| 21 | How do you detect and respond to vulnerabilities in the service, and what are your remediation timescales by severity? | | |

### 3.6 Incident management

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 22* | Within how many hours of becoming aware will you notify [Organisation] of a security incident or personal data breach affecting its information? | | |
| 23 | Do you have a documented incident response procedure with defined severities and roles, and when was it last exercised? | | |
| 24 | What information will your notification contain, and who at your organisation will be the point of contact during an incident? | | |
| 25 | Have you had a security incident affecting client data in the last three years, and what changed as a result? | | |

### 3.7 Business continuity and resilience

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 26 | What availability commitment do you give for the service, and how has it performed over the last twelve months? | | |
| 27* | How often is client data backed up, where are backups stored, and when was a restore last tested? | | |
| 28 | Do you have a business continuity and disaster recovery plan for the service, with recovery time and recovery point objectives, and when was it last tested? | | |
| 29 | What single points of failure exist in the service, including dependence on your own suppliers? | | |

### 3.8 Sub-processors and supply chain

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 30* | Which third parties, including hosting providers, will access or process [Organisation]'s information in delivering the service? | | |
| 31 | How do you assess those third parties before use, and do your contracts with them flow down the obligations you owe to [Organisation]? | | |
| 32 | How will you notify [Organisation] before adding or changing a third party, and can [Organisation] object? | | |
| 33 | How do you manage the security of the software components and open source libraries used in the service? | | |

### 3.9 Data location and transfers

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 34* | In which countries or regions will [Organisation]'s information be stored, processed and accessed, including for support and backups? | | |
| 35 | Can [Organisation] restrict storage and processing to a named region, and is that restriction contractual? | | |
| 36 | Where information leaves the region, which transfer mechanism applies, and will you support a transfer impact assessment? | | |

### 3.10 Personal data handling

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 37* | Will you sign processor terms that meet GDPR Article 28, or provide your own terms for review, before any personal data is shared? | | |
| 38 | Do you use client personal data for any purpose of your own, including analytics, product improvement or training of models? | | |
| 39 | How will you assist [Organisation] with requests from individuals, such as access, correction, deletion and export, and within what time? | | |
| 40 | How do you apply retention and deletion to personal data in the service, including in backups and logs? | | |
| 41 | Do you maintain a record of your processing activities for this service and can you provide the relevant extract? | | |

### 3.11 Exit and data return

| No. | Question | Answer | Evidence |
|---|---|---|---|
| 42* | At the end of the contract, in what format and within what time will you return [Organisation]'s information? | | |
| 43* | How and when will you delete [Organisation]'s information, including backups, and will you certify deletion in writing? | | |
| 44 | What notice do you give before discontinuing the service or changing its terms materially? | | |
| 45 | Can [Organisation] export its data at any time during the contract without your assistance? | | |

## 4. Scoring note

*The reviewer scores each question from 0 to 3.*

| Score | Meaning |
|---|---|
| 0 | Control not in place, no answer, or answer contradicted by evidence |
| 1 | Control described as partly in place, no evidence provided |
| 2 | Control described as in place, evidence described but not provided or not conclusive |
| 3 | Control in place and supported by evidence the reviewer has seen |

*Mark a question Not applicable only where the reviewer agrees, and remove it from the denominator. Domain score is the sum of scores divided by three times the number of applicable questions, as a percentage. Overall score is the average of the domain percentages, so that each domain weighs equally. Outcome: 80 per cent or more is Approved; 60 to 79 per cent is Conditional, with a remediation plan and dates written into the contract; below 60 per cent is Not approved. Any critical question scored 0 overrides the percentage for Tier 1 and Tier 2 and blocks approval until it is remediated or an exception is accepted.*

## 5. Reviewer assessment

| Domain | Score (per cent) | Critical gaps | Notes |
|---|---|---|---|
| 3.1 Organisation and governance | | | |
| 3.2 Certifications and assurance | | | |
| 3.3 Access control | | | |
| 3.4 Encryption | | | |
| 3.5 Logging and monitoring | | | |
| 3.6 Incident management | | | |
| 3.7 Business continuity | | | |
| 3.8 Sub-processors | | | |
| 3.9 Data location | | | |
| 3.10 Personal data | | | |
| 3.11 Exit | | | |
| Overall | | | |

| Field | Entry |
|---|---|
| Outcome | Approved / Conditional / Not approved |
| Conditions and dates | [Conditions] |
| Exceptions accepted (GOV-REG-06 reference) | [Reference] |
| Processor terms required | Yes / No. *Reference PIMS-TPL-02 or the supplier's terms reviewed.* |
| Reviewed by | Information Security Manager, [Date] |
| Privacy review by | Privacy Officer, [Date] |
| GOV-REG-07 entry updated | [Date] |
| Next review due | [Date] |
