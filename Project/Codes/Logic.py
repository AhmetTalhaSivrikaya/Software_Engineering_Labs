class ThermostatController:
    def __init__(self):
        self.state = "Idle"
        self.is_connect = True
        self.human_count = 0
        self.target_temp = 22
        self.manual_mode = False

    def get_current_state(self):
        return self.state

    def set_human_count(self, count):
        self.human_count = count     

    def set_manual_mode(self, status):
        self.manual_mode = status
        if status:
            self.state = "Manual Mode"

    def set_temp(self, temp):
        self.target_temp = temp

    def monitor_occupancy(self):
        if self.human_count == 0:
            self.state = "Energy Saving"

    def auto_temp_adjustment(self):
        if not self.manual_mode:
            self.target_temp = 22 - (self.human_count * 0.5)

    def check_system_status(self):
        if not self.is_connect or self.human_count < 0:
            self.state = "Safe mode"
            self.target_temp = 21