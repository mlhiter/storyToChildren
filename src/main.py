# 外部库
import uvicorn
from fastapi import FastAPI
# 内部函数
from swiper import swiper
from category import category
from story_detail import story_detail

app = FastAPI()


# 获取轮播图数据接口
@app.get("/swiper")
def swiper_get():
    # 必须使用return的形式
    return swiper()


# 分类接口
@app.get("/category")
def category_get():
    return category()


# 根据名字请求故事详情页接口
@app.get("/story_detail/")
def story_get(story_name):
    return story_detail(story_name)


if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8080, reload=True)
