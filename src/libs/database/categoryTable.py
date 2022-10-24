# 种类库
import pymongo
import json
import os

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.story  # 指定操作数据库
collection = db['category-table']  # 指定操作集

filePath = "../../../data/data.json"
with open(filePath, mode="r", encoding="utf-8") as f:
    dataJSON = f.read()  # 字符串
data = json.loads(dataJSON)  # 获得分类数据
deal_data = {}
for item in data:
    deal_item = {"type_id": item["type_id"], "type_name": item["name"]}
    story_list = []
    for story in item["story"]:
        story_list.append(story["name"])
    deal_item.append(story_list)
    deal_data.append(deal_item)
print(deal_data)
print("全部分类信息已存入category-table！")
