---
id: GOV-PRO-16
title: Asset management, classification and handling procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.9
  - ISO/IEC 27001:2022 Annex A 5.10
  - ISO/IEC 27001:2022 Annex A 5.11
  - ISO/IEC 27001:2022 Annex A 5.12
  - ISO/IEC 27001:2022 Annex A 5.13
  - ISO/IEC 27001:2022 Annex A 5.14
  - ISO/IEC 27001:2022 Annex A 7.10
  - ISO/IEC 27001:2022 Annex A 7.14
  - ISO/IEC 27001:2022 Annex A 8.10
  - SOC 2 CC6.1
  - SOC 2 C1.1
  - SOC 2 C1.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] keeps an inventory of information and the assets that hold it, assigns owners, classifies information into four levels, labels and handles it by level, recovers assets from leavers, and wipes or destroys media.
---
## 1. Purpose

This procedure keeps an accurate record of [Organisation]'s information and of the assets that store, process or transmit it, gives each one an accountable owner, classifies information by the harm its loss would cause, and sets the handling rules that follow from each classification.

## 2. Scope

It covers information in every form, including data in systems, documents, messages, recordings and printed material, and the assets that hold it: hardware, software, cloud services, storage media and paper. It applies to all staff, contractors and supplier personnel who handle [Organisation] information.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Asset Owner | Accountable for an asset, classifies its information, approves access, sets handling, reviews the register entry yearly. |
| Custodian | Operates the asset day to day on the owner's instructions, for example an administrator, a team or a provider. |
| Information Security Manager | Keeps GOV-REG-10, checks completeness, runs the yearly reconciliation. |
| IT Manager | Keeps GOV-REG-24 current for hardware and software, issues and recovers devices, carries out disposal. |
| All staff | Label and handle information by its level, return assets on request and on leaving. |

## 4. Procedure

4.1 **Inventory.** The Information Security Manager keeps GOV-REG-10 for information assets and the IT Manager keeps GOV-REG-24 for hardware and software. Every entry names an Asset Owner who is a role, a custodian, the location or system, the classification and the date of last review. New assets are registered before use: a new system at design, a new device at issue, a new cloud service at contract signature.

4.2 **Valuation.** The Asset Owner rates each information asset 1 to 3 for confidentiality, integrity and availability. The asset value is the highest of the three, as in GOV-PRO-05, and drives the classification and the risk assessment in GOV-REG-05.

4.3 **Classification levels.** Information is classified into one of four levels.

| Level | Definition | Typical examples |
|---|---|---|
| Public | Approved for release. Disclosure causes no harm. | Published website content, marketing material, published policies. |
| Internal | For use inside [Organisation]. Disclosure causes minor inconvenience or embarrassment but no material harm. | Internal procedures, organisation charts, general project plans. |
| Confidential | Disclosure causes material harm to [Organisation], a customer or an individual, or breaches a contract or law. | Customer data, personal data, contracts, source code, financial records, open security findings. |
| Restricted | Disclosure causes severe harm. Access is limited to named individuals. | Credentials and keys, special category personal data, incident details, unremediated test results, strategic plans. |

4.4 **Classifying.** The Asset Owner classifies information when it is created or received. Unlabelled information is treated as Internal. A collection is classified at the level of its most sensitive element. Information received from a customer carries the customer's label, or Confidential if it has none. Only the Asset Owner may lower a classification, and the change is recorded in GOV-REG-10.

4.5 **Labelling.** Confidential and Restricted documents carry the level in the header or footer, emails carry it at the start of the subject line, and physical media carry it on a label. Systems carry their classification in GOV-REG-10. Public and Internal items need no label on the item itself.

4.6 **Handling rules.** Each level is handled as follows. Detailed transfer channels are in GOV-PRO-23.

| Rule | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Access | Anyone | All staff | Named roles approved by the owner | Named individuals approved by the owner, reviewed quarterly |
| Storage | Any | Approved systems | Approved systems, access controlled, encrypted at rest | Approved systems, encrypted at rest, no local or personal copies |
| Transmission | Any channel | Organisation email and approved tools | Encrypted in transit, approved channels only | Encrypted in transit and at rest, approved channels, recipient verified |
| External sharing | Free | With a business reason | Under contract or confidentiality agreement, owner approval, access-controlled link | Owner's written approval per recipient, time-limited link, access logged |
| Printing | Free | Allowed, collect immediately | Avoid, collect immediately, store locked | Only with owner approval, logged, shredded the same day |
| Disposal | Ordinary waste | Delete, confidential waste for paper | Secure deletion, cross-cut shredding, media logged in GOV-REG-20 | Verified secure deletion or destruction with certificate, logged in GOV-REG-20 |

4.7 **Use of assets.** Daily rules for devices, accounts, media and services are in GOV-POL-02, remote working in GOV-POL-05 and clear desk in GOV-POL-04.

4.8 **Return of assets.** A leaver or a contractor at the end of an engagement returns every device, token, key, card and document by the last working day. The line manager checks the return against GOV-REG-24 under GOV-CHK-01 and reports anything unreturned to the Information Security Manager within two working days; the IT Manager wipes an unreturned device remotely under GOV-PRO-22. Information on a personal device is removed and the person confirms this in writing.

4.9 **Secure deletion and media disposal.** Before reuse or disposal, storage media is wiped by a method suited to it (cryptographic erase for encrypted media, overwrite for other magnetic media) or physically destroyed, and paper is cross-cut shredded. Data in a cloud service is deleted through the provider's documented process and the confirmation kept. Each disposal of a device or medium that held Confidential or Restricted information is recorded in GOV-REG-20 with method, date, person, witness and, for third party destruction, the certificate reference. Equipment leaves the premises for disposal only after wiping or in a locked container under a contract that requires destruction and a certificate.

4.10 **Software and hardware lifecycle.** GOV-REG-24 records for each product the version, patch cycle, support status and end-of-support date. Software or hardware that will reach end of support within twelve months receives an upgrade or replacement plan recorded against the entry. Unsupported software in use needs a risk acceptance under GOV-PRO-24.

4.11 **Reconciliation.** Each year the Information Security Manager reconciles GOV-REG-24 against an export from the device management and discovery tools and GOV-REG-10 against the list of systems in scope. Differences are corrected within thirty days and the result is reported at management review.

## 5. Records and evidence

- GOV-REG-10 Information asset register with owner, classification and value.
- GOV-REG-24 Software and hardware inventory with assignment, patch cycle and end-of-support dates.
- GOV-REG-20 Media and equipment disposal log and destruction certificates.
- Signed return confirmations from leavers in GOV-CHK-01.
- The yearly reconciliation report.

## 6. Exceptions

A one-off departure from a handling rule needs the Asset Owner's written approval, recorded against the asset. A standing departure needs a risk acceptance under GOV-PRO-24. Classification is never lowered to avoid a handling rule.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after an incident involving mishandled or lost information, and after a change in law or contract that affects classification. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-10 Information asset register
- GOV-REG-20 Media and equipment disposal log
- GOV-REG-24 Software and hardware inventory
- GOV-POL-02 Acceptable use policy
- GOV-POL-04 Clear desk and clear screen policy
- GOV-PRO-05 Risk assessment and treatment methodology
- GOV-PRO-22 Endpoint and mobile device security procedure
- GOV-PRO-23 Information transfer and data loss prevention procedure
- GOV-CHK-01 Onboarding and offboarding security checklist
- PIMS-POL-02 Data retention and disposal policy
