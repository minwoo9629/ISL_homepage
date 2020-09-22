from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    #크롤링할 주소 : 학과 공지사항 
    req = requests.get('https://www.hanbat.ac.kr/prog/bbsArticle/BBSMSTR_000000000333/list.do')
    html = req.text
    #파이썬이 이해할 수 있는 객체 사용
    soup = BeautifulSoup(html, 'html.parser')
    ##txt > div > div.no-more-tables > table > tbody > tr > td.subject > a
    #공지사항 제목만 추출 
    my_titles = soup.select(
        'div > div.no-more-tables > table > tbody > tr > td.subject > a',
    )
    texts = []
    links = []
    
    for title in my_titles:
        texts.append(title.text)

        link = title.get('onclick').split(sep='\'', maxsplit=1)[1]
        link = link.split(sep='\'', maxsplit=1)[0]
        link = 'https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000333/view.do?nttId=' + link + '&mno=sub05_01'
        links.append(link)
    index = list(range(len(texts)))

    return render(request,'home.html', {'links':links, 'texts':texts, 'zips':zip(index, texts,links)})

