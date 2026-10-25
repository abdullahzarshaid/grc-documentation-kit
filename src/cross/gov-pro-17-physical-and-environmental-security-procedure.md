---
id: GOV-PRO-17
title: Physical and environmental security procedure
type: procedure
framework: cross
maps:
  - ISO/IEC 27001:2022 Annex A 7.1
  - ISO/IEC 27001:2022 Annex A 7.2
  - ISO/IEC 27001:2022 Annex A 7.3
  - ISO/IEC 27001:2022 Annex A 7.4
  - ISO/IEC 27001:2022 Annex A 7.5
  - ISO/IEC 27001:2022 Annex A 7.6
  - ISO/IEC 27001:2022 Annex A 7.7
  - ISO/IEC 27001:2022 Annex A 7.8
  - ISO/IEC 27001:2022 Annex A 7.9
  - ISO/IEC 27001:2022 Annex A 7.10
  - ISO/IEC 27001:2022 Annex A 7.11
  - ISO/IEC 27001:2022 Annex A 7.12
  - ISO/IEC 27001:2022 Annex A 7.13
  - SOC 2 CC6.4
  - SOC 2 CC6.5
owner: Information Security Manager
approver: Chief Executive Officer
classification: Internal
review: Annual
summary: How [Organisation] protects its premises, secure areas, equipment and supporting utilities against unauthorised entry, damage and interference, including what still applies when the organisation runs entirely on cloud services.
---
## 1. Purpose

This procedure protects [Organisation]'s information and equipment from unauthorised physical access, theft, damage and environmental failure, by defining zones, controlling who enters them, siting and maintaining equipment properly and protecting the utilities it depends on.

## 2. Scope

It applies to every location where [Organisation] information or equipment is kept: offices, server and network rooms, storage areas, co-working spaces, home workplaces and temporary sites, and to equipment that moves between them. Data centres run by cloud providers are outside [Organisation]'s own physical controls and are assured under GOV-PRO-06 and GOV-PRO-26.

## 3. Roles and responsibilities

| Role | Responsibility |
|---|---|
| Facilities Manager | Operates entry controls, the visitor process and environmental systems, keeps maintenance records, co-runs the yearly inspection. |
| Information Security Manager | Defines zones, approves secure area access lists, reviews GOV-REG-19 monthly, co-runs the yearly inspection. |
| Zone owner | A role accountable for a secure area who keeps its access list current and approves work inside it. |
| Reception or host | Registers visitors, issues badges, escorts, confirms sign-out. |
| All staff | Wear badges visibly, challenge or report unbadged persons, escort their own visitors, follow GOV-POL-04. |

## 4. Procedure

4.1 **Zones.** The Information Security Manager classifies each area into one of four zones and records them on a floor plan held by the Facilities Manager: Public (reception and meeting rooms open to visitors), Office (general working areas), Secure (server and network rooms, records stores, any room where Restricted information is routinely handled) and Service (power, telecommunications entry and plant rooms). Each Secure and Service zone has a named zone owner.

4.2 **Entry controls.** Entry to the Office zone requires a personal badge or fob. Doors close and lock automatically and are never propped open. Secure zones require a second factor at the door (a PIN or a second badge read) and carry no external sign describing their contents. The access control system logs every entry and the logs are kept for [Number] months. A lost badge is reported within one hour and disabled on report. Zone owners review their access lists quarterly and record the review in GOV-REG-12 with the physical access system as the system reviewed.

4.3 **Visitors.** A host pre-registers every visitor. Reception records the visitor's name, organisation, host, purpose, time in, badge number and time out in GOV-REG-19 and checks photographic identity for entry beyond the Public zone. Visitors wear a badge that is visibly different from staff badges and are escorted at all times outside the Public zone. A visitor entering a Secure zone is recorded with the zone and the reason. Contractors with repeated work receive a time-limited badge only after the host confirms the need with the Information Security Manager. Deliveries are received in the Public zone.

