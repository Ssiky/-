import unittest
from conf import config
from lib.HTMLTestRunner_PY3 import HTMLTestRunner
from test_case.test_gascard_reg import TestReg
from test_case.test_gascard_recharge import TestRecharge

suite=unittest.TestSuite()
suite.addTests([TestReg('test_reg_success'),TestReg('test_reg_wrong'),TestRecharge('test_Recharge_sucess')])
# unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == "__main__":
    config.logging.info("测试开始"+"="*50)
    with open(config.report_file,'wb') as f:
        HTMLTestRunner(stream=f,title="加油卡测试报告",description="测试报告").run(suite)

    config.logging.info("测试结束"+"="*50)