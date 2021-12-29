#!/usr/bin/env python
# coding: utf-8

# In[4]:


def factorial(n):
    output = 1
    for i in range(1,n+1):
        output *= i
    return output

factorial(6) # factorial 실행


# In[6]:


def factorial1(n):
    # n이 0이면 1을 return 아니면 n * f(n-1)
    if(n==0):
        return 1
    else:
        return n*factorial1(n-1)
    
factorial1(5)


# In[12]:


# 피보나치 수열 -> f(n) = f(n-1) + f(n-2)

def fibo(n):
    global count
    count += 1
    
    if n==1 or n==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)


# In[19]:


count = 0
print("fibo: ", fibo(25))
print("count: ",count)


# In[23]:


dictionary = {1:1,2:1}
def fibo_m(n):
    global count
    count += 1
    
    if n in dictionary: # 메모화 되어 있으면 메모된 값을 사용
        return dictionary[n]
    else:
        output = fibo_m(n-1) + fibo_m(n-2)
        dictionary[n] = output
        return output
count = 0
fibo(15)
print("count: ", count)
count = 0
fibo_m(100)
print("count: ",count)
print(dictionary)


# In[25]:


tuple_test = (10,20,30,40)
for value in tuple_test:
    print(value)
print(tuple_test[0])
a,b,c = 10,20,30
print("a:{}, b:{}, c:{}".format(a,b,c))

a,b = 10, 20

print("before => a:{}, b{}".format(a,b))
a,b = b,a # a와 b의 값이 바뀜
print("after => a:{}, b{}".format(a,b))


# In[28]:


for (idx, value) in enumerate([1,2,3,4,5]):
    print("{}번째 값: {}".format(idx,value))

a, b = divmod(88,3)
print(a,b)


# In[31]:


# map과 filter 함수 => map(함수, 리스트), filter(함수, 리스트)

def power(x):
    return x*x

def under_3(x):
    if n < 3:
        return x

# lambda 함수로 변경 -> lambda 매개변수 : 리턴값
power = lambda x: x*x
under_3 = lambda x: x<3
    
a_list = [1,2,3,4,5]
b_list = map(power,a_list)
print(b_list)
c_list = list(filter(under_3,a_list))
print("\n",c_list)


# In[34]:


b_list = list(map(lambda x: x*x, a_list))
print(b_list)

c_list = list(filter(lambda x: x<3, a_list))
print(c_list)


# In[37]:


file = open("a.txt","w")
file.write("Hello Python file write !!")
file.close()


# In[39]:


file = open("a.txt","r")
file_data = file.read()
print(file_data)
file.close()


# In[48]:


with open("a.txt","w") as file:
    file.write("with python file open\n")
    file.write("with python file open\n")
    file.write("with python file open\n")

with open("a.txt","r") as file:
    for line in file:
        print(line)
#file_data = file.read()


# In[49]:


with open("score.txt","w") as file:
    name, score = input("이름 성적 입력 > ").split()
    file.write(name + ',' + score)
    
with open("score.txt","r") as file:
    for line in file:
        name,score = line.split(',')
        print(name,': ',score)


# In[59]:


file = open("score.txt","a+")
name, score = input("이름 성적 입력 > ").split()
file.write(name + ',' + score + '\n') # 파일의 마지막 위치를 가리킴

file.seek(0,0)
for line in file:
    name, score = line.split(',')
    print(name, ': ', score)
file.close()


# In[73]:


###### 이름, 국어, 영어, 수학 성적을 입력받아 파일에 저장 file_write()
# 검색할 이름을 입력받아 파일에서 데이터 검색 file_search()
# 검색한 이름과 성적 출력 
# 전체 학생의 인원수와 총점 평균을 구함 file_total()
# 다 함수로 작성
def file_write(filename):
    file = open(filename,"w+")
#     file.close()
    
#     file = open(filename,"a+")
    while(True):
        name, kor, eng, math = input("이름 국어 영어 수학 입력 > ").split()
        if(name=='q'):
            break
        file.write(name + ',' + kor + ',' + eng + ',' + math + '\n')
        
    file.close()

def file_search(filename):
    search_name = input("검색할 이름 > ")
    file = open(filename,"r")
    for line in file:
        name, kor, eng, math = line.split(',')
        if(name==search_name):
            print(name,':',kor,eng,math)

