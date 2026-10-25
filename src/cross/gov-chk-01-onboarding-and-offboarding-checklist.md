---
id: GOV-CHK-01
title: Onboarding and offboarding security checklist
type: checklist
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 6.1
  - ISO/IEC 27001:2022 Annex A 6.5
  - ISO/IEC 27001:2022 Annex A 5.11
  - ISO/IEC 27001:2022 Annex A 5.18
  - SOC 2 CC6.2
  - SOC 2 CC6.3
owner: Human Resources Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: The two task lists that Human Resources, the line manager, the IT Manager and the access administrator complete for every person who joins or leaves [Organisation], with the responsible role, due point and evidence for each task.
---
## 1. How to use this checklist

*Open one copy per person. Human Resources starts it on the day an offer is accepted or a leaving date is known, enters the person's name, role, start or leave date and line manager at the top, and sends it to the roles named in the tables. Each responsible role marks the task done, writes where the evidence is, and initials it. Human Resources files the completed checklist with the person's record within five working days of the start or leave date and reports any task not done on time to the Information Security Manager. The due points count from the start date for onboarding and from the last working day for offboarding. Where a task does not apply, write "not applicable" and the reason, never leave it blank.*

| Field | Entry |
|---|---|
| Name of person | [Name] |
| Job role and team | [Role] |
| Employment type | Employee / Contractor / Agency / Temporary / Intern |
| Line manager | [Role] |
| Start date or last working day | [Date] |
| Screening level for the role | Standard / Enhanced |
| Checklist opened by and date | [Role], [Date] |

## 2. Onboarding checklist

| Task | Responsible role | Due | Done | Evidence |
|---|---|---|---|---|
| 1. Screening completed at the level set for the role, or a documented interim restriction agreed (GOV-PRO-18). | Human Resources Manager | Before start | | Screening record reference |
| 2. Contract or engagement terms with confidentiality, policy compliance and asset return clauses signed. | Human Resources Manager | Before start | | Signed contract on file |
| 3. Confidentiality agreement signed by a contractor or agency worker and recorded in GOV-REG-23. | Engaging manager | Before start | | GOV-REG-23 entry |
| 4. Starter notified to the Information Security Manager, IT Manager and access administrator with start date, role and line manager. | Human Resources Manager | [Number] working days before start | | Notification message |
| 5. Access request raised on GOV-TPL-09 for the standard role and approved by each System Owner. | Line manager | [Number] working days before start | | GOV-TPL-09 reference |
| 6. Device issued, enrolled in device management, encrypted, and recorded against the person in GOV-REG-24. | IT Manager | Day 1 | | GOV-REG-24 entry |
| 7. Accounts created, one-time credential delivered through a separate channel, multi-factor authentication enrolled (GOV-POL-06). | Access administrator | Day 1 | | GOV-TPL-09 section 6 |
| 8. Physical access badge issued for the correct zones and recorded (GOV-PRO-17). | Facilities Manager | Day 1 | | Badge record |
| 9. Induction training completed and recorded in GOV-REG-09 (GOV-PRO-08). | Line manager | Within [Number] working days | | GOV-REG-09 entry |
| 10. Policies acknowledged (GOV-POL-02, GOV-POL-04, GOV-POL-06 and any role-specific policy) and recorded in GOV-REG-23. | Human Resources Manager | Within [Number] working days | | GOV-REG-23 entry |
| 11. Access to Confidential or Restricted information activated only after tasks 9 and 10 are complete. | System Owner | After induction | | GOV-TPL-09 note |
| 12. Role-based training completed before the related duty or access (developers, administrators, personal data handlers). | Line manager | Before related access | | GOV-REG-09 entry |
| 13. Privileged account, where the role needs one, approved separately, held in a separate account and registered in GOV-REG-13. | System Owner | Before first privileged use | | GOV-REG-13 entry |
| 14. Remote working agreement signed and GOV-POL-05 acknowledged, where the person will work remotely. | Line manager | Before first remote work | | Agreement on file |
| 15. Thirty-day check: access matches the role, training complete, no shared credentials in use. | Line manager | Day 30 | | Note on this checklist |

## 3. Offboarding checklist

| Task | Responsible role | Due | Done | Evidence |
|---|---|---|---|---|
| 1. Leaving date notified to the Information Security Manager, IT Manager, access administrator and Facilities Manager. | Human Resources Manager | Day leave date is known | | Notification message |
| 2. Leaver's access and knowledge of shared secrets assessed, and the time of disabling set (immediately for a dismissal or a privileged holder on notice). | Information Security Manager | On notification | | Note on this checklist |
| 3. Work files, repositories, documents and ownership of records transferred to the line manager or a named successor. | Line manager | Before last day | | Transfer confirmation |
| 4. Customers, suppliers and partners for whom the leaver was a named contact told of the new contact. | Line manager | Before last day | | Message copies |
| 5. All logical access disabled, including remote access, email, cloud consoles, code repositories and collaboration tools (GOV-PRO-10). | Access administrator | End of last working day | | Disable confirmation per system |
| 6. Privileged accounts disabled and every shared or built-in credential the leaver knew rotated (GOV-REG-13). | System Owner | End of last working day | | GOV-REG-13 entries |
| 7. Service account credentials and API keys the leaver could read rotated. | System Owner | Within one working day | | Rotation record |
| 8. Mailbox handled under the employee privacy notice: automatic reply set, delegation to the line manager for [Number] days, then closure. | IT Manager | Last working day | | Mailbox setting record |
| 9. Removal from distribution lists, groups, on-call rotas, supplier portals and any external system where [Organisation] sponsored the account. | Access administrator | Last working day | | Removal confirmation |
| 10. Devices, tokens, keys and media returned, checked against GOV-REG-24, and wiped or reissued (GOV-PRO-16). | IT Manager | Last working day | | GOV-REG-24 entry updated |
| 11. Physical badge and keys returned and disabled; unreturned items reported to the Information Security Manager. | Facilities Manager | Last working day | | Badge record |
| 12. [Organisation] data removed from any personal device and the removal confirmed in writing by the leaver. | IT Manager | Last working day | | Signed confirmation |
| 13. Exit meeting held: continuing confidentiality obligations confirmed in writing and asset return confirmed (GOV-PRO-18). | Human Resources Manager | Last working day | | Signed exit letter |
| 14. Disabled accounts deleted or archived and the leaver's records retained under PIMS-POL-02. | Access administrator | Day [Number] after leaving | | Deletion record |
| 15. Checklist reviewed for completeness, exceptions escalated, and filed with the person's record. | Human Resources Manager | Within five working days | | Filed checklist |

## 4. Sign-off

| Field | Entry |
|---|---|
| All onboarding or offboarding tasks complete or marked not applicable | Yes / No |
| Tasks not completed on time and the reason | |
| Reviewed by Human Resources Manager | [Role], [Date] |
| Confirmed by Information Security Manager (offboarding of privileged holders only) | [Role], [Date] |

## 5. Related documents

- GOV-PRO-18 Human resources security procedure
- GOV-PRO-10 Access management procedure (joiners, movers, leavers, privileged access, reviews)
- GOV-PRO-08 Security and privacy awareness and training procedure
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-PRO-17 Physical and environmental security procedure
- GOV-TPL-09 Access request and approval form
- GOV-REG-09 Training and awareness register
- GOV-REG-13 Privileged account register
- GOV-REG-23 Policy acknowledgement register
- GOV-REG-24 Software and hardware inventory
- PIMS-POL-02 Data retention and disposal policy
