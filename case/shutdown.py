import itchat
import os
import time
import cv2

sendMsg = u"{消息助手}: 暂时无法回复"
usageMsg = u"使用方法： \n1. 运行cmd命运: cmd xxx(xxx为命令)\n" \
           u"-例如: 定时关机命令: cmd shutdown -s -t 3600 \n" \
           u"2. 获取当前电脑用户: cap\n" \
           u"3. 启用消息助手(默认关闭): ast\n" \
           u"4. 关闭消息助手: astc"

flag = 0  # 消息助手关闭
nowTime = time.localtime()
fileName = str(nowTime.tm_mday) + str(nowTime.tm_hour) + str(nowTime.tm_min) + str(nowTime.tm_sec) + ".txt"
myFile = open(fileName, 'w', encoding='utf-8')


@itchat.msg_register('Text')
def text_reply(msg):
    global flag
    message = msg['Text']
    fromName = msg['FromUserName']
    toName = msg['ToUserName']

    if toName == 'filehelper':
        if message == 'cap':
            cap = cv2.VideoCapture(0)
            ret, img = cap.read()
            cv2.imwrite('weixinTemp.jpg', img)
            itchat.send('@img@%s' % u'weixinTemp.jpg', 'filehelper')
            cap.release()
        if message[0, 3] == 'cmd':
            os.system(message.strip(message[0:4]))
        if message == 'ast':
            flag = 1
            itchat.send('消息助手已开启', 'filehelper')
        if message == 'astc':
            flag = 0
            itchat.send('消息助手已关闭', 'filehelper')
    elif flag == 1:
        itchat.send(sendMsg, fromName)
        myFile.write(message)
        myFile.write('\n')
        myFile.flush()


if __name__ == '__main__':
    itchat.auto_login()
    itchat.send(usageMsg, 'filehelper')
    itchat.run()