def file_total(filename):
    count = 0
    tot_kor = 0 ; kor_avg = 0
    tot_eng = 0 ; eng_avg = 0
    tot_math = 0 ; math_avg = 0
    
    file = open(filename,"r")
    for line in file:
        name, kor, eng, math = line.split(',')
        count = count + 1
        tot_kor += int(kor)
        tot_eng += int(eng)
        tot_math += int(math)
    #tot = tot_kor + tot_eng + tot_math
    kor_avg = tot_kor/count
    eng_avg = tot_eng/count
    math_avg = tot_math/count
    #tot_avg = tot/count
    return count, kor_avg, eng_avg, math_avg
    
file_write("score.txt")
file_search("score.txt")
count, kor_avg, eng_avg, math_avg = file_total("score.txt")
print("총원: {}, 국어 평균: {}, 영어 평균: {}, 수학 평균: {}".format(count, kor_avg, eng_avg, math_avg))


# In[83]:


# 제너레이터 함수 실행: next(함수명),, 함수 내부에 return 대신 yield 사용

def test():
    print("함수 호출 !!")
    yield "test"
    
    print("함수 호출 2 !!")
    yield "test 2"
    
#함수 호출
print("first call function")
test() # 제너레이터 함수는 일반적인 호출로 실행이 안됨

print("second call function")
test()

file_name = test()
a = next(file_name)
print(a)
print("next ---")
b = next(file_name)
print(b)


# In[86]:


numbers = list(range(1,10+1))

print("홀수만 출력")
print(list(filter(lambda x:x%2==1,numbers)))

print("3이상 7미만 자료만 출력")
print(list(filter(lambda x:3<=x<7,numbers)))

print("제곱해서 50미만 자료만 출력")
print(list(filter(lambda x:x**2<50,numbers)))


# In[89]:


# try ~ except 예외상황 발생 시 처리
try:
    input_number = int(input("정수 입력 >"))
    
    print("원의 반지름: ", input_number)
    print("원의 둘레: ",input_number)
    print("원의 넓이: ", input_number * input_number * 3.14)
except:
    #print("입력 오류 !!")
    pass


# In[95]:


list_data = ['52','345','test','123','44']

list_number = []
for item in list_data:
    try:
        float(item) # 숫자는 float으로 변환
        list_number.append(item)
    except Exception as e:
    # except:
        #print("숫자 아님")
        print(e)
        #pass
    
print(list_number)


# In[96]:


list_data = ['52','345','test','123','44']

list_number = []
for item in list_data:
    try: # 에러 발생 코드
        float(item) # 숫자는 float으로 변환
    except: # 에러 발생 시
        #print("숫자 아님")
        pass
    else: # 에러 발생 안할 시
        list_number.append(item)
    finally: # 무조건 실행
        print("무조건 실행 !!")
print(list_number)


# In[99]:


def test():
    print("test 함수 시작")
    try:
        print("test try start")
        return
        print(" try 구문 return 다음 문장")
    except:
        print("except 구문")
    finally:
        print("finally 구문")
    print("test 함수 end")
    
test()


# In[102]:


# raise 객체: 강제로 에러 발생 시킴

number = input("정수 입력 > ")

if number > 0:
    # 양수일 때 아직 미구현 상태
    raise NotImplementedError
else:
    raise NotImplementedError
    


# In[122]:


## 이름 전화번호를 파일에 저장하는 프로그램 작성
# 파일 이름은 "dataset/telno.txt", 기존에 파일이 존재하면 데이터 추가
# 전화번호 입력은 숫자 3개를 입력 받아 123-456-789 형식으로 저장
# 이름과 전화번호는 ' '로 분리해서 저장
# 저장이 끝나면 파일을 닫고 다시 파일을 open -> 'r' 모드로
# 파일의 내용을 화면에 출력 ex) 홍길동 123-456-7897
# try ~ except ~ finally를 사용해서 작성

def input_telno(filename):
    file = open(filename,'w+')
    while True:
        name = input("이름 입력 > ")
        if(name == 'q'):
            print("전화번호 추가 정지 !!")
            break
        telno = input("전화번호 입력 > ").split()
        if(len(telno)!=3):
            print("전화번호 입력 오류 !!")
            break
            
        telno = '-'.join(telno)
        
        file.write(name + ' ' + telno + '\n')
    file.close()
    
def read_telno(filename):
    file = open(filename,'r')
    for line in file:
        print(line)
        
input_telno("dataset/telno.txt")
read_telno("dataset/telno.txt")


# In[ ]:




