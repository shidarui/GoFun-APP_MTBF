# coding=utf-8
from TestCase.Pages import reservePage, dialog
from Lib.Util import log

class ReserveController(reservePage.ReservePage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'ReserveController'
        self.dialog = dialog.Dialog()
        
    def returnSameTak_set(self):
        if self.copyAddress_exist():
            self.mLog.log(self.mTag, "取车点非同取同还，设置还车点同取车点")
            self.copyAddress_click()
            self.operater.sleep(4)
            
    def car_reserve(self):
        self.mLog.log(self.mTag, "预定车辆")
        self.mLog.log(self.mTag, "判断是否存在费用说明")
        self.mLog.log(self.mTag, self.shuoming)
        if self.shuoming_exist():
            self.shuoming_click()
        self.mLog.log(self.mTag, "点击【确认签署并下单】")
        if self.commit_exist():
            self.mLog.log(self.mTag,"存在【确认签署并下单】按钮")
            self.commit_click()
        else:
            self.mLog.log(self.mTag,"存在【确认签署并下单】按钮1")
            self.commit1_click()
        self.operater.sleep(12)
        if self.dialog.confirm_exist():
            self.mLog.log(self.mTag,"点击【确认预定】")
            self.dialog.confirm_click()
            self.operater.sleep(3)
        if self.reserveStill_exist():
            self.mLog.log(self.mTag,"车辆只能还回本网点：点击【仍然预定】")
            self.dialog.confirm_click()
            self.operater.sleep(3)
            
    def warmTip_check(self):
        self.mLog.log(self.mTag, "检查温馨提示")
        if self.warmTip_exist():
            if self.dialog.warmTipContent_exist():
                # 判断是否存在提示：该网点只支持提前([0-9]{0,})分钟预约，若存在将无法继续测试
                import re
                content = self.dialog.getWarmTipContent()
                try:
                    bb = re.findall("该网点只支持提前([0-9]{0,})分钟预约", content)[0]
                    return False
                except:
                    pass
            self.mLog.log(self.mTag, "温馨提示：点击【我知道了】")
            self.dialog.confirm_click()
            self.operater.sleep(3)
            
    def reserveByOther_check(self):
        self.mLog.log(self.mTag, "检查车辆是否已被他人预订")
        if self.reserveByOther_exist():
            self.mLog.log(self.mTag,"已被他人预定：点击【我知道了】")
            if self.dialog.confirm_exist():
                self.dialog.confirm_click()
            return True
        else:
            return False
            
    def reserveSuc_check(self):
        self.mLog.log(self.mTag, "检查是否有成功预定提示")
        if self.reserveSuc_exist():
            self.mLog.log(self.mTag,"已成功预定：点击【我知道了】")
            self.dialog.confirm_click()
            self.sleep(3)
        else:
            self.mLog.log(self.mTag,"【已成功预定】未出现")
