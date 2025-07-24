import coordinates
import lights
import sysex
from typing import Callable

class Pad():
    def __init__(self, light:lights.PadLight, callback: Callable[[int], None]) -> None:
        self.light = light
        self.callback = callback

class Module():
    def __init__(self, pads: list[tuple[int, int, Pad]]) -> None:
        self.pads = pads

class Element():
    def __init__(self, x: int, y: int, module: Module) -> None:
        self.x = x
        self.y = y
        self.module = module

class Page():
    def __init__(self, elements:list[Element], mode = 0, session_lights = (0, 0)) -> None:
        self.mode = mode
        self.elements = elements
        self.lights = {}
        self.callbacks = {}
        self.session_lights = session_lights
        for elem in elements:
            for pad in elem.module.pads:
                print(pad)
                (x, y, pad) = pad
                x = elem.x + x
                y = elem.y + y
                coords = coordinates.xy_to_pad_coords(x, y)
                self.lights[coords] = pad.light
                self.callbacks[coords] = pad.callback

        self.refresh()
    

    def refresh(self):
        lights.clear_lights(self.mode)
        sysex.session_colors(self.session_lights[0], self.session_lights[1])
        for key, light in self.lights.items():
            (x, y) = coordinates.pad_coords_to_xy(key)
            lights.set_light(x, y, self.mode, light)