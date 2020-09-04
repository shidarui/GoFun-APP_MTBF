# coding=utf-8
from TestCase.Pages import payPage
from Lib.Util import log

class PayController(payPage.PayPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'PayController'

    def litiParking_return(self):
        self.mLog.log(self.mTag, "立体车位")
        if self.litiParking_exist():
            self.mLog.log(self.mTag, "点击【确认车位并锁车】")
            self.confirmAndLock_click()
            self.operater.sleep(8)
            
    def NonLitiParking_return(self):
        self.mLog.log(self.mTag, "非立体车位")
        if self.NonLitiParking_exist():
            self.mLog.log(self.mTag, "点击【还车】")
            self.returnCar_click()
            self.operater.sleep(8)
            
    def useCoupons(self):
        self.mLog.log(self.mTag, "检查是否有可用优惠券，如果有则使用")
        if self.hasCoupons_exist():
            self.mLog.log(self.mTag, "使用优惠券结算")
            self.chooseCoupons_click()
            self.operater.sleep(4)
            self.selectCoupon_click()
            self.operater.sleep(5)
            self.pay_click()
            self.operater.sleep(5)
