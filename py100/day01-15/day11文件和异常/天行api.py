import requests
import json


def main():
    # resp = requests.get('http://api.tianapi.com/guonei/?key=651342e57d8753416e5af3eb9acc2788&num=10')
    # resp = requests.get('https://apis.tianapi.com/areanews/index?key=651342e57d8753416e5af3eb9acc2788&areaname=广东')
    resp = requests.get('https://apis.tianapi.com/caihongpi/index?key=651342e57d8753416e5af3eb9acc2788')
    data_model = json.loads(resp.text)
    # print(data_model)
    print(data_model['result']['content'])
    # for news in data_model['result']['list']:
    #     print(news['title'])


if __name__ == '__main__':
    main()