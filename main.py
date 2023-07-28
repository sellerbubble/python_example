#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def num():
    a=float(input("为一个变量名为a的变量赋数字类型的值"))
    b=float(input("为一个变量名为b的变量赋数字类型的值"))#将输入的数字字符串转换为float类型数
    while 1:
        choice=input("请输入操作指令：\n1：删除数字对象引用\n2:数字类型转换\n3:比较a和b\n4:退出\n")
        match choice:
            case '1':
                del a,b                 #del删除a和b
                print("a和b已经被删除")
            case '2':
                choice1=input("转换为int输入1，转换为float输入2")
                match choice1:
                    case '1':
                        print('int(a)=',int(a)) # 将a转换为int
                    case '2':
                        print('float(a)=',float(a))  #将a转换为float
            case '3':
                if(a>b):print('a>b') 
                elif(a<b):print('a<b')
                else:print('a=b')        #比较a和b的大小
            case '4':
                break
def string():
    a=input("为一个字符串类型的变量a赋值")
    print('字符串长度为',len(a))
    choice=input('输入指令选项：\n1：对字符串进行索引\
    \n2:展示不同的转义字符演示单引号、换行符、制表符、退格符、换页符、ASCII、二进制、八进制数和十六进制数的效果\
    \n3:展示字符串的运算\n4:使用fstring格式化字符串\n')
    match choice:
        case '1':
            start=int(input('起始下标'))
            end=int(input('终点下标'))
            print(a[start:end+1])   #对a字符串进行索引
        case '2':
            print('\'Hello, world!\'')  # \'输出单引号

            print("Hello, world!\tHow are you?")  # 输出：Hello, world!    How are you?

            print("Hello,\b world!")  # 输出：Hello world!  \b用于退格

            print("Hello,\tworld!")  # 输出：\t为横向制表符
                          

            print("A 对应的 ASCII 值为：", ord('A'))  # 输出：A 对应的 ASCII 值为： 65

            decimal_number = ord('A')
            binary_number = bin(decimal_number)  # 十进制转换为二进制
            print('转换为二进制:', binary_number)  # 转换为二进制

            octal_number = oct(decimal_number)  # 十进制转换为八进制
            print('转换为八进制:', octal_number)  # 转换为八进制

            hexadecimal_number = hex(decimal_number)  # 十进制转换为十六进制
            print('转换为十六进制:', hexadecimal_number) # 转换为十六进制
        case '3':
            b=input('为一个字符串类型的变量b赋值')
            print("a + b 输出结果：", a + b)
            print("a * 2 输出结果：", a * 2)
            print("a[1] 输出结果：", a[1])
            print("a[1:4] 输出结果：", a[1:4])
 
            if( b in a) :
                print("b在变量 a 中")   #查询b是否在a中
            else :
                print("b 不在变量 a 中")
            print (r'\n') #r在’前将输出原始字符串
        case '4':
            print(f'a为{a}')
            print(f'a的长度为{len(a)}') #{}中放置表达式，输出其结果到字符串中
def list():
    num=int(input('输入列表元素个数')) #将输入的字符串转换为整数
    list=[None]*num  #先创建一个元素数量为num的空列表
    for i in range(0,num):
        list[i]=input()       #输入列表元素
    choice=input('请输入指令选项：1：添加元素\
    \n2:更改列表元素值\n3：列表拼接\n')
    match choice:
        case '1':
            add=input('请输入新元素')  
            list.append(add)    #使用append为列表添加元素
            print('新列表为',list)
        case '2':
            choice1=input('1:删除列表元素\n2：修改列表元素')
            match choice1:
                case '1':
                    choice2=int(input('删除元素下标为'))
                    del list[choice2]    #删除列表元素
                    print('删除后列表为',list)
                case '2':
                    choice3=int(input('修改元素下标为'))
                    choice4=input('修改元素值为')
                    list[choice3]=choice4     #修改列表元素
                    print('修改后列表为',list)
        case '3':
            num1=int(input('输入新列表元素个数'))
            list1=[None]*num1  #创建空列表
            for i in range(0,num1):
                list1[i]=input()
            list+=list1        #拼接列表
            print('拼接后列表为',list)
def dict():
    num=int(input('输入字典的元素对数'))
    dic={}  #创建一个字典
    for i in range(0,num):
        key=input('输入第%d个key'%(i+1))
        value=input('输入第%d个value'%(i+1))
        dic[key]=value
    print('字典为',dic)
    choice=input('1:查找指定键的值\n2:添加元素\n3:删除元素\n')
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
def set():
    sett=set()  #定义一个空集合 set中最多包含一个argument
    num=int(input('集合的输入数量为'))  
    for i in range(0,num):
        sett.add(input())    #循环输入集合的元素
    print('集合为',sett)
    print('集合元素个数为',len(sett))
    choice=input('1:查找集合元素\n2:对两个集合进行运算\n3:删除集合元素\n')
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
            choice1=input('1:进行-操作 2：进行|操作 3：进行&操作 4：进行^操作\n')
            match choice1:
                case '1':print('集合sett中包含而集合settt中不包含的元素',sett-settt)
                case '2':print('集合sett或settt中包含的所有元素',sett|settt)
                case '3':print('集合sett和settt中都包含了的元素',sett&settt)
                case '4':print('不同时包含于sett和settt的元素',sett^settt)
        case '3':
            target=input('删除元素为')
            sett.discard(target) #discard函数删除元素，即使元素不存在也不报错
while 1:
    choice=input('1:执行num脚本 2:执行string脚本 3:执行list脚本 4:执行dict脚本 5：执行set脚本\n ')
    match choice:
        case '1':
            num()
        case '2':
            string()
        case '3':
            list()
        case '4':
            dict()
        case '5':
            set()
    choice1=input('输入1退出')
    if choice1=='1':break


# In[ ]:




