---
id: GDPR-TPL-08
title: Transfer impact assessment template
type: template
framework: gdpr
maps:
  - GDPR Article 44
  - GDPR Article 45
  - GDPR Article 46
  - GDPR Article 49
  - ISO/IEC 27701 Annex A 7.5.1
  - ISO/IEC 27701 Annex B 8.5.1
owner: Privacy Officer
approver: Privacy Officer
classification: Confidential
review: Annual
summary: The assessment completed under PIMS-POL-03 before personal data is transferred to a country without an adequacy decision on the strength of contractual or corporate safeguards, recording the importer, the destination law, the risk to the data, the supplementary measures and the decision.
---
*Guidance notes are in italics. Complete one assessment per transfer or per group of transfers to the same importer under the same safeguard, before the transfer starts, and record the result in PIMS-REG-05. The assessment is needed where the safeguard is standard contractual clauses, binding corporate rules or another Article 46 instrument; it is not needed for a destination covered by an adequacy decision, and it does not legitimise a transfer that relies on a derogation under Article 49, which must be occasional and documented separately. Onward transfers by the importer to its own sub-processors are part of this assessment. Revisit the assessment when the law of the destination, the importer, the data or the measures change.*

## 1. The transfer

| Field | Entry |
|---|---|
| **Reference** | [PIMS-REG-05 reference] |
| **Exporter** | [Organisation], acting as [controller, processor] |
| **Importer** | [Category of organisation and its role: processor, sub-processor, controller, group company] |
| **Processing activity** | [PIMS-REG-01 reference] |
| **Flows covered** | [GDPR-REG-02 flow references] |
| **Destination country or countries** | [List], including the countries from which the importer provides support or holds backups |
| **Onward transfers by the importer** | [Named sub-processor categories and countries, from the importer's list] |
| **Data categories and subjects** | [List], with the volume and whether any special category or criminal offence data is included |
| **Purpose and duration of the transfer** | [Purpose]; [continuous, periodic, one-off]; [period] |
| **Format** | [Plain, pseudonymised, encrypted in transit only, encrypted at rest with keys held by the exporter] |
| **Transfer mechanism** | [Standard contractual clauses (module and date signed), binding corporate rules (approval reference), other Article 46 instrument] |
| **Assessor** | [Name], [Role], [Date] |

## 2. Assessment of the destination law and practice

*Answer from public sources: the laws of the destination, published decisions, the importer's transparency reporting, reputable analyses. Record the sources used in section 6. Where an answer is "unknown", treat it as an adverse answer until resolved.*

| Question | Answer and source |
|---|---|
| Does the destination have a general data protection law, and is it enforced by an independent authority? | |
| Can public authorities compel the importer to disclose personal data, and under what conditions (court order, administrative demand, secret order)? | |
| Is such access limited to what is necessary and proportionate, with independent oversight? | |
| Can the importer challenge a demand, and can it tell the exporter about it? | |
| Do the people whose data is transferred have an effective remedy against the authorities of the destination? | |
| Is there a law requiring the importer to build in access for authorities, to retain data for them, or to hand over encryption keys? | |
| Has the importer received demands of this kind, and what does its transparency reporting say? *Ask the importer directly where no reporting exists.* | |
| Is the importer, or its sector, a likely target of surveillance given the type of data and the authorities' known practice? | |
| Are there relevant adequacy findings, authority guidance or court rulings about this destination? | |

**Conclusion on the destination:** [The law and practice do not impinge on the effectiveness of the mechanism, The law and practice impinge on the mechanism and supplementary measures are required, The law and practice impinge and no measures can address it].

## 3. Assessment of the risk to the data

| Factor | Assessment |
|---|---|
| Sensitivity of the data | [Low, Medium, High], with reasons |
| Volume and number of people | |
| Likelihood that the data is of interest to the destination's authorities | [Low, Medium, High], with reasons |
| Consequence for the people if accessed | |
| Importer's own safeguards | *Certifications, audit reports, encryption, access controls, internal policy on government demands.* |

## 4. Supplementary measures

*Required where section 2 found that the law impinges. Technical measures are the ones that can address state access; contractual and organisational measures support them but rarely suffice alone. State for each measure whether it is in place, how it is verified and who verifies it.*

| Measure | Type | In place | Verified by |
|---|---|---|---|
| Encryption in transit with current protocols and verified configuration | Technical | [Yes or No] | [Role, evidence] |
| Encryption at rest with keys held only by the exporter or a party outside the destination, so that the importer cannot read the data | Technical | [Yes or No] | |
| Pseudonymisation before transfer with the key held by the exporter | Technical | [Yes or No] | |
| Split processing so that no single party in the destination holds identifiable data | Technical | [Yes or No] | |
| Importer's contractual duty to challenge demands, notify the exporter where lawful, and provide only the minimum | Contractual | [Yes or No] | |
| Importer's transparency reporting and a warrant canary where lawful | Contractual | [Yes or No] | |
| Strict access control, logging and least privilege at the importer, with audit rights exercised | Organisational | [Yes or No] | |
| Internal policy at the importer for handling government demands, reviewed by the exporter | Organisational | [Yes or No] | |
| Data minimisation: reducing the fields and the retention at the importer | Organisational | [Yes or No] | |

**Are the measures sufficient to make the mechanism effective in practice?** [Yes, No], with reasons.

## 5. Decision

| Field | Entry |
|---|---|
| **Outcome** | [Transfer may proceed under the mechanism, Transfer may proceed with the supplementary measures above, Transfer must not proceed] |
| **Conditions** | *Measures to be implemented before the first transfer, with owner and date; verification method; the PIMS-REG-06 row to update for a processor.* |
| **Notice** | *Where the destination is named in the privacy notice built from GDPR-TPL-01 or GDPR-TPL-02 and whether the notice needs a change.* |
| **Approved by** | [Name], Privacy Officer, [Date] |
| **Escalation** | *Where the outcome is "must not proceed" and the business wishes to continue, the matter goes to the Chief Executive Officer under GOV-PRO-24, and a suspension of the transfer is the default until decided.* |
| **Next review** | [Date]. *Twelve months, or on a change in destination law, in the importer, in its sub-processors, in the data, or on a demand received.* |

## 6. Sources and evidence

| Source | Date consulted | What it supported |
|---|---|---|
| [Public source description] | [Date] | [Section 2 question] |
| [Importer questionnaire response, GDPR-TPL-09 reference] | [Date] | [Section 3 or 4 item] |

## 7. Related documents

- PIMS-POL-03 International transfer policy
- PIMS-REG-05 International transfer register
- PIMS-REG-06 Processor and sub-processor register
- GDPR-REG-02 Data flow and transfer map
- GDPR-TPL-09 Supplier GDPR assessment questionnaire
- PIMS-TPL-02 Data processing agreement template
- GOV-PRO-24 Exception and risk acceptance procedure
