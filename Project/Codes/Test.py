import unittest
import time
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

    def test_target_temp_adjusts_with_occupancy(self):
        controller = ThermostatController()
        
        controller.set_human_count(1)
        controller.auto_temp_adjustment()
        temp_with_one = controller.target_temp
        
        controller.set_human_count(5)
        controller.auto_temp_adjustment()
        temp_with_five = controller.target_temp
        
        self.assertTrue(temp_with_five < temp_with_one)
    
    def test_safe_mode_on_sensor_disconnection(self):
        controller = ThermostatController()
        
        controller.is_connect = False 
        controller.check_system_status() 
        
        self.assertEqual(controller.get_current_state(), "Safe mode")
        self.assertEqual(controller.target_temp, 21)

    def test_processing_performance(self):
        controller = ThermostatController()
        
        start_time = time.time()
        controller.monitor_occupancy()
        end_time = time.time()
        
        duration = end_time - start_time
        
        self.assertLess(duration, 3.0)
        
if __name__ == '__main__':
    unittest.main()        