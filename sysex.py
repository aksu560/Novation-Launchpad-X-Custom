import device # type: ignore
def enable_daw_mode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 16, 1]))

def disable_daw_mode():
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 16, 0]))

def select_mode(mode):
    device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 0, mode, 247]))