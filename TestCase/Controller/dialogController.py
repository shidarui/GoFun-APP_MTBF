# coding=utf-8
from TestCase.Pages import dialog
from Lib.Util import log

class DialogController(dialog.Dialog):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'DialogController'
        self = dialog.Dialog()
        
    def faceRec_skip(self):
        self.mLog.log(self.mTag, "跳过面部识别")
        if self.faceRec_exist():
            self.mLog.log(self.mTag, "请完成面部识别：点击【稍后再说】")
            self.later_click()
            self.operater.sleep(2)

    def takeCarOverTime_close(self):
        self.mLog.log(self.mTag, "关闭【取车超时】提示")
        if self.takeCarOverTime_exist():
            self.mLog.log(self.mTag, "上次订单未完成，取车超时已结单，点击【我知道了】")
            self.confirm_click()
            self.operater.sleep(2)

    def freeReturnTip_close(self):
        self.mLog.log(self.mTag, "检查是否存在免费还车提示，存在则点击确认关闭")
        if not self.freeReturnTitle_exist():
            return False
        self.mLog.log(self.mTag, "免费还车？：点击【确认免费还车】")
        self.confirm_click()
        return True

    def finishBelowItem(self):
        self.mLog.log(self.mTag, "请完成以下事项")
        if self.finishBelowItem_exist():
            self.mLog.log(self.mTag, "请完成以下事项：点击【确认】")
            self.confirm_click()
            self.operater.sleep(12)
            
    def confirmBeforeReturn(self):
        self.mLog.log(self.mTag, "锁车前请确认以下事项")
        if self.confirmBeforeReturn_exist():
            self.mLog.log(self.mTag, "结算弹窗：锁车并结算")
            self.closeDoor_click()
            self.operater.sleep(8)
            
    def confirmReturn(self):
        self.mLog.log(self.mTag, "确认还车")
        if self.confirmReturn_exist():
            self.mLog.log(self.mTag, "确认还车：点击【还车】")
            self.confirm_click()
            self.operater.sleep(8)
            
    def dialog_traversal_close(self, dialogList):
        self.mLog.log(self.mTag, "关闭所有提示框")
        for dialog_title in dialogList:
            if self.dialog_exist(dialog_title[0], dialog_title[1]):
                self.mLog.log(self.mTag, dialog_title[0] + "，点击【确认】")
                self.confirm_click()
                self.operater.sleep(4)
            else:
                self.operater.sleep(2)
