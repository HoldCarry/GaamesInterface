import requests
import json

#定义一个叫做request_model的类
#拆分成get和post请求两种类型
#封装两个请求方式
#传参调用get_request这个方法，通过这个方法选择调用get或者post

class  request_model():
    def send_get(self, url, data , headers):
        try:
            result = requests.get(url=url, params=data, headers=headers)
            res_get = result.json()
            res_code = result.status_code
            return res_code,res_get
        except:
            result_text = requests.get(url=url, params=data, headers=headers)
            res_post = result_text.text
            res_code = result_text.status_code
            return res_code, res_post

    def send_post(self,url,data,headers):
        try:
            result = requests.post(url=url, json=data, headers=headers)
            #res_post = json.dumps(result.json(),ensure_ascii=False)
            res_post = result.json()
            res_code = result.status_code
            # if type(res_post) == str:
            #     return res_code,eval(res_post)
            # elif type(res_post) == dict:
            #     return res_code, res_post
            # else:
            #     return print("还返回个啥玩意自己写")
            return res_code,res_post
        except:
            result_text = requests.post(url=url, json=data, headers=headers)
            res_post = result_text.text
            res_code = result_text.status_code
            return res_code,res_post




    def get_request(self, method, url=None, data=None ,headers=None):
        result = None
        if method == 'post':
            result = self.send_post(url, data ,headers)
        elif method == 'get':
            result = self.send_get(url, data , headers)
        else:
            print("你他妈的传错了，这个不是请求")
        return result

if __name__ == '__main__':
    result2 = request_model().get_request('get', 'http://i3-test-browser-cpc.wanyol.com/feedsChannel/getList?session=eyJiYWNhIjoiOTJmMGM5YjBhODdhNTFlMTdlNmJhYTBiNGY1MjAwMDkiLCJzIjoiYmFjYSIsIm9wcG8iOiJvZnM9ZXlKMGVYQWlPaUpLVjFRaUxDSmhiR2NpT2lKSVV6STFOaUo5LmV5SjFkSGx3SWpvd0xDSmlkV2xrSWpvek9EVTNPVFEzT1RFNU9Ua3pOREE0TURBc0ltRjFaQ0k2SW1KeWIzZHpaWElpTENKMlpYSWlPaklzSW5KaGRDSTZNVFU1TVRnMk5EUXpPQ3dpZFc1dElqb2lUMUJIWDJZMFpqWmlZV1EwTURGbU56UXlOMlZoWlRrMlpHWmhZMlJpWVRVMVpERTFJaXdpYVdRaU9pSTVNbVl3WXpsaU1HRTROMkUxTVdVeE4yVTJZbUZoTUdJMFpqVXlNREF3T1NJc0ltVjRjQ0k2TVRZd01ERTRORE14TWl3aVpHTWlPaUowWlhOMEluMC5DXzQ0SXdhdkJtdTNKSHJBcXFfcFdOV3Z0VmV6SlRKaFhSeEVQUUZRZXNjIiwiaW5mbyI6eyJydCI6IjE2MDAxNTU1NjEiLCJmdCI6IjE1OTE4NjQ0MzgiLCJ1biI6Ik9QR19mNGY2YmFkNDAxZjc0MjdlYWU5NmRmYWNkYmE1NWQxNSJ9fQ%3D%3D&newsLangs=id-ID&f=json&version=18&feedssession=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1dHlwIjowLCJidWlkIjozODU3OTQ3OTE5OTkzNDA4MDAsImF1ZCI6ImJyb3dzZXIiLCJ2ZXIiOjIsInJhdCI6MTU5MTg2NDQzOCwidW5tIjoiT1BHX2Y0ZjZiYWQ0MDFmNzQyN2VhZTk2ZGZhY2RiYTU1ZDE1IiwiaWQiOiI5MmYwYzliMGE4N2E1MWUxN2U2YmFhMGI0ZjUyMDAwOSIsImV4cCI6MTYwMDE4NDMxMiwiZGMiOiJ0ZXN0In0.C_44IwavBmu3JHrAqq_pWNWvtVezJTJhXRxEPQFQesc&__t=1600155563&sign=08b76c229b8193ce69f41ceaa608be0f&area=province%253A%25E5%25B9%25BF%25E4%25B8%259C%25E7%259C%2581%253Bcity%253A%25E6%25B7%25B1%25E5%259C%25B3%253Bcountry%253A%25E4%25B8%25AD%25E5%259B%25BD',{"version":"18"})
    print(result2)