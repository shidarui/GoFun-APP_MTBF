# coding=utf-8
from TestCase.Pages import customServicePage,  homePage
from Lib.Util import log

class CustomServiceController(customServicePage.CustomServicePage):    
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'CustomServiceController'
        self.homePage = homePage.HomePage()
        
    def allTrip_open(self):
        self.mLog.log(self.mTag, "点击【行程】，确认正常打开")
        self.allTrip_click()
        self.operater.sleep(10)
        if self.allTripTitle_exist():
            return True
        else:
            return False
            
    def myService_open(self):
        self.mLog.log(self.mTag, "点击【客服】，确认正常打开")
        self.homePage.customService_click()
        self.operater.sleep(10)
        if self.myServiceTitle_exist():
            return True
        else:
            return False
            
    def complain_open(self):
        self.mLog.log(self.mTag, "点击【投诉】，确认正常打开")
        self.complain_click()
        self.operater.sleep(10)
        if self.processTitle_exist():
            return True
        else:
            return False

    def speed_cs_open(self):  
        self.mLog.log(self.mTag, "点击【联系客服】，确认正常打开")
        self.contactService_click()
        self.operater.sleep(5)
        self.mLog.log(self.mTag, "点击【急速在线客服】，确认正常打开")
        self.onlineService_click()
        self.operater.sleep(5)
        self.mLog.log(self.mTag, "判断是否存在隐私协议")
        if self.userPrivatePro_exist():
            self.userPrivateAgree_click()
        self.mLog.log(self.mTag, "确认正常打开小Fun")
        if self.speed_csTitle_exist():
            return True
        else:
            return False
            
    def callService_open(self):  
        self.mLog.log(self.mTag, "点击【联系客服】，确认正常打开")
        self.contactService_click()
        self.operater.sleep(5)
        self.mLog.log(self.mTag, "点击【致电热线客服】，确认正常打开")
        self.callService_click()
        self.operater.sleep(5)
        self.mLog.log(self.mTag, "确认正常打开热线客服")
        if self.callServiceTitle_exist():
            return True
        else:
            return False
            
    def autoService_traversal(self):
        self.mLog.log(self.mTag, "遍历自助服务")
        auto_service_list = self.appConfig.get_list("SERVICE.PROBLEM")
        for index, item in enumerate(auto_service_list):
            if self.operater.exist(item,"判断是否存在：%s" % item):
                self.mLog.log(self.mTag, "客服主页，点击【%s】" % item)
                self.operater.find_click_element(item, item)
                self.operater.sleep(10)
                if self.operater.exist(item, item) and self.myServiceTitle_exist():
                    [device_width, device_height] = self.operater.appConfig.get_x_y("DEVICE.SIZE")
                    [top, right, bottom, left] = self.insurance_record().get_bounds()
                    y1 = int(top * device_height)
                    x1 = int(0.8 * device_width)
                    x2 = int(0.28 * device_width)
                    self.operater.swipe([x1, y1], [x2, y1], [device_width, device_height] )
                    self.operater.sleep(3)
                    self.operater.find_click_element(item, item)
                    self.operater.sleep(10)
                if item == "申请发票":
                    title_name = "发票与报销"
                elif item == "新手引导":
                    title_name = "新手指南"
                else:
                    title_name = item
                if not self.operater.title_exist(text1=title_name) and title_name != "推荐建点":
                    self.operater.fail(u"Go to [%s] fail" % item)
                if item == "推荐建点":
                    self.operater.sleep(10)
                    self.operater.back()
                else:
                    self.operater.t_keyevent("BACK")
                self.operater.sleep(10)
                if not self.myServiceTitle_exist():
                    self.operater.fail("Back to [Service] fail")
                self.mLog.log(self.mTag, "点击back，返回【我的客服】主页")
            else:
                self.mLog.log(self.mTag, "客服主页，未找到【%s】" % item)
