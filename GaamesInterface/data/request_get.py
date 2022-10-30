import requests
import json



url = "http://games-global.wanyol.com"
path = "/games/community/v1/review/delete"

request_url = url + path
headers = {
            "id": "//869372030027653",
            "User-Agent":"b/c/d/e/f/31001//",
            "locale": "zh_CN;IN;TT",
            "UT":"TOKEN_m4xsyi29e2Ywa93EtFMFAuHoWKe3tYSrsY2u9m/HhkEplIZkPHXFbY7KtoGOJGVkt0bnl/a6CXhnH8QGwOPVLjm4hgyIwMI3hPk4KlZeW7U=",
            "Content-Type": "application/JSON; charset=UTF-8",
            "Accept":"application/JSON; charset=UTF-8"
        }
param = {"rid":2149245556681110528}
result = requests.get(url=request_url,headers=headers,params=param)
try:
    print(json.dumps(result.json()))
except:
    print(result.text)
#assert result.status_code == 200