# title:多线性爬取儿童睡前故事（2）
# 网址：https://wap.etgushi.com/sqgs/list_7_1.html
# time：2022.1.25
# 注意事项：注意有一些故事是有两个页面的，我们怎么处理这种情况呢？
# 解决措施：经发现没有第二页的故事也可以通过网址打开第二页，但是网页故事内容为空故爬取内容为空，可以一视同仁全部爬取然后合成
# bug1：保存文件时无法处理段落之间的换行


import requests
from lxml import etree
from concurrent.futures import ThreadPoolExecutor
import time


# 获取该目录下故事的函数
def storydownload(url):
    resp = requests.get(url)
    resp.encoding = "utf-8"
    resp.close()
    # 解析出故事网址
    html = etree.HTML(resp.text)
    ul = html.xpath('/html/body/article/dl/dd/ul')
    for li in ul:
        name = li.xpath('./li/a/text()')
        child_hrefs = li.xpath('./li/a/@href')
        # xpath里元素储存在列表里
    for i in range(0, len(child_hrefs)):
        child_hrefs[i] = "https://wap.etgushi.com" + child_hrefs[i]
        child_urls = [child_hrefs[i]]
        child_urls.append(child_hrefs[i].replace(".html", "_2.html"))
        for child_url in child_urls:
            header = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69"}
            child_resp = requests.get(child_url)
            child_resp.encoding = "utf-8"
            child_resp.close()

            child_html = etree.HTML(child_resp.text)
            articles = child_html.xpath("/html/body/article/dl/dd[2]/article")
            for p in articles:
                story = p.xpath("./p/text()")
                story = "".join(story)  # .replace("\n\n\n","")
                # 无法处理段落之间的换行
                with open("儿童睡前故事2/" + f"{name[i]}.txt", mode="a", encoding="utf-8") as f:
                    f.write(story)
                    print(f"{name[i]}" + "over!")


if __name__ == '__main__':
    urls = []
    for i in range(1, 68):
        urls.append(f"https://wap.etgushi.com/sqgs/list_7_{i}.html")
    t1 = time.time()
    # 创建线性池
    with ThreadPoolExecutor(20) as t:
        for i in range(0, 67):
            t.submit(storydownload, urls[i])
    t2 = time.time()
    print(t2 - t1)
    print("全部爬取完毕！")
