#coding:utf-8
#可以用于用户登录使用的代码
while True:
	print ("Who are you?")
	name = raw_input()
	if name != "KaitouLee":
		continue#不等于时候就跳回上面
	print ("Hello, KaitouLee, What is the password? (it is a fish.)")
	password = raw_input()
	if password == "123456":
		break
print ("Access granted.")