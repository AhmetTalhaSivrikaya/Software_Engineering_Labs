## System Components
- Controller: The brain of the system. Maintains `humanCount`, `currentTemp`, and security status.
- Sensor: Inherits/Aggregates to the controller (Composition relationship) to send data.
- Climate Unit: Managed by the controller to adjust physical temperature.
- Interface: A boundary class for User and Tech Team interactions.

## Relationships
- Composition (Black Diamond): Sensors are integral parts of the Controller.
- Aggregation (White Diamond): Climate Units are managed by the Controller but exist as separate hardware.