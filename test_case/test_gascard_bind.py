import unittest

import requests

from lib import db


class TestBlind(unittest.TestCase):
    def test_blind_sucess(self):
        url="http://115.28.108.130:8080/gasStation/process"
        data={
	            "dataSourceId": "bHRz",
	            "methodId": "01A",
	            "CardUser": {
	        	    "userName": "siky01",
	        	    "idType": "1",
	        	    "idNumber": "201907"
	            },
	    "CardInfo": {
		"cardNumber": "20190907"
	            }
            }
        res=requests.post(url=url,json=data)
        self.assertIn("成功",res.json()['msg'])
        self.assertTrue(db.check_userName("siky01"))

    def test_blind_wrong(self):
        url="http://115.28.108.130:8080/gasStation/process"
        data={
	            "dataSourceId": "bHRz",
	            "methodId": "01A",
	            "CardUser": {
	        	    "userName": "siky01",
	        	    "idType": "1",
	        	    "idNumber": ""
	            },
	    "CardInfo": {
		"cardNumber": "20190909"
	            }
            }
        res=requests.post(url=url,json=data)
        self.assertIn("证件号不能为空",res.json()['msg'])
        self.assertTrue(db.check_userName("siky01"))