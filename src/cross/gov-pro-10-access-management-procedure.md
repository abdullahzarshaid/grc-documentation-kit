---
id: GOV-PRO-10
title: Access management procedure (joiners, movers, leavers, privileged access, reviews)
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.15
  - ISO/IEC 27001:2022 Annex A 5.16
  - ISO/IEC 27001:2022 Annex A 5.17
  - ISO/IEC 27001:2022 Annex A 5.18
  - ISO/IEC 27001:2022 Annex A 8.2
  - ISO/IEC 27001:2022 Annex A 8.3
  - ISO/IEC 27001:2022 Annex A 8.5
  - ISO/IEC 27701 clause 6.6.2
  - SOC 2 CC6.1
  - SOC 2 CC6.2
  - SOC 2 CC6.3
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How access to [Organisation] systems and information is requested, approved, granted, changed, reviewed and removed for joiners, movers, leavers, privileged users, break-glass accounts and service accounts.
---
## 1. Purpose

This procedure controls who can reach which systems and information at [Organisation], so that every account belongs to an identified person or an approved service, carries only the rights its role needs, is reviewed on a fixed cycle, and is removed as soon as it is no longer needed.

## 2. Scope

It applies to every account on every system that [Organisation] owns or administers: cloud consoles, applications, databases, network devices, code repositories, collaboration tools and the physical access system. It covers employees, contractors, supplier personnel with access and automated services.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Line manager | Requests access for their staff, confirms the business need, reports movers and leavers on the day they are known. |
| System Owner | Defines the access roles for the system, approves requests, runs the periodic access review. |
| Access administrator | Grants, changes and removes access exactly as approved, records the action, holds no approval rights. |
| Information Security Manager | Owns the procedure, keeps GOV-REG-12 and GOV-REG-13, checks that reviews happen, reports the metrics in 4.14. |
| Human Resources | Provides the start, move and leave dates that drive the joiner, mover and leaver steps. |
| Account holder | Uses only their own account, protects credentials under GOV-POL-06, reports access they can reach but should not. |

## 4. Procedure

4.1 **Access model.** Each System Owner defines the access roles for their system (for example reader, editor, administrator), the permissions each role carries and the job roles entitled to each. Access is granted by role, never by copying another user's rights. The role definitions are the baseline for every review.

4.2 **Principles.** Every account identifies one person or one named service. Shared accounts are prohibited; where a product offers only one built-in administrator account, its credential is held in the password vault, checked out by name and rotated after each use. Access follows least privilege and need to know.

4.3 **Request.** The line manager completes GOV-TPL-09 naming the person, the systems, the access role, the business justification and, for temporary access, the end date. A request for Restricted information also records the data owner's agreement.

4.4 **Approval.** The System Owner approves or declines in writing within two working days. Approval is never given by the person who will hold the access or by the administrator who will grant it. A request for more than the standard role of the job role also needs the Information Security Manager's approval.

4.5 **Joiner.** Human Resources gives the access administrator the start date at least [Number] working days ahead. Standard access for the job role is provisioned to work on the first day and no earlier than one working day before, and the administrator records the grant on GOV-TPL-09. Access to Confidential or Restricted information is activated only after induction training is recorded in GOV-REG-09.

4.6 **Mover.** When a person changes role, team or line manager, the new line manager raises a new GOV-TPL-09 within five working days. The access administrator removes the rights of the old role before adding the rights of the new one, so that rights do not accumulate. The old and new System Owners both confirm the change.

4.7 **Leaver.** Human Resources, or the engaging manager for a contractor, tells the access administrator the last working day as soon as it is known. All access, including remote access, email, cloud consoles, code repositories, physical tokens and any shared secret the person knew, is disabled by the end of the last working day and never later than one working day after it. For a dismissal, or a person on notice who holds privileged access, access is disabled at notification. Disabled accounts are deleted or archived after [Number] days. The remaining tasks follow GOV-CHK-01.

4.8 **Privileged access.** Administrative rights sit in a separate, identifiable account from the one used for email and daily work. Privileged accounts require multi-factor authentication under GOV-POL-06, are listed in GOV-REG-13 with holder, system, justification, approver and review date, and are reviewed quarterly. Privileged sessions are logged under GOV-PRO-14. Standing privileged access is granted only where time-bound elevation is not possible.

4.9 **Break-glass access.** Each critical system has at least one emergency account whose credential is stored sealed in the password vault, retrievable only by the System Owner or the Information Security Manager. It is used only when normal privileged access is unavailable during an incident. Every use is logged automatically, reported to the Information Security Manager within one working day, followed by a credential rotation, and recorded in GOV-REG-13.

4.10 **Service accounts.** Each service account has a named human owner, a documented purpose, the minimum permissions for that purpose, no interactive login where the platform allows it, and a credential kept in the approved secrets store and rotated at least annually and whenever a person who knew it leaves. Service accounts appear in GOV-REG-13 and are reviewed with privileged accounts.

4.11 **Supplier access.** Supplier personnel receive named accounts for a defined period under GOV-PRO-06, sponsored by a System Owner who raises the leaver step when the engagement ends.

4.12 **Access reviews.** Each System Owner reviews every account and its rights quarterly for systems holding Confidential or Restricted information and for all privileged accounts, and annually for every other system. The review compares an account export taken on the review date with the current staff list and the role definitions in 4.1, and marks each account keep, change or remove. The access administrator applies the changes within five working days. The Information Security Manager records the review, the counts and the export location in GOV-REG-12. A review without an export is not a review.

4.13 **Authentication.** Accounts are created with a one-time credential that must be changed at first use, multi-factor authentication is enrolled before first remote or privileged use, and all other rules follow GOV-POL-06.

4.14 **Metrics.** The Information Security Manager reports quarterly: the percentage of leavers disabled within one working day, reviews completed on time, accounts removed or changed by reviews, and privileged accounts without a current justification.

## 5. Records and evidence

- GOV-TPL-09 Access request and approval form for every grant and change.
- GOV-REG-12 Access review log with the export reference for each review.
- GOV-REG-13 Privileged account register, including service and break-glass accounts.
- Leaver notifications and the administrator's disable confirmations.
- Break-glass use reports and rotation records.

## 6. Exceptions

Temporary access outside this procedure is permitted only during an incident declared under GOV-PRO-07, is granted by the System Owner, lasts no longer than the incident, and is recorded in GOV-REG-13 within one working day. Any other departure, including a standing shared account, needs a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any audit finding about access control, after an incident involving misuse of access, and when a new class of system is introduced. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-09 Access request and approval form
- GOV-REG-12 Access review log
- GOV-REG-13 Privileged account register
- GOV-POL-06 Authentication, password and multi-factor policy
- GOV-PRO-18 Human resources security procedure
- GOV-CHK-01 Onboarding and offboarding security checklist
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-21 Network security and remote access procedure
- GOV-PRO-06 Supplier and third party security procedure
- GOV-PRO-24 Exception and risk acceptance procedure
