---
id: GOV-PRO-20
title: Cryptography and Key Management Procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 8.24
  - SOC 2 CC6.1
  - SOC 2 CC6.7
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: Which cryptographic methods are used for which purpose, and how the keys and certificates behind them are generated, stored, used, rotated, revoked and destroyed.
---
## 1. Purpose

This procedure sets the cryptographic methods [Organisation] uses for each purpose and the lifecycle of the keys and certificates behind them, so that encryption protects data in practice and keys are never the weakest point.

## 2. Scope

It applies to all uses of cryptography in [Organisation]'s systems: encryption of data at rest and in transit, password storage, digital signatures, message authentication, key exchange, application secrets, and public and private certificates, wherever the keys are held: cloud key management services, hardware security modules, secrets stores, certificate stores and devices.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Information Security Manager | Owns the approved algorithm list and this procedure, approves exceptions, reconciles GOV-REG-18 quarterly. |
| Key custodian (named per key store) | Generates, rotates, backs up and destroys keys, under dual control where 4.4 requires it. |
| System Owner | Identifies the cryptographic needs of their system and owns its keys and certificates in GOV-REG-18. |
| Platform team | Operates key management services, certificate automation and expiry monitoring. |
| Developers | Use approved libraries and the secrets store; never implement cryptographic primitives. |

## 4. Procedure

4.1 **Approved methods by purpose.** Only the following families are used. The specific algorithms, modes and parameters are chosen from current public guidance and listed in the approved algorithm list maintained by the Information Security Manager. Custom or modified algorithms are never used.

| Purpose | Approved family | Not permitted |
|---|---|---|
| Data at rest | Symmetric block cipher with a key of at least 256 bits in an authenticated mode | Unauthenticated modes, electronic codebook mode |
| Data in transit | TLS 1.2 or later with forward-secret key exchange and authenticated cipher suites, TLS 1.3 preferred | SSL, TLS 1.0 and 1.1, export and null ciphers |
| Hashing and integrity | SHA-2 or SHA-3 family, and keyed hashing built on them | MD5, and SHA-1 for any security purpose |
| Password storage | Memory-hard or adaptive password hashing with a unique salt per password | Fast general purpose hashes, reversible encryption |
| Digital signatures | RSA of at least 3072 bits, or elliptic curve signatures on approved curves | RSA below 2048 bits, DSA |
| Key exchange | Ephemeral elliptic curve or finite field exchange of approved size | Static or anonymous key exchange |
| Random numbers | Cryptographically secure generators provided by the platform | Application level pseudo-random functions |

4.2 **Key generation.** Production keys are generated inside the key management service or hardware security module, or by an approved library using the platform's secure random source, at the length in the approved list. Keys are never generated on a workstation, typed by hand, or derived from a password, except to protect a single user's device or archive.

4.3 **Storage and access.** Keys live in the key management service, hardware security module, secrets store or managed certificate store, under access roles granted through GOV-PRO-10. Private keys are not exportable unless the purpose requires it, and an exported copy is wrapped by a key of equal or greater strength. Keys and secrets never appear in source code, repository configuration, tickets, chat, email or documents. Applications receive secrets at runtime from the secrets store.

4.4 **Separation of duties.** Key administration roles are separate from the data administration roles of the systems the keys protect. Generation, export, destruction and recovery of root, master and key-encryption keys require two custodians acting together, each recorded. No single person holds both parts of a split secret or both factors of a recovery credential.

4.5 **Rotation.**

| Key or certificate | Rotation |
|---|---|
| Data encryption keys | Annually, or sooner at the volume limit of the mode |
| Key-encryption and master keys | Every three years, with re-wrapping of dependent keys |
| Public TLS certificates | Before expiry, with validity no longer than the public certificate authority limit, renewed by automation where possible |
| Internal certificates | Validity no longer than one year |
| Application secrets, API keys and service credentials | Every 90 days, and within one working day of a custodian leaving or a suspected exposure |
| Signing keys | Every two years |

Any key is rotated at once when compromise is suspected, when a custodian leaves, or when its algorithm is withdrawn from the approved list.

4.6 **Certificate lifecycle.** The System Owner requests a certificate from the approved internal or public authority with the exact names needed. The platform team validates control of the names, installs the certificate, records it in GOV-REG-18 and enrols it in expiry monitoring, which alerts at 30, 14 and 7 days. A certificate whose private key is exposed is revoked within one working day and replaced. Expired or revoked certificates are removed from every endpoint.

4.7 **Inventory.** GOV-REG-18 records every key and certificate with purpose, system, algorithm and length, location, owner, custodian, creation date, rotation due, expiry and status. The Information Security Manager reconciles it quarterly against exports from the key management service and certificate store.

4.8 **Backup, recovery and destruction.** Data encryption keys and key-encryption keys are backed up in a separate protected location so that encrypted backups stay readable for their retention period (GOV-PRO-12). Keys are destroyed under dual control when the data they protect reaches the end of its retention, and the destruction is recorded. Destroying the key is an accepted method of deleting the data (GOV-PRO-16).

4.9 **Compromise.** A suspected key compromise is an incident under GOV-PRO-07: the key is revoked or rotated, data protected by it is re-encrypted where exposure is possible, and dependent certificates are reissued.

4.10 **Legal constraints.** Export, import and lawful access requirements for cryptography in the countries where [Organisation] operates are recorded in GOV-REG-04 and respected in product and deployment decisions.

## 5. Records and evidence

- GOV-REG-18 Cryptographic key and certificate inventory, and the quarterly reconciliation.
- The approved algorithm list and its review record.
- Dual control records for generation, export, destruction and recovery.
- Expiry alerts and renewal records.
- Key compromise incident records in GOV-REG-08.

## 6. Exceptions

A legacy protocol or algorithm required by an external party is permitted only under a risk acceptance in GOV-PRO-24 with compensating controls (isolation, monitoring) and an end date, recorded against the item in GOV-REG-18.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, when public guidance withdraws an algorithm or parameter in use, after a key compromise, and after any outage caused by an expired certificate. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-18 Cryptographic key and certificate inventory
- GOV-PRO-10 Access management procedure
- GOV-PRO-12 Backup and restore testing procedure
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-PRO-07 Information security incident management procedure
- GOV-REG-08 Incident register
- GOV-PRO-24 Exception and risk acceptance procedure
- GOV-REG-04 Legal, regulatory and contractual register
- GOV-PRO-21 Network security and remote access procedure
- GOV-PRO-15 Secure development lifecycle procedure
