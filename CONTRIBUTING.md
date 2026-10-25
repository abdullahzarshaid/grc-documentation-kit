# Contributing

Corrections, clearer wording, missing documents and better register designs are welcome. Please read `AUTHORING.md` first; it is the format and style contract every document follows.

## What to contribute

- A factual correction to a clause, control, criterion or article reference.
- A clearer or more auditable policy statement or procedure step.
- A document the kit lacks, proposed first as an issue with its intended ID, framework and the requirements it serves.
- A register column or dropdown that a real programme needed and the kit missed.
- A translation of a playbook (keep the IDs identical).

## What not to contribute

- Text copied from a standard, a regulation's official commentary, a vendor toolkit, a course or a paid template. The kit is original and stays original.
- Anything from a real organisation: filled registers, evidence, names, systems, screenshots, incident details. Use fictional examples only.
- Claims that using the kit makes an organisation certified or compliant.

## How

1. Fork, branch, edit the Markdown in `src/` or the YAML in `src/registers/`. Do not hand-edit the files under `kit/`; they are generated.
2. Run `python tools/registers.py && python tools/build.py && python tools/checksums.py && python tools/verify.py`. The last command must print a pass line.
3. Open a pull request that says which document changed and why. One topic per pull request.

Python 3.10 or later with `python-docx`, `openpyxl`, `PyYAML` and `markdown-it-py` is enough to build everything.
