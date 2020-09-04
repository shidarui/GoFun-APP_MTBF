# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class HomePage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    homeMenu = appConfig.get("HOME.MENU")
    homeTips = appConfig.get("HOME.MOVE.TIPS")
    homeAdClose = appConfig.get("ALERT.AD.CLOSE.ID")
    homeGo = appConfig.get("HOME.GO")
    location = appConfig.get("HOME.LOCATION")
    homeAccident = appConfig.get("ACCIDENT.ICON")
    homeClean = appConfig.get("CLEAN.ICON")
    homeService = appConfig.get("HOME.SERVICE")
    homeMessage = appConfig.get("MESSAGE.MENU")
    messageNotification = appConfig.get("MESSAGE.TAB")
    messageList = appConfig.get("MESSAGE.LIST")
    homeCard = appConfig.get("HOME.CARD")
    homeCard_two = appConfig.get("HOME.CARD.TWO")
    carListItem = appConfig.get("CARD.LIST.ITEM")
    localCity = appConfig.get("LOCAL.CITY")
    city_list = appConfig.get("CITY.LIST")
    cityName = appConfig.get("CITY.ID")
    ivGuess = appConfig.get("HOME.IV.GUESS")
    returnSameTak = appConfig.get("RETURN.SAME.TAKING")
    returnSameTak_yuyue = appConfig.get("RETURN.SAME.TAKING.TWO")
    yuyue = appConfig.get("YUYUE.TAB")
    yuyuePic = appConfig.get("HOME.YUYUE.PICNAME")
    yuyueCancel = appConfig.get("YUYUE.CACEL")
    yuyueCancel_daily = appConfig.get("YUYUE.CACEL.DAILY")
    wholeRCar = appConfig.get("WHOLERENT.CAR.PIC")
    wholeRAgree = appConfig.get("WHOLERENT.AGREE")
    titleId = appConfig.get("NATIVE.TITLE.TRIP")
    cityPic = appConfig.get("HOME.CITY.PICNAME")
    tuhuiAddress = appConfig.get("TEHUI.ADDRESS")
    Cancel_daily = appConfig.get("CACEL.DAILY") #546 日租账单取消增加二次确认
        
    def __init__(self):
        pass
    
    #主页-menu
    def menu_exist(self):
        return self.operater.exist(self.homeMenu, "存在【主页menu】图标")
        
    def menu_click(self):
        self.operater.find_click_element(self.homeMenu, des="点击【主页menu】图标")

    #主页-广告
    def adClose_exist(self):
        return self.operater.exist(self.homeAdClose, "存在【关闭广告】按钮")
        
    def adClose_click(self):
        self.operater.find_click_element(self.homeAdClose, des="点击【关闭广告】按钮")

    #主页-挪动提示
    def tips_exist(self):
        return self.operater.exist(self.homeTips, "存在区块链及go券商城挪动提示")
        
    def tips_click(self):
        self.operater.find_click_element(self.homeTips, des="点击区块链及go券商城挪动提示")
 
    #主页-go按钮
    def goButton_exist(self):
        return self.operater.exist(self.homeGo, "存在【Go】按钮")
        
    def goButton_click(self):
        self.operater.find_click_element(self.homeGo, des="点击【Go】按钮")

    #主页-位置刷新
    def location_exist(self):
        return self.operater.exist(self.location, "存在【位置刷新】按钮")
        
    def location_click(self):
        self.operater.find_click_element(self.location, des="点击【位置刷新按钮】")

    #主页-事故出险
    def accident_exist(self):
        return self.operater.exist(self.homeAccident, "存在【事故出险】图标")
 
    #主页-清洁奖余额 
    def clean_exist(self):
        return self.operater.exist(self.homeClean, "存在【清洁奖余额】图标")

    #主页-客服
    def customService_exist(self):
        return self.operater.exist(self.homeService, "存在【客服】图标")
        
    def customService_click(self):
        self.operater.find_click_element(self.homeService, des="点击【客服】图标")

    #主页-模拟位置
    def locationSimulate_exist(self):
        return self.operater.exist("模拟位置", "存在【模拟位置】图标")

    #主页-消息流
    def messageMenu_click(self):
        self.operater.find_click_element(self.homeMessage, des="点击【消息】图标")

    def messageTitle_exist(self):
        return self.operater.title_exist(text1="消息流")
        
    #主页-消息流-通知你的事     
    def notification_click(self):
        self.operater.find_click_element(self.messageNotification , des="点击【通知你的事】")
        
    #主页-消息流-消息列表
    def messageList_exist(self):
        return self.operater.exist(self.messageList, "消息列表")
  
    #主页-消息流-查看详情  
    def checkDetail_exist(self):
        return self.operater.exist("查看详情", "存在【查看详情】")
        
    def checkDetail_click(self):
        self.operater.find_click_element("查看详情" , des="点击【查看详情】")

    #主页-有车提醒
    def openCarNoti_exist(self):
        return self.operater.exist("开启该网点有车提醒", "存在【开启该网点有车提醒】图标")
        
    #主页-无可用车辆
    def noCar_exist(self):
        return self.operater.exist("该网点暂无可用车辆", "有车提醒")        
        
    #主页-车辆卡片c
    def homeCard_exist(self):
        return self.operater.exist(self.homeCard, "Homepage card list")
        
    def homeCard_click(self):
        self.operater.find_click_element(self.homeCard , des="Homepage card list")

    def homeCard_two_exist(self):
        return self.operater.exist(self.homeCard_two, "Homepage card list")
        
    def homeCard_two_click(self):
        self.operater.find_click_element(self.homeCard_two , des="Homepage card list")
        
    #主页-车辆卡片，返回 车辆列表
    def getCardList(self):
        homeCard = self.operater.find_element(self.homeCard, "Homepage card list")
        cardList = homeCard.child(self.carListItem)
        return cardList
        
    #主页-城市
    def localCity_exist(self):
        return self.operater.exist(self.localCity, "主页设置城市")
        
    def localCity_click(self):
        self.operater.find_click_element(self.localCity, des="主页设置城市")    
        
    #主页-城市-城市列表
    def cityList_exist(self):
        return self.operater.exist(self.city_list, "城市列表")      
      
    def getcityName(self):
        return self.operater.get_text(self.cityName, "城市名称") 
      
    def cityName_click(self, name):
        self.operater.find_click_element(name, des="城市名称:%s"%name) 
      
    def cityName_exist(self, name):
        return self.operater.exist(name, des="城市名称:%s"%name)   

    def clever_wait(self, item, num = 15):
        return self.operater.clever_wait(item, num)
        
    #主页-分时
    def timeD_click(self):
        self.operater.find_click_element("分时", "点击【分时】按钮") 

    #主页-日租
    def daily_click(self):
        self.operater.find_click_element("日租", "点击【日租】按钮") 
        
    #主页-特惠
    def tehui_click(self):
        self.operater.find_click_element("特惠车", "点击【特惠车】按钮") 
 
    #主页-整租
    def wholeR_click(self):
        self.operater.find_click_element("整租", "点击【整租】按钮") 
        
    #主页-同取同还
    def returnSameTak_exist(self):
        return self.operater.exist(self.returnSameTak, "同取同还")
        
    def returnSameTak_click(self):
        self.operater.find_click_element(self.returnSameTak, des="同取同还")

    #主页-同取同还-预约
    def returnSameTak_yuyue_exist(self):
        return self.operater.exist(self.returnSameTak_yuyue, "预约-同取同还")
        
    def returnSameTak_yuyue_click(self):
        self.operater.find_click_element(self.returnSameTak_yuyue, des="预约-同取同还")
        
    def ivGuess_exist(self):
        return self.operater.exist(self.ivGuess, "iv Guess")
        
    def ivGuess_click(self):
        self.operater.find_click_element(self.ivGuess, des="iv Guess")  

    #判断给定元素是否存在
    def item_exist(self, item, des):
        return self.operater.exist(item, des)
        
    def item_click(self, item, des):
        self.operater.find_click_element(item, des)  

    #预约tab
    def yuyueTab_exist(self):
        return self.operater.exist(self.yuyue, "是否存在【预约】TAB")
    
    #预约图片
    def yuyue_click(self):
        self.operater.xml_pic_click(self.yuyuePic)
        
    #分时-预约
    def yuyue_getTitle(self):
        return self.operater.get_text(self.titleId, "获取标题")
        
    def yuyue_waitDistribute_exist(self):     
        return self.operater.title_exist(self.titleId, "等待派送")
    
    #取消分时-预约
    def yuyueCancel_click(self):
        return self.operater.find_click_element(self.yuyueCancel, "点击【取消】按钮")

    #确认取消预约
    def yuyueCancel_confrim_exist(self):
        return self.operater.exist(self.titleId, "确定取消本次订单？")
 
    #日租-预约
    def yuyueDaily_pay_exist(self):
        return self.operater.exist("支付", "进入【账单】界面")
 
    #取消日租-预约
    def yuyueCancel_daily_click(self):
        return self.operater.find_click_element(self.yuyueCancel_daily, "点击【取消】按钮")

    #整租车辆图片
    def wholeRCar_exist(self):
        return self.operater.exist(self.wholeRCar, "判断是否存在【车辆图片】")
 
    def wholeRCar_click(self):
        return self.operater.find_click_element(self.wholeRCar, "点击【车辆图片】") 
        
    #预定整租
    def wholeReserve_exist(self):
        return self.operater.exist( "预定整租", "判断是否存在【预定整租】按钮")
 
    def wholeReserve_click(self):
        return self.operater.find_click_element("预定整租", "点击【预定整租】") 
        
    def wholeRAgree_click(self):
        return self.operater.find_click_element(self.wholeRAgree, "点击【同意整租规则说明】") 
        
    def wholeRSuc_exist(self):
        return self.operater.exist("整租受理中", "判断是否存在【整租受理中】")

    #取消预定
    def wholeRCancel_exist(self):
        return self.operater.exist("取消预定", "判断是否存在【取消预定】")
 
    def wholeRCancel_click(self):
        return self.operater.find_click_element("取消预定", "点击【取消预定】") 
        
    def homeCityPic_exist(self):
        return self.operater.self.xml_pic_pos(self.cityPic)
        
    def tehui_exist(self):
        return self.operater.exist("场次预告", "判断是否存在【场次预告】")        

    def tehui_exist1(self):
        return self.operater.exist(self.tuhuiAddress, "判断是否存在【特惠车地址栏】")    

    #539版本添加，关闭广告后有用车tip
    def tipNextPage_exist(self):
        return self.operater.exist("下一页", "判断是否存在【下一页】")
 
    def tipNextPage_click(self):
        return self.operater.find_click_element("下一页", "点击【下一页】") 
 
    def tipClose_exist(self):
        return self.operater.exist("关闭", "判断是否存在【关闭】")
 
    def tipClose_click(self):
        return self.operater.find_click_element("关闭", "点击【关闭】")

    # 取消日租-日租账单-546增加二次确认弹框
    def Cancel_daily_click(self):
        return self.operater.find_click_element(self.Cancel_daily, "点击【取消订单】按钮")


