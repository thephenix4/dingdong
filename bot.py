import requests 
from bs4 import BeautifulSoup
import html5lib 
URL = "https://bceceboard.bihar.gov.in/UGEACexIndex.php"

# False flaf for ssl issue 
r = requests.get(URL , verify=False) 
soup = BeautifulSoup(r.content, 'html5lib') 
lis= []

for notice in soup.find_all("div", {"class": "notice"}):
    sub_items = notice.findAll('li')
    for sub_item in sub_items:
        lis.append(sub_item.text)
print(lis)
data = ""
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()

for x in range(len(lis)):
    if data == lis[x]:
        with open("data.txt", "w", encoding="utf-8") as f:
           f.write(lis[0])
           #you can change list element above to check bot is working corectly b/c of site is not through new notification according to you
        break

    else:
        print(lis[x])
        params = {
        "chat_id": "@bobthedog",
        "text": lis[x],
        "parse_mode": "HTML",
        }
        with open(".env", "r", encoding="utf-8") as f:
            token = f.read()
        requests.get(
        "https://api.telegram.org/{}/sendMessage".format(token),
        params=params
        )