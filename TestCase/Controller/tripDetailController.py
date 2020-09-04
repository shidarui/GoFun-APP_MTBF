# coding=utf-8
from TestCase.Pages import tripDetailPage, homePage
from Lib.Util import log

class TripDetailController(tripDetailPage.TripDetailPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'TripDetailController'
        self.homepage = homePage.HomePage()
        
    def autoService_open(self):
        self.mLog.log(self.mTag, "点击【自助服务】，确认正常打开")
        self.autoService_click()
        self.operater.sleep(4)
        if self.feePayment_exist() and self.illegalTraffic_exist() and \
            self.cancel_exist():       
            return True
        else:
            return False

    def carStatus_open(self):
        self.mLog.log(self.mTag, "点击【看车况】，确认正常打开")
        self.carStatus_click()
        self.operater.sleep(4)
        if not self.tripDetail_exist() and self.carPicture_exist():       
            return True
        else:
            return False
 
    def feeRule_open(self):
        self.mLog.log(self.mTag, "点击【计费规则】，确认正常打开")
        self.seeFeeRule_click()
        self.operater.sleep(8)
        if self.feeRule_exist() or self.dailyRule_exist():       
            return True
        else:
            return False
 
    def feeDetail_open(self):
        self.mLog.log(self.mTag, "点击【费用明细】，确认正常打开")
        self.feeDetail_click()
        self.operater.sleep(4)
        if self.feeDetail_exist() and (not self.tripDetail_exist()):       
            return True
        else:
            return False
            
    def invoice_open(self):
        self.mLog.log(self.mTag, "点击【开发票】，确认正常打开")
        self.invoice_click()
        self.homepage.clever_wait("发票与报销")
        if self.invoiceAndReimbursement_exist():       
            return True
        else:
            return False

    def report_open(self):
        self.mLog.log(self.mTag, "点击【报问题】，确认正常打开")
        self.report_click()
        self.operater.sleep(4)
        if not self.tripDetail_exist() and self.reportTitle_exist():       
            return True
        else:
            return False

    def backTo_tripDetail(self):
        self.mLog.log(self.mTag, "点击【自助服务-取消】返回行程详情，确认正常返回")
        self.cancel_click()
        self.operater.sleep(3)    
        if self.feeDetail_exist():
            return True
        else:
            return False
            
    def backTo1_tripDetail(self):
        self.mLog.log(self.mTag, "点击back返回行程详情，确认正常返回")
        self.operater.t_keyevent("BACK")
        self.operater.sleep(2)    
        if self.feeDetail_exist():
            return True
        else:
            return False
