import requests
from bs4 import BeautifulSoup

url = "https://www.ixiaos.net/wap.php?action=list&id=725&uid=&totalresult=96&pageno=1"
headers = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0"
}
response = requests.get(url, headers).text
# print(response)
soup = BeautifulSoup(response, "lxml")
bdss = soup.find("div", class_="container")
# print(bds)
bds = bdss.find_all("div", class_="bd")
# print(bds)
bd = bds[4]
# print(bd)
lis = bd.find_all("li")
for li in lis:
    title = li.text
    print(title,"下载完成")
for num in range(48000, 48030):
    new_url = "https://www.ixiaos.net/wap.php?action=article&id=" + str(num)
    print(new_url)
