#!/usr/bin/env python
# coding: utf-8

# In[3]:


print(10 == 100)
print(10 < 100)
x = 20
print(10 < x < 25)


# In[5]:


if True:
    print("True!!")
print("-------")
if False:
    print("False!!")


# In[11]:


num = int(input("input number > "))
if(num > 0):
    print("양수입니다")
elif(num < 0):
    print("음수입니다")
else:
    print("0입니다")


# In[16]:


num = int(input("input number > "))
if(num%2==0):
    print("짝수입니다")
else:
    print("홀수입니다")


# In[1]:


num = input("input number > ")
if num[-1] in '13579':
    print("홀수입니다")
else:
    print("짝수입니다")


# In[11]:


import datetime

now = datetime.datetime.now()
print(now)
print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))


# In[13]:


import datetime

now = datetime.datetime.now()

if(0 <= now.hour < 12):
    print("오전입니다")
else:
    print("오후입니다")
    
if(3<=now.month<=5):
    print("봄입니다")
elif(6<=now.month<=8):
    print("여름입니다")
elif(9<=now.month<=11):
    print("가을입니다")
else:
    print("겨울입니다")


# In[25]:


num = input("input > ")
print(len(num))
num_arr = num.split()
print(len(num_arr))

if (num_arr[0].isdigit()==False or num_arr[2].isdigit()==False):
    print("계산불가")
elif(num_arr[1] in "+-*/"):
    if(num_arr[1]=='+'):
        print(int(num_arr[0])+int(num_arr[2]))
    elif(num_arr[1]=='-'):
        print(int(num_arr[0])-int(num_arr[2]))
    elif(num_arr[1]=='*'):
        print(int(num_arr[0])*int(num_arr[2]))
    else:
        print(int(num_arr[0])/int(num_arr[2]))
else:
    print("오류")


# In[29]:


list_a = [1,2,3,4]
list_a.insert(1,'1추가')
print(list_a)
print(list_a.insert(2,'2추가'))
print(list_a)


# In[31]:


list_a = [1,2,3]
list_b = [4,5,6]
list_a += list_b
print(list_a)


# In[33]:


# 리스트 요소 제거: del list[인덱스], list.pop(인덱스), list.remove(값)
# 모두 지우기: list.clear()
# 처음 위치의 요소 제거
del list_b[0]
print(list_b)

list_a.pop(1)
print(list_a)


# In[38]:


list_a = [1,2,2,2,3]
list_b = [3,4,5]
list_a.remove(2)
list_a


# In[49]:


num = input("input data a b > ")
num = num.split()
num_a = int(num[0])
num_b = int(num[1])
sum_ab = 0

if(num_a > num_b):
    for i in range(num_b,num_a+1,1):
        sum_ab += i
        print(i)
else:
    for i in range(num_a,num_b+1,1):
        sum_ab += i
        print(i)

print(sum_ab)
        


# In[53]:


list_of_list = [
    [1,2,3],
    [4,5,6,7],
    [8,9],
]
arr = list_of_list[0] + list_of_list[1]+list_of_list[2]

for i in range(1,len(arr)+1,1):
    print(i)


# In[57]:


numbers = [1,2,3,4,5,6,7,8,9]
output = [[],[],[]]

for number in numbers:
    output[(number%3)-1].append(number)
    
print(output)


# In[80]:


dict_a = {
    "name":"7D 건조 망고",
    "type":"당절임"
}
print(dict_a)
print(dict_a["name"])

dict_a["ingredient"] = ["망고","설탕","나트륨"]
print(dict_a)

dict_a["name"] = "8D 건조 망고"
print(dict_a)

dict_a["ingredient"].append("콩")
print(dict_a)

#del dict_a["type"]
#print(dict_a)

if "type" in dict_a:
    print("type key 존재함")
else:
    print("type key 존재 안함")
    
for key in dict_a:
    print(key,dict_a[key])
    
print(type(list_a),type(dict_a),type(dict_a["name"]))

for key, value in dict_a.items():
    print(key, value)


# In[103]:


list_a = []

sum_num = 0
for i in range(5):
    num = int(input("input number data > "))
    list_a.append(num)

for i in range(len(list_a)):
    sum_num += list_a[i]
print(list_a)
print(sum_num)


# In[121]:


dict_a = {"이름":[], "국어":[], "영어":[], "수학":[],"합계":[]}

while(1):
    data_a = input("input 이름 > ")
    if(data_a=="quit"):
        print("quit!!")
        break
    else:
        dict_a["이름"].append(data_a)
    
    data_b = int(input("input 국어 > "))
    dict_a["국어"].append(data_b)
    
    data_c = int(input("input 영어 > "))
    dict_a["영어"].append(data_c)
    
    data_d = int(input("input 수학 > "))
    dict_a["수학"].append(data_d)
    
    dict_a["합계"].append(data_b + data_c + data_d)
    print(dict_a["합계"])
    print(dict_a)
    
    
name = input("input name > ")
for idx,value in enumerate(dict_a["이름"]):
    #print(idx,value)
    if(name == dict_a["이름"][idx]):
        print("이름: {}, 국어: {}, 영어: {}, 수학: {}, 합계: {}".format(dict_a["이름"][idx],dict_a["국어"][idx],dict_a["영어"][idx],dict_a["수학"][idx],dict_a["합계"][idx]))
        break
    


# In[123]:


numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers:
    if(number in counter):
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)


# In[136]:


character={
    "name":"기사",
    "level":12,
    "items":{
        "sword":"불꽃의 검",
        "armor":"풀플레이트",
    },
    "skill":["베기","세게 베기","아주 세게 베기"]
}

for key in character:
    if(type(character[key]) == list):
        for value in character[key]:
            print("{} : {}".format(key,value))
    elif(type(character[key]) == dict):
        for key1, value1 in character[key].items():
            print("{} : {}".format(key1,value1))
    else:
        print("{} : {}".format(key,character[key]))

