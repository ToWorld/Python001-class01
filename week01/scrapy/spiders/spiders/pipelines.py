# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SpidersPipeline:
    def process_item(self, item, spider):
        name = item['name']
        tag = item['tag']
        time = item['time']
        unit = [name, tag, time]
        columns_name = ["name", "tag", "time"]
        file_name = 'top10_film_info.csv'
        pd.DataFrame(columns=columns_name, [unit]).to_csv(file_name, mode='a', encoding='utf-8', header=False)
        return item
