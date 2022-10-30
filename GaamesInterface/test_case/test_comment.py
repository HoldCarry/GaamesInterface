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


class Test_comment():

    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_comment", "community_vdo"))
    def test_community_vdo(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            # print(request_result)

            if expect["status_code"] == 200:
                assert request_result[0] == expect["status_code"]
                assert request_result[1]["msg"] == expect["msg"]
                assert request_result[1]["status"] == 0
            else:
                assert request_result[0] == expect["status_code"]
                assert expect["error"] == request_result[1]["error"]
            # return request_result
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



    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_comment", "community_h5"))
    def test_community_h5(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            # print(request_result)

            if expect["status_code"] == 200:
                assert request_result[0] == expect["status_code"]
                assert request_result[1]["msg"] == expect["msg"]
                assert request_result[1]["status"] == 0
            else:
                assert request_result[0] == expect["status_code"]
                assert expect["error"] == request_result[1]["error"]
            # return request_result
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


    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_comment", "commentlist_graphic"))
    def test_commentlist_graphic(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            request_result = request_model().get_request(method, URL, param, headers)
            # print(request_result)

            if expect["status_code"] == 200:
                assert request_result[0] == expect["status_code"]
                assert request_result[1]["msg"] == expect["msg"]
                assert request_result[1]["status"] == 0
            else:
                assert request_result[0] == expect["status_code"]
                assert expect["error"] == request_result[1]["error"]
            # return request_result
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



    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_submitcoment"))
    def test_gemes_submitcoment(self, path, headers, data, method, case, expect):
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
            if "data" in eval(requests_result[1]["data"]):
                if requests_result[1]["status"] == 0:
                    assert len(eval(requests_result[1]["data"])["data"]) > 10
                    assert type(int(eval(requests_result[1]["data"])["data"])) == int
                else:
                    assert eval(requests_result[1]["data"])["data"] == expect["data"]
            else:
                pass

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



    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_videocoment"))
    def test_gemes_videocoment(self, path, headers, data, method, case, expect):
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
            if "data" in requests_result[1]:
                if requests_result[1]["status"] == 0:
                    assert len(str(requests_result[1]["data"])) > 10
                    assert type(requests_result[1]["data"]) == int
                else:
                    assert requests_result[1]["data"] == expect["data"]
            else:
                pass
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


    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_leavesh5"))
    def test_gemes_leavesh5(self, path, headers, data, method, case, expect):
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
            if "data" in eval(requests_result[1]["data"]):
                if requests_result[1]["status"] == 0:
                    assert len(eval(requests_result[1]["data"])["data"]) > 10
                    assert type(int(eval(requests_result[1]["data"])["data"])) == int
                else:
                    assert eval(requests_result[1]["data"])["data"] == expect["data"]
            else:
                pass
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



    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_leavesvdeo"))
    def test_gemes_leavesvdeo(self, path, headers, data, method, case, expect):
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
            if "data" in requests_result[1]:
                if requests_result[1]["status"] == 0:
                    assert len(str(requests_result[1]["data"])) > 10
                    assert type(requests_result[1]["data"]) == int
                else:
                    assert requests_result[1]["data"] == expect["data"]
            else:
                pass

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



    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_threadup"))
    def test_gemes_threadup(self, path, headers, data, method, case, expect):
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
            if "data" in eval(requests_result[1]["data"]):
                if requests_result[1]["status"] == 0:
                    assert eval(requests_result[1]["data"])["data"] == expect["data"]
                else:
                    assert eval(requests_result[1]["data"])["data"] == expect["data"]
            else:
                pass
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



    @pytest.mark.parametrize('path,headers,data,method,expect,case', get_book02("Games_comment", "gemes_thread_up_video"))
    def test_gemes_thread_up_video(self, path, headers, data, method, case, expect):
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
            if "data" in requests_result[1]:
                if requests_result[1]["status"] == 0:
                    assert requests_result[1]["data"] == expect["data"]
                else:
                    assert requests_result[1]["data"] == expect["data"]
            else:
                pass
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



    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_comment", "gemes_comment_delete_video"))
    def test_vdocomment_deleted(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            if param["tid"] == "NA" and param["cid"] == "NA" and  case == "正常删除根评论":
                param["tid"] = front_comment.videothread_front_maincomment()[0]
                param["cid"] = json.loads(front_comment.videothread_front_maincomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA" and param["cid"] == "NA" and  case == "正常删除叶评论":
                param["tid"] = front_comment.videothread_front_maincomment()[0]
                param["cid"] = json.loads(front_comment.videothread_front_subcomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA" and param["cid"] == "NA":
                param["tid"] = front_comment.videothread_front_maincomment()[0]
                param["cid"] = json.loads(front_comment.videothread_front_maincomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA":
                param["tid"] = front_comment.videothread_front_maincomment()[0]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["cid"] == "NA":
                param["cid"] = json.loads(front_comment.videothread_front_subcomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            else:
                request_result = request_model().get_request(method, URL, param, headers)
            assert request_result[0] == expect["status_code"]
            assert request_result[1]["status"] == expect["status"]
            assert request_result[1]["msg"] == expect["msg"]

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


    @pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_comment", "gemes_comment_delete_graphic"))
    def test_graphiccomment_deleted(self, path,param,headers,method,expect,case):
        time_begin = time.time()
        logger = Log(os.path.basename(__file__)).set_logger()
        logger.info(f'.\n用例标题：{case}')
        try:
            URL = baseurl.Games_url + path
            if param["tid"] == "NA" and param["cid"] == "NA" and  case == "正常删除根评论":
                param["tid"] = front_comment.graphicthread_front_maincomment()[0]
                param["cid"] = json.loads(front_comment.graphicthread_front_maincomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA" and param["cid"] == "NA" and  case == "正常删除叶评论":
                param["tid"] = front_comment.graphicthread_front_subcomment()[0]
                param["cid"] = json.loads(front_comment.graphicthread_front_subcomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA" and param["cid"] == "NA":
                param["tid"] = front_comment.graphicthread_front_maincomment()[0]
                param["cid"] = json.loads(front_comment.graphicthread_front_maincomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["tid"] == "NA":
                param["tid"] = front_comment.graphicthread_front_maincomment()[0]
                request_result = request_model().get_request(method, URL, param, headers)
            elif param["cid"] == "NA":
                param["cid"] = json.loads(front_comment.graphicthread_front_subcomment()[1])["data"]
                request_result = request_model().get_request(method, URL, param, headers)
            else:
                request_result = request_model().get_request(method, URL, param, headers)
            assert request_result[0] == expect["status_code"]
            assert request_result[1]["status"] == expect["status"]
            assert request_result[1]["msg"] == expect["msg"]

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





if __name__ == '__main__':
    # print(Test_comment().test_send_maincomment())
    pytest.main(["test_comment.py", "-s", "--alluredir", "../report/res"])
