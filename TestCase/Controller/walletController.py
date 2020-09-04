# coding=utf-8
from TestCase.Pages import walletPage, personalCenterPage
from Lib.Util import log

class WalletController(walletPage.WalletPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'WalletController'
        self.perspage = personalCenterPage.PersonalCenterPage()
        
    def coupon_open(self):
        self.mLog.log(self.mTag, "点击【优惠券】，确认打开正常")
        self.coupon_click()
        self.operater.sleep(4)
        if not self.couponTitle_exist():
            return False
        else:
            return True
            
    def exchange_open(self):
        self.mLog.log(self.mTag, "点击【兑换】，确认打开正常")
        self.exchange_click()
        self.operater.sleep(4)
        if not self.exchangeTitle_exist():
            return False
        else:
            return True
 
    def payWithoutPassword_open(self):
        self.mLog.log(self.mTag, "点击【免密支付】，确认打开正常")
        self.payWithoutPassword_click()
        self.operater.sleep(4)
        if not self.payWithoutPasswordTitle_exist():
            return False
        else:
            return True     
          
    def encouragement_open(self):
        self.mLog.log(self.mTag, "点击【鼓励金】，确认打开正常")
        self.encouragement_click()
        self.operater.sleep(4)
        if not self.encouragementTitle_exist():
            return False
        else:
            return True 
 
    def deposit_open(self):
        self.mLog.log(self.mTag, "点击【履约保证金】，确认打开正常")
        self.deposit_click()
        self.operater.sleep(12)
        if not self.depositTitle_exist():
            return False
        else:
            return True 

    def travelCard_open(self):
        self.mLog.log(self.mTag, "点击【出行卡】，确认打开正常")
        self.travelCard_click()
        self.operater.sleep(10)
        if not self.travelCardTitle_exist():
            return False
        else:
            return True 

    def travelCardHis_open(self):
        self.mLog.log(self.mTag, "点击【购卡历史】，确认打开正常")
        self.travelCardHis_click()
        self.operater.sleep(10)
        if not self.travelCardHisTitle_exist():
            return False
        else:
            return True 

    def receipt_open(self):
        self.mLog.log(self.mTag, "点击【发票与报销】，确认打开正常")
        self.receipt_click()
        self.operater.sleep(12)
        if not self.receiptTitle_exist():
            return False
        else:
            return True 
            
    def backTo_wallet(self):
        self.mLog.log(self.mTag, "返回【个人中心-钱包】页，确认返回正常")
        for i in range(5):
            if not self.perspage.walletTitle_exist():
                self.mLog.log(self.mTag, "点击back图标")
                self.operater.t_keyevent("BACK")
                self.operater.sleep(6)
            else:
                self.mLog.log(self.mTag, "返回【钱包】主页")
                return True
        else:
            return False
