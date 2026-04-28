import unittest
from Logic import ThermostatController

class TestThermostat(unittest.TestCase):
    def test_initial_state_is_idle(self):
        control = ThermostatController()
        current_state = control.get_current_state()
        self.assertEqual(current_state, "Idle")

if __name__ == '__main__':
    unittest.main()