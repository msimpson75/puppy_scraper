# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field

# class QuoteItem(Item):
#     quote_content = Field()
#     tags = Field()
#     author_name = Field()
#     author_birthday = Field()
#     author_bornlocation = Field()
#     author_bio = Field()


class PuppyItem(Item):
    puppyName = Field()
    puppy_id = Field()
    puppy_sex = Field()
    puppy_breed = Field()
    puppy_age = Field()
    puppy_link = Field()


class PuppyDeets(Item):
    puppyID = Field()
    puppy_status = Field()
    puppy_intake_date = Field()
