import pytest
from common.readexcel import get_book02
from common.request_method import request_model
import json
from common import baseurl
import requests
from logs.logger import Log
import time
import os
import traceback

class Test_message():

    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_message", "MessageTable"))
    def test_MessageTable(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, data, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
            assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))

    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_message", "MessageTop"))
    def test_MessageTop(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, data, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
            assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))

    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_message", "MessageRead"))
    def test_MessageRead(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, data, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
            assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))


    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_message", "MessageAllRead"))
    def test_MessageAllRead(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, data, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
            assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))

    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_message", "MessageReddot"))
    def test_MessageReddot(self, path, param, headers, method, expect, case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, param, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
        # assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.info(f'报错信息：{traceback.format_exc()}')
            # logger.error(traceback.format_exc())
            raise error
        # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求参数：{param}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))


    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_message", "MessageBlack"))
    def test_MessageBlack(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            requests_result = request_model().get_request(method, URL, data, headers)
            # logger.debug(f'发送请求：{requests_result}')
            # return requests_result
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
            assert requests_result[1]["data"] == expect["data"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))



if __name__ == '__main__':
    print(Test_message().test_MessageBlack02("/games/message/v1/black",{"Accept": "application/json;charset=UTF-8",
            "User - Agent": "OnePlus%2FIN2010%2F30%2F11%2FOxygen+OS+11.0.4.4.IN21DA%2F31001%2F600%2F2.7.0.0",
            "locale":"zh;IN;CN",
            "ut": "TOKEN_LUi3clqlr3Pei36ZJyA2NqONyjM+kGOy6m0FDc8p1EwanGnlbMov/voyN750m2/HtAXHMSl2lbHiajQPlzvU/CSZU492B4p0wSi0dqQzxYA=",
            "Content - Type":"application/json;charset=UTF-8"},{"blackType": 1, "blackSubject": 5, "operationType": 2},"post"))
