Home Temperature Adjustment System (HTAS) This project is a design for an intelligent and autonomous IoT system that dynamically manages household temperature by monitoring real-time occupancy (human count). It aims to maximize user comfort while preventing energy waste caused by traditional manual systems.

Key Features Autonomous Occupancy Monitoring: Detects the number of people in the house via sensors and adjusts climate units accordingly.

Energy Saving Mode: Automatically shuts down or lowers power for climate units when no occupancy is detected.

Hybrid Control: Allows users to override autonomous mode at any time and enter manual temperature settings.

Safe Mode: In case of critical failures (e.g., sensor disconnection), the system operates at a standard "Safe" temperature (e.g., 21°C) to maintain basic comfort.

High Performance: Sensor data is processed in less than 3 seconds to ensure real-time responsiveness.

Technical Architecture The system is designed to operate within five core states (Idle, Manual, Automatic, Energy Saving, Safe Mode). The architectural components include:

Controller: The central unit that manages human count, current temperature, and safety protocols.

Sensors: Hardware components providing real-time occupancy and environmental data.

Climate Unit: The physical unit that adjusts temperature based on commands from the controller.

Interface: A dual-purpose UI for standard users (monitoring/settings) and the technical team (configuration).
