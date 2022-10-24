# title:多线程爬取儿童睡前故事（我用协程爬取时出错太多了，bug改不过了，只能退而求其次，过几天再看一下）
# time：2022.1.25
# 网站：https://www.qigushi.com/baobao/
# 共72个目录页面，大约700个故事左右
# 问题：线程池提交遇到了许多问题，试了许多次，尚需加强
import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time


# 获得所有目录网站链接的函数
def catalogue():
    urltasks = []
    urltasks.append("https://www.qigushi.com/baobao/index.html")
    for i in range(2, 73):
        urltasks.append(f"https://www.qigushi.com/baobao/index_{i}.html")
    return urltasks


# 爬取每个目录中故事的函数
def story_download(url):
    # 获得目录源码
    header = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"}
    resp = requests.get(url, headers=header)
    resp.encoding = "utf-8"
    resp.close()

    # 第一步：从目录源码中解析出故事的名字和地址
    html = etree.HTML(resp.text)
    articles = html.xpath('//*[@id="main"]')
    child_hrefs = []
    names = []
    for article in articles:
        name = article.xpath('./article/header/h2/a/text()')
        child_href = article.xpath('./article/header/h2/a/@href')
        child_hrefs.append(child_href)
        names.append(name)
        # 第二步：爬取故事
        # 这里的child_hrefs是个二维列表，我也不知道为什么，试出来的，反正想要取值只能用二维的方法
        # 我的目的是把地址取出来，所以不能是个列表，必须是把列表中的字符串取出来
    for i in range(0, len(child_hrefs[0])):
        child_href = child_hrefs[0][i]
        name = names[0][i]
        child_resp = requests.get(child_href)
        child_resp.encoding = "utf-8"
        child_resp.close()
        child_html = etree.HTML(child_resp.text)
        story = child_html.xpath('/html/body/div[2]/div[2]/div[1]/div[1]/div[4]/p/text()')
        story = "\n".join(story).replace("www.qigushi.com儿童睡前故事", "").replace("www.qigushi.com睡前故事",
                                                                                    "")  # 故事里这句话很碍眼，删了
        with open("儿童睡前故事/" + f"{name}.txt", mode="w", encoding="utf-8") as f:
            f.write(story)
            print(f"{name}爬取完毕！")


if __name__ == '__main__':
    urls = catalogue()
    t1 = time.time()
    with ThreadPoolExecutor(30) as t:
        # 这里这个30是10或者20都差的不大，应该是越大越快，但是越大对cpu负荷越大，我们的cpu都没问题处理这种小的爬虫
        for i in range(0, 72):
            t.submit(story_download, urls[i])
    t2 = time.time()
    print(t2 - t1)
    print("报告指挥官，故事已全部爬取完毕！")
