import pytest
from common.readexcel import get_book02
from common.request_method import request_model
import json
from common import baseurl
import requests
from logs.logger import Log
import traceback
import time
import os
from Front_lib import front_comment
import time
from common import random_data

class Test_AppComment():

    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_AppComment", "AppMaincommentList"))
    def test_AppMaincommentList(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            assert request_result[0] == expect["status_code"]
            assert request_result[1]["status"] == expect["status"]
            assert request_result[1]["msg"] == expect["msg"]
            assert len(request_result[1]["data"]) == len(expect["data"])
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
        finally:
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求参数：{param}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{request_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))


    @pytest.mark.parametrize('path,headers,data,method,expect,case',
                             get_book02("Games_AppComment", "AppMaincommentPost"))
    def test_AppMaincommentPost(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            while type(data["pkgName"]) == str:
                data["pkgName"] = random_data.random_str()
                break
            while type(data["pkgName"]) == int:
                data["pkgName"] = random_data.random_int()
                break
            requests_result = request_model().get_request(method, URL, data, headers)
            time.sleep(1)
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            if type(requests_result[1]["data"]) == int:
                assert type(requests_result[1]["data"]) == int
                assert requests_result[1]["msg"] == expect["msg"]
            else:
                assert requests_result[1]["data"] == expect["data"]
                assert requests_result[1]["msg"] == expect["msg"]

        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            while type(requests_result[1]["data"]) == int:
                rid = requests_result[1]["data"]
                delede_result = front_comment.app_front_deletecomment(rid)
                break
            logger.info(f'请求到的rid是：{rid}')
            logger.info(f'删除结果是：{delede_result}')
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))



    @pytest.mark.parametrize('path,headers,data,method,expect,case',
                             get_book02("Games_AppComment", "AppMaincommentPost_Second"))
    def test_AppMaincommentPost_Second(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            first_comment = front_comment.app_front_postmaincomment()
            time.sleep(1)
            requests_result = request_model().get_request(method, URL, data, headers)
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]

        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            while type(first_comment) == int:
                deleted_result = front_comment.app_front_deletecomment(first_comment)
                break
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info(f'第一次请求到的评论id是：{first_comment}')
            logger.info(f'删除结果是：{deleted_result}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))



    @pytest.mark.parametrize('path,headers,data,method,expect,case',
                             get_book02("Games_AppComment", "AppsubcommentPost"))
    def test_AppsubcommentPost(self, path, headers, data, method, case, expect):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            maincommentid = front_comment.app_front_postmaincomment()
            time.sleep(1)
            if data["parentId"] == "rootId":
                data["rootId"] = maincommentid
                data["parentId"] = maincommentid
            elif data["parentId"] == "parentId":
                data["rootId"] = maincommentid
                subcommentid = front_comment.app_front_postsubcomment(maincommentid,maincommentid)
                time.sleep(1)
                data["parentId"] = subcommentid
                deleted_result02 = front_comment.app_front_deletecomment(subcommentid)
                logger.info(f'删除子评论结果是：{deleted_result02}')
            else:
                pass
            requests_result = request_model().get_request(method, URL, data, headers)
            assert requests_result[0] == expect["status_code"]
            assert requests_result[1]["status"] == expect["status"]
            assert requests_result[1]["msg"] == expect["msg"]
        except Exception as error:
            logger.error(f'报错，错误信息是：{traceback.format_exc()}')
            raise error
            # 返回或者记录结果
        finally:
            deleted_result01 = front_comment.app_front_deletecomment(maincommentid)
            logger.info(f'请求接口：{path}')
            logger.info(f'请求到头：{headers}')
            logger.info(f'请求body：{data}')
            logger.info(f'请求的期望结果：{expect}')
            logger.info(f'请求到的信息是：{requests_result}')
            logger.info(f'删除主评论结果是：{deleted_result01}')
            logger.info('共耗时 {0} 秒.\n'.format(time.time() - time_begin))

