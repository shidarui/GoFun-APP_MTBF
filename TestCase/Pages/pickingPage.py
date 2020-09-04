# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class PickingPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    freeReturn = appConfig.get("GOING.RETURN.CAR")
    pickingVoice = appConfig.get("PICKING.VOICE.FIND")
    pickFaceRec = appConfig.get("PICKING.FACE.RECOGNITION")
    useCar = appConfig.get("PICKING.USE.CAR")
    specificReason = appConfig.get("SPECIFIC.REASON")
    commitButton = appConfig.get("COMMIT.BUTTON")
    reasonArrow = appConfig.get("REASON.ARROW")
    nevigate = appConfig.get("NAVIGATION.BUTTON")
    nevLogout = appConfig.get("NAVIGATION.LOGOUT")
    nevLogoutConfirm = appConfig.get("NAVIGATION.LOGOUT.SURE")
    titleId = appConfig.get("NATIVE.TITLE.TRIP")
    
    def __init__(self):
        pass
        
    def freeReturn_exist(self):
        return self.operater.exist("免费还车", "存在【免费还车】")

    #取车页面
    def pickingCar_exist(self):
        return self.operater.exist("取车中", "[Title] Picking-up car")

    #取车页面-声音寻车
    def pickingVoice_click(self):
        self.operater.find_click_element(self.pickingVoice, des="[voice find car]")

    #人脸识别
    def faceRecButton_exist(self):
        return self.operater.exist(self.pickFaceRec, "取车中：人脸识别按钮")
        
    #取车页面-用车
    def useCar_click(self):
        self.operater.find_click_element(self.useCar, des="user car")
        
    #车况上报-上报完毕
    def reportFinish_exist(self):
        return self.operater.exist("上报完毕", des="上报完毕")    

    def reportFinish_click(self):
        self.operater.find_click_element("上报完毕", des="上报完毕")    

    #取消订单
    def cancleOrder_exist(self):
        return self.operater.exist("取消订单", "取消订单")
        
    def cancleOrder_click(self):
        self.operater.find_click_element("取消订单", "取消订单") 

    def cancleConfirm_exist(self):
        return self.operater.exist("确定取消本次订单？", "confirm cancel oder?")

    def cancleOrderSuc_exist(self):
        return self.operater.exist("订单已取消", "text：【订单已取消】")

    #取消订单具体原因
    def specificReason_exist(self):
        return self.operater.exist(self.specificReason, "检测是否存在【具体原因】")
        
    def specificReason_click(self):
        self.operater.find_click_element(self.specificReason, "点击【具体原因】") 
        
    def commitButton_click(self):
        self.operater.find_click_element(self.commitButton, "点击【提交】按钮") 
        
    def reasonArrow_exist(self):
        return self.operater.exist(self.reasonArrow, "检测是否存在【原因箭头】")
        
    def reasonArrow_click(self):
        self.operater.find_click_element(self.reasonArrow, "点击【原因箭头】") 

    #导航
    def nevigate_click(self):
        self.operater.find_click_element(self.nevigate, "点击【取车界面导航】按钮")     
    
    def nevigate1_exist(self):
        return self.operater.exist('站内导航', '判断是否存在【站内导航】')
        
    def nevigate1_click(self):
        self.operater.find_click_element('站内导航', '点击【站内导航】') 
 
    def builtInNevigate_exist(self):
        return self.operater.exist('内置导航', '判断是否存在【内置导航】')
        
    def builtInNevigate_click(self):
        self.operater.find_click_element('内置导航', '点击【内置导航】') 
        
    def nevLogout_click(self):
        self.operater.find_click_element(self.nevLogout, '点击导航界面退出按钮') 
        
    def nevLogoutConfirm_click(self):
        self.operater.find_click_element(self.nevLogoutConfirm,  '点击导航界面退出导航按钮')

    #结算订单
    def settleOrder_exist(self):
        return self.operater.exist("结算订单", "[Picking-up] [Settlement]")
        
    def settleOrder_click(self):
        self.operater.find_click_element("结算订单", "[Picking-up] [Settlement]") 

    def settleOrderComfirm_exist(self):
        return self.operater.exist("确定结算订单?", "Dialog [Confirm cancel order?]")
