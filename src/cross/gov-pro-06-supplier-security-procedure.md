---
id: GOV-PRO-06
title: Supplier and Third Party Security Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.19
  - ISO/IEC 27001:2022 Annex A 5.20
  - ISO/IEC 27001:2022 Annex A 5.21
  - ISO/IEC 27001:2022 Annex A 5.22
  - ISO/IEC 27001:2022 Annex A 5.23
  - ISO/IEC 27701 clause 7.2.6
  - ISO/IEC 27701 Annex B 8.5.6
  - SOC 2 CC9.2
  - GDPR Article 28
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How suppliers and other third parties are tiered, assessed before use, bound by contract, monitored while in use and exited without losing or exposing information.
---
## 1. Purpose

This procedure controls the risk that a supplier, contractor or cloud service brings to [Organisation]'s information, so that the organisation knows which third parties can reach its information, has assessed each in proportion to that reach, holds the right contract terms, and can leave any of them without losing or exposing data.

## 2. Scope

It applies to every external party that stores, processes, transmits or can access [Organisation]'s information or systems: cloud and software services, hosting and managed service providers, contractors with accounts, advisers who receive confidential material, and their sub-processors. Where [Organisation] is a processor for its clients, client obligations flow down through this procedure. Suppliers of goods with no information access are recorded at Tier 4 only.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Supplier owner | The business role that requested the supplier. Tiers it, collects evidence, holds the reviews, runs the exit. |
| Information Security Manager | Sets tier criteria, assesses due diligence, approves security terms for Tier 1 and Tier 2, keeps GOV-REG-07. |
| Privacy Officer | Decides whether the supplier is a processor, approves processor terms and transfer safeguards, keeps PIMS-REG-06. |
| Procurement or finance [Role] | Releases no purchase order or payment for a supplier not Approved or Conditional in GOV-REG-07. |
| Legal [Role] | Confirms the contract carries the clauses in step 4.5. |
| Supplier | Answers truthfully, provides evidence, notifies incidents within the contracted time, cooperates with reviews and exit. |

## 4. Procedure

4.1 **Tiering.** Before any contract, trial or free account, the supplier owner assigns the highest tier whose criteria apply and records it in GOV-REG-07.

| Tier | Criteria | Examples |
|---|---|---|
| 1 Critical | Holds Restricted information or personal data of more than [Number] individuals, holds privileged access to production, or its failure stops a critical service within one day | Hosting platform, identity provider, payroll processor |
| 2 Important | Holds Confidential information or any personal data, or has user-level access to internal systems | Collaboration tools, source code hosting, contractor with an account |
| 3 Standard | Holds Internal information only and is readily replaceable | Training provider, travel booking |
| 4 Low | No access to information or systems | Office supplies, catering |

4.2 **Due diligence.** The supplier owner collects the evidence for the tier and the Information Security Manager assesses it before approval. Tier 1: the full GOV-TPL-04 questionnaire, a current independent certificate or assurance report covering the service, review of that report under SOC-PRO-02, a penetration test summary from the last twelve months and a financial viability check. Tier 2: the full GOV-TPL-04 questionnaire, or a current certificate whose scope is confirmed to cover the service. Tier 3: the organisation, access control, incident and exit domains of GOV-TPL-04 as a self-attestation. Tier 4: the register entry only. Services with AI features are also assessed under AI-PRO-02. The score and open gaps are recorded in GOV-REG-07.

4.3 **Processor determination.** The Privacy Officer applies PIMS-PRO-01 to decide whether the supplier processes personal data on [Organisation]'s behalf. Where it does, no personal data is shared until processor terms meeting GDPR Article 28 are signed, using PIMS-TPL-02 or the supplier's own terms reviewed with GDPR-TPL-09. The Privacy Officer records the supplier in PIMS-REG-06, assesses any transfer outside the region under PIMS-POL-03 using GDPR-TPL-08, and records the safeguard in PIMS-REG-05.

4.4 **Gaps and risk.** Each gap found in due diligence is closed before approval in one of three ways: a remediation commitment with a date written into the contract, a compensating control operated by [Organisation], or an exception accepted under GOV-PRO-24 and recorded in GOV-REG-06. For Tier 1 and Tier 2 the Information Security Manager records the residual supplier risk in GOV-REG-05 using GOV-PRO-05.

4.5 **Contract.** Before signature the legal [Role] confirms the contract contains, as the tier requires: confidentiality; the security measures the supplier described in its answers; annual assurance evidence, and for Tier 1 a right to audit; notification of incidents affecting [Organisation] within [Number] hours of awareness (24 hours by default for Tier 1, 72 for Tier 2); sub-contracting only with prior notice and the same obligations flowed down; data location and transfer restrictions; return and verified deletion of data at exit within [Number] days; service levels and continuity commitments for Tier 1; and compliance with applicable law. The contract reference is entered in GOV-REG-07.

4.6 **Onboarding.** The supplier owner requests access under GOV-PRO-10 with named accounts, least privilege, multi-factor authentication and an end date. Contractors sign the confidentiality agreement and policy acknowledgement under GOV-PRO-18. Interfaces are recorded in GOV-REG-25. The Information Security Manager sets the GOV-REG-07 status to Approved, or to Conditional while a contracted remediation is open.

4.7 **Monitoring in service.** The supplier owner holds a service review quarterly for Tier 1 and annually for Tier 2, covering performance, incidents, service changes and sub-processor notices. The Information Security Manager tracks supplier security notices, records incidents affecting [Organisation] in GOV-REG-08, obtains renewed certificates or reports at expiry, and re-tiers the supplier when its data or access changes. A tier increase repeats step 4.2.

4.8 **Annual review.** By the next review date in GOV-REG-07 the supplier owner and the Information Security Manager confirm the tier, obtain current assurance, confirm the contract still describes the service, check the supplier's access against GOV-REG-12, review the year's incidents and performance, and record the outcome. The next review is set twelve months ahead, or six months for a Tier 1 supplier with an open finding.

4.9 **Supplier incidents.** An incident reported by or suspected at a supplier is handled under GOV-PRO-07 with the supplier owner as liaison. Where personal data is involved the Privacy Officer runs PIMS-PRO-04 from the moment [Organisation] becomes aware. A supplier that misses its notification obligation is recorded as a nonconformity in GOV-REG-03 and its tier and status are reviewed.

4.10 **Exit.** On termination or non-renewal the supplier owner removes access within one working day under GOV-PRO-10, obtains the data in an agreed format, obtains written confirmation of deletion including backups, revokes the keys and interfaces recorded in GOV-REG-18 and GOV-REG-25, and sets the status to Exited with the confirmation reference. Tier 1 suppliers have an exit plan from onboarding, and a data export is tested at least annually under GOV-PRO-26.

4.11 **Sub-processors engaged by [Organisation].** Where [Organisation] processes personal data for clients, every supplier that touches that data is approved under this procedure, listed in PIMS-REG-06, and notified to clients as each client contract requires before it starts work.

## 5. Records and evidence

- GOV-REG-07 Supplier register: one row per supplier with tier, assurance, contract, reviews and status.
- Completed GOV-TPL-04 questionnaires, certificates and assurance reports with assessment notes.
- Signed contracts and processor terms; entries in PIMS-REG-06 and PIMS-REG-05.
- Service review, annual review and exit records with deletion confirmations.
- Supplier risks in GOV-REG-05 and exceptions in GOV-REG-06.

## 6. Exceptions

A Tier 1 or Tier 2 supplier may start work before due diligence completes only with the Chief Executive Officer's written approval, a completion date within thirty days and an entry in GOV-REG-06. Free, trial and personally registered services that hold Internal or higher information are not exempt. No other exception applies.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any Severity 1 or Severity 2 supplier incident, after a change in processor obligations or applicable law, and after an audit finding about suppliers. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-04 Supplier security and privacy questionnaire
- GOV-REG-07 Supplier register
- GOV-PRO-07 Information security incident management procedure
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-PRO-26 Cloud services security procedure
- PIMS-PRO-01 Determining controller and processor roles
- PIMS-TPL-02 Data processing agreement template
