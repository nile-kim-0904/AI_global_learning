#!/usr/bin/env python
# coding: utf-8

# In[8]:


list_a = [1,2,3,4,5]

for i in reversed(range(len(list_a))):
    print("{}번째 반복".format(i))
print()

for idx,value in enumerate(list_a):
    print("{}번째 반복: {}".format(idx,value))


# In[18]:


dict_ = {}

while(True):
    name = input("input name > ")
    if (name == 'q'):
        break
    score = int(input("input score > "))
    dict_[name] = score
        
    search = input("input search name > ")
    for idx, value in enumerate(dict_):
        #print(idx)
        #print(value)
        if (search == value):
            print("{}: {}".format(search,dict_[search]))
            break
        if idx == len(dict_)-1:
            print("자료 없음")


# In[29]:


input_arr = []

while(True):
    input_arr = input("input expression > ").split()
    if(input_arr[0]=='q'):
        break
    input_arr[0] = int(input_arr[0])
    input_arr[2] = int(input_arr[2])
    if (len(input_arr) != 3 or not input_arr[1] in 
        "+-*/%//"):
        print("error!!")
        continue
    elif(input_arr[1]=='+'):
        print(input_arr[0]+input_arr[2])
    elif(input_arr[1]=='-'):
        print(input_arr[0]-input_arr[2])
    elif(input_arr[1]=='*'):
        print(input_arr[0]*input_arr[2])
    elif(input_arr[1]=='/'):
        print(input_arr[0]/input_arr[2])
    elif(input_arr[1]=='%'):
        print(input_arr[0]%input_arr[2])
    elif(input_arr[1]=='//'):
        print(input_arr[0]//input_arr[2])


# In[31]:


import time

number = 0
target_time = time.time() + 5

while (time.time() < target_time):
    number += 1

print("5초동안 {}번 반복 실행".format(number))


# In[33]:


# 리스트 내포: [i for i in 반복 조건식]
array = [i for i in range(10) if i % 2 == 0]
print(array)


# In[40]:


odd_sum = sum([i for i in range(101) if i%2==1])
print(odd_sum)

even_sum = sum([i for i in range(101) if i %2==0])
print(even_sum)


# In[42]:


a = (1,2,3,4)
a[1]


# In[47]:


list_a = ['1','2','3','4','5']
print("-".join(list_a))

join_list = "::".join(list_a)
print(join_list)
join_list.split(sep="::")


# In[50]:


numbers = [1,2,3,4,5]
r_num = reversed(numbers)

print("reversed_numbers: ",r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
#print(next(r_num))


# In[64]:


list_ = []
dict_ = {}

while(True):
    list_ = input("input name & number > ").split()
    
    if(list_[0]=='q'):
        break
    dict_[list_[0]] = '-'.join(list_[1:])
    
    search = input("search name > ")
    if (search in dict_):
        print(dict_[search])
    else:
        print("자료 없음")


# In[68]:


def print_n_times(n,*values):
    for i in range(n):
        for value in values:
            print(value)   
        print()
        
print_n_times(2,"안녕하세요")


# In[ ]:





# In[72]:


def calculator(a,b,sign):
    if sign in '+-*/%//':
        if(sign == '+'):
            return a + b
        elif(sign == '-'):
            return a - b
        elif(sign == '*'):
            return a * b
        elif(sign == '/'):
            return a / b
        elif(sign == '%'):
            return a % b
        elif(sign == '//'):
            return a // b
    else:
        print("오류!!")
        
print(calculator(2,3,'-'))


# In[ ]:





# In[ ]:


dict_ = {}

def input_tot_avg(dict_):
    for name, score in dict_.items():
        score.append(sum(score))
        dict_[name].append(score[3]/len(score[:-1]))
        print(score)
        
def find_min_max(dict_):
    max_score = -1
    max_name = ""
    min_score = 1000
    min_name = ""
    for name,score in dict_.items():
        if (score[3] > max_score):
            max_score = score[3]
            max_name = name
        else:
            pass
    print(max_name, max_score)
    
    for name,score in dict_.items():
        if (score[3] < min_score):
            min_score = score[3]
            min_name = name
        else:
            pass
    print(min_name, min_score)

# def find_tot_avg(dict_):
#     tot_sum = 0
#     tot_avg = 0
#     for idx, score in enumerate(dict_):
#         tot_sum += score[3]
#     tot_avg = tot_sum/len(dict_[name])
#     print(tot_avg)
    
def input_data():

    while(True):
        data = input("input data > ").split()
        if (data[0]=='q'):
            break
        data[1] = int(data[1])
        data[2] = int(data[2])
        data[3] = int(data[3])
        dict_[data[0]] = data[1:]
        print(dict_)
        
        input_tot_avg(dict_)
        find_min_max(dict_)
#         find_tot_avg(dict_)
        
input_data()


# In[ ]:




