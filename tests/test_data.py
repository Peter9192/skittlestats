from unittest import TestCase

import skittlestats
from skittlestats.command_line import main

class TestData(TestCase):
    def test_data_dimensions(self):
        assert (15*8==120)

class TestConsole(TestCase):
    def test_command_line(self):
        main()
