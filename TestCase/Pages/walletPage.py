# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class WalletPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    encouragementTitle = appConfig.get("WALLET.ENCOURAGEMENT.TITLE")
    payWithoutPasswordTitle =appConfig.get("WALLET.PAYWIOPASSWORD.TITLE")
    encourageBack = appConfig.get("ENCOURAGE.HOMEPAGE.BACK")
    
    def __init__(self):
        pass
 
    #钱包-优惠券
    def coupon_click(self):
        self.operater.find_click_element("优惠券", des="点击【优惠券】")   
     
    def couponTitle_exist(self):
        return self.operater.title_exist(text1="优惠券")
    
    #钱包-优惠券-兑换
    def exchange_click(self):
        self.operater.find_click_element("兑换", des="点击【兑换】")
 
    def exchangeTitle_exist(self):
        return self.operater.title_exist(text1="优惠券兑换") 

    #钱包-免密支付
    def payWithoutPassword_click(self):
        self.operater.find_click_element("免密支付", des="点击【免密支付】")
    #图片识别
    def payWithoutPasswordTitle_exist(self):
        return self.operater.xml_pic_pos(self.payWithoutPasswordTitle)

    #钱包-鼓励金
    def encouragement_exist(self):
        return self.operater.exist("鼓励金", "存在【鼓励金】")  
        
    def encouragement_click(self):
        self.operater.find_click_element("鼓励金", des="点击【鼓励金】")   
     
    def encouragementTitle_exist(self):
        return self.operater.title_exist(id=self.encouragementTitle, text1="鼓励金")
        
    def encouragementBack_click(self):
        self.operater.find_click_element(self.encourageBack, des="点击【鼓励金后退键】") 

    #钱包-履约保证金
    def deposit_click(self):
        self.operater.find_click_element("履约保证金", des="点击【履约保证金】")
 
    def depositTitle_exist(self):
        return self.operater.title_exist(text1="履约保证金") 
 
    #钱包-发票与报销
    def receipt_click(self):
        self.operater.find_click_element("发票与报销", des="点击【发票与报销】")
 
    def receiptTitle_exist(self):
        return self.operater.title_exist(text1="发票与报销")  

    #钱包-出行卡
    def travelCard_exist(self):
        return self.operater.exist("出行卡",  "存在【出行卡】")  
        
    def travelCard_click(self):
        self.operater.find_click_element("出行卡", des="点击【出行卡】")
 
    def travelCardTitle_exist(self):
        return self.operater.title_exist(text1="出行卡") 
 
    #钱包-出行卡-购卡历史
    def travelCardHis_click(self):
        self.operater.find_click_element("购卡历史", des="点击【购卡历史】")
 
    def travelCardHisTitle_exist(self):
        return self.operater.title_exist(text1="购卡历史")  
