from urllib import request
import urllib.parse
import string
from bs4 import BeautifulSoup
from mylog import MyLog as mylog

class Item(object):
    title = None
    firstAuthor = None
    firstTime = None
    reNum = None
    content = None
    lastAuthor = None
    lastTime = None

class GetInfo(object):
    def __init__(self, url):
        self.url = url
        self.pageSum = 10
        self.log = mylog()
        self.urls = self.getUrls(self.pageSum)
        self.items = self.spider(self.urls)
        self.pipelines(self.items)

    def getUrls(self, pageSum):
        urls = []
        pns = [str(i * 50) for i in range(pageSum)]
        ul = self.url.split('=')
        for pn in pns:
            ul[-1] = pn
            url = '='.join(ul)
            urls.append(url)
        self.log.info(u'获取URLS成功')
        return urls

    def getResponseContent(self, url):
        try:
            new_url = urllib.parse.quote(url, safe=string.printable)
            response = request.urlopen(new_url)
        except:
            self.log.error(u'返回URL：%s 数据失败' % url)
        else:
            self.log.info(u'返回URL：%s 数据成功' % url)
            return response.read()

    def spider(self, urls):
        items = []
        for url in urls:
            htmlContent = self.getResponseContent(url)
            soup = BeautifulSoup(htmlContent, 'lxml')
            tagsli = soup.find_all('li', attrs={'class': 'j_thread_list'})
            for tag in tagsli:
                if tag.find('i', attrs={'class': 'icon-good'}):
                    continue
                item = Item()
                # win默认GBK，用u字符将字符串Unicode化，再编码
                item.title = tag.find('a', attrs={'class': 'j_th_tit'}).get_text().strip()
                item.firstAuthor = tag.find('span', attrs={'class': 'tb_icon_author'}).a.get_text().strip()
                item.firstTime = tag.find('span', attrs={'title': u'创建时间'.encode('utf8')}).get_text().strip()
                item.reNum = tag.find('span', attrs={'title': u'回复'.encode('utf8')}).get_text().strip()
                item.content = tag.find('div', attrs={'class': 'threadlist_abs_onlyline'}).get_text().strip()
                item.lastAuthor = tag.find('span', attrs={'class': 'tb_icon_author_rely'}).a.get_text().strip()
                item.lastTime = tag.find('span', attrs={'title': u'最后回复时间'.encode('utf8')}).get_text().strip()
                items.append(item)
                self.log.info(u'获取标题为《%s》的项成果' % item.title)
            return items

    def pipelines(self, items):
        fileName = u'百度贴吧_某科学的超电磁炮.txt'.encode('GBK')
        with open("result.txt", "w+", encoding='utf8') as f:
            for item in items:
                f.write(
                    'title:%s \t firstAuthor:%s \t firstTime:%s \t content:%s \t number:%s \t lastAuthor:%s \t lastTime:%s \n'
                    %(item.title, item.firstAuthor, item.firstTime, item.content, item.reNum, item.lastAuthor,
                       item.lastTime))
                self.log.info(u'标题为《%s》的项输入到“%s”成功' % (item.title, fileName))

if __name__ == '__main__':
    url = 'https://tieba.baidu.com/f?kw=某科学的超电磁炮&ie=utf-8&pn=0'
    GTI = GetInfo(url)




