---
id: GOV-PRO-15
title: Secure Development Lifecycle Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.25
  - ISO/IEC 27001:2022 Annex A 8.26
  - ISO/IEC 27001:2022 Annex A 8.27
  - ISO/IEC 27001:2022 Annex A 8.28
  - ISO/IEC 27001:2022 Annex A 8.29
  - ISO/IEC 27001:2022 Annex A 8.30
  - ISO/IEC 27001:2022 Annex A 8.31
  - SOC 2 CC8.1
owner: Head of Engineering
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How security and privacy are built into software from requirements to release, covering threat modelling, the coding standard, peer review, pipeline checks, secrets, test data, environment separation, release approval and open source licences.
---
## 1. Purpose

This procedure builds security and privacy into software that [Organisation] develops or has developed for it, so that vulnerabilities are prevented or found before production and every release is traceable to reviewed, tested code.

## 2. Scope

It applies to all software developed by or for [Organisation] that runs in production or handles [Organisation] data: applications, interfaces, infrastructure definitions, automation scripts, data pipelines and machine learning components. It binds staff, contractors and outsourced developers. Configuration changes to third party software are covered by GOV-PRO-09.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Head of Engineering | Owns this procedure and the secure coding standard, approves exceptions to merge rules. |
| Product owner | Records security and privacy requirements in the backlog and accepts them as done. |
| Developers | Follow the standard, review peers' changes, fix findings. |
| Security champion (one per team) | Runs threat modelling, triages pipeline findings, liaises with the Information Security Manager. |
| Information Security Manager | Sets the analysis tooling requirements, reviews threat models for high risk systems, tracks findings in GOV-REG-14. |
| Privacy Officer | Reviews personal data requirements under PIMS-PRO-06 and approves test data exceptions. |

## 4. Procedure

4.1 **Security requirements.** At the start of a new service or significant feature, the product owner records as backlog items with acceptance criteria: the classification of data handled, the authentication and authorisation model, logging per GOV-PRO-14, encryption per GOV-PRO-20, input validation, rate limiting, privacy requirements from PIMS-PRO-06, and legal or contractual requirements from GOV-REG-04. The feature is not accepted until these items pass.

4.2 **Threat modelling.** The security champion runs a threat modelling session for every new service, every new external interface, and every change to authentication, authorisation or data flows. The session draws the data flows and trust boundaries, lists threats per element using a recognised category list, decides a control or an accepted risk for each, and records the result with the design. Threat models for systems holding Restricted data are reviewed by the Information Security Manager and revisited annually.

4.3 **Secure coding standard.** Developers follow the standard maintained by the Head of Engineering, which covers at least: validate all input on the server; encode output for its context; use parameterised queries; use the platform's authentication and session frameworks rather than custom code; authorise every request on the server for the specific object requested; fail closed; handle errors without exposing internals; pin and verify dependencies; keep secrets out of code; log per GOV-PRO-14. Developers complete secure coding training at induction and annually (GOV-PRO-08).

4.4 **Peer review.** Every change to a production branch goes through a merge request that at least one developer other than the author approves after reading the change against the standard. Protected branch rules block direct pushes and merges without approval and passing checks. Changes to authentication, cryptography, payment or personal data handling are also reviewed by the security champion.

4.5 **Pipeline checks.** Every build runs static analysis, dependency vulnerability analysis, secret detection and licence checking. A Critical or High finding blocks the merge unless the Head of Engineering approves a time-limited exception recorded in GOV-REG-14. Findings are triaged within the deadlines in GOV-PRO-11.

4.6 **Secrets management.** Application secrets are generated and stored in the approved secrets store, injected at runtime, rotated per GOV-PRO-20, and never committed to a repository, placed in a ticket or shared in chat. A secret found in a repository is treated as compromised: it is rotated within one working day and the event is recorded in GOV-REG-14.

4.7 **Test data.** Non-production environments use synthetic or anonymised data. Production personal data may be used only with the Privacy Officer's written approval for a stated purpose and period, under the same access controls as production, and is deleted at the end of the period with the deletion recorded.

4.8 **Separation of environments.** Development, test and production run in separate accounts or network segments with separate credentials. Developers hold no standing write access to production. Deployments run through the pipeline under an approved change (GOV-PRO-09). Production data does not flow to lower environments except under 4.7.

4.9 **Security testing.** Dynamic application testing runs before each major release. A penetration test by a party independent of the development team is performed before go-live of an internet-facing service and at least annually afterwards. Findings go to GOV-REG-14 and are retested after the fix.

4.10 **Release approval.** A release is a change under GOV-PRO-09 and requires passing pipeline checks, peer approval, test evidence and a rollback plan. A new system also passes the go-live gate in PB-07, with the verdict recorded on GOV-TPL-12. The release record lists the components and versions deployed.

4.11 **Open source and third party components.** Developers use components only under licences on the approved list maintained by the Head of Engineering; copyleft and unknown licences require review before use. A component inventory is produced for every release and retained with it. Components are kept on supported versions and tracked in GOV-REG-24.

4.12 **Outsourced development.** Contracts with external developers require this procedure or an equivalent, [Organisation]'s ownership of the code and the right to review and test it, delivery through [Organisation]'s repositories and pipelines, and supplier management under GOV-PRO-06.

## 5. Records and evidence

- Backlog items with security and privacy acceptance criteria and their acceptance.
- Threat models and their reviews.
- Merge request approvals, protected branch settings and pipeline results.
- GOV-REG-14 entries for pipeline, test and penetration findings, and merge exceptions.
- Test data approvals and deletion records.
- Release records with component inventories and GOV-TPL-12 verdicts.

## 6. Exceptions

Merge blocking exceptions follow 4.5 and test data exceptions follow 4.7. Any other departure from this procedure requires a risk acceptance under GOV-PRO-24.

## 7. Review and maintenance

The Head of Engineering reviews this procedure annually, after any incident caused by a software defect, after an audit finding, and when a new language, platform or pipeline is adopted. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-09 Change management procedure
- GOV-PRO-11 Vulnerability and patch management procedure
- GOV-REG-14 Vulnerability register
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-20 Cryptography and key management procedure
- PIMS-PRO-06 Privacy by design and by default procedure
- GOV-PRO-08 Security and privacy awareness and training procedure
- PB-07 Playbook: the go-live security and privacy gate
- GOV-TPL-12 Readiness verdict note
- GOV-PRO-06 Supplier and third party security procedure
- GOV-REG-24 Software and hardware inventory
- GOV-REG-04 Legal, regulatory and contractual register
- GOV-PRO-24 Exception and risk acceptance procedure
