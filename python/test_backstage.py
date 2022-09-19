# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.backstage()
        self.assertEquals("Backstage passes to a TAFKAL80ETC concert", items[0].name)

        
if __name__ == '__main__':
    unittest.main()
