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


class Test_GamePkg_Send():

    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_GamePkg_Send", "game_pkg_send"))
    def test_game_pkg_send(self, path, headers, data, method, case, expect):
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
            assert requests_result[1]["msg"] == expect["message"]
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
    Test_GamePkg_Send().test_game_pkg_send("/games/data/v1/upload", {
        "Accept": "application/json",
        "locale": "zh_CN;IN;IN",
        "User-Agent": "OPPO/PAFM00/29/10.0/5.1/31001/10000/1.0.0",
        "ut": "TOKEN_"
    }, {
                                               "gameUsageRecordList":
                                                   [{
                                                       "pkg": 123456,
                                                       "lastUsageTime": 1624414692916,
                                                       "usageTimes": 1
                                                   }]
                                           }, "post",{"status_code":200,"status":0,"message":"success","data":"success"},"填充包名字段为数字进行推送")
