from bs4 import BeautifulSoup
import requests
import json
import re
main_url='https://www.nuitdelinfo.com/inscription/defis/liste'

with open('list.txt','r',encoding='utf-8') as f:
    text=f.read()
lis=text.split('\n')
i=0
for link in lis:
    print(i,link)
    i+=1
    code=re.findall(r'[0-9]+',link)[0]
    html=requests.get(link)
    html.encoding='utf-8'
    with open(f'sites/{code}.html','w',encoding='utf-8') as f:
        f.write(html.text)
