# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class HasCarNotiPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    carReminder = appConfig.get("CAR.REMINDER")
    repeatDate = appConfig.get("CAR.REMINDER.REPEATDATE")
    startTime = appConfig.get("CAR.REMINDER.STARTTIME")
    selectTimeConf = appConfig.get("SELECT.TIME.SURE")
    findCarByType = appConfig.get("FIND.CAR.BYTYPE")

    def __init__(self):
        pass
        
    #主页-有车提醒     
    def carReminder_click(self):
        self.operater.find_click_element(self.carReminder, des="点击有车提醒按钮") 

    def carReminderTitle_exist(self):
        return self.operater.title_exist(text1="设置有车提醒")
        
    def repeatDate_click(self):
        self.operater.find_click_element(self.repeatDate, des="找车时间【重复】按钮") 

    def repeatDateTitle_exist(self):
        return self.operater.title_exist(text1="选择重复日期")
        
    def startTime_click(self):
        self.operater.find_click_element(self.startTime, des="点击【开始时间】") 
        
    def startTimeTitle_exist(self):
        return self.operater.title_exist(text1="选择找车开始时间")
        
    def endTimeTitle_exist(self):
        return self.operater.title_exist(text1="选择找车结束时间")
        
    def selectTimeConfirm_click(self):
        self.operater.find_click_element(self.selectTimeConf, des="点击【确认】") 
        
    def findCarByType_click(self):
        self.operater.find_click_element(self.findCarByType, des="点击【全部车型】") 
        
    def selectCarType_exist(self):
        return self.operater.exist("选择车型", des="选择车型")   
        
    def confirmText_exist(self):
        return self.operater.exist("确定", des="确定")   
        
    def confirmText_click(self):
        self.operater.find_click_element("确定", des="确定") 
