#Clinic Management System

This diagram represents the functional flow of a healthcare facility's digital appointment and transaction system.

## Actors
Patient:The primary user seeking medical services.
Admin:Manages schedules and oversees system operations.
Clinic Database: Central repository for patient records and appointment logs.

## Functional Components
Appointment:The initial step where a patient schedules a visit.
ID Verification: A mandatory (Includes) step for patients to access the transaction phase.
Transaction:The main container for medical services, featuring an "Invalid ID" extension for error handling.
-Medical Departments
    * Simple Diseases
    * Dentistry
    * Child Health

## System Design
The system ensures that no transaction (treatment/consultation) occurs without prior ID verification, maintaining data integrity within the Clinic Database.