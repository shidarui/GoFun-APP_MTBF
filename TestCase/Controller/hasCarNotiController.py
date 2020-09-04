# coding=utf-8
from TestCase.Pages import hasCarNotiPage
from Lib.Util import log

class HasCarNotiController(hasCarNotiPage.HasCarNotiPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'HasCarNotiController'

    def reminderSetting_open(self):
        self.mLog.log(self.mTag, "点击主页有车提醒，确认打开【设置有车提醒】页面")
        self.carReminder_click()
        self.operater.sleep(6)
        if self.carReminderTitle_exist():
            return True
        else:
            return False
            
    def repeatDate_open(self):
        self.mLog.log(self.mTag, "点击【重复】，确认打开【选择重复日期】")
        self.repeatDate_click()
        self.operater.sleep(6)
        if self.repeatDateTitle_exist():
            return True
        else:
            return False
            
    def startTime_open(self):
        self.mLog.log(self.mTag, "点击开始时间，确认打开【选择找车开始时间】")
        self.startTime_click()
        self.operater.sleep(6)
        if self.startTimeTitle_exist():
            return True
        else:
            return False
            
    def carType_open(self):
        self.mLog.log(self.mTag, "点击【全部车型】，确认打开【选择车型】")
        self.findCarByType_click()
        self.operater.sleep(4)
        if self.selectCarType_exist():
            return True
        else:
            return False
