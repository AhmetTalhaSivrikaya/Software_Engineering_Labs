class ThermostatController:
    def __init__(self):
        self.state = "Idle"
        self.human_count = 0
        self.target_temp = 22
        self.is_connect = True  

    def get_current_state(self):
        return self.state

    def set_human_count(self, count):
        self.human_count = count

    def monitor_occupancy(self):
        if self.human_count == 0:
            self.state = "Energy Saving"

    def auto_temp_adjustment(self):
       
        self.target_temp = 22 - (self.human_count * 0.5)

    def check_system_status(self):
     
        if not self.is_connect:
            self.state = "Safe mode"
            self.target_temp = 21
    def monitor_occupancy(self):
      
        if self.is_connect:
            if self.human_count == 0:
                self.energy_save()
            else:
                self.auto_temp_adjustment()
        else:
            self.check_system_status()

    def energy_save(self):
        self.state = "Energy Saving"
        
        self.target_temp = 0 