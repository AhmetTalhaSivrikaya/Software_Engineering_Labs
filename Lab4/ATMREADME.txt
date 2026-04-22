# ATM System - Sequence Diagram

This diagram details the step-by-step interaction between the User, the ATM hardware, and the Bank Database during a withdrawal process.

## Process Flow
1. Card Validation: The user inserts a card; the ATM verifies it with the database.
   - Conditional Logic: If valid, the system requests a PIN. If invalid, the card is ejected.
2. Authentication: The user enters a PIN, which is then verified by the database.
3. Transaction Request: Once verified, the user initiates a 'Withdraw Money' request.
4. Fund Verification: The ATM checks with the database for sufficient funds.
5. Completion: Upon confirmation of enough funds, the ATM dispenses cash and returns the card to the user.

## Key Interactions
- Synchronous Messages: PIN verification and Fund checks.
- Alternative Paths: Integrated `if/else` block for card validity handling.