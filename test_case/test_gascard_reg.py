import unittest
import requests
import json
from lib import db
from lib import load_data
from lib.case_log import log_case_info
from conf import config


class TestReg(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.sheet=load_data.get_sheet(config.data_file,"添加加油卡")
    def test_reg_success(self):
        if db.check_cardNumber("20190101"):
            db.del_cardNumber("20190101")
        case_data=load_data.get_case(self.sheet,"test_reg_success")
        url=case_data[2]
        try:
            data=json.loads(case_data[3])
            expected_res=json.loads(case_data[4])
        except json.decoder.JSONDecodeError as e:
            print("用例数据不是合法的json")
        res=requests.post(url=url,json=data)
        log_case_info("test_reg_success",url,data,case_data[4],res.text)
        self.assertIn("成功",res.json()["msg"])
        self.assertEqual(res.json()["code"],200)
        self.assertTrue(db.check_cardNumber("20190101"))
        try:
            res_json =res.json()
        except json.decoder.JSONDecodeError as e:
            print("返回结果不是json格式")
        # self.assertDictEqual(expected_res,res.json())
        db.del_cardNumber("20190101")

    def test_reg_wrong(self):
        case_data=load_data.get_case(self.sheet,"test_reg_wrong")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,json=data)
        log_case_info("test_reg_wrong",url,data,case_data[4],res.text)
        self.assertIn("不能为空",res.json()["msg"])
