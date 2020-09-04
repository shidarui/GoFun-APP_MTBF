# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class ReservePage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    advInsurance = appConfig.get("ADVANCED.INSURANCE")
    copyAddress = appConfig.get("RESERVE.COPY.ADDRESS")
    shuoming = appConfig.get("RESERVE.SHUOMING")
    commit = appConfig.get("RESERVE.COMMIT")
    commit1 = appConfig.get("RESERVE.COMMIT1")
    yuyueTime_button = appConfig.get("SELECT.TIME.BUTTON")
    yuyueTime_confirm = appConfig.get("SELECT.TIME.SURE")
    timeOption = appConfig.get("TIME.OPTION")
        
    def __init__(self):
        pass

    #订单页-三者无忧
    def advInsurance_exist(self):
        return self.operater.exist(self.advInsurance, "advanced insurance")  

    #订单页-取车点非同取同还
    def copyAddress_exist(self):
        return self.operater.exist(self.copyAddress, "return park: copy take park")

    def copyAddress_click(self):
        self.operater.find_click_element(self.copyAddress, "return park: copy take park")

    #订单页-说明
    def shuoming_exist(self):
        return self.operater.exist(self.shuoming, "说明")

    def shuoming_click(self):
        self.operater.find_click_element(self.shuoming, "点击【说明】")
        
    #订单页-确认签署并下单
    def commit_exist(self):
        return self.operater.exist(self.commit, "确认签署并下单")

    def commit_click(self):
        self.operater.find_click_element(self.commit, "点击【确认签署并下单】")
        
    def commit1_exist(self):
        return self.operater.exist(self.commit1, "确认签署并下单")

    def commit1_click(self):
        self.operater.find_click_element(self.commit1, "点击【确认签署并下单】")
 
    #订单页-仍然预定 
    def reserveStill_exist(self):
        return self.operater.exist("本网点车辆只能还回本网点。是否仍要预定？", "仍然预定")
        
    #订单页-温馨提示框
    def warmTip_exist(self):
        return self.operater.exist("温馨提示", "warm tip")

    #订单页-车辆已被他人预订
    def reserveByOther_exist(self):
        return self.operater.exist("车辆已被他人预订，请选择其他车辆", "reserved by other")
        
    #订单页-成功预定
    def reserveSuc_exist(self):
        return self.operater.exist("已成功预定", "[Reserved success]")
        
    def noteTitle_exist(self):
        return self.operater.title_exist(text1="提示")

    #预约-时间
    def yuyueTime_button_click(self):
        self.operater.find_click_element(self.yuyueTime_button, "选择预约取车时间")
        
    #预约-时间确认
    def yuyueTime_confirm_click(self):
        self.operater.find_click_element(self.yuyueTime_confirm, "选择预约取车时间")
        
    def getTimeOption(self):
        return self.operater.find_element(self.timeOption,"预约时间：日期")
        
    def selectTime_exist(self):
        return self.operater.exist("请选择预约取车时间", "判断是否存在【请选择预约取车时间】")       
        
        
