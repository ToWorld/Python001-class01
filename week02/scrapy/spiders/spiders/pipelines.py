# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class SpidersPipeline:
    def __del__(self):
        self.conn.close()
    def __init__(self):
        self.host = 'localhost'
        self.port = '3306'
        self.user = 'root'
        self.db = 'python_learn'
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            db = self.db
        )
        self.cursor = self.conn.cursor()
    def process_item_with_local_csv(self, item):
        name = item['name']
        tag = item['tag']
        time = item['time']
        unit = [name, tag, time]
        columns_name = ["name", "tag", "time"]
        file_name = 'top10_film_info.csv'
        pd.DataFrame(columns=columns_name, [unit]).to_csv(file_name, mode='a', encoding='utf-8', header=False)
        return item
    def process_item(self, item, spider):
        # return process_item_with_local_csv(self, item)
        return process_item_with_mysql(self, item)
    def process_item_with_mysql(self, item):
        sql = """INSERT INTO PYTHON_LEARN(NAME, TAG, TIME) \
              VALUES('%s', '%s', '%s')""" % \
              (item['name'], item['tag'], item['time'])  
        try:
            cursor.execute(sql)
            db.commit()
        except:
            db.rollback()
