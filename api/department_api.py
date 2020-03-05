import requests


class DEP_API:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.dep_list_url = "http://182.92.81.159/api/company/department"
        self.dep_updata_url = "http://182.92.81.159/api/company/department/"
    def dep_login(self,mobile,password):
        return requests.post(self.login_url,json={"mobile":mobile,"password":password})

    def dep_list(self,headers):
        return requests.get(self.dep_list_url,headers=headers)

    def dep_add(self,headers,name,code):
        return requests.post(self.dep_list_url,headers = headers,json={"name":name,"code":code})

    def dep_get(self,dep_id,headers):
        return requests.get(self.dep_updata_url+dep_id,headers=headers)

    def dep_updata(self,dep_id,headers,name,code):
        return requests.put(self.dep_updata_url+dep_id,headers=headers,json={"name":name,"code":code})

    def dep_del(self,dep_id,headers):
        return requests.delete(self.dep_updata_url+dep_id,headers=headers)