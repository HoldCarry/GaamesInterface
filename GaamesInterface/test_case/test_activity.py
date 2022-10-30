import pytest
from common.readexcel import get_book02
from common.request_method import request_model
from common import baseurl
from logs.logger import Log
import time
import os
import traceback


class Test_activity():

    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_activity", "gemes_activityh5"))
    def test_gemes_activityh5(self, path, param, headers, method, expect, case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            assert request_result[0] == expect["status_code"]
            assert request_result[1]["msg"] == expect["msg"]
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
            logger.info(f'请求到的信息是：{request_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))


    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_activity", "gemes_activityvdeo"))
    def test_gemes_activityvdeo(self, path, param, headers, method, expect, case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            assert request_result[0] == expect["status_code"]
            assert request_result[1]["msg"] == expect["msg"]
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
            logger.info(f'请求到的信息是：{request_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))