# -*- coding:utf-8 -*-
#import os
import itchat
from itchat.content import *
import sys
import time
import random
itchat.auto_login(hotReload=True)
idnow=0
ifgame=False
user={}
weuser={}
role={}
userlist=[]
groupchatmain='@@ed283c62a59ccea2029e7f4a9b6331edbd47ae304f5869d1281224528103d6c6'#测试用
groupchatlangren='@@ed283c62a59ccea2029e7f4a9b6331edbd47ae304f5869d1281224528103d6c6'#测试用
def sendmsg(message,touser):
    itchat.send_msg('%s'%message,toUserName=touser)
@itchat.msg_register([TEXT])
def text_reply(msg):
    global idnow
    global user
    global weuser
    global role
    global userlist
    if msg['Content']=='开始游戏':
        if ifgame==False:
#            sendmsg('加入成功，您的id:%s'%idnow,msg['FromUserName'])
            if not weuser.get(msg['FromUserName'],-1)==-1:
                itchat.send_msg('请勿重复加入。',toUserName=msg['FromUserName'])
            else:
                itchat.send_msg('加入成功，您的id:%s\n请等待游戏开始.\n游戏开始前，您也可以输入\"退出游戏\"来退出游戏。'%idnow,toUserName=msg['FromUserName'])
                user[idnow]=msg['FromUserName']
                weuser[msg['FromUserName']]=idnow
                userlist.append(msg['FromUserName'])
                print(user)
                print(weuser)
                idnow=idnow+1
                if len(userlist)>=8:
                    #开始游戏
                    start()
    if msg['Content']=='退出游戏':
        k=weuser.get(msg['FromUserName'],-1)
        if k!=-1:
            for (a,b) in user.items():
                if b==msg['FromUserName']:
                    fa=a
            for (c,d) in weuser.items():
                if c==msg['FromUserName']:
                    fc=c
            user.pop(fa)
            weuser.pop(fc)
            for us in range(len(userlist)):
                if userlist[us]==msg['FromUserName']:
                    fus=us
            userlist.pop(us)
            itchat.send_msg('成功退出游戏。',toUserName=msg['FromUserName'])
        else:
            itchat.send_msg('退出失败，您未加入游戏.',toUserName=msg['FromUserName'])
        print(userlist)
        print(weuser)
        print(role)
        print(user)
    if msg['FromUserName'] not in userlist:
            print('请先加入游戏。回复\"开始游戏\"')
            itchat.send_msg('请先加入游戏。回复\"开始游戏\"\n--狼人杀Beta',msg['FromUserName'])
            return
    #if各种控制模块
    if role[weuser[msg['FromUserName']]]='langren':
        #狼人发来的消息
    elif role[weuser[msg['FromUserName']]]='nvwu':
        #女巫发来的消息，作消息处理
    elif role[weuser[msg['FromUserName']]]='yuyanjia':
        #预言家发来的消息，作消息处理
    else:
        #村民发来的消息
def start():
    #global idnow
    global user
    global weuser
    global role
    global userlist
    #初始化
    #包含分配角色 建群等
    #建群获得的id赋值给groupchatmain和groupchatlangren
@itchat.msg_register([TEXT],isGroupChat=True)
#这里注册的消息是群聊回复状态
def toupiao(msg):
    #global idnow
    global user
    global weuser
    global role
    global userlist
    print('%s' % msg['Content'])
    print('%s' % msg['FromUserName'])
    if msg['FromUserName']==groupchatmain:#来自主群的消息
        #itchat.send_msg('ITCHATTest'+msg['Content'],toUserName=groupchatmain)
        #其实没有什么必要 最多防作弊，主群本来就是用来讨论的
    elif msg['FromUserName']==groupchatlangren:#来自狼人的消息
        #itchat.send_msg('ITCHATTestLangren'+msg['Content',toUserName=groupchatlangren])
        #数据处理，算出最后被杀
def mainloop():
    global user
    global weuser
    global role
    global userlist
    #大循环[天黑请闭眼--天亮请睁眼--下一次天黑请闭眼]
    #各种判断模块，判断谁被杀以及剧情发展
    #最后如果女巫/预言家被杀，仍然要一个random的sleep
    #如果所有非狼人/狼人被杀完，游戏结束进入ending，开始120秒倒计时然后强制踢出所有人
    mainloop()
def ending():
    global user
    global weuser
    global role
    global userlist
    #各种结果公布+倒计时踢人
itchat.run()