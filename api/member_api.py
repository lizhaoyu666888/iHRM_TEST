import requests


class memberAPI:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"
        self.add_url = "http://182.92.81.159/api/sys/user"
        self.get_url = "http://182.92.81.159/api/sys/user/"
        self.updata_url = "http://182.92.81.159/api/sys/user/"
        self.del_url = "http://182.92.81.159/api/sys/user/"

    def login(self,mobile,password):
        jsonData = {"mobile": mobile, "password": password}
        return requests.post(self.login_url,json=jsonData)

    def add_member(self,headers,username,mobile):
        jsonData = {"username": username,
                   "mobile": mobile,
                   "timeOfEntry": "2020-02-01",
                   "formOfEmployment": 1,
                   "departmentName": "酱油2部",
                   "departmentId": "1205026005332635648",
                   "correctionTime": "2020-02-03T16:00:00.000Z"}
        return requests.post(self.add_url,json=jsonData,headers=headers)

    def get_member(self,member_id,headers):
        return requests.get(self.get_url+member_id,headers=headers)

    def updata_member(self,member_id,username,headers):
        jsonData = {"username": username}
        return requests.put(self.updata_url+member_id,json=jsonData, headers=headers)

    def del_member(self,member_id,headers):

        return requests.delete(self.del_url+member_id, headers=headers)