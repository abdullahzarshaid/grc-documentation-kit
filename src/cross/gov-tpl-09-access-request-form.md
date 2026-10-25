---
id: GOV-TPL-09
title: Access request and approval form
type: template
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.15
  - ISO/IEC 27001:2022 Annex A 5.18
owner: Information Security Manager
approver: Information Security Manager
classification: Internal
review: Annual
summary: The form used to request, justify, approve and record every grant, change and removal of access to [Organisation] systems under GOV-PRO-10.
---
## 1. How to use this form

*Complete one form per person. List every system in section 3. The line manager completes sections 2 to 4, each System Owner approves their own row in section 5, and the access administrator completes section 6 after granting. Quote the request reference in GOV-REG-12 when the access is reviewed and in GOV-REG-13 for any privileged account. A request without a business justification or without the required approvals is not actioned.*

## 2. Request details

| Field | Entry |
|---|---|
| Request reference | [Number] |
| Request type | New starter / Change of role / Additional access / Temporary access / Removal |
| Name of person | [Name] |
| Employment type | Employee / Contractor / Supplier personnel / Temporary |
| Job role and team | [Role] |
| Line manager | [Role] |
| Date access is needed | [Date] |
| Screening complete | Yes / No / In progress |
| Induction training recorded in GOV-REG-09 | Yes / No (access to Confidential or Restricted information is activated only when Yes) |
| Requested by and date | [Role], [Date] |

## 3. Access requested

| System | Access role | Permissions beyond the standard role | Duration or end date |
|---|---|---|---|
| [System name] | [Role] | None / [describe] | Permanent / [Date] |
| [System name] | [Role] | None / [describe] | Permanent / [Date] |
| [System name] | [Role] | None / [describe] | Permanent / [Date] |

## 4. Business justification

*State what the person will do that needs this access. If permissions beyond the standard role are requested, explain why the standard role is not enough. For Restricted information, name the data owner who agreed.*

| Field | Entry |
|---|---|
| Justification | |
| Data owner agreement (Restricted information only) | [Role], [Date] |
| Related ticket, project or contract | |

## 5. Approvals

*An approver never approves access for themselves. The administrator who grants the access does not approve it.*

| Approver | Role | Decision | Date | Signature |
|---|---|---|---|---|
| Line manager | [Role] | Approved / Declined | [Date] | |
| System Owner for [System name] | [Role] | Approved / Approved with changes / Declined | [Date] | |
| System Owner for [System name] | [Role] | Approved / Approved with changes / Declined | [Date] | |
| Information Security Manager (required for privileged access and for permissions beyond the standard role) | [Role] | Approved / Declined | [Date] | |

## 6. Provisioning record

| Field | Entry |
|---|---|
| Access administrator | [Role] |
| Date granted | [Date] |
| Account identifiers created or changed | |
| One-time credential delivered through a separate channel | Yes / No / Not applicable |
| Multi-factor authentication enrolled | Yes / No / Not applicable |
| Privileged account recorded in GOV-REG-13 | Yes / Not applicable |
| Expiry set for temporary access | [Date] / Not applicable |
| Grant checked against the request by a second person | [Role], [Date] |

## 7. Change and removal record

*Use this section whenever the access on this form is changed, removed or expires, so that the form shows the full life of the grant.*

| Date | Action | Performed by | Reason | Confirmation reference |
|---|---|---|---|---|
| [Date] | Changed / Removed / Expired | [Role] | | |
| [Date] | Changed / Removed / Expired | [Role] | | |

## 8. Related documents

- GOV-PRO-10 Access management procedure (joiners, movers, leavers, privileged access, reviews)
- GOV-REG-12 Access review log
- GOV-REG-13 Privileged account register
- GOV-POL-06 Authentication, password and multi-factor policy
- GOV-CHK-01 Onboarding and offboarding security checklist
