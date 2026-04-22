## Workflow Logic
1. Mode Selection: System checks if the user wants 'Manual' or 'Automatic' mode.
2. Automatic Path: - Monitors occupancy via sensors.
   - If house is empty -> Energy Saving Mode.
   - If occupancy detected -> Checks `currentTemp` vs `targetTemp` and adjusts accordingly.
3. Loop: The system continuously monitors and re-checks temperature to maintain the target.