4.4 **Working in secure areas.** Only people on the zone owner's list work unescorted in a Secure zone. Photography and recording need the zone owner's written approval. Third parties are supervised throughout. Food and drink are kept away from equipment. The area is locked whenever it is unattended, and anyone working alone in it tells the Facilities Manager before starting and after finishing.

4.5 **Equipment siting.** Servers and network equipment are installed in locked racks inside a Secure zone. Screens are positioned so that they cannot be read from windows, corridors or the Public zone. Equipment is kept away from water, heat sources and direct sunlight. Printers used for Confidential output sit in the Office zone with pull printing where the device supports it. Every item carries the asset tag recorded in GOV-REG-24.

4.6 **Cabling.** Power and data cables run in trunking, under floors or above ceilings, labelled at both ends. Patch panels sit in locked cabinets. Network points in the Public zone are disabled unless in use. Cabling is checked during the yearly inspection.

4.7 **Supporting utilities.** Equipment in Secure zones runs on an uninterruptible power supply that the Facilities Manager tests quarterly. Fire detection and suppression suitable for electrical equipment, temperature and humidity monitoring with alerts to the Facilities Manager, and water detection where pipework runs nearby are installed and serviced by competent contractors. Test and service dates are recorded.

4.8 **Maintenance.** Equipment is serviced to the manufacturer's schedule by authorised personnel, who are escorted in Secure zones. Storage media is removed or wiped under GOV-PRO-16 before equipment leaves the premises for repair, unless the repair contract requires confidentiality and the media is encrypted. Maintenance records are kept against the GOV-REG-24 entry.

4.9 **Off-site assets.** Equipment leaves the premises only when assigned to a named person in GOV-REG-24. Laptops and phones travel as hand luggage, are never left visible in a vehicle and are locked away at home. The rules in GOV-POL-05 apply. Loss or theft is reported within one hour under GOV-PRO-07 and handled under GOV-PRO-22.

4.10 **Clear desk and disposal.** GOV-POL-04 applies in every zone. Equipment and media awaiting disposal are stored in a Secure zone and disposed of under GOV-PRO-16.

4.11 **Inspection.** The Information Security Manager and the Facilities Manager inspect every zone yearly against this procedure, record the findings, and raise corrective actions under GOV-PRO-04.

4.12 **Cloud-only and small organisations.** Where [Organisation] has no server room and runs on cloud services, the following still apply: entry control, visitor registration and clear desk in the office; locked storage for paper and spare devices; encryption, asset registration and loss reporting for laptops and phones; the home working rules in GOV-POL-05; and provider data centre assurance obtained under GOV-PRO-26 and recorded in GOV-REG-07. In a shared co-working space the whole space is treated as a Public zone: [Organisation] relies on device and screen controls, keeps no Restricted paper there, and uses a lockable locker for anything left on site.

## 5. Records and evidence

- GOV-REG-19 Physical access and visitor log.
- Access control system logs and the quarterly access list reviews in GOV-REG-12.
- Utility test and maintenance records.
- The yearly inspection report and resulting corrective actions.
- Provider assurance records in GOV-REG-07 for cloud data centres.

## 6. Exceptions

Emergency services enter any zone without registration during an emergency and the Facilities Manager records the event afterwards. Unescorted access for a contractor is granted only in writing by the Information Security Manager for a stated period and is noted in GOV-REG-19. No other exception applies.

## 7. Review and maintenance

The Information Security Manager reviews this procedure annually, after any physical security incident, and before and after a move or change of premises. Changes follow GOV-PRO-01.

## 8. Related documents

- GOV-REG-19 Physical access and visitor log
- GOV-REG-12 Access review log
- GOV-REG-24 Software and hardware inventory
- GOV-POL-04 Clear desk and clear screen policy
- GOV-POL-05 Remote and mobile working policy
- GOV-PRO-16 Asset management, classification and handling procedure
- GOV-PRO-22 Endpoint and mobile device security procedure
- GOV-PRO-26 Cloud services security procedure
- GOV-PRO-07 Information security incident management procedure
