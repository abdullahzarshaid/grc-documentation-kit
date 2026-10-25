---
id: ISMS-STM-01
title: ISMS scope statement
type: statement
framework: iso27001
maps:
  - ISO/IEC 27001:2022 clause 4.3
  - ISO/IEC 27001:2022 clause 4.1
  - ISO/IEC 27001:2022 clause 4.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: Defines the boundary of the information security management system, the organisation, locations, services, systems, interfaces and exclusions it covers, and how that boundary is changed.
---
## 1. Statement of scope

The information security management system (ISMS) of [Organisation] covers the people, processes, information and technology used to design, deliver, operate and support [Service or product description] for its customers from the locations listed in section 2, together with the corporate functions named there. The boundary was set after the context analysis recorded in ISMS-REG-03 and takes account of the internal and external issues, the interested parties and the dependencies described below.

The scope wording used on certificates and in public statements is:

*The information security management system supporting the design, development, operation and support of [Service or product description] for customers, delivered from [Location] and the hosted infrastructure described in the Statement of Applicability version [Number].*

## 2. Organisation and locations

| Location | Function performed | In scope |
|---|---|---|
| [Head office city] | Leadership, engineering, operations, customer support, finance, people | Yes |
| [Second office city] | [Function] | [Yes or No] |
| Home working locations of staff | Engineering, operations and support work performed under GOV-POL-05 | Yes, for the staff and managed devices covered by that policy |
| [Provider hosting region] | Hosting of production and non-production environments | Yes, within the shared responsibility split in section 5 |

Employees, contractors and temporary workers who perform work within the functions above are inside the scope for the duration of their engagement.

## 3. Services and products

| Service or product | Description | Service Owner |
|---|---|---|
| [Service name] | [One sentence on what it does and for whom] | [Role] |
| Customer support | Handling of support requests and the customer information they contain | [Role] |
| Internal corporate systems | Identity, email, collaboration, finance and people systems that hold [Organisation] information | [Role] |

## 4. Information, systems and networks

| Element | What is included |
|---|---|
| Information | Customer data processed by the services above; personal data of staff, candidates and customer contacts; source code, configuration, credentials and keys; commercial and financial records; the records of this ISMS. |
| Systems | Production and non-production environments of [Service name]; the source code repository and build pipeline; the identity provider; the device management platform; the ticketing and documentation systems; end user devices issued to staff. |
| Networks | The office network at [Location]; the virtual networks in the hosting account or accounts; the remote access path used by administrators; the managed device fleet. Home networks are outside the scope except for the controls placed on the device under GOV-POL-05. |
| Registers of record | GOV-REG-10 lists each information asset in scope with its owner and classification. GOV-REG-24 lists hardware and software, including end of support dates. |

## 5. Interfaces and dependencies

[Organisation] relies on external providers for parts of the environment. The split of responsibility is recorded here and in GOV-PRO-26, and the providers themselves are listed in GOV-REG-07.

| Dependency | Provider responsibility | [Organisation] responsibility |
|---|---|---|
| Cloud hosting | Physical security of data centres, hypervisor, physical network, availability of the platform services used | Account configuration, identity and access, encryption settings, logging, backups, network rules, workload patching |
| Identity and productivity suite | Service availability, security of the platform itself | Tenant configuration, user lifecycle, multi-factor enforcement, data sharing settings |
| Payment, email and analytics processors | Security of their own service as contracted | Choice of provider, contract terms, data minimisation, monitoring under GOV-PRO-06 |
| Outsourced development or support, where used | Delivery to the contract and to the security clauses in it | Oversight, access provisioning, code review and acceptance |

Interfaces between in-scope and out-of-scope elements, for example an integration from [Service name] to a customer's own system, are listed in GOV-REG-25 with their classification and protection.

## 6. Exclusions and justification

| Excluded element | Justification | Remaining interface |
|---|---|---|
| [Business unit or product not covered] | Separately managed, separate systems, no access to in-scope information | Shared identity provider; the shared tenant controls stay in scope |
| Physical security of provider data centres | Operated by the provider and covered by its own assurance reports, which are reviewed under GOV-PRO-06 | Assurance report review recorded in GOV-REG-07 |
| Personal devices not enrolled in device management | Not permitted to reach in-scope systems under GOV-POL-02 | Technical block enforced by the identity provider |

An exclusion is permitted only where it does not reduce [Organisation]'s ability to protect in-scope information or to meet a requirement recorded in ISMS-REG-03. Each exclusion is re-examined during the annual risk assessment.

## 7. Requirements considered

The scope reflects the requirements of the interested parties recorded in ISMS-REG-03, the legal and contractual obligations in GOV-REG-04, and the issues identified through ISMS-PRO-01. Where a customer contract requires a particular system or location to sit within a certified scope, that requirement is recorded against the contract in GOV-REG-04 and reflected here.

## 8. Changes to the scope

8.1 Any role may propose a scope change. The proposal names the element to add or remove, the reason, the affected interested parties and the expected effect on risk.

8.2 The Information Security Manager assesses the proposal against the risk register (GOV-REG-05) and the Statement of Applicability (ISMS-REG-01) and presents it to the steering committee defined in GOV-POL-01.

8.3 The Chief Executive Officer approves the change. The Information Security Manager then updates this statement, GOV-REG-10, the risk assessment and ISMS-REG-01 within thirty days, and notifies the certification body where a certificate is held.

8.4 The following events require a scope review within thirty days: a new product or service, a new office or hosting region, an acquisition or divestment, a new category of customer data, a change of principal provider, or a contract that requires a change of scope.

## 9. Records and related documents

- ISMS-REG-03 Interested parties and requirements register
- ISMS-REG-01 Statement of Applicability
- ISMS-PRO-01 Context of the organisation and interested parties procedure
- GOV-REG-10 Information asset register
- GOV-REG-25 Data flow and interface inventory
- GOV-REG-07 Supplier register
- GOV-REG-04 Legal, regulatory and contractual register
- GOV-POL-01 Information security and privacy governance framework
- GOV-PRO-26 Cloud services security procedure
