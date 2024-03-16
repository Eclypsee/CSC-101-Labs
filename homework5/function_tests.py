"""function_tests.py"""

import unittest

from creature import Creature
from loader import CREATURES, CREATURES_RED, CREATURES_BLUE
from functions import *


class FunctionTests(unittest.TestCase):

    def test_function_01_example(self):
        self.assertEqual(365, get_total_experience(CREATURES_RED[0]))
        self.assertEqual(352, get_total_experience(CREATURES_RED[1]))
        self.assertEqual(320, get_total_experience(CREATURES_RED[2]))

        self.assertEqual(320, get_total_experience(CREATURES_BLUE[2]))
        self.assertEqual(765, get_total_experience(CREATURES[99]))

    def test_function_02_example(self):
        self.assertAlmostEqual(91.25, get_average_experience(CREATURES_RED[0]))
        self.assertAlmostEqual(88.00, get_average_experience(CREATURES_RED[1]))
        self.assertAlmostEqual(80.00, get_average_experience(CREATURES_RED[2]))

        self.assertAlmostEqual(111.5, get_average_experience(CREATURES_BLUE[3]))
        self.assertAlmostEqual(119.5, get_average_experience(CREATURES[87]))


    def test_function_03_example(self):
        self.assertEqual(100, get_attribute(CREATURES_RED[0], 'willpower'))
        self.assertEqual(77, get_attribute(CREATURES_RED[1], 'RESilienCe'))
        self.assertEqual(0, get_attribute(CREATURES_RED[2], 'bank account balance'))

        self.assertEqual(0, get_attribute(CREATURES_BLUE[2], 'Elon Musk'))
        self.assertEqual(186, get_attribute(CREATURES[2], 'determination'))

    def test_function_04_example(self):
        self.assertTrue(has_kind(CREATURES_RED[3], 'nature'))
        self.assertTrue(has_kind(CREATURES_RED[3], 'DaRk'))
        self.assertFalse(has_kind(CREATURES_RED[3], 'fire'))
        self.assertFalse(has_kind(CREATURES_RED[3], 'candy corn'))

        self.assertFalse(has_kind(CREATURES_BLUE[3], 'water'))
        self.assertFalse(has_kind(CREATURES[3], 'HoRsE'))

    def test_function_05_example(self):
        self.assertEqual(['Dinospore', 'Emberspark', 'Ripplefin'], get_names(CREATURES_RED[:3]))
        self.assertEqual(['Slumberbug', 'Shadowgnome', 'Emberfox'], get_names(CREATURES_RED[3:6]))
        self.assertEqual(['Nightgale', 'Urania', 'Harvinger', 'Pearlificent'], get_names(CREATURES_RED[6:]))
        self.assertEqual([], get_names(CREATURES_RED[0:0]))

        self.assertEqual(['Lumiworm', 'Lanternsprite', 'Frostkit'], get_names(CREATURES_BLUE[3:6]))
        self.assertEqual(['Ripplefin', 'Waveorca'], get_names(CREATURES[6:8]))

    def test_function_06_example(self):
        self.assertEqual(['Dinospore', 'Ripplefin', 'Slumberbug'],
                         get_names(filter_by_description(CREATURES_RED, 'small')))
        self.assertEqual(['Shadowgnome', 'Emberfox'], get_names(filter_by_description(CREATURES_RED, 'FrIeNdLy')))
        self.assertEqual([], get_names(filter_by_description(CREATURES_RED, 'definitely not a pokemon')))

        self.assertEqual(['Lanternsprite'], get_names(filter_by_description(CREATURES_BLUE, 'FrIeNdLy')))
        self.assertEqual([], get_names(filter_by_description(CREATURES, 'we go to mars')))

    def test_function_07_example(self):
        self.assertEqual(['Emberspark', 'Shadowgnome', 'Emberfox', 'Harvinger'],
                         get_names(filter_by_kind(CREATURES_RED, 'fire')))
        self.assertEqual(['Nightgale', 'Urania'], get_names(filter_by_kind(CREATURES_RED, 'WiNd')))
        self.assertEqual([], get_names(filter_by_kind(CREATURES_RED, 'unkind')))

        self.assertEqual(['Emberspark', 'Lanternsprite'], get_names(filter_by_kind(CREATURES_BLUE, 'fire')))
        self.assertEqual([], get_names(filter_by_kind(CREATURES, 'the rock obama')))

    def test_function_08_example(self):
        self.assertEqual(['Emberspark', 'Ripplefin', 'Shadowgnome'],
                         get_names(filter_by_attribute_less_than(CREATURES_RED, 'resilience', 90)))
        self.assertEqual(['Emberspark', 'Slumberbug', 'Harvinger'],
                         get_names(filter_by_attribute_less_than(CREATURES_RED, 'WiLlPoWeR', 100)))
        self.assertEqual(get_names(CREATURES_RED),
                         get_names(filter_by_attribute_less_than(CREATURES_RED, 'YouTube followers', 255)))

        self.assertEqual(['Voltantler'],
                         get_names(filter_by_attribute_less_than(CREATURES_BLUE, 'WiLlPoWeR', 40)))
        self.assertEqual(['Metalynx', 'Steelskitter', 'Viruking'],
                         get_names(filter_by_attribute_less_than(CREATURES, 'determination', 10)))

    def test_function_09_example(self):
        self.assertEqual(['Shadowgnome', 'Nightgale', 'Urania', 'Harvinger'],
                         get_names(filter_by_attribute_greater_than(CREATURES_RED, 'determination', 210)))
        self.assertEqual(['Urania'], get_names(filter_by_attribute_greater_than(CREATURES_RED, 'CoUrAgE', 200)))
        self.assertEqual([], get_names(filter_by_attribute_greater_than(CREATURES_RED, 'GPA', 4)))

        self.assertEqual(['Lanternsprite', 'Voltantler', 'Moracle', 'Pearlificent'], get_names(filter_by_attribute_greater_than(CREATURES_BLUE, 'CoUrAgE', 190)))
        self.assertEqual([], get_names(filter_by_attribute_greater_than(CREATURES, 'Space X', 400000)))

    def test_function_10_example(self):
        self.assertEqual('Dinospore', get_most_experienced(CREATURES_RED[:3]).name)
        self.assertEqual('Slumberbug', get_most_experienced(CREATURES_RED[3:6]).name)
        self.assertEqual('Urania', get_most_experienced(CREATURES_RED[6:]).name)
        self.assertEqual(None, get_most_experienced(CREATURES_RED[0:0]))

        self.assertEqual('Neptunea', get_most_experienced(CREATURES_BLUE).name)
        self.assertEqual('Demonarch', get_most_experienced(CREATURES).name)


if __name__ == '__main__':
    unittest.main()
