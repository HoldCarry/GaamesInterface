import pytest




if __name__ == "__main__":
    # 执行test_case目录下的所有用例生成测试报告
    pytest.main(['../test_case/test_AppComment.py','--html=../report/Games_explore.html'])
