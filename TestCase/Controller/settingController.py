# coding=utf-8
from TestCase.Pages import settingPage, personalCenterPage
from Lib.Util import log

class SettingController(settingPage.SettingPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'SettingController'
        self.perspage = personalCenterPage.PersonalCenterPage()
        
    def switchButton_switch(self, times):
        self.mLog.log(self.mTag, "点击【接近还车网点提示】，确认正常开关")
        for i in range(int(times)):
            self.switchButton_click()
            self.operater.sleep(3)
        
    def appStore_open(self):
        self.mLog.log(self.mTag, "点击【给GoFun好评】，确认正常打开")
        self.gofunValuation_click()
        self.operater.sleep(4)
        if self.appStore_exist():
            return True
        else:
            return False
            
    def backTo_gofunGood(self):
        self.mLog.log(self.mTag, "从应用市场返回【设置】，确认返回正常")
        for i in range(5):
            self.operater.back()
            if self.gofunValuation_exist():
                return True
            self.sleep(2)
        return False
        
    def aboutUs_open(self):
        self.mLog.log(self.mTag, "点击【关于我们】，确认正常打开")
        self.aboutUs_click()
        self.operater.sleep(4)
        if self.weChatSubscription_exist():
            return True
        else:
            return False

    def logoff_open(self):
        self.mLog.log(self.mTag, "点击【注销账户】，确认正常打开")
        self.logoff_click()
        self.operater.sleep(4)
        if self.logoffClaim_exist():
            self.readAndAgree_click()
        if self.logoff_exist():
            return True
        else:
            return False

    def legalProvision_open(self):
        self.mLog.log(self.mTag, "点击【法律条款与平台规则】，确认正常打开")
        self.legalProvision_click()
        self.operater.sleep(8)
        if self.legalProvTitle_exist():
            return True
        else:
            return False

    def backTo_setting(self):
        self.mLog.log(self.mTag, "返回【设置】，确认返回正常")
        self.operater.t_keyevent("BACK")
        self.operater.sleep(2)
        if self.perspage.settingTitle_exist() or self.exitAccount_exist():
            return True
        else:
            return False
