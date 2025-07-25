class Settings():
    def __init__(self) -> None:
        self.settings = {
            "page.negative_edge": {
                "value": False,
                "options": [False, True]
            },
            "performance.movement_step": {
                "value": 1,
                "options": [1, 8]
            },
            # 0: Session, 1: Note, 4-7: Custom 1-4, 13: Faders, 127: Programmer
            "startup.mode": {
                "value": 1,
                "options": [0, 1, 4, 5, 6, 7, 13,]
            }
        }

    def get_setting(self, setting):
        return self.settings[setting]["value"]
    
    def get_setting_options(self, setting):
        return self.settings[setting]["options"]
    
    def set_setting(self, setting, value):
        if value in self.get_setting_options(setting):
            self.settings[setting]["value"] = value
        else:
            raise(Exception("Invalid value '", value, "' for setting '", setting, "'"))