# Medical Clinic - State Machine Analysis

This diagram focuses on the states of a patient's session within the Medical Clinic System.

## Lifecycle States
ID Check: The initial state where the patient's identity is verified.
Exit State: Reached if an 'Invalid ID' is provided, terminating the session.
Appointment: The active state where the patient schedules their visit.
Choose Sickness (Sub-states):** A composite state where the specific department is selected:
    * Dentistry
    * Simple Diseases (Note: Spelled as "Diases" in diagram)
    * Child Health
Final State:The session is successfully completed after the department selection.

## Transitions
- ID Check -> Exit:Triggered by an authentication failure.
- ID Check -> Appointment: Triggered by a successful ID match.
- Appointment -> Choose Sickness: Progression to department-specific selection.