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


class Test_get_explore():
	# @classmethod
	@pytest.mark.parametrize('path,param,headers,method,expect,case', get_book02("Games_explore", "explore"))
	def test_GamesExplore(self, path, param, headers, method, expect, case):
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


if __name__ == '__main__':
	Test_get_explore().test_GamesExplore('/games/dynamic/v1/explore', 'start=10000000&size=10',
	                                         {"Accept": "application/json", "locale": "zh_CN;IN;IN",
	                                          "User-Agent": "OPPO/PAFM00/29/10.0/5.1/31001/10000/1.0.0",
	                                          "id": "777777777777777"}, 'get')
# print(type(Test_get_explore().test_GamesExploreV1_1('/games/dynamic/v1/explore', 'start=0&size=10', '{"Accept": "application/json", "locale": "zh_CN;IN;IN","User-Agent": "OPPO/PAFM00/29/10.0/5.1/31001/10000/1.0.0", "id": "777777777777777"}', 'get')))
# pytest.main(["test_games_explore.py", "-s", "--alluredir", "../report/res"])
# pytest.main(Test_get_explore().test_GamesExploreV1_2())
