# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class CustomServicePage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
        
    def __init__(self):
        pass

    #我的客服
    def myServiceTitle_exist(self):
        return self.operater.title_exist(text1="我的客服")
 
    #我的客服-全部行程 
    def allTrip_exist(self):
        return self.operater.exist("全部行程", "存在【全部行程】")  
        
    def allTrip_click(self):
        self.operater.find_click_element("全部行程", des="点击【全部行程】")
        
    def allTripTitle_exist(self):
        return self.operater.title_exist(text1="全部行程")

    #我的客服-投诉
    def complain_exist(self):
        return self.operater.exist("投诉", "存在【投诉】")  
        
    def complain_click(self):
        self.operater.find_click_element("投诉", des="点击【投诉】")
        
    def processTitle_exist(self):
        return self.operater.title_exist(text1="处理进度")

    #我的客服-联系客服
    def contactService_click(self):
        self.operater.find_click_element("联系客服", des="点击【联系客服】")
        
    def onlineService_click(self):
        self.operater.find_click_element("极速在线客服", des="点击【极速在线客服】")

    def callService_click(self):
        self.operater.find_click_element("致电热线客服", des="点击【致电热线客服】")

    def userPrivatePro_exist(self):
        return self.operater.exist("用户隐私协议", "存在【用户隐私协议】") 
       
    def userPrivateAgree_click(self):
        self.operater.find_click_element("同意授权并继续 ", des="点击【同意授权并继续 】")     

    #极速在线客服打开页面
    def speed_csTitle_exist(self):
        return self.operater.title_exist(text1="小Fun")
 
    #致电热线客服打开页面
    def callServiceTitle_exist(self):
        return self.operater.title_exist(text1="选择电话")
        
    def insurance_record(self):
        return self.operater.find_element("出险记录", des="出险记录") 
