# Dev testing page
from pages import Page, Element, Module, Pad
from lights import PadLight

class TestingPage(Page):
    def __init__(self, controller) -> None:

        test_elem = Element(
            1, 1,
            Module([
                (0, 0, Pad(PadLight("JADE"), self.test_cb_1)),
            ])
        )

        shift_elem = Element(
            1, 1,
            Module([
                (0, 0, Pad(PadLight("RED"), self.test_cb_shift)),
            ]),
            True
        )

        super().__init__(controller, [test_elem, shift_elem])

    def test_cb_1(self, _):
        print("foo")
    
    def test_cb_shift(self, _):
        print("FOO")