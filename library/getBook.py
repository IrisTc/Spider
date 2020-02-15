import requests
import glob
import fitz

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.100 Safari/537.36',
    'Cookie': 'Hm_lvt_07cfb20d5f1d7402d600e55de80e9127=1581684317,1581685985,1581729228,1581729504; Hm_lpvt_07cfb20d5f1d7402d600e55de80e9127=1581729504'
}
urls = []
doc = fitz.open()
for i in range(1,249+1):
    url = 'http://cebxol.apabi.com/api/getservice?orgid=&UserName=calisuser&MetaId=ISBN5053-5096-X%2FTP.2536&Time=2020-2-15 2:18:25&Sign=C7C2C496A70E06D3E94231BE04CCA891&Rights=1-0_00&width=800&height=1200&page='+str(i)+'&ServiceType=imagepage'   
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('Page %d collected success'%i)
        pic = response.content

    with open('img/%d.jpg'%i,'wb') as f:
        f.write(pic)
        print('Pape %d saved'%i)
    img = 'img/%d.jpg'%i
    imgdoc = fitz.open(img)         # 打开图片
    pdfbytes = imgdoc.convertToPDF()    # 使用图片创建单页的 PDF
    imgpdf = fitz.open("pdf", pdfbytes)
    doc.insertPDF(imgpdf)
    print('Page %d inserted success'%i)
doc.save("book.pdf")          # 保存pdf文件
doc.close()
#http://cebxol.apabi.com/api/getservice?orgid=&UserName=calisuser&MetaId=ISBN5053-5096-X%2FTP.2536&Time=2020-2-14 14:13:08&Sign=033EE2422E1CAA39D8FEB903D0D6B8B3&Rights=1-0_00&width=800&height=1200&page=12&ServiceType=imagepage
#api/getservice?orgid=&UserName=calisuser&MetaId=ISBN5053-5096-X%2FTP.2536&Time=2020-2-14 14:13:08&Sign=033EE2422E1CAA39D8FEB903D0D6B8B3&Rights=1-0_00&width=800&height=1200&page=10&ServiceType=imagepage
#api/getservice?orgid=&UserName=calisuser&MetaId=ISBN5053-5096-X%2FTP.2536&Time=2020-2-14 14:13:08&Sign=033EE2422E1CAA39D8FEB903D0D6B8B3&Rights=1-0_00&width=800&height=1200&page=11&ServiceType=imagepage