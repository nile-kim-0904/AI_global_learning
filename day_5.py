#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
math.cos(10)
math.ceil(5.6) 
math.floor(5.6)

# from 모듈명 import 필요한 변수 또는 함수
from math import cos,ceil,floor


# In[9]:


# random 모듈: 임의의 수를 발생시키는 함수들을 ㅈ;모듈
import random as rnd

print("random 모듈: ")

# random(): 0.0 < x < 1.0 사이의 float 리턴
print("random(): ",rnd.random())

# uniform(min,max): min < x < max 사이의 float 리턴
print("uniform(): ",rnd.uniform(10,20))

# randrange([min,max]): min < x < max 사이의 int 리턴, 0부터 max
print("randrange(): ",rnd.randrange(10,20))

# choice(list): 리스트 내부의 임의의 요소를 리턴
print("choice(): ", rnd.choice(list(range(10))))

# shuffle(list): 리스트 요소를 랜덤하게 섞음
a = list(range(10))
print("shuffle(): ",rnd.shuffle(a),a)

# sample(list,k=숫자): 리스트에서 숫자의 갯수 요소를 랜덤하게 리턴
print("sample(): ",rnd.sample(a,k=3))


# In[11]:


# sys 모듈: 시스템 관련 정보를 가져 옴
import sys

print("copyright: ",sys.copyright)
print("version: ",sys.version)
# sys.exit()


# In[15]:


# os 모듈: 운영체제와 관련된 명령어
import os

print("현재 운영체제: ",os.name)
print("현재 작업 경로: ",os.getcwd())
print("현재 폴더 리스트: ",os.listdir())


# In[22]:


# 디렉토리 생성
# os.mkdir("test_dir")
os.listdir()

# os.rmdir("test_dir")
os.listdir()

# file 이름 변경: rename(old_name,new_name)

#file 삭제: remove(파일명)

get_ipython().system('dir')


# In[24]:


# datetime 모듈: 날짜를 형식에 맞게 편집 가능
import datetime as dt
dt.datetime.now()


# In[27]:


# time 모듈: 일정 시간 멈춤
import time
print("time start")
time.sleep(5)
print("time finish")


# In[38]:


# urllib 모듈: url 라이브러리
# 인터넷 검색 1. url open, 2. 해당 데이터 읽어 옴
from urllib import request

# urlopen() 구글의 메인 페이지
target = request.urlopen("https://www.google.com")
# output = target.read()

# print(output)


# In[40]:


# <html> ~ </html> tag 형식으로 변환해 주는 모듈: BeautifulSoup
#import BeautifulSoup
#!pip install beautifulsoup4
from bs4 import BeautifulSoup

soup = BeautifulSoup(target)
soup


# In[3]:


from urllib import request
from bs4 import BeautifulSoup

url = "https://www.weather.go.kr/w/weather/forecast/mid-term.do"
target = request.urlopen(url)

soup = BeautifulSoup(target)

for location in soup.find_all('tr'):
    if location.find('td',class_='midterm-city'):
        print("도시명: {}, 최저기온: {}, 최대기온: {}".format(location.find('td',class_='midterm-city').text,location.find('span',class_='tmn').text,location.find('span',class_='tmx').text))


# In[11]:


from urllib import request
from bs4 import BeautifulSoup

url = "https://www.weather.go.kr/w/weather/forecast/mid-term.do"
target = request.urlopen(url)

soup = BeautifulSoup(target)
print(soup.find_all('span'))

# for location in soup.find_all('tr'):
#     if location.find('td',class_='midterm-city'):
#         print("도시명: {}, 최저기온: {}, 최대기온: {}".format(location.find('td',class_='midterm-city').text,location.find('span',class_='tmn').text,location.find('span',class_='tmx').text))


# In[14]:


# !pip install flask
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello World!!</h1>"


# In[ ]:





# In[16]:


def test(function):
    def wrapper():
        print("Hello Start !!")
        function()
        print("Hello End !!")
    return wrapper

@test # 데코레이션 함수
def hello():
    print("Hello")

hello()


# In[18]:


# 모듈 만들기
import os
#os.mkdir("module_basic")


# In[22]:


import test_package.module_a as a
import test_package.module_b as b

print("module_a: ",a.variable_a)
print("module_b: ",b.variable_b)


# In[1]:


from test_package import *

print("module_a: ",module_a.variable_a)
print("module_b: ",module_b.variable_b)

