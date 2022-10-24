from fastapi import FastAPI
import pymysql

db = pymysql.connect(host="localhost", port=3306, user="root", passwd="123321", charset="utf8")
cursor = db.cursor()
cursor.execute("use gushi")
app = FastAPI()


# 故事分类内容接口
@app.get("/gushi")
def category():
    resp_id = 0
    resp_list = []
    cates = ['虫', '刺猬', '狗', '猴子', '狐狸', '花', '鸡', '恐龙', '狼', '老虎', '鹿', '马', '蚂蚁', '猫', '魔法',
             '鸟', '牛',
             '猪', '青蛙', '狮子', '鼠', '树', '松鼠', '兔子', '蜗牛', '象', '熊', '鸭子', '羊', '萤火虫', '鱼',
             '月亮', '长颈鹿', '其他']
    for cate in cates:
        cursor.execute(f"select * from fl where lb like {cate}")
        items = cursor.fetchall()
        story_list = []
        story_id = 0
        for item in items:
            story_id = story_id + 1
            story_item = {'story_id': story_id, 'name': item[1], 'content': item[2]}
            story_list.append(story_item)
        resp_item = {"type_id": resp_id, "name": {cate}, "story": story_list}
        resp_list.append(resp_item)
    return resp_list
