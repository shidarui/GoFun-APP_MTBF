# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class PayPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    insurance_list = appConfig.get("SETTLEMENT.INSURANCE")
    pay = appConfig.get("PAY.CAR.CONFIRM")
    chooseCoupons = appConfig.get("CHOOSE.COUPONS.FOR.SETTLE")
    selectCoupon = appConfig.get("SELECT.COUPONS")
    evaluate = appConfig.get("EVALUATE.ORDER")
    evaluateClose =appConfig.get("EVALUATE.CLOSE.BUTTON")
    toHome = appConfig.get("TRAVEL.END.TO.HOMEPAGE")
    backArrow = appConfig.get("COUPON.BACK")
    dailyPayBackArrow = appConfig.get("CANCEL.DAILY.ORDER")
    
    def __init__(self):
        pass
        
    def get_insuranceList(self):
        return self.operater.find_element(self.insurance_list, "[Settle]: insurance list")
        
    def pay_click(self):
        self.operater.find_click_element(self.pay, des="[Return car], [return & settle]")

    #立体车位
    def litiParking_exist(self):
        return self.operater.exist("正确选择车辆停放位置", "立体车位：还车确认")
 
    # 确认车位并锁车
    def confirmAndLock_click(self):
        self.operater.find_click_element("确认车位并锁车", "reserve car commit")
        
    #非立体车位
    def NonLitiParking_exist(self):
        return self.operater.exist("还车确认事项", "非立体车位，还车确认")
 
    # 还车
    def returnCar_click(self):
        self.operater.find_click_element("还车", "还车")

    #有可用优惠券
    def hasCoupons_exist(self):
        return self.operater.exist("您有未使用的优惠券", "You have unused coupons")

    #使用优惠券结算
    def chooseCoupons_click(self):
        self.operater.find_click_element(self.chooseCoupons, "use coupons for settlement")

    #选择优惠券
    def selectCoupon_click(self):
        self.operater.find_click_element(self.selectCoupon, "select new user coupons")
        
    #评价
    def evaluateOrder_exist(self):
        return self.operater.exist(self.evaluate, "提示：请您评价本次行程的用车感受~，存在！")
        
    #关闭评价
    def evaluateClose_click(self):
        self.operater.find_click_element(self.evaluateClose, "点击评价页面关闭按钮")
        
     #行程完成
    def travelFinish_exist(self):
        return self.operater.exist("行程完成", "行程完成")
        
    #行程完成返回home
    def backToHome_exist(self):
        return self.operater.exist( self.toHome, "判定是否存在：[to homepage]")
        
    def backToHome_click(self):
        self.operater.find_click_element(self.toHome, "点击返回home")
        
    #日租账单页
    def dailyPay_exist(self):
        return self.operater.exist("日租账单", "【日租账单】页面")     

    def dailyPayBackArrow_click(self):
        self.operater.find_click_element(self.dailyPayBackArrow, "点击【后退】按钮")
 
    #行程账单
    def tripBill_exist(self):
        return self.operater.exist("行程账单", "【行程账单】页面")   

    def byCarIntTitle_exist(self):
        return self.operater.title_exist(text1="购车意向调查")

    def byCarIntTitle2_exist(self):
        return self.operater.title_exist(text1="问卷调查")
