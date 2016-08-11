import requests,random,datetime
from bs4 import BeautifulSoup

headers = {}
params = {'_xsrf':'4bc694da0d705ab714eb14363847ddf1','account':'zhiyongwu@live.cn','password':'i5639421275'}
session = requests.Session()
r = session.post('http://www.zhihu.com#singin',data= params)
print(r.text)



