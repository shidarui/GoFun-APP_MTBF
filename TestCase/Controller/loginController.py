# coding=utf-8
from TestCase.Pages import loginPage
from Lib.Util import log

class LoginController(loginPage.LoginPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'LoginController'
        self = loginPage.LoginPage()
        
    def login(self):
        self.mLog.log(self.mTag, "登录操作")
        self.unlogin_click()
        self.operater.sleep(4)
        self.username_input()
        self.operater.sleep(4)
        self.nextButton_click()
        self.operater.sleep(4)
        self.password_input()
        self.operater.sleep(4)


        
