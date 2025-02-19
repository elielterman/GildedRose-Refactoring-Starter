# -*- coding: utf-8 -*-
class GildedRose(object):

    def __init__(self, items):
        self.items = items



    def aged_brie(self):
        for item in self.items:
            if item.quality < 50:
                item.quality += 1
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.quality < 50:
                    item.quality += 1

    def backstage(self):
        for item in self.items:
            if item.quality < 50:
                item.quality += 1
                if item.quality < 50:
                    if item.sell_in < 6:
                        item.quality += 2
                    elif item.sell_in < 11:
                        item.quality += 1
            item.sell_in -= 1
            if item.sell_in < 0:
                if item.quality < 50:
                        item.quality += 1

    def hand(self):
        for item in self.items:
            if item.quality < 50:
                item.quality += 1
            if item.sell_in < 0:
                if item.quality < 0:
                    item.quality = 0

    def conjured(self):
        for item in self.items:
            item.sell_in -= 1
            item.quality -= 2

             
    # def update_quality(self):
    #     for item in self.items:
    #         if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert" and item.name != "Sulfuras, Hand of Ragnaros":
    #             if item.quality > 0:
    #                 item.quality -= 1
    #         else:
    #             if item.quality < 50:
    #                 item.quality += 1
    #                 if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #                     if item.quality < 50:
    #                         if item.sell_in < 6:
    #                             item.quality += 2
    #                         elif item.sell_in < 11:
    #                             item.quality += 1
    #         if item.name != "Sulfuras, Hand of Ragnaros":
    #             item.sell_in -= 1
    #         if item.sell_in < 0:
    #             if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
    #                 if item.quality > 0:
    #                     if item.name != "Sulfuras, Hand of Ragnaros":
    #                         item.quality -= 1
    #                 else:
    #                     item.quality = 0
    #             else:
    #                 if item.quality < 50:
    #                     item.quality += 1


class Item: #don't edit
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
