# coding=utf-8
from TestCase.Pages import dialog, pickingPage
from Lib.Util import log

class PickingController(pickingPage.PickingPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'PickingController'
        self.dialog = dialog.Dialog()   
        
    def cancle_order(self):
        self.mLog.log(self.mTag, "如果存在取消订单则点击")
        if self.cancleOrder_exist():
            self.mLog.log(self.mTag, "点击【取消订单】")
            self.cancleOrder_click()
            return True
        else:
            return False
 
    def cancelOrder_confirm(self):
        self.mLog.log(self.mTag, "检查是否存在确认提示")
        self.operater.clever_wait("确定取消本次订单？")
        if not self.cancleConfirm_exist():
            return False
        self.mLog.log(self.mTag, "确定取消本次行程？：点击【确定】")
        self.dialog.confirm_click()
        self.operater.sleep(4)
        return True

    def specificReason_submit(self):
        self.mLog.log(self.mTag, "提交取消订单具体原因")
        self.specificReason_click()
        self.operater.sleep(4)
        self.commitButton_click()

    def settleOrder(self):
        self.mLog.log(self.mTag, "取车中页面结算订单")
        self.settleOrder_click()
        self.operater.sleep(10)
        if not self.settleOrderComfirm_exist():
            self.fail("Dialog [Confirm settle order?] not exist")
        self.dialog.confirm_click()
        self.operater.sleep(5)        
