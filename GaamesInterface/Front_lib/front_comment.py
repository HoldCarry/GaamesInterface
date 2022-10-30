import requests
from common import baseurl
import json
import time
from common import random_data

url = baseurl.Games_url
##headers用于调试，可以通过参数化写入
headers = {
    "id": "//869372030027653",
    "User-Agent": "b/c/d/e/f/31001//",
    "locale": "zh_CN;IN;TT",
    "UT": "TOKEN_m4xsyi29e2Ywa93EtFMFAuHoWKe3tYSrsY2u9m/HhkEplIZkPHXFbY7KtoGOJGVkt0bnl/a6CXhnH8QGwOPVLjm4hgyIwMI3hPk4KlZeW7U=",
    "Content-Type": "application/JSON; charset=UTF-8",
    "Accept": "application/JSON; charset=UTF-8"
}


##通过接口获取视频贴主评论
def videothread_front_maincomment():
    path = url + "/games/community/v1/comment"
    body = {"tid": 93, "content": "tell me what to say", "rootId": 0, "parentId": 0}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    # print(requests_result)
    return body["tid"], requests_result


##通过接口获取视频贴子评论
def videothread_front_subcomment():
    path = url + "/games/community/v1/comment"
    body = {"tid": 93, "content": "tell me what to say", "rootId": "1985503848937038848",
            "parentId": "1985503848937038848"}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    # print(requests_result)
    return body["tid"], requests_result


##通过接口获取图文贴主评论
def graphicthread_front_maincomment():
    path = url + "/games/community/v1/comment"
    body = {"tid": 335, "content": "海南海南海南海南", "rootId": 0, "parentId": 0}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    # print(requests_result)
    return body["tid"], requests_result


##通过接口获取图文贴子评论
def graphicthread_front_subcomment():
    path = url + "/games/community/v1/comment"
    body = {"tid": 335, "content": "海南海南海南海南", "rootId": "1985503848937038848", "parentId": "1985503848937038848"}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    # print(requests_result)
    return body["tid"], requests_result


##通过评论发送接口发送app详情页主评论
def app_front_postmaincomment():
    pkgname = random_data.random_str()
    path = url + "/games/community/v1/review"
    body = {"content": "123456", "pkgName": pkgname, "rootId": 0, "parentId": 0, "point": 100,
            "mobileCode": "LE2125", "mobileName": "OnePlus LE2125", "playTime": 0}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    rid = json.loads(requests_result)["data"]
    # print(requests_result)
    return rid


# 通过评论接口发送app详情页的子评论
def app_front_postsubcomment(rootId, parentId):
    path = url + "/games/community/v1/review/leaf"
    body = {"content": "12345", "pkgName": None, "rootId": rootId, "parentId": parentId, "point": 0, "mobileCode": None,
            "mobileName": None, "playTime": 0}
    requests_result = json.dumps(requests.post(url=path, headers=headers, json=body).json())
    rid = json.loads(requests_result)["data"]
    # print(requests_result)
    return rid


##通过评论删除接口删除app主评论
def app_front_deletecomment(raid):
    path = "/games/community/v1/review/delete"
    request_url = url + path
    rid = raid
    param = {"rid": rid}
    # result = json.dumps(requests.get(url=request_url, headers=headers, params=param).json())
    result = json.dumps(requests.get(url=request_url, headers=headers, params=param).json())
    return result


if __name__ == '__main__':
    # print(app_front_deletecomment(app_front_postmaincomment()))
    print(app_front_postmaincomment())
