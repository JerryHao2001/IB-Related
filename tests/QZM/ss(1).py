import requests
from lxml import etree
import re

# 使用手机UA
headers = {
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"
}
# 视频url
video_url = 'https://www.bilibili.com/video/av39009763'

#"https://www.bilibili.com/blackboard/bnj2019.html?spm_id_from=333.334.b_63686965665f7265636f6d6d656e64.1&aid=36570401&p="
html = requests.get(url=video_url, headers=headers).content.decode('utf-8')
# 获取弹幕url的参数
cid = re.findall(r"comment: '//comment.bilibili.com/' \+ (.*?) \+ '.xml',", html)
print(cid)
url = "https://comment.bilibili.com/" + cid[0] + ".xml"
print(url)
response = requests.get(url, headers=headers)
html = response.content

xml = etree.HTML(html)

# 提取数据
str_list = xml.xpath("//d/text()")
# 写入文件
with open('拜年祭 弹幕爬虫.txt', 'w', encoding='utf-8') as f:
    for line in str_list:
        f.write(line)
        f.write('\n')
