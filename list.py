#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def main():
    num=int(input('输入列表元素个数')) #将输入的字符串转换为整数
    list=[None]*num  #先创建一个元素数量为num的空列表
    for i in range(0,num):
        list[i]=input()       #输入列表元素
    choice=input('请输入指令选项：1：添加元素\
    \n2:更改列表元素值\n3：列表拼接')
    match choice:
        case '1':
            add=input('请输入新元素')
            list.append(add)
            print('新列表为',list)
        case '2':
            choice1=input('1:删除列表元素\n2：修改列表元素')
            match choice1:
                case '1':
                    choice2=int(input('删除元素下标为'))
                    del list[choice2]
                    print('删除后列表为',list)
                case '2':
                    choice3=int(input('修改元素下标为'))
                    choice4=input('修改元素值为')
                    list[choice3]=choice4
                    print('修改后列表为',list)
        case '3':
            num1=int(input('输入新列表元素个数'))
            list1=[None]*num1
            for i in range(0,num1):
                list1[i]=input()
            list+=list1
            print('拼接后列表为',list)
            
while 1:
    main()

