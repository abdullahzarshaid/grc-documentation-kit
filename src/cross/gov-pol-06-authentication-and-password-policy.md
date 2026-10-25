---
id: GOV-POL-06
title: Authentication, password and multi-factor policy
type: policy
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 5.17
  - ISO/IEC 27001:2022 Annex A 8.5
  - SOC 2 CC6.1
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: The rules for passwords, password managers, multi-factor authentication, secrets, lockout, initial credentials, recovery and sessions on every [Organisation] system, for people and for services.
---
## 1. Purpose

This policy sets how people and services prove who they are to [Organisation] systems, so that a stolen or guessed password is not enough to get in and secrets do not leak through code, chat or documents.

## 2. Scope

It applies to every account on every system [Organisation] owns, administers or subscribes to, including user, administrator, service and emergency accounts, and to every password, key, token and certificate used to authenticate to them.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| All users | Choose and protect credentials as stated below, enrol in multi-factor authentication, report suspected exposure. |
| System Owner | Configures each system to enforce these statements, or records a risk acceptance. |
| IT Manager | Operates the identity provider, password manager, secrets store and help desk recovery process. |
| Information Security Manager | Owns the policy, reviews configuration evidence quarterly, approves exceptions. |

## 4. Policy statements

4.1 **One identity per account.** Every account belongs to one person or one named service under GOV-PRO-10, and every system above Public classification requires authentication before access.

4.2 **Length.** A user password or passphrase is at least 14 characters. Systems accept at least 64 characters and impose no rules on mixing character types. A passphrase of several unrelated words is encouraged.

4.3 **Screening.** A new password is rejected if it appears on a list of known breached or common passwords, or contains the user's or [Organisation]'s name.

4.4 **No scheduled expiry.** Passwords change only on suspected compromise, when a person who knew a shared or privileged credential leaves, or where a system cannot meet 4.7 and its risk acceptance requires it. The last [Number] passwords may not be reused.

4.5 **Unique passwords.** Every account has its own password; a work password is never reused for a personal account or another [Organisation] system.

4.6 **Password manager.** Every user keeps work credentials in the password manager approved by the IT Manager, protected by a passphrase of at least 20 characters and multi-factor authentication. Credentials are not kept in browser stores, documents, spreadsheets or notes.

4.7 **Multi-factor authentication.** Multi-factor authentication is required for all remote and privileged access and for every other system that supports it, enrolled before first use. Privileged accounts and identity administrators use phishing-resistant methods (hardware security keys or platform authenticators); other users may use an authenticator application; text message codes are a documented fallback only. Users deny and report any prompt they did not initiate.

4.8 **Secrets.** Passwords, keys, tokens, certificates and connection strings are never placed in source code, committed configuration, tickets, chat, email, documents or spreadsheets. They live in the secrets store under GOV-PRO-20 with a named owner and an expiry date. A secret found exposed is rotated within 24 hours and reported under GOV-PRO-07.

4.9 **Service accounts and keys.** Service credentials and API keys are generated at random with at least 32 characters, scoped to the minimum permissions, rotated at least annually and when a person who had access leaves, and recorded in GOV-REG-13.

4.10 **Lockout.** An account locks after no more than ten consecutive failed attempts, for at least 15 minutes or with a progressive delay. Lockouts are logged and repeated lockouts raise an alert under GOV-PRO-14. A privileged account stays locked until an administrator has confirmed the holder's identity.

4.11 **Initial credentials.** A first or reset credential is unique, delivered through a channel separate from the account name, valid for no more than 24 hours and changed at first use. Default vendor credentials are changed before a device or application connects to the network.

4.12 **Recovery.** The help desk resets a credential or re-enrols multi-factor authentication only after verifying identity independently of the request (a call back to a registered number, line manager confirmation or an in-person check), never on a single email or chat request. Self-service resets require multi-factor authentication. Recovery codes are kept in the password manager.

4.13 **Sessions.** Sessions end after no more than [Number] minutes of inactivity, and sooner for privileged sessions as set by the System Owner. Sensitive actions require re-authentication. Users sign out of shared devices.

4.14 **Protection of credentials.** Credentials travel only over encrypted channels, are stored only as salted hashes from an algorithm family approved under GOV-PRO-20, and are never written to logs.

4.15 **Prohibited behaviour.** Users do not share credentials, write them down, enter them on a page reached from a message link without checking the address, or use them on an unmanaged device.

4.16 **Configuration evidence.** Each System Owner keeps an export of the settings that enforce these statements, refreshed after any change and at least yearly, which the Information Security Manager reviews quarterly.

## 5. Records and evidence

- Authentication configuration exports for each system.
- Multi-factor enrolment, lockout and reset reports from the identity provider and help desk.
- GOV-REG-13 Privileged account register with rotation dates.
- Exposure incidents in GOV-REG-08.

## 6. Exceptions

A system that cannot meet a statement is recorded with compensating controls under GOV-PRO-24, approved by the Information Security Manager and reviewed at least every twelve months. No exception applies to statement 4.8.

## 7. Review and maintenance

The Information Security Manager reviews this policy annually, after a credential-related incident, and when the identity provider or password manager changes. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-PRO-10 Access management procedure (joiners, movers, leavers, privileged access, reviews)
- GOV-REG-13 Privileged account register
- GOV-PRO-20 Cryptography and key management procedure
- GOV-PRO-14 Logging, monitoring and alert handling procedure
- GOV-PRO-07 Information security incident management procedure
