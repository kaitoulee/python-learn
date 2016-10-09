#coding:utf-8

#代码块
# name = 'hello' 不会显示直接舍弃
# name = 'Mary' #显示 Hello Mary
# if name == 'Mary':
# 	print ('Hello Mary')
# password = 'sowrdfish'
# if password == 'sowrdfish':
# 	print ('Access granted.')
# else:
# 	print ('Wrong password.')


'''
if语句包含以下部分
if关键字
条件（即求值为true 或False的表达式）
冒号
在下一行开始，缩进的代码块（称为if子句）

例如，假定有一些代码，检查某人的名字是否为Alice（假设此前曾为name赋值）
'''
# name = "Alice"
# if name == 'Alice':
# 	print ("Hi,Alice")

#else语句
#只有if语句的条件为False时，else才会执行。
#else不包含条件。
#else关键字
#冒号
#在下一行开始，缩进的代码块（称为else语句）

#例子 回到上面Alice的例子，

# name = "Alice"
# if name == "Alice":
# 	print ("Hello, Alice") #这里不需要冒号
# else:
# 	print ("Hello,Stranger.")


#elif语句 否则如果，总是跟在if或另一个elif语句后面。提供另一个条件，仅在前面的条件是false时才
#检查该条件
#elif关键字
#条件（即求值为True或False的表达式）
#冒号
#在下一行，缩进的代码块（称为elif子语句）
#例子  在名字检查程序中添加elif。

# name = "kaitoulee"
# age = 1
# age = 18
# if name == "Kaitoulee":
# 	print ("Kaitoulee")

# elif age < 12:
# 	print ("You are not Kaitoulee,kiddo.")
# elif age > 12:
# 	print ("luodan")

#while循环语句 让代码块一遍又一遍执行。只要while语句为True。
#关键字
#条件（求值为True或False的表达式）
#冒号
#从新行开始，缩进的代码块

#if语句

# spam = 0
# if spam < 5:
# 	print("Hello World")
# 	spam = spam + 1


#while语句

# spam = 0
# while spam < 5:
# 	print ("Hello,Wrold")
# 	spam = spam + 1
# 	print (spam)

#下面这个没有实现报错，目前怀疑没有导入系统库的原因。原因是input（）是数值类型的输入，int、float raw_input()是字符串类型，string类型
# name = ""
# while name != "heilian":
# 	print ("Please you name ")
# 	name = input()
# print ("Thank you")


#break语句

# while True:
# 	print ("please type your name ")
# 	name = raw_input()
# 	if name == "youname":
# 		break
# print ("Thank your")

#continue语句 continue语句用于循环内部。如果程序执行遇到continue语句，就会马上跳回到循环开始处，重新对循环条件求值
#也就是执行到达循环末尾发生的事情。

# while True:#无限循环
# 	print ("who are your?")
# 	name = raw_input()#获取用户输入
# 	if name != "Kaitoulee":#如果用户输入Kaitoulee就终止
# 		continue #终止
# 	print ("Hello, Kaitoulee, What is the password?( It is a fish.)")
# 	password = raw_input()#获取用户输入
# 	if password == "heilian":#如果获取为heilian就终止
# 		break#返回
# print ("Access granted。")

#无限循环执行
# while True:
# 	print("Hello")

# while True:
# 	print ("you name")
# 	name = raw_input()
# 	if name != "kaitoulee":
# 		continue
# 	print("Hello Kaitoulee")
# 	password = raw_input()
# 	if password == "heilian":
# 		break
# print("Access")

# for x in range(10):
# 	if x == 5:
# 		break

# 	print x

#for循环和range()函数
#在条件为True时，while循环就会继续循环。但如果你想让一个代码块执行固定次数，可以通过for循环语句和range()函数来实现。

name = ""
while not name:
	print("Enter you name:")
	name = raw_input()
	print("How many guests will you have?")
	numOfGuests = int(raw_input())
	if numOfGuests:
		print("Be sure to have enough room for all your guests.")
		print("Done")

total = 0
for num in range(101):
	total = total + num
print(total)

#必须是整型的 可以是负数
# for i in range(-1,1):
# 	print(i)
#第一个参数是开始，第二个参数是终止的参数，第三个是隔几个。
# for i in range(0,9,2):
# 	print(i)

# for i in range(5,-1,-1):
# 	print(i)

# for i in range(5,0):
# 	print(i)

# import random
# for i in range(5):
# 	print(random.randint(1, 10))









