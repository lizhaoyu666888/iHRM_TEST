import unittest
import logging

import pymysql
import requests

from api.department_api import DEP_API
from utils import assert_utils


class Test_DEP(unittest.TestCase):
    def setUp(self):
        self.dep_api = DEP_API()
    def tearDown(self):
        pass

    #登录,获取token
    def test01_login_success(self):
        global headers
        response = self.dep_api.dep_login("13800000002","123456")
        assert_utils(self,response,200,True,10000,"操作成功")
        token = "Bearer "+ response.json().get("data")
        headers = {"Content-Type":"application/json","Authorization":token}
        logging.info("请求头的数据为: {}".format(headers))

    #添加部门
    def test02_add_dep_success(self):
        response = self.dep_api.dep_add(headers,"我是传奇050部","HAHA050")
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("添加部门成功: {}".format(response.json()))

    #获取所有部门列表,数据库连接,获得添加部门id
    def test03_dep_list_success(self):
        global dep_id
        response = self.dep_api.dep_list(headers)
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("获取所有部门列表成功: {}".format(response.json()))
        conn = pymysql.connect(host="182.92.81.159",user="readuser",password="iHRM_user_2019",database="ihrm")
        cursor = conn.cursor()
        cursor.execute("select id from co_department where name = '我是传奇050部';")
        dep_id = str(cursor.fetchone()[0])
        logging.info("获取添加的部门id成功: {}".format(dep_id))
        conn.close()
        cursor.close()

    #查询添加的部门信息
    def test04_dep_get_success(self):
        response = self.dep_api.dep_get(dep_id,headers)
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("查询部门成功: {}".format(response.json()))

    #修改部门信息
    def test05_dep_updata_success(self):
        response = self.dep_api.dep_updata(dep_id,headers,"我是传奇-new50","HAHA-new50")
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("修改部门成功: {}".format(response.json()))

    #删除部门
    def test06_dep_del_success(self):
        response = self.dep_api.dep_del(dep_id,headers)
        assert_utils(self, response, 200, True, 10000, "操作成功")
        logging.info("删除部门成功: {}".format(response.json()))







