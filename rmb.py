#!/usr/bin/env python
# coding: utf-8

# In[18]:


import math
try:
    num=float(input())
except:
    num=float(input('重新输入有效数字'))
if(num>=10000000)or(num<0):
    num=float(input('输入范围错误请重新输入'))
k=math.modf(num)
print(k)
small=k[0]#存储小数部分
big=int(k[1])  #存储整数部分并转换为整数
small=small*100 #将小数的前两位转换为整数部分
small=round(small)
print(big,small)
bigstr=str(big)
print(bigstr)
smallstr=str(small)
print(smallstr)
bignum=len(bigstr)
bigstr=bigstr.zfill(7)#对高位进行补零
smallstr=smallstr.zfill(2)#对低位进行补零
flag=0  #判断是否需要输出万
dic={0:'零',1:'一',2:'二',3:'三',4:'四',5:'五',6:'六',7:'七',8:'八',9:'九'}
if int(bigstr[0])!=0:
    print(dic[int(bigstr[0])]+'百',end='')
    flag=1
if int(bigstr[1])!=0:
    print(dic[int(bigstr[1])]+'十',end='')
    flag=1
if int(bigstr[2])!=0:
    if(bigstr[0]!='0')and(bigstr[1]=='0'):
        print('零',end='')   #对零的判断
    print(dic[int(bigstr[2])],end='')
    flag=1
if flag==1:
    print('万',end='')
flagg=0 #判断是否有元
if int(bigstr[3])!=0:
    print(dic[int(bigstr[3])]+'千',end='')
    flagg=1
if int(bigstr[4])!=0:
    if(bigstr[3]=='0')and flag==1:#当有万且无千有百时百前面带零
        print('零',end='')
    print(dic[int(bigstr[4])]+'百',end='')
    flagg=1
if int(bigstr[5])!=0:
    if(bigstr[4]=='0')and(flag==1 or bigstr[3]!='0'):#当有万或者有千且无百时十前面带零
        print('零',end='')    
    print(dic[int(bigstr[5])]+'十',end='')
    flagg=1
if int(bigstr[6])!=0:
    if(bigstr[5]=='0')and (flag==1 or bigstr[4]!='0' or bigstr[3]!='0' ):#当有万或者有千或者有百但是无十时前面带零
        print('零',end='')
    print(dic[int(bigstr[6])],end='')
    flagg=1
if flag==1 or flagg==1:
    print('元',end='')
if int(smallstr[0])!=0:
    print(dic[int(smallstr[0])]+'角',end='')
if int(smallstr[1])!=0:
    print(dic[int(smallstr[1])]+'分',end='')

    
'''
def judege(a,b):  #需a和b的最大位数相同才能判断该位的数值 b为0.1或0.01
    i=0
    while 1:
        a=a-b
        if a<0:
            return i
        i+1
'''


# In[ ]:


oo


# In[ ]:




