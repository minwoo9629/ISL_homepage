import requests
from bs4 import BeautifulSoup
import webbrowser
#url = 'https://www.hanbat.ac.kr/prog/bbsArticle/BBSMSTR_000000000333/list.do' 
#req = requests.get('https://www.hanbat.ac.kr/prog/bbsArticle/BBSMSTR_000000000333/list.do')
#req = requests.get('https://beomi.github.io/beomi.github.io_old/')
#html = req.text
# header = req.headers
# status = req.status_code
# is_ok = req.ok

for i in range(1,10):
    url = 'https://www.hanbat.ac.kr/prog/bbsArticle/BBSMSTR_000000000333/list.do' 
    url = url + '?pageIndex=' + str(i)
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
        ##location > h2
        ###txt > div > div.no-more-tables > table > tbody > tr:nth-child(1) > td.subject > a
        ##txt > div > div.no-more-tables > table > tbody > tr:nth-child(1) > td.regDate
    my_titles = soup.select(
        'div > div.no-more-tables > table > tbody > tr > td.subject > a',
        #'div > div.no-more-tables > table > tbody > tr > td.regDate'
    )
    for title in my_titles:
        print(title.text)
        #print(title.get('href'))
        #print(title.get('onclick'))
        ##link = title.get('onclick').split(sep='\'', maxsplit=1)[1]
        #link = link.split(sep='\'', maxsplit=1)[0]
        #print(link)
        
    #a = 'https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000333/view.do?nttId=' + link + '&mno=sub05_01'
    #webbrowser.open(a)

