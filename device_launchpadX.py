# name=Novation Launchpad X Custom
import lights
import sysex
import device # type: ignore

class LaunchpadX():
    def __init__(self) -> None:
        pass

    def reset(self) -> None:
        sysex.select_mode(1)
        sysex.daw_clear()
        sysex.active_note_color(0)
        sysex.session_colors()
        lights.clear_lights(0)

    def OnInit(self):
        # Set device to DAW mode.
        sysex.enable_daw_mode()
        self.reset()


controller = LaunchpadX()
def OnInit():
    controller.OnInit()