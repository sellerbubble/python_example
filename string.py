#!/usr/bin/env python
# coding: utf-8

# In[10]:


def main():
    a=input("为一个字符串类型的变量a赋值")
    print('字符串长度为',len(a))
    choice=input('输入指令选项：\n1：对字符串进行索引\
    \n2:展示不同的转义字符演示单引号、换行符、制表符、退格符、换页符、ASCII、二进制、八进制数和十六进制数的效果\
    \n3:展示字符串的运算\n4:使用fstring格式化字符串')
    match choice:
        case '1':
            start=input('起始下标')
            end=input('终点下标')
            print('a[start:end+1]')
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
                print("b在变量 a 中")
            else :
                print("H 不在变量 a 中")
            print (r'\n') #r在’前将输出原始字符串
        case '4':
            print(f'a为{a}')
            print(f'a的长度为{len(a)}') #{}中放置表达式，输出其结果到字符串中
main()

