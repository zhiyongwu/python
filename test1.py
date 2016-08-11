import requests

r = requests.post('http://vertical.rsvptech.cn:8080/ChineseVerticalServer/data/json/weather')
print(r.text)