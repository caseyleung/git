# 导入工具包
import json
import requests
from wxauto import WeChat

# 给单人发送消息
to = "casey"  # 要发送的人
wx = WeChat()  # 获取当前微信客户端
wx.Search(to)  # 打开聊天窗口

for x in range(1, 4):
    # resp = requests.get('https://apis.tianapi.com/caihongpi/index?key=651342e57d8753416e5af3eb9acc2788') # 彩虹屁
    resp = requests.get('https://apis.tianapi.com/tiangou/index?key=651342e57d8753416e5af3eb9acc2788')  # 舔狗日记
    data_model = json.loads(resp.text)
    content = data_model['result']['content']
    wx.SendMsg(content)  # 发送消息
    print("发送结束！")



