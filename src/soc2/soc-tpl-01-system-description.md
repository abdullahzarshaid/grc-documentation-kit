---
id: SOC-TPL-01
title: System description template
type: template
framework: soc2
maps:
  - SOC 2 CC2.1
  - SOC 2 CC2.3
  - SOC 2 CC9.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The template for the system description section of [Organisation]'s SOC 2 report, with every section the description criteria expect, placeholders, and guidance notes on what each section must and must not say.
---
## 1. How to use this template

*The system description is written by [Organisation] and included in the SOC 2 report under management's assertion. The auditor tests whether it is fairly presented: complete enough that a reader understands the system, accurate against what the auditor observes, and free of claims the controls do not support. Write in the present tense for the period covered. Every statement about a control must match a row in SOC-REG-01. Remove the italic guidance before issue. Keep names of staff out; use roles. The description is a controlled document under GOV-PRO-01 and is re-approved for every report.*

| Field | Entry |
|---|---|
| System described | [System name] |
| Report type | Type 1 as at [Date] / Type 2 for the period [Date] to [Date] |
| Trust services categories | Security / Availability / Processing integrity / Confidentiality / Privacy (delete those not in scope) |
| Description version | [Number] |
| Prepared by | Information Security Manager |
| Approved by | Chief Executive Officer |

## 2. Overview and services provided

*Two to four paragraphs. What [Organisation] is, what the service does for its customers, who the customers are in general terms, and the business function the service performs. A reader with no prior knowledge should understand the service after this section.*

[Organisation] provides [System name], a [description of service] used by [type of customer] to [business purpose]. The service is delivered as [delivery model, for example a multi-tenant web application and an interface for programmatic access] and is operated by [Organisation]'s [team names by function].

## 3. Principal service commitments and system requirements

*Service commitments are what [Organisation] promises customers: in contracts, service level agreements, terms of service, privacy notices and public security statements. System requirements are what the system must do internally to keep those promises. Each category in scope needs at least one commitment. Every commitment here must be real and traceable to a signed or published document; the auditor will ask for it.*

| Category | Principal service commitments | System requirements that support them |
|---|---|---|
| Security | [For example: customer data is accessible only to authenticated and authorised users; multi-factor authentication is enforced for administrative access; data is encrypted in transit and at rest] | [For example: role-based access under GOV-PRO-10; configuration baselines under GOV-CHK-02; key management under GOV-PRO-20] |
| Availability | [For example: the service is available [Number] percent of each calendar month excluding announced maintenance; recovery time objective of [Number] hours] | [Capacity monitoring under GOV-PRO-19; backup and restore under GOV-PRO-12; continuity under GOV-PRO-13] |
| Processing integrity | [For example: submitted transactions are processed completely and accurately within [Number] hours] | [SOC-POL-01; SOC-PRO-03; SOC-PRO-04] |
| Confidentiality | [For example: customer data is classified Confidential, shared with no third party except named subservice organisations, and deleted within [Number] days of contract end] | [GOV-PRO-16; GOV-PRO-23; PIMS-POL-02] |
| Privacy | [For example: personal information is collected and used only as the privacy notice states and data subject requests are answered within one month] | [PIMS-POL-01; PIMS-PRO-03; PIMS-PRO-05] |

## 4. Components of the system

### 4.1 Infrastructure

*The physical and virtual resources that run the service: hosting provider accounts, network segments, compute, storage, databases, content delivery, identity provider. Describe by function and by provider type, with the region or location category stated in general terms. Do not list internal addresses or account identifiers.*

| Component | Purpose | Provided by | Location category |
|---|---|---|---|
| [Production environment] | [Runs the service] | [Subservice organisation or [Organisation]] | [Region type, for example a single cloud region with a secondary for backup] |
| [Identity provider] | [Authenticates staff and customers] | | |
| [Database service] | [Stores customer data] | | |

### 4.2 Software

*The application software [Organisation] writes and the commercial or open source software it relies on: operating systems, platforms, databases, monitoring, ticketing, source control, build and deployment tooling. Group by purpose; version numbers are not needed.*

| Software | Purpose | Owner role |
|---|---|---|
| [Application] | [Customer-facing service] | Head of Engineering |
| [Source control and build service] | [Change control, deployment] | Head of Engineering |
| [Monitoring and alerting] | [Operations monitoring under GOV-PRO-14] | IT Manager |

