---
id: GOV-PRO-22
title: Endpoint and Mobile Device Security Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.1
  - ISO/IEC 27001:2022 Annex A 8.7
  - ISO/IEC 27001:2022 Annex A 8.9
  - SOC 2 CC6.8
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The baseline every laptop, desktop, phone and tablet must meet before it accesses [Organisation] information, how compliance is enforced, the conditions for personal devices, and what happens when a device is lost.
---
## 1. Purpose

This procedure keeps the devices that access [Organisation]'s information in a known secure state, enforces that state through device management, and defines the response when a device is lost, stolen or leaves the organisation.

## 2. Scope

It applies to every endpoint that accesses [Organisation] systems or data: devices owned by [Organisation], devices supplied by a contractor, and personal devices used under the conditions in 4.8. Servers and network devices are covered by GOV-CHK-02 and GOV-PRO-21.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns the endpoint baseline and the device management platform. |
| Endpoint administrator | Enrols devices, enforces the baseline, reviews compliance, performs remote lock and wipe. |
| Information Security Manager | Approves the baseline, reviews compliance monthly, leads lost device incidents. |
| Line manager | Approves device issue and personal device use for their staff. |
| Device user | Keeps the device under their control, applies updates when prompted, reports loss immediately. |

## 4. Procedure

4.1 **Baseline.** Every managed device meets the workstation baseline in GOV-CHK-02 before it accesses data. Minimum settings: full disk encryption with the recovery key escrowed in the management platform; screen lock after at most 10 minutes of inactivity with authentication to resume; host firewall enabled; malware protection active; automatic operating system and application updates; the user works without administrative rights; only software from the approved list; a managed browser; remote lock and wipe enabled; the device recorded in GOV-REG-24 with its user.

4.2 **Enrolment.** The endpoint administrator enrols each device in the device management platform at issue, applies the baseline profile and records the device in GOV-REG-24. Sign-in to [Organisation] services is permitted only from a device the platform reports as compliant.

4.3 **Malware protection.** Malware protection runs continuously on every device, updates its detection data at least daily, reports to a central console, and raises alerts into the triage process in GOV-PRO-14. Detected malware is handled under GOV-PRO-07. Removable media are scanned on connection where their use is permitted (GOV-PRO-23).

4.4 **Updates.** Operating system and application updates install automatically; users may defer for at most [Number] days. Critical updates follow the deadlines in GOV-PRO-11. A device running an operating system version no longer supported by its vendor is blocked until upgraded or replaced.

4.5 **Administrative rights.** Users hold no standing local administrator rights. Elevation for an approved task is granted just in time through the management platform, expires with the session and is logged. Developers who need elevated rights for their work receive them on a separate account or under a managed exception recorded in GOV-REG-13.

4.6 **Phones and tablets.** Managed phones and tablets require a passcode of at least six digits or a biometric with passcode fallback, device encryption, automatic updates, and a work profile or application container controlled by the management platform. Devices with vendor restrictions removed are refused.

4.7 **Compliance monitoring.** The endpoint administrator reviews the compliance report weekly and contacts the user of any non-compliant device. A device that stays non-compliant for seven days is blocked until corrected. The Information Security Manager reviews compliance figures monthly and reconciles the management platform against GOV-REG-24.

4.8 **Personal devices.** A personal device may access [Organisation] email, calendar and collaboration tools only when the user accepts the conditions in GOV-POL-02, enrols the work profile or container in the management platform, meets the passcode, encryption and supported-version requirements, and consents to remote wipe of the work container. Personal devices do not access systems holding Restricted data, do not store Confidential data outside the container, and are removed from the platform when the person leaves (GOV-CHK-01). [Organisation] wipes only the work container, never personal content.

4.9 **Lost or stolen device.** The user reports a lost or stolen device immediately, and within one hour at most, through the incident channel in GOV-PRO-07. The endpoint administrator locks the device remotely at once and wipes it if it is not recovered within [Number] hours or if it held Confidential or Restricted data. The Information Security Manager resets the user's credentials and tokens, assesses what data the device held and whether encryption was active, updates GOV-REG-24, and starts the personal data breach assessment under PIMS-PRO-04 where personal data may be affected.

4.10 **Return and disposal.** At the end of use the device is returned per GOV-CHK-01, wiped through the management platform, and either reissued after a fresh baseline or disposed of under GOV-PRO-16 with the record in GOV-REG-20.

## 5. Records and evidence

- GOV-REG-24 entries per device with user and compliance status, and the monthly reconciliation.
- Device management compliance reports and weekly follow-up records.
- GOV-CHK-02 workstation baseline with version history and the Information Security Manager's approval.
- Lost device incident records, wipe confirmations and breach assessments.
- Personal device acceptance records.

## 6. Exceptions

A device that cannot run the management agent (for example a test rig) is recorded in GOV-REG-24 with compensating controls, isolated per GOV-PRO-21, and covered by a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any incident involving an endpoint, when the management platform changes, and when a major operating system release changes the available controls. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-CHK-02 Secure configuration baseline checklist
- GOV-REG-24 Software and hardware inventory
- GOV-PRO-11 Vulnerability and patch management procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-PRO-23 Information transfer and data loss prevention procedure
- GOV-POL-02 Acceptable use policy
- GOV-POL-05 Remote and mobile working policy
- GOV-CHK-01 Onboarding and offboarding security checklist
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-REG-20 Media and equipment disposal log
- GOV-REG-13 Privileged account register
- PIMS-PRO-04 Personal data breach assessment and notification procedure
- GOV-PRO-21 Network security and remote access procedure
- GOV-PRO-24 Exception and risk acceptance procedure
