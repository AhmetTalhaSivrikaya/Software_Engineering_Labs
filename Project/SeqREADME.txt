## Message Flow
- Auto Mode: The System sends `readOccupancy()` and `getCurrentTemp()` to Sensors.
- Alt A (Heater Control): If the room is cold, the System sends `turnOnHeater()` to the Climate Unit.
- Alt B (Confirmation): The System notifies the User once the target temperature is reached (`heatIsOK`).
- Manual Mode: User directly sets the temperature, triggering a `selfCheck` on the System.