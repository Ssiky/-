import unittest

# suite=unittest.TestSuite()
# suite.addTests([test_gascard_reg.TestReg('test_reg_success'),test_gascard_reg.TestReg('test_reg_wrong'),test_gascard_recharge.TestRecharge('test_Recharge_sucess')])

# # 遍历所有用例：
# suite=unittest.defaultTestLoader.discover('.')
# # 添加模块
# loader=unittest.TestLoader()
# suite=loader.loadTestsFromModule(test_gascard_reg)
# # 添加测试类中的测试用例
# loader=unittest.TestLoader()
# suite=loader.loadTestsFromTestCase(test_gascard_reg.TestReg)
# suite=loader.loadTestsFromTestCase(test_gascard_recharge.TestRecharge)
# # 按名称添加
# loader=unittest.TestLoader()
# suite=loader.loadTestsFromName("test_gascard_reg.TestReg.test_reg_success")



if __name__=='__main__':
    unittest.TextTestRunner(verbosity=2).run(suite)