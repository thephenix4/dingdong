import requests 
from bs4 import BeautifulSoup
import html5lib 
URL = "https://bceceboard.bihar.gov.in/UGEACexIndex.php"
r = requests.get(URL , verify=False) 
#print(r.content) 
soup = BeautifulSoup(r.content, 'html5lib') 
#print(soup.prettify()) 
print("after this")
#notice = soup.find_all("div", {"class": "notice"})
#print(notice)
lis= []

for notice in soup.find_all("div", {"class": "notice"}):
    sub_items = notice.findAll('li')
    for sub_item in sub_items:
        lis.append(sub_item.text)
 #   print(lis)
        #print(sub_item.text)
#print(lis)

# it's save 0 list element in txt file
'''with open("data.txt", "w", encoding="utf-8") as f:
    f.write(lis[0])'''


'''
b = (str(lis))
#print(b)
print(lis[0])
a= str('\n'.join(lis))
#print(a)
'''
data = ""
with open("data.txt", "r", encoding="utf-8") as f:
    data = f.read()

for x in range(len(lis)):
    if data == lis[x]:
        print(x)
        #write index 0 element
        with open("data.txt", "w", encoding="utf-8") as f:
           f.write(lis[0])
        break

    else:
        #send = lis[x]
        #print(send)
        params = {
        "chat_id": "@bobthedog",
        "text": lis[x],
        "parse_mode": "HTML",
        }
        #botID="bot1666045843:AAEIzQl3CIEUVf0c71Hh2pJZYlgez5hxjMM"
        with open(".env", "r", encoding="utf-8") as f:
            token = f.read()
        #pass
        #send it to bot https://api.telegram.org/bot1666045843:AAEIzQl3CIEUVf0c71Hh2pJZYlgez5hxjMM/getUpdates
        #requests.get("https://api.telegram.org/bot1666045843:AAEIzQl3CIEUVf0c71Hh2pJZYlgez5hxjMM/sendMessage?chat_id=@bobthedog&text={'lets check'}")
        requests.get(
        "https://api.telegram.org/{}/sendMessage".format(token),
        params=params
        )