### 4.3 People

*The teams involved in operating the system and their responsibilities, by role. Include third parties who perform roles, such as a managed security provider. The reader should see who approves access, who deploys changes, who answers incidents.*

| Role or team | Responsibility in the system |
|---|---|
| Chief Executive Officer | Approves policies, chairs the steering committee under GOV-POL-01. |
| Information Security Manager | Owns the control set, risk assessment, incident management and vendor assurance. |
| Head of Engineering | Owns the software lifecycle, change management and processing integrity. |
| IT Manager | Operates infrastructure, identity, endpoints and backups. |
| Operations team | Monitors the service, handles alerts and customer incidents. |
| People team | Screening, onboarding, offboarding and training records. |

### 4.4 Procedures

*The automated and manual procedures that run the service. Reference the kit documents by ID rather than restating them; the auditor reads the documents themselves. Cover at a minimum: access management, change management, incident management, vulnerability and patch management, backup and recovery, logging and monitoring, vendor management, and the procedures for each additional category in scope.*

| Area | Procedure |
|---|---|
| Access | GOV-PRO-10, GOV-POL-06 |
| Change | GOV-PRO-09, GOV-PRO-15 |
| Incidents | GOV-PRO-07, PIMS-PRO-04 where personal data is involved |
| Vulnerabilities | GOV-PRO-11 |
| Backup and recovery | GOV-PRO-12, GOV-PRO-13 |
| Monitoring | GOV-PRO-14, GOV-PRO-19 |
| Vendors | GOV-PRO-06, SOC-PRO-02 |
| Processing integrity | SOC-POL-01, SOC-PRO-03, SOC-PRO-04 |
| Confidentiality | GOV-PRO-16, GOV-PRO-23, PIMS-POL-02 |
| Privacy | PIMS-POL-01, PIMS-PRO-03, PIMS-PRO-05 |

### 4.5 Data

*The types of data the system processes, their classification under GOV-PRO-16, how they enter and leave the system, and where they are stored. State whether personal information is processed and in what role (controller or processor). Reference GOV-REG-25 and PIMS-REG-01 rather than reproducing them.*

| Data type | Classification | Source | Stored in | Personal information |
|---|---|---|---|---|
| [Customer content] | Confidential | [Customer upload or interface] | [Database and object store] | [Yes, as processor] |
| [Account and billing data] | Confidential | [Customer sign-up] | [Database] | [Yes, as controller] |
| [Operational logs] | Internal | [System generated] | [Log platform] | [Limited, account identifiers] |

## 5. System boundaries

*State precisely what is inside the description and what is outside. Inside: the environments, accounts, networks and teams that deliver the service. Outside: corporate systems that do not touch customer data, development sandboxes, other products. The boundary decides what the auditor tests; a vague boundary leads to testing everything.*

The system comprises [the production environment, the identity provider used for staff and customer authentication, the build and deployment pipeline that releases to production, the monitoring platform and the ticketing system used for change and incident records]. It excludes [corporate email and office productivity systems, the marketing website, development and test environments that hold no customer data, and products other than [System name]].

## 6. Relevant aspects of the control environment, risk assessment, information and communication, and monitoring

*A short account of how the common criteria CC1 to CC5 are met at the organisation level. One paragraph per heading, each pointing to the kit documents and registers. Keep claims testable.*

- Control environment: GOV-POL-01 establishes the steering committee, roles and reporting lines; GOV-POL-03 is the policy approved by the Chief Executive Officer; GOV-PRO-18 covers screening, terms and consequences; GOV-PRO-08 covers training.
- Risk assessment: GOV-PRO-05 is the methodology; GOV-REG-05 the register; fraud and change are considered as the methodology states; GOV-PRO-24 governs acceptances.
- Information and communication: ISMS-PLN-02 sets internal and external communication; GOV-PRO-01 controls documents; GOV-REG-23 records acknowledgements; customers are informed of commitments, changes and incidents through [channel type].
- Monitoring: GOV-PRO-02 internal audit, SOC-PRO-01 control testing, ISMS-PRO-04 measurement, GOV-PRO-03 management review; deficiencies are tracked in GOV-REG-03.
- Control activities: SOC-REG-01 lists each control with its criteria, frequency, owner and evidence.

## 7. Trust services categories and criteria in scope

