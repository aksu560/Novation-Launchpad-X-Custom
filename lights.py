import device # type: ignore
import coordinates

class PadColor():
    def __init__(self, color:str) -> None:
        self.color = color
        pass

    def color_num(self):
        # Special names for specific colors.
        special = {
            "BLACK": 0,
            "DARK_GRAY": 1,
            "LIGHT_GRAY": 2,
            "WHITE": 3,
        }
        # How manyeth block the color range is.
        color_range_index = {
            "WHITE": 0,
            "RED": 1,
            "ORANGE": 2,
            "YELLOW": 3,
            "GREEN": 4,
            "LIME": 5,
            "JADE": 6, # There's 3 different greens and 5 blues in this palette, cut me some slack.
            "AQUA": 7,
            "TURQ": 8,
            "CYAN": 9,
            "BLUE": 10,
            "PURPLE": 11,
            "LILAC": 12,
            "MAGENTA": 13,
            "PINK": 14,
            "GROUND": 15 #The last set of colours is weird.
        }
        color_mod_index = {
            "LIGHT": 0,
            "NORMAL": 1,
            "DARK": 3
        }

        # If colour is a number, use the number directly (this gives access to codes >63)
        try:
            return(int(self.color))
        except:
            pass
        for k, v in special.items():
            if k == self.color:
                return v
        
        # Dynamic names that allow access to the first 64 colours.

        split = self.color.split("_")
        mod = "NORMAL"
        color = "RED"        
        if len(split) == 1:
            color = split[0]
        elif len(split) == 2:
            mod = split[0]
            color = split[1]
        else:
            raise(Exception("Invalid dynamic color"))
        
        return(color_range_index[color] * 4 + color_mod_index[mod])
        
class PadLight():
    def __init__(self, color: str = "0", pulse_mode = 0, pulse_color: str = "0") -> None:
        self.color = PadColor(color)
        self.pulse_mode = pulse_mode
        self.pulse_color = PadColor(pulse_color)

def set_light(x: int, y: int, mode: int, light: PadLight):
    """Set lighting data for the launchpad.
    ## Args
    * x: X coordinate of pad
    * y: Y coordinate of pad
    * mode: Which page to light (0: Session)
    * light: PadLight object
    """

    # https://github.com/MetallicAsylum/Novation-Launchpad-X-MK3/blob/main/helpers.py
    mod_state_cc_map = {-1:176, 0:144, 1:152, 13:181, 127:144}

    # Black magic from Maxwell's script...
    if (9 in [x, y]):
            mode = -1

    device.midiOutMsg(mod_state_cc_map[mode],
                      mod_state_cc_map[mode],
                      coordinates.xy_to_pad_coords(x, y),
                      light.color.color_num())
    
    # Set a second light if a pulse mode is enabled.
    if light.pulse_mode != 0:
        device.midiOutMsg(mod_state_cc_map[mode],
                      mod_state_cc_map[mode] + light.pulse_mode,
                      coordinates.xy_to_pad_coords(x, y),
                      light.pulse_color.color_num())
        
def set_session_light(active: PadColor, inactive: PadColor):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 20, active.color_num(), inactive.color_num(), 247]))

def clear_lights(mode):
    light = PadLight("0", 0)
    for x in range(0, 10):
        for y in range(0, 10):
            set_light(x, y, mode, light)