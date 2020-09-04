# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class LoginPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    unlogin = appConfig.get("USER.UNLOGIN")
    username_box = appConfig.get("PHONE.NUM")
    username = appConfig.get("ACCOUNT.NUM")
    next_button = appConfig.get("LOGIN.NEXT")
    password_box = appConfig.get("LOGIN.CAPTCHA")
    password = appConfig.get("ACCOUNT.PASSWD")
    password = appConfig.get("ACCOUNT.PASSWD")
        
    def __init__(self):
        pass

    #登录-输入用户名
    def username_input(self):
        self.operater.set_text_by_id(self.username_box, self.username, "输入用户名")

    #登录-输入密码
    def password_input(self):
        self.operater.set_text_by_id(self.password_box, self.password, "输入用密码")

    #登录-next按钮
    def nextButton_click(self):
        self.operater.find_click_element(self.next_button, des="点击next按钮")
 
    #登录-“未登录”状态 
    def unlogin_exist(self):
        return self.operater.exist("登录去！", "unlogin")
        
    def unlogin_click(self):
        self.operater.find_click_element(self.unlogin, des="点击登录按钮")
