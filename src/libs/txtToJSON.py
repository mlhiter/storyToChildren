# 将轮播图txt改为JSON
import json
import pymongo
import os

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.story  # 指定操作数据库
collection = db['swiper-table']  # 指定操作集

# JSON字典,mongodb要求的写入格式
storyDict = {}

# 获取到所有txt文件名
filePath = "../../data/swiper/text"
fileList = os.listdir(filePath)
for file in fileList:
    fileName = file.replace(".txt", "")
    # with open 不用关闭文件，会自动关闭，代码更加简洁
    with open(os.path.join(filePath, file), mode='r', encoding='utf-8') as f:
        storyDict[fileName] = f.read()
# 插入数据
collection.insert_one(storyDict)

# 读取数据

# 删除操作
result = collection.delete_many({})
print(result)