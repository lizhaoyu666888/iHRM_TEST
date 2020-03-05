import json
import os

import pymysql


def assert_utils(self,response,status_code,success,code,message):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))

# 封装数据库
class DBUtils:

    # 初始化类时，要运行的代码
    def __init__(self, host="182.92.81.159", user='readuser', password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # 代表使用with语法时，进入函数时会先运行enter的代码
    def __enter__(self):
        # 与数据库建立连接
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        # 获取游标
        self.cusor = self.conn.cursor()
        return self.cusor

    # 代表退出with语句块时，会运行exit的代码
    def __exit__(self, exc_type, exc_val, exc_tb):
        # 关闭游标和关闭连接
        if self.cusor:
            self.cusor.close()
        if self.conn:
            self.conn.close()

def get_data():
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    filename = Base_Dir + "/data/login.json"
    list1 = []
    with open(filename,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        for i in jsonData:
            mobile = i.get("mobile")
            password = i.get("password")
            http_code = i.get("http_code")
            success = i.get("success")
            code = i.get("code")
            message = i.get("message")
            list1.append((mobile,password,http_code,success,code,message))
    return list1


def add_member_data():
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    filename = Base_Dir + "/data/member.json"
    add_list = []
    with open(filename,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        add_data = jsonData.get("add_member")
        username = add_data.get("username")
        mobile = add_data.get("mobile")
        http_code = add_data.get("http_code")
        success = add_data.get("success")
        code = add_data.get("code")
        message = add_data.get("message")
        add_list.append((username,mobile,http_code,success,code,message))
    return add_list

def get_member_data():
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    filename = Base_Dir + "/data/member.json"
    get_list = []
    with open(filename,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        get_data = jsonData.get("get_member")
        http_code = get_data.get("http_code")
        success = get_data.get("success")
        code = get_data.get("code")
        message = get_data.get("message")
        get_list.append((http_code,success,code,message))
    return get_list

def updata_member_data():
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    filename = Base_Dir + "/data/member.json"
    updata_list = []
    with open(filename,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        updata_data = jsonData.get("updata_member")
        new_name = updata_data.get("new_name")
        http_code = updata_data.get("http_code")
        success = updata_data.get("success")
        code = updata_data.get("code")
        message = updata_data.get("message")
        updata_list.append((new_name,http_code,success,code,message))
    return updata_list


def del_member_data():
    Base_Dir = os.path.dirname(os.path.abspath(__file__))
    filename = Base_Dir + "/data/member.json"
    del_list = []
    with open(filename,"r",encoding="utf-8") as f:
        jsonData = json.load(f)
        del_data = jsonData.get("del_member")
        http_code = del_data.get("http_code")
        success = del_data.get("success")
        code = del_data.get("code")
        message = del_data.get("message")
        del_list.append((http_code,success,code,message))
    return del_list


if __name__ == '__main__':
    add_member_data()




