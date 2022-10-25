def story_detail(story_name):
    import pymongo

    client = pymongo.MongoClient(host='localhost', port=27017)
    db = client.story  # 指定操作数据库
    collection = db['main-table']
    result = collection.find_one({"story_name": story_name})
    result = result["story_content"]  # 这句话不能跟在上句话后边
    print("返回故事详情完毕!")
    return result
