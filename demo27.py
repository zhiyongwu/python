import requests

r = requests.get('http://faxiaobot.cn/download/image/device/thumb/94a1a2a008ec_1464856734148.jpg')
print(r.text)
print(r.status_code)