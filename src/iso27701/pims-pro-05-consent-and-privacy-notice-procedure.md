---
id: PIMS-PRO-05
title: Consent and privacy notice management procedure
type: procedure
framework: iso27701
maps:
  - ISO/IEC 27701 clause 7.2.3
  - ISO/IEC 27701 clause 7.2.4
  - ISO/IEC 27701 clause 7.3.2
  - ISO/IEC 27701 clause 7.3.3
  - ISO/IEC 27701 clause 7.3.4
  - ISO/IEC 27701 Annex A 7.2.3
  - ISO/IEC 27701 Annex A 7.2.4
  - ISO/IEC 27701 Annex A 7.3.2
  - ISO/IEC 27701 Annex A 7.3.3
  - ISO/IEC 27701 Annex A 7.3.4
  - GDPR Article 7
  - GDPR Article 12
  - GDPR Article 13
  - GDPR Article 14
owner: Privacy Officer
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: When consent is the right basis, what makes it valid, how it is captured, recorded and withdrawn, what every privacy notice must contain and when it must be shown, and how notices are changed under control.
---
## 1. Purpose

This procedure makes consent provable and notices accurate. A consent that cannot be shown to have been given freely, specifically and knowingly is no basis at all, and a notice that does not match what actually happens to the data is a transparency failure that every other control inherits.

## 2. Scope

It applies to every processing activity in PIMS-REG-01 where [Organisation] is a controller, to every point at which personal data is collected from or about an individual, to every privacy notice, cookie notice and consent form published by [Organisation], and to the systems that record consent and withdrawal.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Privacy Officer | Decides the lawful basis, approves every consent capture and notice, owns the notice versions and runs the annual check. |
| Processing Owner | Proposes the basis, designs the capture point with the product team, keeps the PIMS-REG-04 entry current and actions withdrawals. |
| Head of Engineering or System Owner | Builds the capture, the record, the withdrawal mechanism and the suppression, and provides the sample exports for checks. |
| Legal adviser | Reviews notices and consent wording before first publication and after a material change. |
| Marketing lead | Applies the marketing rules in this procedure and the suppression list. |

## 4. Procedure

4.1 **Choosing the basis.** For each purpose the Processing Owner proposes a lawful basis and the Privacy Officer confirms it in PIMS-REG-01. Consent is used only where the individual has a genuine choice and can refuse or withdraw without detriment. It is not used for processing needed to deliver a contract, to meet a legal obligation, or that [Organisation] would carry out regardless of the answer. For employees and applicants consent is used only for genuinely optional matters, such as a voluntary benefit, because the imbalance of power makes other consent unreliable. Where legitimate interests are proposed, GDPR-TPL-07 is completed first.

4.2 **Conditions for valid consent.** A consent capture approved under this procedure meets all of these: the request is separate from other terms and written in plain language; the purpose is specific, and each distinct purpose has its own choice; the individual is told who is asking, what data, for what purpose, that they can withdraw at any time and how, and what happens if they refuse; consent is given by a clear affirmative act, never by a pre-ticked box, silence, inactivity or continued use; refusing has no effect on the service beyond the part that depends on the consent; and withdrawing is as easy as giving. For special categories the consent is explicit: a statement or a ticked statement that names the category and the purpose. For children below the age set in GOV-REG-04 for the jurisdiction, consent is given or authorised by the holder of parental responsibility, verified in proportion to the risk.

4.3 **Designing a capture point.** Before a capture point goes live the Processing Owner records it in PIMS-REG-04 with the purpose, the audience, the mechanism, the notice version shown, the consent wording version, where the records are stored and the withdrawal method, and obtains the Privacy Officer's approval. Forms are based on GDPR-TPL-06. Cookie and tracker consent follows GDPR-TPL-04 and the inventory in GDPR-REG-04, with non-essential trackers blocked until consent is given.

4.4 **Recording consent.** The system records, for each consent: who gave it, when, through which capture point, the version of the notice and of the wording shown, which purposes were accepted and which refused, and the evidence of the affirmative act. Records are kept in the system of record for the life of the processing plus the period in PIMS-REG-07, protected against alteration, and exportable for a request under PIMS-PRO-03 or an authority enquiry. A consent whose record cannot be produced is treated as not given.

