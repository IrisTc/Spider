import requests
from bs4 import BeautifulSoup

url = 'https://www.zhihu.com/hot'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'cookie': '_zap=67e9c884-e389-49d2-a6ef-509bf6321e13; _xsrf=f9b74244-748c-424a-ab72-4e3e5b15ffef; d_c0="AABvkC4cXRCPTs554MojYvsfr8Xn-bcfbng=|1573906419"; capsion_ticket="2|1:0|10:1581596803|14:capsion_ticket|44:NWM0MGRjYTQ5YWMzNDcyMGExODFjOTc3ODRjYjk5ODE=|01f8e30f71dd554996bb3a157f852ff58ef5d789f382604146163ff9b5f2db73"; z_c0="2|1:0|10:1581596831|4:z_c0|92:Mi4xU25ReUNnQUFBQUFBQUctUUxoeGRFQ1lBQUFCZ0FsVk5uNDR5WHdDRmJ0cjZjaHJIcE5vNS1oRUI0QzVMYkJwYXRR|2fd1c650ec5915993b6383c194644e37366403785f7a082e28cc4c1dde63ead3"; q_c1=161067ee4367483cb3db53e8c1f10e2d|1581597498000|1581597498000; tst=h; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1581477534,1581596725,1581596775,1581598396; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1581599973; KLBRSID=cdfcc1d45d024a211bb7144f66bda2cf|1581600510|1581596726'
}

response = requests.get(url, headers=headers).content.decode()
soup = BeautifulSoup(response, 'lxml')
items = soup.find_all('section', attrs={'class': 'HotItem'})

for item in items:
    rank = item.find('div', attrs={'class': 'HotItem-rank'}).get_text()
    title = item.find('h2', attrs={'class': 'HotItem-title'}).get_text()
    with open('HotList.txt', 'a+', encoding='utf8') as f:
        f.write('rank:%s   title:%s\n'%(rank, title))

with open('HotList.txt', 'a+', encoding='utf8') as f:
    f.write('-------------------------------------------------------------------\n\n\n')