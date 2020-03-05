import requests


class loginAPI:
    def __init__(self):
        self.login_url = "http://182.92.81.159/api/sys/login"

    def login(self,mobile,password):
        return requests.post(self.login_url,json={"mobile":mobile,"password":password})

    def login_param(self,jsonData):
        return  requests.post(self.login_url,json=jsonData)