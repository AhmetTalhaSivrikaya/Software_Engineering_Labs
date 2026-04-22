# Car Insurance - Business Workflow

An Activity Diagram illustrating the user journey from login to policy activation.

## Workflow Stages
Entry Point: The process starts with a login check. New users are directed to 'Login/Register'.
Main Menu: The central hub where users choose between 'Renew Policy' or 'File a Claim'.
Claim Path:User files a claim and enters a 'Wait for Admin' state for approval.
Renewal & Payment Path: 1. User selects 'Renew Policy' and views the details.
    2. A Decision Diamond handles the payment. If unsuccessful, the user is looped back to the payment stage.
    3. If successful, the database is updated.
Activation:After a set time (timer event), the policy status transitions to 'Active Policy'.

## Design Elements
- Decision Nodes: Used for Login and Payment status.
- Event Wait: Represents the delay between database update and final policy activation.