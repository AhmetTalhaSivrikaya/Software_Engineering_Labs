## Operational States
- Idle: Waiting for user entry or sensor trigger.
- Manual Mode: Direct user control state.
- Automatic Mode: A composite state containing:
  - `Monitoring Occupancy` -> `Checking Temp` -> `Adjust Temp` (Internal Loop).
- Energy Saving: Low-power state when no one is home.
- Safe Mode: Triggered by a Critical Fault. Can only be exited via Technical Team Reset.