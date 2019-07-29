
from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def main(request):
    return render(request, 'home.html')

def parse(request):
    url = request.POST.get('parse_url','')
    res = requests.get('https://ko.wikipedia.org/wiki/'+ url) #해당 url로 GET 요청을 함
    

    parsed_page = BeautifulSoup(res.content, 'html.parser')
    
    title = parsed_page.find('span').text #title 태그 찾아서 텍스트만 추출하기
    body = parsed_page.find(attrs = {'class': 'txtblue'} )
    contents = body.find('a').text # 첫 번째 p 태그의 텍스트 가져 오기 text 빼먹어서 안 됐었음
    return render(request, 'parse.html', {'title': title, 'contents': contents})