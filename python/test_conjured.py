# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Conjured Item", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.conjured()
        self.assertEquals("Conjured Item", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
