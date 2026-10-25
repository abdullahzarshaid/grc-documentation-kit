---
id: GOV-PRO-21
title: Network Security and Remote Access Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.20
  - ISO/IEC 27001:2022 Annex A 8.21
  - ISO/IEC 27001:2022 Annex A 8.22
  - ISO/IEC 27001:2022 Annex A 8.23
  - ISO/IEC 27001:2022 Annex A 6.7
  - SOC 2 CC6.6
  - SOC 2 CC6.7
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How networks are segmented, how traffic is allowed by exception rather than by default, how management interfaces and remote access are protected, and how firewall rules are reviewed.
---
## 1. Purpose

This procedure protects [Organisation]'s networks and the services on them by segmenting them into zones, allowing only documented traffic, protecting management interfaces, requiring a multi-factor gateway for remote access, and keeping the rule base current.

## 2. Scope

It applies to all networks that [Organisation] controls: cloud virtual networks and security groups, office networks, wireless networks, management networks, site-to-site and remote access connections, and the edge services (load balancers, gateways, content delivery and name resolution) that expose [Organisation]'s services. Home and public networks used by staff are governed by GOV-POL-05 and by the device requirements in GOV-PRO-22.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns the network architecture and approves changes to the zone model. |
| Network or platform administrator | Implements and documents rules, operates gateways, runs the quarterly rule review. |
| Information Security Manager | Approves security-relevant rule changes, runs the monthly exposure review, co-signs the quarterly rule review. |
| System Owner | Owns the rules that serve their system and confirms them at review. |
| All staff and contractors | Connect to internal resources only through the approved remote access method. |

## 4. Procedure

4.1 **Architecture and zones.** The Head of Engineering maintains a network diagram and zone model that separates at least: public edge, application, data, management, corporate user, guest and non-production. Each zone has a written purpose and allowed traffic directions. The diagram is reviewed twice a year and after any change under GOV-PRO-09. Flows that cross zones or organisations are recorded in GOV-REG-25.

4.2 **Default deny.** Every firewall, security group and network access list denies inbound traffic by default and allows only documented flows. Outbound traffic from the data and management zones is restricted to named destinations. Each rule records its owner, business justification, the change reference and, for a temporary rule, an expiry date. Rules with an unrestricted source or destination on a sensitive zone are not permitted.

4.3 **Segmentation.** Production is separated from corporate and non-production networks with no shared credentials and no routing beyond the defined flows. Systems holding Restricted data sit in a zone reachable only from the application tier. Systems out of vendor support (GOV-PRO-11) and any operational technology are isolated in a dedicated zone with monitored access.

4.4 **Management interfaces.** Administrative interfaces (consoles, remote shells, database administration ports, hypervisor and cloud provider APIs) are never exposed to the internet. Administrators reach them through a bastion or privileged access gateway that requires multi-factor authentication, records sessions, and accepts connections only from managed devices. Default credentials are changed before a device is connected, management protocols are encrypted, and management traffic is logged under GOV-PRO-14.

4.5 **Remote access.** Staff and contractors reach internal resources only through the approved gateway (a virtual private network or an identity-aware proxy) that enforces multi-factor authentication per GOV-POL-06, checks device compliance per GOV-PRO-22, ends idle sessions after [Number] minutes, and logs every session. Access is scoped to the resources the role needs. Third party remote access is granted per engagement, limited in time, supervised or recorded, and removed on completion (GOV-PRO-10).

4.6 **Wireless.** Corporate wireless uses enterprise authentication with per-user credentials or device certificates and current encryption standards. Guest wireless is isolated from corporate networks and rate limited. The administrator checks offices for unauthorised access points quarterly.

4.7 **Filtering.** Managed devices and corporate networks resolve names through a filtering resolver that blocks known malicious domains and the categories listed in GOV-POL-02. Blocking events are logged, and staff are told about filtering through GOV-POL-02.

4.8 **Edge protection.** Internet-facing services sit behind a load balancer or gateway with denial-of-service protection, and behind a web application firewall where the service accepts user input. Only the ports and protocols the service needs are open. Transport encryption follows GOV-PRO-20.

4.9 **Exposure review.** The Information Security Manager reviews monthly the inventory of public addresses, open ports and public storage against the approved list, and records any unapproved exposure as a High finding in GOV-REG-14.

4.10 **Quarterly rule review.** The administrator exports every firewall and security group rule each quarter. Each System Owner confirms, removes or re-justifies their rules; expired temporary rules are deleted; the Information Security Manager co-signs the review. The record names the reviewers, the date, and the rules removed and changed.

4.11 **Changes.** All rule and topology changes are changes under GOV-PRO-09. A change that opens a new inbound flow from the internet, a new zone-crossing flow or a new third party connection is security-relevant and requires the Information Security Manager's approval.

## 5. Records and evidence

- The network diagram and zone model with review dates.
- The rule base with owner, justification and change references.
- Quarterly rule review records.
- Monthly exposure reviews and the resulting GOV-REG-14 findings.
- Remote access and management session logs.
- GOV-REG-25 Data flow and interface inventory.

## 6. Exceptions

The Information Security Manager may approve a temporary rule outside the model for at most 30 days, with the expiry set in the rule itself. Anything longer requires a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any incident that used a network path, after a redesign of the cloud network, and after an audit finding. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-09 Change management procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-20 Cryptography and key management procedure
- GOV-PRO-22 Endpoint and mobile device security procedure
- GOV-PRO-10 Access management procedure
- GOV-POL-05 Remote and mobile working policy
- GOV-POL-06 Authentication, password and multi-factor policy
- GOV-POL-02 Acceptable use policy
- GOV-REG-25 Data flow and interface inventory
- GOV-REG-14 Vulnerability register
- GOV-PRO-11 Vulnerability and patch management procedure
- GOV-PRO-24 Exception and risk acceptance procedure
