#coding:utf-8
import itchat
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
	itchat.send(['Text'], msg['FromUserName'])

itchat.auto_login()
itchat.run()