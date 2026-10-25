---
id: GOV-PRO-23
title: Information Transfer and Data Loss Prevention Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.14
  - ISO/IEC 27001:2022 Annex A 8.12
  - SOC 2 C1.1
  - SOC 2 C1.2
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: Which channels may carry each classification of information, how external sharing is approved and reviewed, the controls on email, removable media and printing, and how exfiltration channels are monitored within privacy limits.
---
## 1. Purpose

This procedure controls how information leaves a system or the organisation, so that each classification travels only by a channel that protects it, external sharing is deliberate and time-limited, and loss through everyday channels is detected.

## 2. Scope

It applies to all transfers of [Organisation] information between people, systems and organisations by email, file sharing, messaging, system interfaces, removable media, printing and physical delivery, by staff, contractors and suppliers. Classification levels are defined in GOV-PRO-16. Transfers of personal data outside the home jurisdiction also follow PIMS-POL-03.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information owner (System Owner or document owner) | Approves transfers of Confidential and Restricted information and sets the sharing conditions. |
| Information Security Manager | Maintains the approved channel list, configures and tunes loss prevention rules, reviews alerts and sharing reports. |
| Collaboration or platform administrator | Implements email, sharing and media controls and produces the quarterly reports. |
| Privacy Officer | Reviews monitoring rules for proportionality and transfers of personal data. |
| All staff | Use only approved channels and report a misdirected or unauthorised transfer within one hour. |

## 4. Procedure

4.1 **Approved channels by classification.**

| Classification | Permitted channels | Conditions |
|---|---|---|
| Public | Any channel | The owner has approved publication |
| Internal | Corporate email, collaboration platform, corporate file sharing | Links limited to the organisation; no personal accounts |
| Confidential | Corporate email with transport encryption, named-recipient sharing links, approved customer or supplier portals | Named recipients, link expiry of at most 30 days, download controls where available, owner aware |
| Restricted | Approved secure transfer service, an encrypted file with the key sent by a separate channel, or an authenticated system interface | Owner's written approval per transfer or per standing arrangement, recipient under contract, transfer logged |

4.2 **External sharing.** Sharing links default to internal. A link for an external party requires a named recipient, an expiry date and, for Confidential or above, the owner's approval recorded in the sharing platform or a ticket. Guest accounts on collaboration platforms are reviewed quarterly under GOV-PRO-10 and removed when the engagement ends. Standing transfers to a supplier or customer are covered by a contract or data processing terms (GOV-PRO-06) and listed in GOV-REG-25.

4.3 **Email controls.** The administrator enforces transport encryption for outbound mail, configures sender authentication for [Organisation]'s domains, warns users when a recipient is external, blocks automatic forwarding to external addresses, and blocks attachments matching Restricted data patterns unless they are encrypted. A sender who misdirects mail reports it immediately and it is handled under GOV-PRO-07.

4.4 **Removable media.** Writing to removable media is disabled on managed devices by default. Where a role needs it, the Information Security Manager approves the exception, the device encrypts the media automatically, and the media is recorded, returned and disposed of under GOV-PRO-16 with the record in GOV-REG-20.

4.5 **Printing.** Confidential documents are printed only with secure release at the printer and collected at once. Restricted documents are printed only with the owner's approval, numbered where practical, and shredded after use. Printing at home follows GOV-POL-05.

4.6 **Messaging and personal services.** Staff do not send [Organisation] information to personal email, consumer messaging services or personal cloud storage. Use of external AI tools follows AI-POL-01. Approved messaging platforms are configured for retention and export so that records can be produced.

4.7 **Physical transfer.** Media and paper carrying Confidential or Restricted information travel encrypted or sealed, by tracked courier or in the personal custody of a staff member, with a chain of custody record signed at each handover.

4.8 **System interfaces.** Automated transfers between systems or to third parties use authenticated, encrypted interfaces (GOV-PRO-20), are recorded in GOV-REG-25 with owner, data classification and review date, and are reviewed annually by the owner.

4.9 **Monitoring of exfiltration channels.** The Information Security Manager runs loss prevention rules on email, file sharing and managed endpoints for Restricted data patterns (for example payment card numbers, national identifiers, bulk exports of personal data) and for anomalous volumes. Alerts are triaged under GOV-PRO-14. Each rule is documented with its purpose; the Privacy Officer reviews the rules annually; staff are told these channels are monitored through GOV-POL-02. Content inspection is limited to what the rule needs and is not used for any other purpose.

4.10 **Agreements.** Before a recurring transfer with another organisation begins, the information owner confirms a signed agreement covering confidentiality, permitted use, security measures, personal data terms where relevant, incident notification, and return or deletion at the end of the relationship.

## 5. Records and evidence

- The approved channel list and the loss prevention rule documentation with the Privacy Officer's annual review.
- External sharing reports and quarterly guest account reviews.
- Removable media exception approvals and disposal records in GOV-REG-20.
- GOV-REG-25 Data flow and interface inventory with annual reviews.
- Chain of custody records.
- Alert triage records and misdirected transfer incidents in GOV-REG-08.

## 6. Exceptions

A one-off transfer outside the table in 4.1 requires the Information Security Manager's approval and a record of what was sent, to whom and how. A standing deviation requires a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any data loss incident, when a collaboration or email platform changes, and when a law on data transfer changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-16 Asset management, classification and handling procedure
- PIMS-POL-03 International transfer policy
- GOV-PRO-10 Access management procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-25 Data flow and interface inventory
- GOV-PRO-07 Information security incident management procedure
- GOV-REG-08 Incident register
- GOV-REG-20 Media and equipment disposal log
- GOV-POL-05 Remote and mobile working policy
- GOV-POL-02 Acceptable use policy
- AI-POL-01 Acceptable use of AI tools policy
- GOV-PRO-20 Cryptography and key management procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-24 Exception and risk acceptance procedure
