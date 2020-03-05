import os
import unittest
from HTMLTestRunner_PY3 import HTMLTestRunner
import time

from script.test_ihrm_department import Test_DEP
from script.test_ihrm_login import Test_login
from script.test_ihrm_member import Test_Ihrm_Member

Base_Dir = os.path.dirname(os.path.abspath(__file__))
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(Test_login))
suite.addTest(unittest.makeSuite(Test_DEP))


# suite = unittest.TestLoader().discover(Base_Dir+"/script/",pattern="test*.py")
# filename = Base_Dir+"/report/report {}.html".format(time.strftime("%Y%m%d %H%M%S"))
# jenkins中时间戳没办法指定,所以改成固定的文件名
filename = Base_Dir+"/report/report.html"

with open(filename,"wb") as f:
    runner = HTMLTestRunner(f,verbosity=2,title="iHRM接口自动化测试",description="Win10")
    runner.run(suite)