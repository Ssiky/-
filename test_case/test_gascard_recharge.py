import unittest
import json
import requests
from lib import db
from lib import load_data
from conf import config
from lib.case_log import log_case_info

class TestRecharge(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sheet=load_data.get_sheet(config.data_file,"充值")
    def test_Recharge_sucess(self):
        case_data=load_data.get_case(self.sheet,"test_Recharge_sucess")
        url=case_data[2]
        data=json.loads(case_data[3])
        res=requests.post(url=url,json=data)
        log_case_info("test_Recharge_sucess",url,data,case_data[4],res.text)
        self.assertEqual(res.json()['msg'],"充值成功")
