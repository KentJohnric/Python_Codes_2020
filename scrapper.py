#this project is studied from youtube tutorial by: Dev Ed "Build A Python App that Tracks Amazon Prices!"
#pip install request
#pip install beautifulsoup4
#pip install bs4

import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/DisplayPort-Benfei-Adapter-Gold-Plated-Compatible/dp/B07JFTK8YV/ref=sr_1_1_sspa?dchild=1&keywords=DP+to+HDMI&qid=1608706536&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUExOFJHQ1U0VjZPUVlQJmVuY3J5cHRlZElkPUEwODc4NjY2MkFDNDVQRVROR0ZXNyZlbmNyeXB0ZWRBZElkPUEwNDc4MDA2MldLVkhWQkY4WFVYVyZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36 Edg/87.0.664.66'}

page = requests.get(URL,headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle")

print(title)