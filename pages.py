import coordinates
import lights
import sysex
from typing import Callable
from debug import print_event

class Pad():
    def __init__(self, light:lights.PadLight, callback: Callable) -> None:
        self.light = light
        self.callback = callback

class Module():
    def __init__(self, pads: list[tuple[int, int, Pad]]) -> None:
        self.pads = pads

class Element():
    def __init__(self, x: int, y: int, module: Module, shift = False) -> None:
        self.x = x
        self.y = y
        self.shift = shift
        self.module = module

class Page():
    """
    Page class. Pages are used for creating custom behaviour for session mode.
    Switching between them is done with the LaunchpadX.LoadPage() function.
    """
    def __init__(self, controller, elements:list[Element], mode = 0, session_lights = (0, 0)) -> None:
        self.controller = controller
        self.mode = mode
        self.elements = elements
        self.lights = {}
        self.callbacks = {}
        self.refresh_callback = lambda: None
        self.session_lights = session_lights
        self.held_keys = set()
        self.enable_shift = True
        for elem in elements:
            for pad in elem.module.pads:
                (x, y, pad) = pad
                x = elem.x + x
                y = elem.y + y
                # Keys under shift are shifted 100 positions upwards.
                coords = coordinates.xy_to_pad_coords(x, y) + (elem.shift * 100)
                self.lights[coords] = pad.light
                self.callbacks[coords] = pad.callback

    def refresh(self):
        lights.clear_lights(self.mode)
        sysex.session_colors(self.session_lights[0], self.session_lights[1])

        for x in range(1, 10):
            for y in range(1, 10):
                if coordinates.xy_to_pad_coords(x, y) + (self.is_shift_pressed() * 100) in self.lights.keys():
                    light = self.lights[coordinates.xy_to_pad_coords(x, y) + (self.is_shift_pressed() * 100)]
                else:
                    light = lights.PadLight("0")
                lights.set_light(x, y, self.mode, light)
            
        
        self.refresh_callback()

    def key_event(self, eventData):
        match eventData.status:
            # Polyphonic Aftertouch.
            case 160:
                if eventData.note not in self.held_keys:
                    self.held_keys.add(eventData.note)
            # Edge Buttons
            case 176:
                # Release event
                if eventData.velocity == 0:
                    self.held_keys.discard(eventData.note)
                    self.key_activate(eventData, True)
                # Press event
                else:
                    self.held_keys.add(eventData.note)
                    self.key_activate(eventData, False)
            case 144:
                # Release event
                if eventData.velocity == 0:
                    self.held_keys.discard(eventData.note)
                    self.key_activate(eventData, True)
                # Press event
                else:
                    self.held_keys.add(eventData.note)
                    self.key_activate(eventData, False)
        
        eventData.handled = True        

    def key_activate(self, event, release):
        if event.note == 98:
            self.on_shift()
            return
        # Negative edge check. Session button ignores negative edge for reasons.
        if self.controller.settings.get_setting("page.negative_edge") == release or event.note == 95:
            event.note += 100 * self.is_shift_pressed()
            if event.note in self.callbacks.keys():
                if self.callbacks[event.note](event):
                    self.refresh()

    def is_shift_pressed(self) -> bool:
        return self.enable_shift and 98 in self.held_keys
    
    def on_shift(self):
        self.refresh()

    def OnInit(self):
        pass

    def OnDeInit(self):
        pass

    def OnMidiIn(self, eventData):
        pass

    def OnMidiMsg(self, eventData):
        self.key_event(eventData)

    def OnSysEx(self, eventData):
        pass

    def OnNoteOn(self, eventData):
        pass
    
    def OnNoteOff(self, eventData):
        pass

    def OnControlChange(self, eventData):
        pass

    def OnProgramChange(self, eventData):
        pass

    def OnPitchBend(self, eventData):
        pass

    def OnKeyPressure(self, eventData):
        pass

    def OnChannelPressure(self, eventData):
        pass

    def OnMidiOutMsg(self, eventData):
        pass

    def OnIdle(self):
        pass

    def OnProjectLoad(self, status):
        pass

    def OnRefresh(self, flags):
        pass

    def OnDoFullRefresh(self):
        pass

    def OnUpdateBeatIndicator(self, value):
        pass

    def OnDisplayZone(self):
        pass

    def OnUpdateLiveMode(self, lastTrack):
        pass

    def OnDirtyMixerTrack(self, index):
        pass

    def OnDirtyChannel(self, index, flag):
        pass

    def OnFirstConnect(self):
        pass

    def OnUpdateMeters(self):
        pass

    def OnWaitingForInput(self):
        pass

    def OnSendTempMsg(self, message, duration):
        pass