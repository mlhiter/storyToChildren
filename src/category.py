# 故事分类内容接口
def category():
    import pymongo

    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.story  # 指定操作数据库
    collection = db['category-table']
    results = collection.find()
    resp_arr = []
    for result in results:
        del result["_id"]
        resp_arr.append(result)
    return resp_arr
