#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    sett=set()  #定义一个空集合 set中最多包含一个argument
    num=int(input('集合的输入数量为'))  
    for i in range(0,num):
        sett.add(input())    #循环输入集合的元素
    print('集合为',sett)
    print('集合元素个数为',len(sett))
    choice=input('1:查找集合元素\n2:对两个集合进行运算\n3:删除集合元素')
    match choice:
        case '1':
            result= (input('要查找的元素为') in sett)  #查找元素是否在集合中
            if result:print('存在')
            else:print('不存在')
        case '2':
            settt=set()
            num1=int(input('新集合的输入数量为'))
            for i in range(0,num):
                settt.add(input())
            print('新集合为',settt)
            choice1=input('1:进行-操作 2：进行|操作 3：进行&操作 4：进行^操作')
            match choice1:
                case '1':print('集合sett中包含而集合settt中不包含的元素',sett-settt)
                case '2':print('集合sett或settt中包含的所有元素',sett|settt)
                case '3':print('集合sett和settt中都包含了的元素',sett&settt)
                case '4':print('不同时包含于sett和settt的元素',sett^settt)
        case '3':
            target=input('删除元素为')
            sett.discard(target) #discard函数删除元素，即使元素不存在也不报错
while 1:
    main()


# In[9]:


for input() in range(0,2):
    print(1)


# In[21]:


a=set('1')
print(a.discard('2'))


# In[ ]:




