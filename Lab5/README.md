# Software Engineering - The Bowling Game Kata (TDD Lab)

This project implements the **Bowling Game Kata**, a classic exercise in Test-Driven Development (TDD). The primary goal of this lab was to practice incremental design and master the Red-Green-Refactor cycle.

##Learning Objectives
- Understanding the **Red-Green-Refactor** cycle.
- Applying the **Three Laws of TDD**.
- Observing how design emerges from tests (e.g., transitioning from a simple score variable to a list of rolls).
- Mastering **Pair Programming** using the Ping-Pong approach.

##Ping-Pong Pair Programming
Following the instructions in the lab manual, we utilized the **Ping-Pong** method:
1. **Student A (Red):** Wrote a failing test for a specific requirement (e.g., Gutter Game, Spares, Strikes).
2. **Student B (Green):** Wrote the minimal code necessary to make the test pass.
3. **Student B (Refactor):** Improved the code structure without changing its behavior, then wrote the next failing test.
4. **Roles Swapped** for each increment.

##Bowling Scoring Rules Handled
- **Gutter Game:** A game where all 20 rolls result in 0 pins (Score: 0).
- **All Ones:** A game where all 20 rolls result in 1 pin (Score: 20).
- **One Spare:** A frame where two rolls total 10, plus the next roll's bonus.
- **One Strike:** A frame where the first roll is 10, plus the bonus of the next two rolls.
- **Perfect Game:** 12 consecutive strikes (Score: 300).

##Project Structure
- `Logic.py`: Contains the `BowlingGame` class and the scoring logic.
- `test_bowling.py`: Contains the `unittest` suite covering all scoring scenarios.

##How to Run Tests
To verify the implementation and see the TDD results, run the following command in your terminal:
```bash
python -m unittest test_bowling.py
