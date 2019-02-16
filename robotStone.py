import requests
import json

def Run(text):
    url = "http://openapi.tuling123.com/openapi/api/v2"#api地址
    req = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text
            },
            "selfInfo": {
                "location": {
                    "city": "",
                    "province": "",
                    "street": ""  #输入自己的，可以获得天气之类的
                }
            }
        },
        "userInfo": {
            "apiKey": "",#从图灵机器人获取
            "userId": ""#你的id
        }
    }
    req = json.dumps(req).encode('utf-8')
    post = requests.request('POST',url,data=req,headers={'content-type': 'application/json'})#发送一个post请求
    response_dic = json.loads(post.text)
    print(response_dic['results'][0]['values']['text'])#提取text


while True:
    try:
        inputtext = input("Me(p to quit):")
        if(inputtext=='p'):
            break
        Run(inputtext)
    except:
        print("抱歉发生错误，请再次尝试")
print("真是愉快的一次聊天啊！！")