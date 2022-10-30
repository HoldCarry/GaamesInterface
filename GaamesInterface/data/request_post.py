import requests
import json



url = "https://games-global.wanyol.com"
path = "/games/community/v1/review"
# path = "/games/community/v1/comment"
request_url = url + path
headers = {
            "id": "//869372030027653",
            "User-Agent":"b/c/d/e/f/31001//",
            "locale": "zh_CN;IN;TT",
            "UT":"TOKEN_m4xsyi29e2Ywa93EtFMFAuHoWKe3tYSrsY2u9m/HhkEplIZkPHXFbY7KtoGOJGVkt0bnl/a6CXhnH8QGwOPVLjm4hgyIwMI3hPk4KlZeW7U=",
            "Content-Type": "application/JSON; charset=UTF-8",
            "Accept":"application/JSON; charset=UTF-8"
        }
data = {"content":"doewmofmo","pkgName":"com.lkhfkkdjnsm","rootId":0,"parentId":0,"point":0,"mobileCode":"LE2125","mobileName":None,"playTime":0}

result = requests.post(url=request_url,headers=headers,json=data)
try:
    print(json.dumps(result.json()))
    print(str(result.status_code))
except:
    print(result.text)
assert result.status_code == 200

# i = 9999
# while i < 10099:
#     data = {"tid": 62, "content": "wolawolabiuycbic"+str(i), "rootId": 0, "parentId": 0}
#     result = requests.post(url=request_url, headers=headers, json=data)
#     try:
#         print(json.dumps(result.json()))
#         print(str(result.status_code))
#     except:
#         print(result.text)
#     assert result.status_code == 200
#     i += 1
