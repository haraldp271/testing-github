import unittest
from hellopy.greetme import greetme


class TestGreetme(unittest.TestCase):
    def test_greetme(self):
        greeting = greetme(name="Dude")
        self.assertEqual(greeting, "Hello Dude!")
