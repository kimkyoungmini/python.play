
# coding: utf-8

# In[1]:

import numpy as np
import datetime


# ## list vs. nparray

# In[2]:

#list
li = list(range(1,10000000))
startTime = datetime.datetime.now()

for i in li :
    i*10

print('List execution time :',datetime.datetime.now()-startTime)

#nparray
ar = np.arange(1,10000000)
startTime = datetime.datetime.now()

ar*10

print('ndarray execution time :',datetime.datetime.now()-startTime)


# ## array

# In[7]:

ar = np.arange(25) #0-24
print(ar, '\n')

#5*5 행렬 변환
ar = ar.reshape(5,5)
print(ar, '\n')

#to diagonal matrix
#[0,0]을 기준으로 대각선 데이터만 가져와서 생성
# k : [0,k] 값의 대각선 방향으로 생성
print(np.diag(ar), '\n')
print(np.diag(ar, k=1), '\n')


# ## 난수생성

# In[41]:



print(np.random.normal(size =3), "\n") #size = #random_num
print(np.random.normal(size =(3,3)))

#seed : 난수표 번호 
#seed를 맞추면 계속 동일한 난수 발생
for i in range(3):
    np.random.seed(seed =5)
    print(np.random.normal(size =3)) 
    
#0과 1을 추출 1의 확률을 0.3으로 10번 추출
# N : trials
# p : prob.
print(np.random.binomial(n=1, p=0.5, size=10))
print(np.random.binomial(n=10, p=0.5, size=10))


# ## 행렬연산

# In[44]:

li1 = [1,2,3]
li2 = [4,5,6]

print(li1+li2) #리스트 결합

ar1 = np.array(li1)
ar2 = np.array(li2)

print(ar1+ar2) #nparray는 same shape일 경우, 산술연산


# In[57]:

ar = np.arange(1,13).reshape(4,3)
print('original \n' ,ar)
print('\n첫 행  : \n' ,ar[0])
print('\n0-3행  : \n' ,ar[0:3])
print('\n1행1열 : \n' ,ar[1,1])
print('\n0,3행  : \n', ar[[0,3]]) #0, 3행출력


# In[67]:

ar = np.arange(100,500,100).reshape(2,2)

ar= np.array([[2,3],[2,10]])

print(ar)
print(np.prod(ar, axis=0)) #[4, 30]
print(np.prod(ar, axis=1)) #[6, 20]

print(np.matmul(ar,ar))


# In[73]:

k = [[1,2],[3,4]]
l = [[5,6],[7,8]]

print(np.concatenate((k,l), axis=0))

print(np.concatenate((k,l), axis=1))

print(np.split(k,(1,1), axis=1))


# In[84]:

m = np.arange(16).reshape(4,4)
print(m, '\n')
m_split = np.split(m, [2,3], axis =0)
#[2,3] 자르는 자리 --> 즉, 1,2번째 열 / 3번째 열 / 나머지 열 이렇게 split 됨!

for i in range(len(m_split)):
    print( m_split[i])
    
    


# 

# In[ ]:





