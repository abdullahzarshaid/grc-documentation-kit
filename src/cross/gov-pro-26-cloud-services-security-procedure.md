---
id: GOV-PRO-26
title: Cloud Services Security Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.23
  - ISO/IEC 27001:2022 Annex A 8.9
  - SOC 2 CC6.1
  - SOC 2 CC9.2
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How cloud services are used securely, covering shared responsibility, account structure, region and residency decisions, identity federation, the areas that must be proved with evidence, and provider exit.
---
## 1. Purpose

This procedure sets how [Organisation] uses cloud services securely: who is responsible for what, how accounts are structured and administered, where data may be located, how identities are federated, which areas must be proved with evidence before and during use, and how the organisation would leave a provider.

## 2. Scope

It applies to all infrastructure, platform and software services consumed from cloud providers for [Organisation]'s business, in every account, subscription, project and tenancy that [Organisation] owns or administers, including trials and sandboxes. Assessment of the provider as a supplier follows GOV-PRO-06; this procedure covers configuration and operation of the services.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns the account structure, the guardrails and this procedure. |
| Cloud platform team | Administers the organisation root, the landing zone, identity federation and posture monitoring. |
| System Owner | Owns the accounts and services for their system and the evidence for the must-prove areas. |
| Information Security Manager | Approves region decisions, reviews posture findings monthly, verifies evidence at go-live and annually. |
| Privacy Officer | Confirms residency and processing decisions for personal data. |

## 4. Procedure

4.1 **Shared responsibility.** For each cloud service in use, the System Owner records which party is responsible for each layer: physical, host and hypervisor, network, operating system, platform, application, identity and access, data, logging and backup. The provider's assurance report (GOV-PRO-06) evidences the provider's side; this procedure and GOV-CHK-02 evidence [Organisation]'s side. The record is kept with the system's entry in GOV-REG-10.

4.2 **Account structure.** The cloud platform team operates a management or root account used only for organisation settings and billing, with separate accounts, subscriptions or projects for production, non-production, security and logging, and sandbox. Root or global administrator credentials are held under break-glass control: hardware-backed multi-factor authentication, credentials in a sealed store, every use alerting under GOV-PRO-14 and recorded in GOV-REG-13. Organisation-level guardrails prevent disabling audit logging, deploying outside approved regions and creating public storage without an approved exception.

4.3 **Region and residency.** The System Owner proposes the regions for each system from the residency obligations in GOV-REG-04, the privacy requirements in PIMS-POL-03 and customer contracts; the Information Security Manager and the Privacy Officer approve. Unapproved regions are disabled by guardrail where the provider allows it. Approved regions are recorded per system in GOV-REG-10, and provider services that replicate or process data outside the approved region are listed in GOV-REG-25 as external processing.

4.4 **Identity federation.** All human access to consoles and APIs comes through [Organisation]'s central identity provider with single sign-on and multi-factor authentication per GOV-POL-06. Local cloud users are limited to break-glass and documented service identities. Roles follow least privilege, privileged roles are time-bound and approved per use, and access is reviewed quarterly under GOV-PRO-10 with results in GOV-REG-12. Workloads use short-lived role credentials; any long-lived key is recorded in GOV-REG-18 and rotated under GOV-PRO-20.

4.5 **Must-prove areas.** Before a system goes live, and at least annually afterwards, the System Owner produces the evidence below and the Information Security Manager verifies it under the gate in PB-07 using GOV-REG-29. Each item of evidence shows the account, region, date and the identity that captured it (PB-09).

| Area | What must be true | Evidence to capture |
|---|---|---|
| Account and region | Workloads run only in approved accounts and regions | Account list from the organisation; region settings export |
| Privileged access and multi-factor | Every privileged identity is federated with multi-factor enforced; break-glass sealed | Identity provider policy export; privileged role membership; last break-glass use record |
| Exposure | No unapproved public storage, addresses, ports or shared snapshots | Posture report; public resource inventory against the approved list |
| Encryption and keys | Storage and databases encrypted at rest; customer-managed keys for Restricted data; TLS on every endpoint | Encryption settings export; GOV-REG-18 entries; endpoint scan |
| Logging and retention | Audit logging on in every account and region, delivered to the central store, retained per GOV-PRO-14 | Logging configuration export; central store retention setting |
| Backups and restore | Backups configured per GOV-PRO-12 in a separate account and restore tested | Backup policy export; latest GOV-REG-15 entry |
| External processing | Every provider service and sub-processor that receives data is known and contracted | GOV-REG-25 rows; provider sub-processor list; GOV-REG-07 entry |

4.6 **Baseline and posture.** Accounts meet the cloud account checks in GOV-CHK-02. A posture monitoring service evaluates configuration continuously; findings are triaged under GOV-PRO-11 with the same deadlines. Infrastructure is defined in code reviewed under GOV-PRO-15; manual console changes in production are changes under GOV-PRO-09 and are reconciled against the definitions weekly.

4.7 **Tagging and ownership.** Every account and resource carries tags for owner, system, environment and data classification. Untagged resources are reported weekly and removed after 30 days if unclaimed.

4.8 **New services and discovery.** A new cloud service or provider requires the System Owner's request, a review against this procedure and GOV-PRO-06, and the Information Security Manager's approval before any data is placed in it. The cloud platform team reviews billing and identity provider sign-in records quarterly to detect unapproved services.

4.9 **Provider exit.** For each critical provider the System Owner documents the data and configuration to export and in what format, the export procedure and who runs it, the provider's retention and deletion commitments after termination, and the alternative arrangement. The export procedure is tested annually on a sample and recorded in GOV-REG-16.

## 5. Records and evidence

- Shared responsibility records per service.
- Account structure and guardrail configuration exports.
- Region approvals per system.
- Must-prove evidence packs per system with the verification record (GOV-TPL-12).
- Posture findings in GOV-REG-14 and the monthly review.
- Quarterly discovery reviews and annual provider exit tests.

## 6. Exceptions

A public resource or a region outside the approved list is permitted only under a time-limited risk acceptance in GOV-PRO-24 approved by the Head of Engineering and the Information Security Manager, with the guardrail exception documented and set to expire.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after a provider incident affecting [Organisation], when a new provider is adopted, and when a residency obligation changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-07 Supplier register
- GOV-CHK-02 Secure configuration baseline checklist
- GOV-REG-10 Information asset register
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-REG-13 Privileged account register
- GOV-REG-04 Legal, regulatory and contractual register
- PIMS-POL-03 International transfer policy
- GOV-REG-25 Data flow and interface inventory
- GOV-POL-06 Authentication, password and multi-factor policy
- GOV-PRO-10 Access management procedure
- GOV-REG-12 Access review log
- GOV-REG-18 Cryptographic key and certificate inventory
- GOV-PRO-20 Cryptography and key management procedure
- PB-07 Playbook: the go-live security and privacy gate
- PB-09 Playbook: evidence management
- GOV-REG-29 Go-live gate checklist
- GOV-TPL-12 Readiness verdict note
- GOV-PRO-11 Vulnerability and patch management procedure
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-09 Change management procedure
- GOV-PRO-12 Backup and restore testing procedure
- GOV-REG-15 Backup and restore test log
- GOV-REG-16 Business continuity exercise log
- GOV-REG-14 Vulnerability register
- GOV-PRO-24 Exception and risk acceptance procedure
