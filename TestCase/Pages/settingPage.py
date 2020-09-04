# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class SettingPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    switchButton = appConfig.get("SWITCH.BUTTON")
    agree = appConfig.get("READ.AGREE")
        
    def __init__(self):
        pass

    #个人中心-设置-接近还车网点提示
    def switchButton_exist(self):
        return self.operater.exist(self.switchButton, "存在【接近还车网点提示】")
        
    def switchButton_click(self):
        self.operater.find_click_element(self.switchButton, des="点击【接近还车网点提示】")
 
    #个人中心-设置- 给GoFun好评
    def gofunValuation_click(self):
        self.operater.find_click_element("给GoFun好评", des="给GoFun好评")
        
    def appStore_exist(self):
        return self.operater.xml_pic_pos("appstore_gofun")
        
    def gofunValuation_exist(self):
        return self.operater.exist("给GoFun好评", "给GoFun好评")

    #个人中心-设置- 关于我们
    def aboutUs_click(self):
        self.operater.find_click_element("关于我们", des="关于我们")

    #个人中心-设置- 微信公众号
    def weChatSubscription_exist(self):
        return self.operater.exist("微信公众号", "微信公众号")

    #个人中心-设置- 退出登录
    def exitAccount_exist(self):
        return self.operater.exist("退出登录", "退出登录")
 
    #个人中心-设置- 注销账户 
    def logoff_click(self):
        self.operater.find_click_element("注销账户", des="注销账户")
        
    def logoff_exist(self):
        return self.operater.exist("注销账户", "注销账户")
        
    def logoffClaim_exist(self):
        return self.operater.exist("账户注销声明", "账户注销声明")  
        
    def readAndAgree_click(self):
        self.operater.find_click_element(self.agree, des="点击【我已阅读并同意】")

    #个人中心-设置- 法律条款与平台规则
    def legalProvision_click(self):
        self.operater.find_click_element("法律条款与平台规则",  des="点击【法律条款与平台规则】")  
        
    def legalProvTitle_exist(self):
        #return self.operater.title_exist(text1="法律条款与平台规则")
        return self.operater.title_exist(text1="平台协议与规则")         
  
  
        
