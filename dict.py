#!/usr/bin/env python
# coding: utf-8

# In[13]:


def main():
    num=int(input('输入字典的元素对数'))
    dic={}  #创建一个字典
    for i in range(0,num):
        key=input('输入第%d个key'%(i+1))
        value=input('输入第%d个value'%(i+1))
        dic[key]=value
    print('字典为',dic)
    choice=input('1:查找指定键的值\n2:添加元素\n3:删除元素')
    match choice:
        case '1':
            key=input('key为')
            result=dic.get(key)
            if result==None:print('该键不存在')
            else: print('键值为%s'%result)
        case '2':
            key=input('key为')
            value=input('value为')
            dic[key]=value
            print('添加成功')
        case '3':
            key=input('删除的key为')
            print('删除的键值为',dic.pop(key))
            
main()

