---
id: GOV-CHK-02
title: Secure Configuration Baseline Checklist (Server, Workstation, Cloud Account)
type: checklist
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.9
  - SOC 2 CC6.8
  - SOC 2 CC7.1
owner: Head of Engineering
approver: Information Security Manager
classification: Internal
review: Annual
summary: Three vendor-neutral checklists that define the minimum secure configuration for a server, a workstation and a cloud account, each check with how to verify it and the evidence to keep.
---
## 1. How to use this checklist

*Run the relevant table when a server, workstation image or cloud account is built, after a significant change, and at least annually. Record Pass, Fail or Not applicable per check, with the evidence reference. A Fail on a check marked with an asterisk blocks go-live until fixed or covered by a risk acceptance under GOV-PRO-24; any other Fail becomes a finding in GOV-REG-14. Where a configuration management or posture tool enforces a check continuously, its report is the evidence. Keep the completed checklist with the asset's entry in GOV-REG-24.*

## 2. Server baseline

| Ref | Check | How to verify | Evidence to keep |
|---|---|---|---|
| S-01 * | Built from an approved, version-controlled image or definition | Compare the running build identifier with the approved image list | Image identifier and build record |
| S-02 | Only required roles, services and packages are installed | List running services and installed packages against the role's allowed list | Service and package listing |
| S-03 * | Host firewall denies inbound by default; only required ports are open | Export the host firewall rules and scan open ports from another host | Rule export and port scan output |
| S-04 * | Vendor default accounts are removed or disabled and default passwords changed | List local accounts; attempt sign-in with documented defaults in a test window | Account listing and test record |
| S-05 | Local administrative access is limited to named roles; no shared accounts | Compare local administrator group members with GOV-REG-13 | Group membership export |
| S-06 * | Remote administration uses an encrypted protocol with key or multi-factor authentication; password sign-in is disabled | Inspect the remote access daemon configuration and test a password sign-in | Configuration excerpt and test record |
| S-07 * | Security updates apply automatically or on the monthly cycle; last update within the GOV-PRO-11 deadline | Read the update log and compare with the latest vendor release | Update log excerpt |
| S-08 | Time is synchronised to the approved source | Query the time service status and offset | Time service output |
| S-09 * | Events in GOV-PRO-14 section 4.1 are logged and forwarded to the central store | Trigger a test event and find it in the central store | Search result with timestamp |
| S-10 | Endpoint detection or anti-malware agent is installed and reporting (where the platform supports it) | Check the agent status locally and in the central console | Console screenshot showing the host |
| S-11 * | Data volumes are encrypted at rest | Read the volume encryption status | Encryption status output |
| S-12 | Permissions on configuration and secret files restrict read access to the service account | List permissions on the configuration directory | Permission listing |
| S-13 * | No secrets are stored in plain text on disk or in environment files; secrets come from the secrets store | Search the file system and environment for credential patterns | Search output |
| S-14 | Legacy protocols and weak cipher suites are disabled | Scan exposed services for protocol and cipher support | Scan output |
| S-15 | Exploit mitigations and mandatory access controls offered by the platform are enabled | Read the relevant kernel or system security settings | Settings output |
| S-16 * | Backup agent or snapshot policy applies per GOV-PRO-12 | Confirm the host appears in the backup schedule and the last job succeeded | Backup job report |
| S-17 | The host is recorded in GOV-REG-24 with owner, environment and classification | Look up the host in the inventory | Inventory row |
| S-18 | Configuration drift against the baseline is checked at least weekly and deviations alert | Review the drift report for the host | Drift report |
| S-19 | Administrative sessions time out after inactivity and display an authorised-use notice | Read the session settings and sign in to observe the notice | Settings excerpt |
| S-20 | The host is in scope of authenticated vulnerability scanning | Find the host in the latest scan report | Scan report row |

## 3. Workstation baseline

| Ref | Check | How to verify | Evidence to keep |
|---|---|---|---|
| W-01 * | Enrolled in the device management platform and reporting compliant | Look up the device in the management console | Console record |
| W-02 * | Full disk encryption is on and the recovery key is escrowed | Read encryption status on the device and confirm the key in the console | Status output and console record |
| W-03 | Screen locks after at most 10 minutes of inactivity and requires authentication to resume | Read the applied profile and observe the lock | Profile excerpt |
| W-04 * | The user account has no standing administrative rights | List local administrators | Group listing |
| W-05 | Host firewall is enabled | Read firewall status | Status output |
| W-06 * | Malware protection is active, updated within 24 hours and reporting centrally | Check the agent locally and in the console | Console record |
| W-07 * | Operating system is a vendor-supported version with automatic updates on; last update within the GOV-PRO-11 deadline | Read the version and update history | Update history |
| W-08 | Only software from the approved list is installed; application control is enforced where available | Compare the installed software list with the approved list | Software inventory |
| W-09 | The browser is managed, with extensions controlled and password saving disabled | Read the browser policy | Policy excerpt |
| W-10 | Writing to removable media is disabled unless an exception exists | Read the media policy and test with a device | Policy excerpt and test record |
| W-11 * | Remote lock and wipe are enabled and have been tested on the device model | Confirm the capability in the console and the model test record | Console record |
| W-12 | The remote access client is installed and configured per GOV-PRO-21 | Open the client and read its configuration | Client configuration |
| W-13 | Security events are forwarded to the central log store | Trigger a test event and find it centrally | Search result |
| W-14 | No shared or guest local accounts exist | List local accounts | Account listing |
| W-15 | Secure boot is enabled and firmware settings are password protected | Read the boot security status | Status output |
| W-16 | The device is labelled and recorded in GOV-REG-24 with its assigned user | Look up the asset tag in the inventory | Inventory row |
| W-17 | A password manager is deployed and the user has been shown how to use it | Confirm the application is installed and the training record exists | Installation record |
| W-18 | User data is synchronised to the approved storage location | Read the synchronisation client status | Client status |

## 4. Cloud account baseline

| Ref | Check | How to verify | Evidence to keep |
|---|---|---|---|
| C-01 * | The account sits in the organisation hierarchy under the correct unit with purpose and owner tags | Read the organisation tree and the account tags | Organisation export |
| C-02 * | Root or global administrator credentials have hardware multi-factor authentication, no access keys, sealed storage and an alert on use | Read the root credential report and the alert rule | Credential report and alert rule |
| C-03 * | All human users are federated through the central identity provider; no local users beyond break-glass | List local users and compare with GOV-REG-13 | User listing |
| C-04 * | Multi-factor authentication is enforced for all console and API access | Read the identity provider and account access policies | Policy export |
| C-05 | Privileged roles are time-bound and require approval per use | Read the privileged role configuration and a sample of activations | Role configuration and activation log |
| C-06 * | Organisation guardrails are applied: region restriction, logging cannot be disabled, no public storage without exception | Read the organisation policy set attached to the account | Policy export |
| C-07 * | Audit logging is enabled in every region, delivered to the central security account and retained for at least twelve months | Read the logging configuration and the destination retention setting | Logging configuration export |
| C-08 | Log storage is in a separate account and locked against deletion for the retention period | Read the storage lock and access policy on the log destination | Policy export |
| C-09 * | Default network rules deny inbound; no security group allows unrestricted access to administrative ports | Export security group rules and search for unrestricted sources | Rule export |
| C-10 * | No public storage buckets or containers exist outside the approved list | Run the public access report | Report output |
| C-11 * | No public snapshots, images or database instances exist | Run the public resource inventory | Inventory output |
| C-12 * | Encryption at rest is on by default for storage and database services, with customer-managed keys for Restricted data | Read the encryption defaults and a sample of resources | Settings export |
| C-13 | Keys are held in the key management service with rotation enabled and least privilege key policies | Read the key list and policies and compare with GOV-REG-18 | Key listing |
| C-14 * | Application secrets are in the secrets manager; none in plain text in code, configuration or environment variables | Search definitions and environment configuration for credential patterns | Search output |
| C-15 | Posture monitoring is enabled and open Critical and High findings are in GOV-REG-14 | Read the posture dashboard and compare with the register | Dashboard export |
| C-16 * | Backup policies are configured with a copy in a separate account and a restore tested per GOV-PRO-12 | Read the backup policy and the latest GOV-REG-15 entry | Policy export and log entry |
| C-17 | Billing alerts and service quotas are set to detect runaway cost or abuse | Read the budget alerts and quota settings | Alert configuration |
| C-18 | Mandatory tags (owner, system, environment, classification) are enforced | Run the untagged resource report | Report output |
| C-19 | Unused regions and unused services are disabled | Read the enabled region and service list | Settings export |
| C-20 | Workload identities use short-lived credentials; any long-lived key is in GOV-REG-18 and rotated within 90 days | Read the access key age report | Key age report |

## 5. Records and review

A completed checklist is a record under GOV-PRO-22 (workstations) and GOV-PRO-26 (cloud accounts), and supports the server controls in GOV-PRO-21 and GOV-PRO-11. It is kept with the asset in GOV-REG-24 for the life of the asset plus one year. The Head of Engineering reviews the checks annually and when a platform adds or removes a control; the Information Security Manager approves changes.

## 6. Related documents

- GOV-PRO-22 Endpoint and mobile device security procedure
- GOV-PRO-26 Cloud services security procedure
- GOV-PRO-21 Network security and remote access procedure
- GOV-PRO-11 Vulnerability and patch management procedure
- GOV-PRO-12 Backup and restore testing procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-REG-14 Vulnerability register
- GOV-REG-15 Backup and restore test log
- GOV-REG-18 Cryptographic key and certificate inventory
- GOV-REG-24 Software and hardware inventory
- GOV-REG-13 Privileged account register
