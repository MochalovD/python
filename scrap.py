import requests
from bs4 import BeautifulSoup

response = requests.get("https://gamemag.ru/")
soup = BeautifulSoup(response.content, "html.parser")

url = []

for data in soup.find_all('div', class_='news-item__text-wrapper'):
    for a in data.find_all('a'):
        url.append(a.get('href'))
        
testmessage = f"https://gamemag.ru{url[0]}\n" + f"https://gamemag.ru{url[1]}\n" + f"https://gamemag.ru{url[2]}\n" + f"https://gamemag.ru{url[3]}\n" + f"https://gamemag.ru{url[4]}"

mUrl = "https://discord.com/api/webhooks/1178117663747227728/Bn4yzvS0mi4el6GBIlv6KSjLfGFeyPEPGS7JX5bUQa2AQGqYyFXPr9-h0IgvlrZQrxc8"
data = {"content": testmessage}
response = requests.post(mUrl, json=data)
print(response.status_code)
print(response.content)
