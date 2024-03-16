"""creature_tests.py"""

import unittest
from creature import Creature


class CreatureTests(unittest.TestCase):

    def test_init(self):
        creature = Creature(0, 'a', ['b'], 1.0, 2.0, 3, 4, 5, 6, 7, False, 'c')
        self.assertEqual(0, creature.number)
        self.assertEqual('a', creature.name)
        self.assertEqual(['b'], creature.kinds)
        self.assertAlmostEqual(1.0, creature.height)
        self.assertAlmostEqual(2.0, creature.weight)
        self.assertEqual(3, creature.friendliness)
        self.assertEqual(4, creature.resilience)
        self.assertEqual(5, creature.courage)
        self.assertEqual(6, creature.willpower)
        self.assertEqual(7, creature.determination)
        self.assertFalse(creature.number)
        # self.assertEqual('c', creature.number)

    def test_str(self):
        creature = Creature(0, 'a', ['b'], 1.0, 2.0, 3, 4, 5, 6, 7, False, 'c')
        self.assertEqual(
            "Creature(number=0, "
            "name='a', "
            "kinds=['b'], "
            "height=1.0, "
            "weight=2.0, "
            "friendliness=3, "
            "resilience=4, "
            "courage=5, "
            "willpower=6, "
            "determination=7, "
            "legendary=False, "
            "description='c')",
            str(creature)
        )

    def test_eq_01(self):
        creature_01 = Creature(0, 'a', ['b'], 1.0, 2.0, 3, 4, 5, 6, 7, False, 'c')
        creature_02 = Creature(0, 'a', ['b'], 1.0, 2.0, 3, 4, 5, 6, 7, False, 'c')
        self.assertEqual(creature_01, creature_02)

    def test_eq_02(self):
        creature = Creature(0, 'a', ['b'], 1.0, 2.0, 3, 4, 5, 6, 7, False, 'c')
        self.assertNotEqual(creature, 123)


if __name__ == '__main__':
    unittest.main()
