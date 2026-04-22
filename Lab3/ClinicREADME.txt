# Medical Clinic - Class Diagram
This diagram illustrates the core management system of a medical clinic, linking staff, patients, and the central system logic.

## Class Overview

### 1. System
The central controller of the application.
- Attributes: `patients: List<Patient>`, `staffList: List<Staff>`.
- Methods: `addPatient()`, `getPatient()`, `updatePatient()`.

### 2. Staff
Represents medical or administrative personnel.
- Attributes: `staffID` (int), `name` (String), `role` (String).
- Methods: `addPatient()`, `updatePatient()`.

### 3. Patient
Represents the individuals receiving care.
- Attributes: `patientID` (int), `name` (String), `diagnosis` (String).
- Methods: `getInfo()`, `updateInfo()`.

## Relationships
- Composition/Aggregation: The `System` class is the central hub connected via diamond connectors to both `Staff` and `Patient`. This indicates that the `System` manages the lifecycle and storage of both staff and patient data.