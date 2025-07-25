# Dev testing page
from pages import Page, Element, Module, Pad
from lights import PadLight

class TestingPage(Page):
    def __init__(self, controller) -> None:

        test_elem = Element(
            5, 9,
            Module([
                (0, 0, Pad(PadLight("JADE"), self.test_cb_1)),
            ])
        )

        super().__init__(controller, [test_elem])

    def test_cb_1(self, _):
        print("foo")