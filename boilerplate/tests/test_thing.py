import unittest
from boilerplate import Thingy


class TestThingy(unittest.TestCase):
    def test_thingy(self):
        t = Thingy()
        self.assertIsNone(t.stuff)
