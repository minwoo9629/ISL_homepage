from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.

def home(request):
    #크롤링할 주소 : 학과 공지사항 
    req_com = requests.get('https://www.hanbat.ac.kr/prog/bbsArticle/BBSMSTR_000000000333/list.do')
    req_han = requests.get('https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000050/list.do?mno=sub07_01')

    html_com = req_com.text
    html_han = req_han.text
    #파이썬이 이해할 수 있는 객체 사용
    soup_com = BeautifulSoup(html_com, 'html.parser')
    soup_han = BeautifulSoup(html_han, 'html.parser')
    #print(soup)
    ##txt > div > div.no-more-tables > table > tbody > tr > td.subject > a
    #컴퓨터 공학과 공지사항 제목 및 날짜 추출 
    com_titles = soup_com.select(
        'div > div.no-more-tables > table > tbody > tr > td.subject > a',

    )
    com_dates = soup_com.select(
        'div > div.no-more-tables > table > tbody > tr > td.regDate'
    )
    #한밭대학교 공지사항 제목 및 날짜 추출
    han_titles = soup_han.select(
        'div > div.no-more-tables > table > tbody > tr > td.subject > a'
    )
    han_dates = soup_han.select(
        ' div > div.no-more-tables > table > tbody > tr > td.regDate'
    )

    com_list = []
    han_list = []
    for i in range(5):
        link = com_titles[i].get('onclick').split(sep='\'', maxsplit=1)[1]
        link = link.split(sep='\'', maxsplit=1)[0]
        link = 'https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000333/view.do?nttId=' + link + '&mno=sub05_01'
        com_list.append((com_titles[i].text, link, com_dates[i].text))
        #print(com_list)
    #https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000050/view.do?nttId=B000000078305Ap3fF7a&mno=sub07_01
    for i in range(5):
        i = i+3
        link = han_titles[i].get('onclick').split(sep='\'', maxsplit=1)[1]
        link = link.split(sep='\'', maxsplit=1)[0]
        link = 'https://www.hanbat.ac.kr/bbs/BBSMSTR_000000000050/view.do?nttId=' + link + '&mno=sub07_01'
        han_list.append((han_titles[i].text, link, han_dates[i].text))

    if request.user.groups.values().exists():
        user_group = request.user.groups.values()[0]['name']
    else:
        user_group = None
    return render(request,'home.html', {'com_zips' : com_list, 'han_zips':han_list, 'user_group':user_group})

