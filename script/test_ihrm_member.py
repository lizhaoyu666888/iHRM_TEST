import unittest,logging
from parameterized import parameterized
import pymysql
import requests

from api.member_api import memberAPI
from utils import add_member_data, assert_utils, get_member_data, updata_member_data, DBUtils, del_member_data


class Test_Ihrm_Member(unittest.TestCase):

    def setUp(self):
        self.memberapi = memberAPI()

    def tearDown(self):
        pass


    def test01_login_success(self):
        global headers
        response_login = self.memberapi.login("13800000002", "123456")
        logging.info("登录结果为: {}".format(response_login.json()))
        token = "Bearer " + response_login.json().get("data")
        logging.info("取出的令牌为：{}".format(token))
        headers = {"Content-Type": "application/json", "Authorization": token}
        logging.info("员工模块请求头为：{}".format(headers))

    add_data = add_member_data()
    @parameterized.expand(add_data)
    def test02_add_member_success(self,username,mobile,http_code,success,code,message):
        global member_id
        response_add_member = self.memberapi.add_member(headers, username, mobile)
        logging.info("添加员工的结果为: {}".format(response_add_member.json()))
        member_id = response_add_member.json().get("data").get("id")
        logging.info("添加的员工id为: {}".format(member_id))
        assert_utils(self, response_add_member, http_code, success, code, message)

    get_data = get_member_data()
    @parameterized.expand(get_data)
    def test03_get_member_success(self,http_code, success, code, message):
        response_get_member = self.memberapi.get_member(member_id, headers)
        logging.info("查询的员工信息为: {}".format(response_get_member.json()))
        assert_utils(self, response_get_member, http_code, success, code, message)

    updata_data = updata_member_data()
    @parameterized.expand(updata_data)
    def test04_updata_member_success(self,new_name,http_code,success,code,message):
        response_updata_member = self.memberapi.updata_member(member_id, new_name, headers)
        logging.info("修改的员工信息为: {}".format(response_updata_member.json()))
        assert_utils(self, response_updata_member, http_code, success, code, message)
        with DBUtils() as db:
            db.execute("select username from bs_user where id = {}".format(member_id))
            result = db.fetchone()[0]
            self.assertEqual(new_name,result)
            logging.info("数据库查询的结果为: {}".format(result))

    del_data = del_member_data()
    @parameterized.expand(del_data)
    def test05_del_mumber_success(self,http_code,success,code,message):
        response_del_member = self.memberapi.del_member(member_id, headers)
        logging.info("删除的员工信息为: {}".format(response_del_member.json()))
        assert_utils(self, response_del_member, http_code, success, code, message)
