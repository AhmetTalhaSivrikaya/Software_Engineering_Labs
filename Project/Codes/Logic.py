class ThermostatController:
    def __init__(self):
        self._state = "Idle"
        self._human_count = 0

    def get_current_state(self):
        return self._state

    def set_human_count(self, count):
        self._human_count = count

    def monitor_occupancy(self):
        # TDD "Green" aşaması: Testin beklediği durumu sağlayan minimum mantık
        if self._human_count == 0:
            self._state = "Energy Saving"