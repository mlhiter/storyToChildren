import pymongo
import os

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.story  # 指定操作数据库
collection = db['main-table']  # 指定操作集

# 删除操作
result = collection.delete_many({})
print("删除完毕！")
