---
id: GDPR-TPL-06
title: Consent form templates (customers and employees)
type: template
framework: gdpr
maps:
  - GDPR Article 7
  - GDPR Article 4
  - GDPR Article 9(2)(a)
  - ISO/IEC 27701 Annex A 7.2.3
  - ISO/IEC 27701 Annex A 7.2.4
owner: Privacy Officer
approver: Privacy Officer
classification: Internal
review: Annual
summary: Two consent forms, one for customers and users and one for employees, each containing the elements that make consent valid, with the record that PIMS-REG-04 keeps for every consent given or withdrawn.
---
*Guidance notes are in italics and are removed before use. Consent is the right basis only when the person has a real choice and the organisation would accept a refusal; PIMS-PRO-05 records that decision before a form is used. A valid consent is freely given, specific to a stated purpose, informed, and shown by a clear affirmative act. It is never a pre-ticked box, silence, inactivity or a condition buried in terms. The form must be as easy to withdraw as to give, and the organisation must be able to show, for each person, what they consented to, when, how and under which version of the wording.*

## 1. Customer and user consent form

*Use one form per purpose, or one form with one separately tickable box per purpose. Each box is unticked by default. The service must work without the box being ticked unless the data is genuinely needed for it, in which case consent is the wrong basis.*

**[Organisation] would like your permission**

We would like to [state the purpose in one sentence, for example: send you a monthly newsletter about new features and offers by email].

To do this we will use [the data concerned, for example: your name and email address]. We will not use it for anything else without asking you.

[Where relevant: We will share it with [named recipient] so that they can [purpose]. / We will keep it for [period] or until you withdraw your permission.]

You do not have to agree. If you do not, [state the consequence, which must be none for the core service, for example: you can still use your account exactly as before].

You can withdraw your permission at any time by [the mechanism, for example: clicking the link at the bottom of any message, or changing the setting at Account, Preferences]. Withdrawing does not affect anything we did before.

[ ] Yes, I agree that [Organisation] may [purpose] using [data]. *(one box per purpose; unticked by default)*

[ ] Yes, I agree that [Organisation] may share my [data] with [named recipient] for [purpose]. *(only where sharing is itself consented to)*

Our privacy notice at [location] explains your rights. Questions: [contact].

*Where the data is special category data (for example health data in a wellbeing feature), the box must say "explicit" consent in substance: name the type of data, state the purpose and ask the person to confirm. Where the person is a child below the age set by the applicable law, obtain and verify the consent of the holder of parental responsibility under PIMS-PRO-05 and record how it was verified.*

## 2. Employee consent form

*Consent from an employee is valid only where refusal carries no detriment and the organisation can show that. Do not use consent for anything the employment contract, a legal duty or a legitimate interest already covers; use it for genuinely optional matters such as a photograph on the public website, participation in a wellbeing programme, equality monitoring, or a reference beyond the standard factual one. Collect it on paper or in the HR system, never by a reply to a group email.*

**Optional permission request**

Name: [Name]  Role: [Role]  Date: [Date]

[Organisation] would like your permission to [purpose, for example: publish your name, role and photograph on the team page of our public website].

This is optional. Saying no has no effect on your employment, your pay, your development or how you are treated. If you say nothing, we will treat that as no.

The data involved is [data]. It will be seen by [recipients] and kept [for the period, or until you withdraw permission]. It will not be used for any other purpose.

You can withdraw your permission at any time by telling [the people function contact] in writing. We will [action on withdrawal, for example: remove the photograph within five working days]. Withdrawal does not affect anything done before.

[ ] I give my permission for the use described above.

[ ] I do not give my permission.

Signature: [Signature]  Date: [Date]

*For special category data (for example health data for a wellbeing programme or an occupational health referral beyond the legal duty), add: "I understand that this involves information about my [health / ethnic origin / other] and I explicitly agree to its use for the purpose above and no other."*

## 3. The consent record

*For every consent given or withdrawn, create or update one entry in PIMS-REG-04 with the fields below. Where consent is collected in a product, the product must capture the same fields; a boolean flag without the wording version and timestamp is not a record. Keep the wording of every version of each form under GOV-REG-01 so that the record can be read back.*

| Field | Entry |
|---|---|
| Person identifier | [Account identifier, employee number, or email address] |
| Purpose consented to | [The purpose as worded on the form] |
| Form and version | [GDPR-TPL-06 derived form reference and version] |
| Method | [Web form tick, signed paper, HR system tick, verified parental consent] |
| Date and time given | [Date and time] |
| Evidence | [Signed form reference, system event reference] |
| Withdrawn on | [Date and time, or blank] |
| Withdrawal method | [Link, settings change, written notice] |
| Action taken on withdrawal | [What stopped, and when] |

## 4. Checks before a form is used

*The Privacy Officer confirms each item and records the check in PIMS-REG-04 or the form's approval record.*

1. The purpose is one the organisation would accept a refusal for.
2. One box per purpose, none pre-ticked, consent not bundled with terms.
3. The data, recipients and retention named on the form match PIMS-REG-01.
4. Withdrawal takes no more effort than giving consent, and the withdrawal action is implemented and tested.
5. The record in section 3 is captured automatically or by a defined manual step.
6. For employees, the detriment statement is true and the manager is not the person collecting the form.

## 5. Related documents

- PIMS-PRO-05 Consent and privacy notice management procedure
- PIMS-REG-04 Consent record register
- GDPR-TPL-01 Privacy notice template (customers and website)
- GDPR-TPL-04 Cookie and tracking technologies notice template
- GDPR-PRO-02 HR data handling procedure
- GDPR-POL-01 Data protection policy
