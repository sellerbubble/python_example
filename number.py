#!/usr/bin/env python
# coding: utf-8

# In[4]:


def check_variable(variable_name):
    if variable_name in locals():
        return 1     
    else:
        return 0
def main():
    a=float(input("为一个变量名为a的变量赋数字类型的值"))
    b=float(input("为一个变量名为a的变量赋数字类型的值"))#将输入的数字字符串转换为float类型数
    while 1:
        choice=input("请输入操作指令：\n1：删除数字对象引用\n2:数字类型转换\n3:比较a和b\n4:退出")
        match choice:
            case '1':
                del a,b
                print("a和b已经被删除")
            case '2':
                if (check_variable(a))==0:
                    a=float(input("为一个变量名为a的变量赋数字类型的值"))
                    b=float(input("为一个变量名为a的变量赋数字类型的值"))#将输入的数字字符串转换为float类型数                             
                choice1=input("转换为int输入1，转换为float输入2")
                match choice1:
                    case '1':
                        print('int(a)=',int(a))
                    case '2':
                        print('float(a)=',float(a))
            case '3':
                if(a>b):print('a>b')
                elif(a<b):print('a<b')
                else:print('a=b')
            case '4':
                break
main()
            
            


    


# In[8]:


def check_variable(variable_name):
    if variable_name in locals():
        return 1     
    else:
        return 0
a=1
check_variable(a)
def k():
    a=1
    print(check_variable(a))
k()
print(locals())


# In[ ]:




