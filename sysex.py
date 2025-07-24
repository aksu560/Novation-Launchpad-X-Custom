import device # type: ignore
def enable_daw_mode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 16, 1, 247]))

def disable_daw_mode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 16, 0, 247]))

def select_mode(mode):
    # 0: Session (DAW Only)
    # 1: Note
    # 4-7: Custom 1-4
    # 13: Faders (DAW Only)
    # 127: Programmer
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 0, mode, 247]))

def select_note_mode(mode):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 21, mode, 247]))  

def note_mode_configuration(mode, param):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 22, mode, param, 247]))  

def active_note_color(color):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 23, color, 247])) 

def daw_clear():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 18, 1, 1, 1, 247]))

def session_colors(hi = 0, lo = 0):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 20, hi, lo, 247]))