# name=Novation Launchpad X Custom
import lights
import sysex
import device # type: ignore

class LaunchpadX():
    def __init__(self) -> None:
        pass

    def reset(self) -> None:
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 0, 1, 247]))        # Set View To Note Mode
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 15, 0, 247]))       # Set Note Mode To Scale
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 18, 1, 1, 1, 247])) # Clear Session, Drum, and CC
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 23, 0, 247]))       # Change Note Active color
        device.midiOutSysex(bytes([240, 0, 32, 41, 2, 12, 20, 0, 0, 247]))

        lights.clear_lights(0)

    def OnInit(self):
        # Set device to DAW mode.
        sysex.enable_daw_mode()
        self.reset()


controller = LaunchpadX()
def OnInit():
    controller.OnInit()