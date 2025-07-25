# name=Novation Launchpad X Custom
import lights
import sysex
from pages import Page
from settings import Settings
from page_testing import TestingPage

class LaunchpadX():
    def __init__(self) -> None:
        self.settings = Settings()
        # Place custom startup settings here
        # Example: pad startup takes you to the session tab immediately.
        self.settings.set_setting("startup.mode", 0)
        self.settings.set_setting("page.negative_edge", True)
        self.page: Page = TestingPage(self)
        self.page.OnInit()

    def reset(self) -> None:
        sysex.select_mode(self.settings.get_setting("startup.mode"))
        self.mode = self.settings.get_setting("startup.mode")
        sysex.daw_clear()
        sysex.active_note_color(0)
        sysex.session_colors()
        self.LoadPage(self.page)

    def OnInit(self):
        # Set device to DAW mode.
        sysex.enable_daw_mode()
        self.reset()

    def LoadPage(self, page: Page):
        self.page = page
        self.page.refresh()


controller = LaunchpadX()

def OnInit():
    controller.OnInit()

def OnDeInit():
    controller.page.OnDeInit()

def OnMidiIn(event):
    controller.page.OnMidiIn(event)

def OnMidiMsg(event):
    if event.status == 208:
        raise(Exception("Controller sent 208 status message. To fix this, enable polyphonic aftertouch."
                        " https://userguides.novationmusic.com/hc/en-gb/articles/23731440793490-Launchpad-X-s-Settings-menu"))
    
    # Mode buttons
    match event.note:
        case 95:
            if controller.mode == 0 and event.velocity == 127:
                controller.page.OnMidiMsg(event)
            controller.mode = 0
            
        case 96:
            controller.mode = 1

        case 97:
            controller.mode = 4 # 4 for all custom modes.

        case _:
            controller.page.OnMidiMsg(event)

def OnSysEx(event):
    controller.page.OnSysEx(event)

def OnNoteOn(event):
    controller.page.OnNoteOn(event)

def OnNoteOff(event):
    controller.page.OnNoteOff(event)

def OnControlChange(event):
    controller.page.OnControlChange(event)

def OnProgramChange(event):
    controller.page.OnProgramChange(event)

def OnPitchBend(event):
    controller.page.OnPitchBend(event)

def OnKeyPressure(event):
    controller.page.OnKeyPressure(event)

def OnChannelPressure(event):
    controller.page.OnChannelPressure(event)

def OnMidiOutMsg(event):
    controller.page.OnMidiOutMsg(event)

def OnIdle():
    controller.page.OnIdle()

def OnProjectLoad(status):
    controller.page.OnProjectLoad(status)

def OnRefresh(flags):
    controller.page.OnRefresh(flags)

def OnDoFullRefresh():
    controller.page.OnDoFullRefresh()

def OnUpdateBeatIndicator(value):
    controller.page.OnUpdateBeatIndicator(value)

def OnDisplayZone():
    controller.page.OnDisplayZone()

def OnUpdateLiveMode(lastTrack):
    controller.page.OnUpdateLiveMode(lastTrack)

def OnDirtyMixerTrack(index):
    controller.page.OnDirtyMixerTrack(index)

def OnDirtyChannel(index, flag):
    controller.page.OnDirtyChannel(index, flag)

def OnFirstConnect():
    controller.page.OnFirstConnect()

def OnUpdateMeters():
    controller.page.OnUpdateMeters()

def OnWaitingForInput():
    controller.page.OnWaitingForInput()

def OnSendTempMsg(message, duration):
    controller.page.OnSendTempMsg(message, duration)