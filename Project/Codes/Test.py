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

    def test_target_temp_adjusts_with_occupancy(self):
        # Arrange
        controller = ThermostatController()
        
        # Act: Evde 1 kişi varken 22 derece ideal olsun
        controller.set_human_count(1)
        controller.auto_temp_adjustment()
        temp_with_one = controller.target_temp
        
        # Evde 5 kişi varken (insan ısısı arttığı için) hedef sıcaklık düşmeli
        controller.set_human_count(5)
        controller.auto_temp_adjustment()
        temp_with_five = controller.target_temp
        
        # Assert: 5 kişi varken hedef sıcaklık daha düşük olmalı
        self.assertTrue(temp_with_five < temp_with_one)


if __name__ == '__main__':
    unittest.main()        