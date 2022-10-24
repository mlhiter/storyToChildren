# 全部txt改为JSON
import pymongo
import os

client = pymongo.MongoClient(host='localhost', port=27017)
db = client.story  # 指定操作数据库
collection = db['main-table']  # 指定操作集

# 获取到所有txt文件名
filePath = "../../../data/stories-txt"
fileList = os.listdir(filePath)
story_id = 0
for file in fileList:
    fileName = file.replace(".txt", "")
    story_id = story_id + 1  # python没有自增运算符
    # with open 不用关闭文件，会自动关闭，代码更加简洁
    with open(os.path.join(filePath, file), mode='r', encoding='utf-8') as f:
        item = {"story_id": story_id, "story_name": fileName, "story_content": f.read()}
    collection.insert_one(item)
print("全部故事已存入main-table！")
