# Authoring guide for the kit

Every document in `src/` is an original work written for this kit. Nothing is copied from a standard, a vendor toolkit, a course or a client file. The standards themselves are copyrighted: cite clause numbers and control numbers, never reproduce their text.

## File format

One Markdown file per document, UTF-8, LF line endings, named `<id-lowercase>-<slug>.md`, for example `isms-pol-01-information-security-policy.md`. The file starts with YAML front matter:

```yaml
---
id: ISMS-POL-01
title: Information Security Policy
type: policy            # policy | procedure | plan | statement | record | template | checklist | playbook | guide
framework: iso27001     # iso27001 | iso27701 | soc2 | gdpr | ai | cross
maps:                   # requirement references, one per line, exact numbering of the public standard
  - ISO/IEC 27001:2022 clause 5.2
  - ISO/IEC 27001:2022 Annex A 5.1
  - SOC 2 CC1.1
owner: Information Security Manager      # a ROLE, never a person
approver: Chief Executive Officer        # a ROLE
classification: Internal
review: Annual
summary: One sentence that says what the document is for.
---
```

The body uses these headings, in this order, for a policy or procedure. Playbooks, guides and checklists may use their own headings.

```
## 1. Purpose
## 2. Scope
## 3. Roles and responsibilities
## 4. Policy statements        (or "## 4. Procedure" for a procedure, with numbered steps)
## 5. Records and evidence      (what proves the document is followed; name registers from the kit)
## 6. Exceptions
## 7. Review and maintenance
## 8. Related documents         (kit IDs only)
```

## Writing rules

- Placeholders are in square brackets and title case: `[Organisation]`, `[System name]`, `[Role]`, `[Date]`, `[Number]`. Never invent a company, a person, a product, a cloud region, a URL, an email address or a date. The only names allowed are public standards, laws and well known product categories.
- Plain English, short sentences, active voice. One idea per sentence. No marketing adjectives, no "ensure" chains, no "shall" unless it is a policy statement.
- Policy statements are numbered `4.1`, `4.2` and so on, each a single enforceable sentence or two. A reader must be able to audit each statement: what is required, who does it, how often, what proves it.
- Procedures are numbered steps with an actor at the start of each step: "The system owner approves...", "The reviewer records...".
- Every document names the records that prove it (register IDs from the kit, for example `ISMS-REG-02 Risk register`) and states review frequency and trigger events.
- No dashes of any kind except the plain hyphen inside words. Use commas, colons, full stops or a new sentence instead of an em or en dash. Numeric ranges use "to" ("1 to 5") or a plain hyphen.
- No reference to any tool that automates testing or writing, and no mention of how the document was produced.
- Standards: cite as "ISO/IEC 27001:2022 clause 6.1.2" or "Annex A control 8.12", "ISO/IEC 27701:2019 clause 7.2.1", "SOC 2 Trust Services Criteria CC6.1", "GDPR Article 30". Do not quote their text.
- British spelling except for proper nouns and the word "program" when it means a security programme in SOC 2 context.
- Length: policies 500 to 900 words, procedures 600 to 1,200 words, playbooks up to 2,500 words. Complete, not padded.
- Tables are Markdown pipe tables with a header row. Keep them under 6 columns.

## What a good policy statement looks like

Weak: "The organisation shall ensure that access is controlled."

Good: "4.3 The system owner grants access to [System name] only on a written request approved by the requester's line manager, applies the least privilege needed for the role, and records the grant in ISMS-REG-07 Access register within one working day."

## Registers

Registers are not Markdown. They are defined in `src/registers/*.yaml` and built into Excel by `tools/registers.py`. A register spec has an id, a title, the frameworks and requirements it serves, a two-sentence purpose, columns (name, width, optional dropdown values, optional 1 to 5 validation, optional formula), and one fictional example row for the preview. The workbook itself ships blank.

## Checks before a document is accepted

`python tools/verify.py` must pass: front matter complete, required headings present for policies and procedures, no banned term, no dash character, no placeholder outside square brackets, every related document ID exists.