*List the categories in scope and, for any criterion that does not apply to the system, the reason. Criteria are rarely not applicable; a common case is physical access criteria for an organisation with no premises of its own, where the subservice organisation's controls are relied on.*

| Criterion | Applicable | Reason if not applicable |
|---|---|---|
| CC1.1 to CC9.2 | Yes | |
| [A1.1 to A1.3] | [Yes / No] | |
| [PI1.1 to PI1.5] | [Yes / No] | |
| [C1.1, C1.2] | [Yes / No] | |
| [P1.1 to P8.1] | [Yes / No] | |
| [CC6.4, physical access] | [Partially] | [Premises are offices only; data centre physical access is a subservice organisation control, see section 9.] |

## 8. Complementary user entity controls

*Controls that customers must operate for the criteria to be met. List only those genuinely necessary; each one is a shared responsibility the customer's auditor will check. Phrase them as what the customer does.*

| Reference | User entity control | Criteria |
|---|---|---|
| UEC-1 | Customers administer their own users in [System name], grant roles on a least privilege basis and remove users who leave. | CC6.1, CC6.2, CC6.3 |
| UEC-2 | Customers protect the credentials, keys and tokens issued to them and report suspected compromise to [Organisation] without delay. | CC6.1, CC7.3 |
| UEC-3 | Customers review the notifications, reports and reconciliations [System name] sends and raise discrepancies within [Number] days. | PI1.4, CC2.3 |
| UEC-4 | Customers submit inputs in the agreed format with control totals as the specification requires. | PI1.2 |
| UEC-5 | Customers determine the lawful basis for personal information they submit and respond to data subject requests that fall to them. | P1.1 to P8.1 or C1.1 |

## 9. Subservice organisations

*Name each supplier whose controls are necessary to meet a criterion, the services used, the method, and the controls [Organisation] assumes the supplier operates. The auditor will check that SOC-PRO-02 reviews are on file for each one.*

Method: [Organisation] uses the carve-out method for the subservice organisations below. Their controls are not included in this description or in the auditor's tests. [Organisation] monitors them as SOC-PRO-02 describes.

| Subservice organisation | Service used | Criteria depending on it | Complementary subservice organisation controls relied on |
|---|---|---|---|
| [Hosting provider] | [Compute, storage, network, physical data centres] | CC6.4, CC6.5, A1.2, CC6.6 | Physical access to data centres is restricted and monitored; environmental protections operate; underlying infrastructure is patched; customer data is logically separated. |
| [Identity provider] | [Authentication for staff and customers] | CC6.1 | Authentication service is available and protects credentials; multi-factor configuration is enforced as set. |
| [Other] | | | |

Monitoring: [Organisation] obtains each subservice organisation's SOC 2 Type 2 report annually, reviews it under SOC-PRO-02, maps the complementary user entity controls to SOC-REG-01 and records the result in GOV-REG-07.

## 10. Significant changes during the period

*Type 2 only. Changes to the system, the control set, the organisation or the subservice organisations during the period that a reader needs to understand the results. Include: a new control that started partway through the period and its start date, a replaced supplier, a reorganisation, an acquisition, a migration. If nothing significant changed, say so.*

| Date | Change | Effect on controls |
|---|---|---|
| [Date] | [Change] | [Which controls were added, retired or altered, and from when] |

## 11. Incidents during the period

*Type 2 only. Incidents that resulted in a failure to meet a service commitment or a criterion, with nature, timing, extent and the response. Minor incidents handled under GOV-PRO-07 with no commitment missed are not described individually. If none occurred, say so in one sentence.*

| Date identified | Nature and extent | Commitment or criterion affected | Response and remediation |
|---|---|---|---|
| [Date] | [What happened and how many customers or records were affected] | [Commitment] | [Containment, notification, corrective action reference in GOV-REG-03] |

## 12. Management's assertion reference and document control

*The assertion is a separate signed statement that accompanies the description. Record here which assertion version this description supports and its approval.*

| Field | Entry |
|---|---|
| Assertion signed by | Chief Executive Officer |
| Assertion date | [Date] |
| Description approved by | Chief Executive Officer on [Date] |
| Control matrix version | SOC-REG-01 version [Number] |
| Previous description superseded | Version [Number] dated [Date] |
| Related documents | SOC-REG-01, SOC-PRO-01, SOC-PRO-02, SOC-GDE-01, GOV-REG-07, GOV-REG-25, PIMS-REG-01 |
