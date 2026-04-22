# ATM System - Use Case

This project defines the functional requirements for a standard Automated Teller Machine (ATM) system using a Use Case Diagram.

## Actors
User:The primary actor who interacts with the ATM to perform banking tasks.
Bank Database:The secondary actor (system) that validates credentials and processes financial records.
Admin: Responsible for maintenance and system monitoring.

## Key Use Cases
Authentication:The system requires a `CARD` and a `PIN`. Note that the PIN is included as a mandatory step.
Transaction: The core process that encompasses multiple financial actions.
Invalid PIN: An extension point that handles incorrect credential entries.
Financial Services:** Includes `Withdraw Money`, `Deposit`, and `Transfer`.

## Relationships
Includes: PIN entry is mandatory for card usage.
Extends: Invalid PIN logic triggered only during failed authentication.