4.5 **Withdrawal.** Withdrawal is available through at least the channel through which consent was given, and always through the privacy mailbox. The Processing Owner actions a withdrawal within two working days, and for marketing within 72 hours: processing for that purpose stops, the suppression is applied so that the individual is not re-added by a later import, processors are instructed within the same time, and the data is deleted under PIMS-POL-02 unless another recorded basis applies to it. The withdrawal is recorded with the date and confirmed to the individual. Processing that took place before withdrawal remains lawful.

4.6 **Refreshing consent.** The Processing Owner reviews each capture point every twelve months and records it in PIMS-REG-04. Consent is obtained again when the purpose, the data or the recipients change materially, when the wording that was shown would no longer meet step 4.2, and for marketing where there has been no contact for [Number] months.

4.7 **Notice content.** Every notice covers, for data collected from the individual: the identity and contact details of [Organisation] and of the Privacy Officer; each purpose and its lawful basis; the legitimate interests relied on; the recipients and categories of recipients; transfers outside the region and the safeguard used; the retention period or the criteria that set it; the rights, including withdrawal of consent and the right to complain to the supervisory authority; whether providing the data is a legal or contractual requirement and what happens if it is not provided; and the existence, logic and significance of any automated decision making. For data not collected from the individual the notice also states the categories of data and their source. The templates GDPR-TPL-01, GDPR-TPL-02, GDPR-TPL-03 and GDPR-TPL-04 contain these elements.

4.8 **Notice timing.** A notice is provided at the point of collection where data comes from the individual, with a layered summary at the form and the full notice one step away. Where data comes from elsewhere, the notice is provided within one month, or at the first communication with the individual, or before the first disclosure to another recipient, whichever is earliest, unless the Privacy Officer records that the individual already has the information or that providing it is impossible or would involve disproportionate effort, in which case the information is published instead.

4.9 **Notice form.** Notices are written in plain language, structured under headings that match the content list, readable on a small screen, available in the languages [Organisation] serves its individuals in, and in language a child can understand where children are the audience. Each notice shows its version and effective date, and every previous version is retained.

4.10 **Notice change control.** A change to a notice is drafted by the Privacy Officer from a change in PIMS-REG-01, PIMS-REG-05 or PIMS-REG-06, reviewed by the legal adviser, approved by the Privacy Officer and published under GOV-PRO-01 with a new version number. A change that adds a purpose, a recipient, a transfer or a longer retention is communicated to the affected individuals before it takes effect, through the channel in ISMS-PLN-02, and consent is obtained again where the change affects a consented purpose. Notice versions are listed in GOV-REG-01.

4.11 **Annual check.** Once a year the Privacy Officer compares every published notice against PIMS-REG-01, PIMS-REG-05, PIMS-REG-06 and GDPR-REG-04, samples consent records from each capture point, tests a withdrawal end to end, and records the results in PIMS-REG-04. A notice that does not match the registers is corrected within thirty days and the gap is recorded in GOV-REG-03.

## 5. Records and evidence

- PIMS-REG-04 Consent record register: every capture point with its versions, record location, checks and status.
- Consent records in the systems of record, exportable per individual.
- Published notices with version history and approval records in GOV-REG-01.
- GDPR-REG-04 Cookie and tracker inventory and the consent configuration of the website.
- Withdrawal confirmations and suppression list exports.

## 6. Exceptions

A capture point may go live with a notice summary rather than the full notice only where the full notice is reachable from it in one step. No exception applies to the conditions in step 4.2.

## 7. Review and maintenance

The Privacy Officer reviews this procedure annually, after a complaint about consent or transparency, after authority guidance on consent or cookies, and after a new product or channel starts collecting personal data. Changes follow GOV-PRO-01.

## 8. Related documents

- GDPR-TPL-01 Privacy notice template (customers and website)
- GDPR-TPL-02 Employee privacy notice template
- GDPR-TPL-03 Job applicant privacy notice template
- GDPR-TPL-04 Cookie and tracking technologies notice template
- GDPR-TPL-06 Consent form templates (customers and employees)
- GDPR-TPL-07 Legitimate interests assessment template
- GDPR-REG-04 Cookie and tracker inventory
- PIMS-REG-04 Consent record register
- PIMS-REG-01 Personal data processing inventory
- PIMS-PRO-03 Data subject rights handling procedure
- ISMS-PLN-02 Communication plan
