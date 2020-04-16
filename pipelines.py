# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3


class PuppyPipeline(object):

    def __init__(self):
        self.create_connection()

    def create_connection(self):
        puppies_db = "C:/Users/nfa87/OneDrive/Desktop/Development/Scrapy_Tutorial/tutorial/puppies.db"
        self.conn = sqlite3.connect(puppies_db)
        self.c = self.conn.cursor()

    def process_item(self, items, spider):
        print("Pipeline: " + items['puppyName'][0])
        self.store_db(items)
        return items

    def store_db(self, items):
        t = (items['puppyName'][0], items['puppy_id'][0], items['puppy_sex'][0], items['puppy_breed'][0], items['puppy_age'][0], items['puppy_link'],)
        y = (items['puppyID'][0], items['puppy_status'][0], items['puppy_intake_date'][0])
        z = (items['puppyID'][0])
        s = str(items['puppy_id'][0])
        n = str(items['puppyName'][0])

        self.c.execute("SELECT id FROM puppies WHERE id IN ('{}')".format(s))
        data = self.c.fetchone()

        if data is not None:
            self.c.execute("UPDATE puppies SET name = ?, id = ?, sex = ?, breed = ?, age = ?, url = ? WHERE id = '{}'".format(s), t)
            print("{} exists".format(n))
        else:
            self.c.execute("INSERT INTO puppies (name, id, sex, breed, age, url) VALUES (?,?,?,?,?,?)", t)
            print("{} has been added".format(n))

        if z not in items:
            pass
        else:
            self.c.execute("UPDATE puppies SET status = ?, intake_date = ? WHERE id = '{}'".format(z), y)
            print("Status updated for {}".format(z))

        self.conn.commit()
