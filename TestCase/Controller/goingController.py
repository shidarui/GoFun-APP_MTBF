# coding=utf-8
from TestCase.Pages import goingPage, dialog
from Lib.Util import log

class GoingController(goingPage.GoingPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'GoingController'
        self.dialog = dialog.Dialog()
        
    def goging_car_health(self):
        if self.carHealth_exist():
            self.mLog.log(self.mTag, "车内清洁：点击【还不错】")
            try:
                self.healthClose_click()
            except Exception as err:
                self.mLog.log(self.mTag,"未找到车内卫生清洁关闭按钮，报错：%s" % err)
            self.operater.sleep(3)
        else:
            self.mLog.log(self.mTag,"无车内清洁")
 
    def firstExperienceTip_close(self):
        self.mLog.log(self.mTag,"首次体验提示检查")
        if self.dialog.firstExperience_exist():
            self.mLog.log(self.mTag,"您首次体验该车型：点击【继续用车】")
            self.dialog.cancel_click()
            self.operater.sleep(4)
            
    def changeCar_exit(self):
        self.mLog.log(self.mTag,"退出换车")
        self.mLog.log(self.mTag,"非A取A还，点击我知道了")
        self.dialog.dismiss_click()
        self.operater.sleep(4)
        #后退按钮
        self.dialog.backArrow_click()
        self.operater.sleep(4)
        if not self.tripGoing_exist():
            return False
        else:
            return True

    def soFar_close(self):
        self.mLog.log(self.mTag,"存在【车辆太远】提示框则关闭")
        if self.soFarClose_exist():
            self.soFarClose_click()
