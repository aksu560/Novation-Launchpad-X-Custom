# name=Novation Launchpad X Custom
import lights
import sysex
import pages

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

        test_pad = pages.Pad(lights.PadLight("GREEN"), test_function)

        test_module = pages.Module([(0, 0, test_pad)])
        test_page = pages.Page(
            [pages.Element(1, 1, test_module)],
            session_lights=(5, 10)
        )

        test_page.refresh()


controller = LaunchpadX()
def OnInit():
    controller.OnInit()

def test_function(_):
    print("Foo")