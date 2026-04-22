# Car Insurance - Class Diagram

A simplified representation of the interaction between a customer and an insurance provider.

## Class Overview

### 1. Customer
Represents the entity seeking insurance services.
- Attributes: `customerID` (int), `name` (String), `phone` (String).
- Methods: `requestInsurance()`.

### 2. Company
Represents the service provider.
- Attributes: `companyID` (int), `name` (String).
- Methods: `createPolicy()`.

## Relationships
- Directed Association: A `Customer` initiates a request to the `Company`. This shows a one-way interaction where the customer depends on the company's service to generate a policy.