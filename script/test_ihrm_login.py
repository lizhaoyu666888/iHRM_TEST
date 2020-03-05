import unittest
import logging
from parameterized import parameterized
import requests

from api.login_api import loginAPI
from utils import assert_utils, get_data


class Test_login(unittest.TestCase):
    def setUp(self):
        self.loginapi = loginAPI()
    def tearDown(self):
        pass

    def test01_login_success(self):
        response = self.loginapi.login("13800000002","123456")
        assert_utils(self,response,200,True,10000,"操作成功")
        logging.info("登录的结果为: {}".format(response.json()))

    def test02_login_no_user(self):
        response = self.loginapi.login("13900000002", "123456")
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test03_login_error_password(self):
        response = self.loginapi.login("13800000002", "1234567")
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test04_login_no_param(self):
        response = requests.post("http://182.92.81.159/api/sys/login")
        assert_utils(self, response, 200, False, 99999, "抱歉，系统繁忙，请稍后重试")
        logging.info("登录的结果为: {}".format(response.json()))

    def test05_login_empty_mobile(self):
        response = self.loginapi.login("", "1234567")
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test06_login_empty_password(self):
        response = self.loginapi.login("13800000002", "")
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test07_login_less_mobile_param(self):
        response = self.loginapi.login_param({"password":"123456"})
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test08_login_less_password_param(self):
        response = self.loginapi.login_param({"mobile": "13800000002"})
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    def test09_login_more_one_param(self):
        response = self.loginapi.login_param({"mobile":"13800000002","password": "123456","a":"1"})
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("登录的结果为: {}".format(response.json()))

    def test10_login_error_param(self):
        response = self.loginapi.login_param({"moble": "13800000002","password":"123456"})
        assert_utils(self, response, 200, False, 20001, "用户名或密码错误")
        logging.info("登录的结果为: {}".format(response.json()))

    data = get_data()
    @parameterized.expand(data)
    def test11_login_param(self,mobile,password,http_code,success,code,message):
        response = self.loginapi.login(mobile, password)
        assert_utils(self, response, http_code, success, code, message)
        logging.info("登录的结果为: {}".format(response.json()))
