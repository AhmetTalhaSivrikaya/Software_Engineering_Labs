import unittest
from Logic import ThermostatController

class TestThermostat(unittest.TestCase):
    def test_initial_state_is_idle(self):
        control = ThermostatController()
        current_state = control.get_current_state()
        self.assertEqual(current_state, "Idle")

    def test_energy_saving_mode_when_empty(self):
        controller = ThermostatController()       
        controller.set_human_count(0)
        controller.monitor_occupancy() 
        self.assertEqual(controller.get_current_state(), "Energy Saving")    




if __name__ == '__main__':
    unittest.main()        