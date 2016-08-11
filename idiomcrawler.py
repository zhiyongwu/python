import requests
import re
import pymysql
from bs4 import BeautifulSoup
import string
import threading

homepage = 'http://www.hydcd.com/cy/chengyu/cy.htm'
dbconfig = {'host': 'localhost', 'user': 'root', 'passwd': 'root', 'db': 'data', 'charset': 'utf8'}
conn = pymysql.connect(**dbconfig)


def insert_db(idi, para):
    cur = conn.cursor()
    cur.execute('''insert into idiom (idiom,paraphrase) VALUE ('%s','%s')''' % (idi, para.strip(string.punctuation)))
    conn.commit()
    cur.close()


def get_all_links():
    try:
        r = requests.get(homepage)
        text = r.content.decode('gb2312', errors='ignore')
        bsObj = BeautifulSoup(text, 'html.parser')
        for item in bsObj.find('table', {'border': '1', 'style': 'border-collapse: collapse'}).find_all('a', {
            'href': re.compile(r'^cy.*.htm')}):
            yield 'http://www.hydcd.com/cy/chengyu/' + item.attrs['href']
    except:
        yield None


def get_idiom(url):
    try:
        r = requests.get(url)
        text = r.content.decode('gb2312', errors='ignore')
        bsObj = BeautifulSoup(text, 'html.parser')
        for idiom in bsObj.find('table', {'border': '0', 'cellpadding': '4', 'id': 'table1',
                                          'style': 'font-size: 11pt'}).find_all('a'):
            idi, link = idiom.get_text(), 'http://www.hydcd.com/cy' + idiom.attrs['href'].replace('..', '')
            yield idi, link
    except:
        yield None, None


def get_paraphrase(url):
    r = requests.get(url)
    text = r.content.decode('gb2312', errors='ignore')
    bsObj = BeautifulSoup(text, 'html.parser')
    try:
        paraphrase = bsObj.find('table',
                                {'border': '1', 'cellspacing': '1', 'style': 'border-collapse: collapse'}).find('font',
                                                                                                                {
                                                                                                                    'color': '#000000'}).find(
            'p').find('p')
        paraphrase = str(paraphrase).lstrip('<p>')
        paraphrase = paraphrase[0:paraphrase.find('<')]
        return paraphrase.strip()
    except:
        return None

def task(links):
    a = get_idiom(links)
    for idi, link in a:
        if link:
            paraphrase = get_paraphrase(link)
        insert_db(idi, paraphrase)
        print(idi)


if __name__ == '__main__':
    for links in get_all_links():
        if links:
            t = threading.Thread(target=task, args=(links,))
            t.start()
            t.join()