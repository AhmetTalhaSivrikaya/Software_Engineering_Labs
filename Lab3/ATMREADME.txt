# ATM System - Class Diagram

This document describes the structural design of the ATM system, focusing on the data management and core banking logic.

## Class Overview

### 1. ATM Machine
Responsible for the physical interface and transaction requests.
- Attributes: `Location` (String), `atmID` (int).
- Methods: `start()`, `authenticateUser()`, `requestTransaction()`.

### 2. Database
Acts as the middleware that manages account data and validation.
- Attributes: `List -> Account` (A collection of account objects).
- Methods: `validateUser()`, `getAccount()`, `updateBalance()`.

### 3. Account
Represents the individual user's financial data.
- Attributes: `accountNumber` (int), `balance` (double).
- Methods: `deposit(amount)`, `withdraw(amount)`, `getBalance()`.

## Relationships
- Association: The `ATM Machine` communicates with the `Database` to verify users.
- Aggregation:The `Database` contains a list of `Account` objects, implying a whole-part relationship where accounts exist independently.