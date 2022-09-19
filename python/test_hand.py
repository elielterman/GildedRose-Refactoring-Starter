# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.hand()
        self.assertEquals("Sulfuras, Hand of Ragnaros", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
