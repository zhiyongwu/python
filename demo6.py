import time,base64,re,requests,os,threading
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import os.path

def getFileName(url):
    file_name = url.split('?')[0].split('/')[-1]
    return file_name if file_name else None

def downloadImg(url,path,filename = None):
    if not os.path.exists(path):
        os.makedirs(path)
    headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    try:
        print(url)
        r = requests.get(url,headers = headers)
        if filename is None:
            filename = getFileName(url)
        with open(os.path.join(path,filename),'wb') as f:
            if r and r.status_code == 200 and r.content is not None:
                f.write(r.content)
    except Exception as e:
        print(e)
    

def getBaiduImg(keyword,phantomjsPath = 'C:/phantomjs-2.1.1-windows/bin/phantomjs'):
    r = webdriver.PhantomJS(executable_path=phantomjsPath)
    r.get('http://image.baidu.com')
    time.sleep(1)
    r.find_element_by_id('kw').send_keys(keyword + Keys.RETURN)
    time.sleep(1)
    bsObj = BeautifulSoup(r.page_source,'html.parser')
    imgLinks = bsObj.findAll('div',{'class':re.compile(r'imgbox.*')})
    for link in imgLinks:
        link = 'http://image.baidu.com/' + link.find('a').attrs['href']
        r = requests.get(link)
        bsObj = BeautifulSoup(r.text,'html.parser')
        img = bsObj.find('img',{'id':'hdFirstImgObj'}).attrs['src']
        t = threading.Thread(target=downloadImg,args = (img,'../imgs'))
        t.start()
        t.join()



if __name__ == '__main__':
    getBaiduImg('奥巴马')