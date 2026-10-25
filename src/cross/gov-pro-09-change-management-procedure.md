---
id: GOV-PRO-09
title: Change Management Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.32
  - SOC 2 CC8.1
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How changes to production systems, infrastructure, configuration and security controls are requested, assessed, approved, tested, implemented, communicated and reviewed.
---
## 1. Purpose

This procedure controls change to [Organisation]'s production environment so that every change is assessed for security and service impact before it happens, approved by someone accountable for the affected system, tested, reversible, and traceable to a record that an auditor can follow from request to review.

## 2. Scope

It applies to changes to production infrastructure, platforms, applications, databases, network and security configuration, identity and access systems, cloud account settings, monitoring rules, and to the controls listed in the Statement of Applicability (ISMS-REG-01). It covers changes made by staff, contractors and suppliers acting on [Organisation]'s instruction. Source code work before release follows GOV-PRO-15; the release itself is a change under this procedure. Routine data entry and content updates within an application's normal use are not changes.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Change requester | Completes GOV-TPL-08, supplies the assessment, test and rollback material, and answers the approver's questions. |
| System Owner | Approves changes to the system they own at Low risk, co-approves at Medium risk, and confirms the post-implementation result. |
| Head of Engineering | Chairs the change advisory group, approves Medium and High risk changes, and authorises emergency changes. |
| Information Security Manager | Reviews every security-relevant change, sits on the change advisory group, and samples GOV-REG-11 quarterly. |
| Implementer | Carries out the change exactly as approved and records the outcome. Never approves their own change. |
| Tester or reviewer | Executes the test plan or reviews the configuration before approval. Is not the implementer. |

## 4. Procedure

4.1 **Change types.** Every change is one of three types.

| Type | Definition | Approval |
|---|---|---|
| Standard | A repeatable, low risk change with a documented, tested procedure that the change advisory group has pre-approved and listed in the standard change catalogue. | Pre-approved. Each execution is still logged. |
| Normal | Any change that is not standard and is not an emergency. | Per the authority table in 4.4, before implementation. |
| Emergency | A change needed within hours to resolve an incident or remove an imminent security risk. | Head of Engineering or on-call deputy, recorded. Retrospective record within two working days. |

4.2 **Request.** The requester raises a change record in the change system, or on GOV-TPL-08, with: description, reason, systems and data affected, data classification, risk and impact assessment, test plan and evidence, rollback plan, implementation window, communication plan and the implementer's name. A request without a rollback plan is returned to the requester.

4.3 **Risk and impact assessment.** The requester rates the change Low, Medium or High using four criteria: the number of users or customers affected, the classification of data touched, whether a security control is changed, and how easily the change can be reversed. The highest criterion sets the rating. A change is security-relevant when it alters authentication, authorisation, network exposure, encryption, logging, backup, or a data flow to an external party. The Information Security Manager reviews every security-relevant change regardless of rating.

4.4 **Approval authority.**

| Rating | Approver | Lead time |
|---|---|---|
| Low | System Owner | Before implementation |
| Medium | System Owner and Head of Engineering | At least two working days before the window |
| High | Change advisory group (Head of Engineering, Information Security Manager, affected System Owners), which meets at least weekly | At least five working days before the window |

The approver is never the implementer. Approval is recorded with name, date and any conditions.

4.5 **Standard change catalogue.** The change advisory group admits a procedure to the catalogue only after it has succeeded at least three times as a normal change. The catalogue names the procedure, the systems it applies to, the roles allowed to run it and the checks performed. The group reviews the catalogue annually and removes any entry that has failed in the period.

4.6 **Testing.** The tester runs the test plan in a non-production environment that matches production configuration, attaches the results to the change record and states whether the change is ready. Configuration and infrastructure definition changes are peer reviewed and approved before they are merged. A change with failed or missing tests is not approved.

4.7 **Scheduling and communication.** The implementer schedules the change within the published maintenance windows. Affected users are told at least [Number] working days before a Medium or High change. Customer-facing notice follows the contractual commitment for each service.

4.8 **Implementation.** The implementer follows the approved plan and records start time, end time and result in the change record. If the success criteria are not met within the window, or an unplanned effect appears, the implementer executes the rollback plan and informs the approver. Any deviation from the approved plan stops the change until the approver agrees to the deviation in writing.

4.9 **Emergency change.** The implementer obtains approval from the Head of Engineering or the on-call deputy through any recorded channel, states the incident or risk that justifies it, implements with a second person present or observing where possible, and completes GOV-TPL-08 within two working days. The change advisory group reviews every emergency change at its next meeting.

4.10 **Post-implementation review.** The System Owner reviews every High and emergency change within five working days, and a sample of at least [Number] Low and Medium changes each month, confirming that the change achieved its purpose, caused no incidents and left documentation current. A failed change with a process cause raises a corrective action under GOV-PRO-04.

4.11 **Related updates.** Before the change is closed, the implementer updates the affected entries in GOV-REG-24, GOV-REG-25 and GOV-REG-10, and any network diagram or runbook the change affects. The Information Security Manager samples GOV-REG-11 quarterly to confirm each change has an approval, test evidence and a recorded result.

4.12 **Supplier-initiated changes.** The System Owner assesses a change notified by a supplier under its contract as a normal change and records the supplier's reference in the change record.

## 5. Records and evidence

- GOV-REG-11 Change log: one row per change with type, rating, approver, dates and result.
- GOV-TPL-08 Change request form, or the equivalent change record, with test evidence and rollback plan attached.
- The standard change catalogue and its annual review record.
- Change advisory group minutes.
- Post-implementation review records and the quarterly sample review.

## 6. Exceptions

The emergency path in 4.9 is the only exception to prior approval. A change found in production without a change record is recorded as a nonconformity under GOV-PRO-04 and, where it touched a security control, assessed as an incident under GOV-PRO-07.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any change that caused an incident at one of the two highest severity levels in GOV-PRO-07, after an audit finding about change control, and when the deployment platform or change tooling is replaced. Changes to this procedure follow GOV-PRO-01.

## 8. Related documents

- GOV-TPL-08 Change request form
- GOV-REG-11 Change log
- GOV-PRO-15 Secure development lifecycle procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-PRO-04 Nonconformity and corrective action procedure
- GOV-PRO-01 Document control procedure
- GOV-REG-24 Software and hardware inventory
- GOV-REG-25 Data flow and interface inventory
