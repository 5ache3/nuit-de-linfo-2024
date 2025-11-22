import re
with open('list.txt','r',encoding='utf-8') as f:
    text=f.read()

patern=r"https://www.nuitdelinfo.com/inscription/defis/[0-9]+"
matches=re.findall(patern,text)

with open('list.txt','w',encoding='utf-8') as f:
    for link in matches :
        f.write(f'{link} \n')