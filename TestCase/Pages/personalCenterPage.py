# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class PersonalCenterPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    walletTitle= appConfig.get("WALLET.TITLE")
    tripTitle = appConfig.get("NATIVE.TITLE.TRIP")
    tripList = appConfig.get("TRIP.LIST")
    keyboard = appConfig.get("ALERT.AD.CLOSE.ID")
    medalMenu = appConfig.get("MEDAL.MENU")
    myMedal = appConfig.get("MY.MEDAL")
    wmf = appConfig.get("WMF.MENU")
        
    def __init__(self):
        pass
 
    #个人中心-钱包
    def wallet_exist(self):
        return self.operater.exist("钱包", "存在【钱包】")

    def wallet_click(self):
        self.operater.find_click_element("钱包", des="点击【钱包】")

    def walletTitle_exist(self):
        return self.operater.title_exist(text1=self.walletTitle)

    #个人中心-行程
    def trip_click(self):
        self.operater.find_click_element("行程", des="点击【行程】")

    def tripTitle_exist(self): 
        return self.operater.title_exist(id=self.tripTitle, text1="行程") 
        
    def tripList_exist(self):
        return self.operater.exist(self.tripList, "存在【行程列表】")
        
    def tripList1_click(self):
        self.operater.atx_d(self.tripList).child()[0].click()
        
    def tripList2_click(self):
        self.operater.atx_d(self.tripList).child()[1].click()
     
    #个人中心-邀请有礼
    def invitation_click(self):
        self.operater.find_click_element("邀请有礼", des="点击【邀请有礼】")

    def invitateFriends_exist(self):
        return self.operater.exist("邀请好友", "存在【邀请好友】")
        
    def invitateRule_exist(self):
        return self.operater.exist("规则", "存在【规则】")
        
    def invitateRule1_exist(self):
        return self.operater.exist("邀请规则", "存在【邀请规则】")
    
    #键盘
    def keyboard_exist(self):
        return self.operater.exist(self.keyboard, "存在【键盘】")
        
    def keyboard_click(self):
        self.operater.find_click_element(self.keyboard, des="关闭【键盘】")
 
    #个人中心-交通违法
    def illegalTraffic_click(self):
        self.operater.find_click_element("交通违法", des="点击【交通违法】")
        
    def illegalTrafficTitle_exist(self):
        return self.operater.title_exist(text1="交通违法") 

    #个人中心-设置
    def setting_click(self):
        self.operater.find_click_element("设置", des="点击【设置】")
        
    def settingTitle_exist(self):
        return self.operater.title_exist(text1="设置") 
        
     #个人中心-我的勋章
    def medal_click(self):
        self.operater.find_click_element(self.medalMenu, des="点击【我的勋章】")
        
    def medalTitle_exist(self):
        return self.operater.exist(self.myMedal, "存在【我的勋章】")

     #个人中心-文明用车分
    def wmf_click(self):
        self.operater.find_click_element(self.wmf, des="点击【文明用车分】")
        
    def wmfTitle_exist(self):
        return self.operater.exist('文明用车分', "判断是否出现【文明用车分】")

     #个人中心-Go券商城
    def coupon_click(self):
        self.operater.find_click_element("Go券商城", "点击【Go券商城】")
        
    def coupon_exist(self):
        return self.operater.exist("Go券商城", "判定是否存在【Go券商城】")
        
    def couponHis_click(self):
        self.operater.find_click_element("购买记录", "点击【购买记录】")
        
    def couponHis_exist(self):
        return self.operater.exist("购买记录", "判定是否存在【购买记录】")
        
    def couponHisTitle_exist(self):
        return self.operater.title_exist(text1="购买记录") 
        
