import unittest

from boilerplate import new_stuff


class TestStuff(unittest.TestCase):
    def test_stuff(self):
        self.assertEqual(new_stuff(None), "Here's some new stuff!")
