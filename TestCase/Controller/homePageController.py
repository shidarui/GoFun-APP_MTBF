# coding=utf-8
from TestCase.Pages import homePage, dialog
from Lib.Util import log

class HomePageController(homePage.HomePage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'HomePageController'
        self.dialog = dialog.Dialog()
        
    def ad_close(self):
        self.mLog.log(self.mTag, "判断首页广告是否存在，存在则关闭")
        self.operater.sleep(2)
        if self.adClose_exist():
            self.mLog.log(self.mTag, "关闭广告按钮存在，点击关闭")
            self.adClose_click()
            self.operater.sleep(1)
        #539版本添加，关闭广告后有用车tip，需要关闭
        for i in range(6):
            if self.tipNextPage_exist():
                self.mLog.log(self.mTag, "存在【下一页】，点击【下一页】")
                self.tipNextPage_click()
                self.operater.sleep(2)
            else:
                break
        if self.tipClose_exist():
            self.mLog.log(self.mTag, "存在【关闭】，点击【关闭】")
            self.tipClose_click()
            self.operater.sleep(1)
        

    def tip_close(self):
        self.mLog.log(self.mTag, "判断首页挪动提示是否存在，存在则关闭")
        self.operater.sleep(2)
        if self.tips_exist():
            self.mLog.log(self.mTag, "提示按钮存在，点击关闭")
            self.tips_click()

    def location_refresh(self, times):
        self.mLog.log(self.mTag, "点击首页【位置】按钮进行刷新")
        for i in range(int(times)):
            self.location_click()
            self.operater.sleep(8)
            
    def go_click(self):
        self.mLog.log(self.mTag, "判断首页【Go】按钮是否存在，存在则点击")
        for i in range(5):
            if not self.goButton_exist():
                self.operater.sleep(3)
                self.mLog.log(self.mTag, "未找到go按钮，继续等待")
            else:
                self.mLog.log(self.mTag, "点击【GO】按钮")
                self.goButton_click()
                self.operater.sleep(12)
                return True
        else:
            return False

    def message_open(self):
        self.mLog.log(self.mTag, "点击主页【消息】图标，确认打开正常")
        self.messageMenu_click()
        self.operater.sleep(5)
        if self.messageTitle_exist():
            return True
        else:
            return False

    def messageNoti_open(self):
        self.mLog.log(self.mTag, "点击【通知你的事】，判断是否有消息列表")
        self.notification_click()
        self.operater.sleep(4)
        if self.messageList_exist():
            return True
        else:
            return False
            
    def messageDetail_open(self):
        self.mLog.log(self.mTag, "点击【查看详情】，判断是否打开正常")
        self.checkDetail_click()
        self.operater.sleep(4)
        if not self.messageList_exist():
            return True
        else:
            return False
 
    def  backToHome(self):
        self.mLog.log(self.mTag, "返回首页")
        for i in range(5):
            if not self.menu_exist():
                self.operater.t_keyevent("BACK")
                self.operater.sleep(3)
            else:
                self.mLog.log(self.mTag, "点击back，成功返回首页")
                return True
        else:
            return False
 
    def cityList_swipe(self, times):
        [device_width, device_height] = self.operater.appConfig.get_x_y("DEVICE.SIZE")#self.getDeviceSize()
        y1 = int(0.325 * device_height)
        y2 = int(0.867 * device_height)
        x1 = int(0.5 * device_width)
        for j in range(int(times)):
            self.operater.sleep(1)
            if j % 2 == 0:
                self.operater.swipe([x1, y1], [x1, y2], [device_width, device_height] )
            else:
                self.operater.swipe([x1, y2], [x1, y1], [device_width, device_height] )
                
    def yuyueTab_switch(self):
        self.mLog.log(self.mTag, "点击预约切换至预约tab")
        if self.yuyueTab_exist():
            self.yuyue_click()
            return True
        else:
            return False

    def click_carCard(self):
        self.mLog.log(self.mTag, "点击车辆卡片")
        if self.homeCard_exist():
            self.homeCard_click()
        else:
            self.homeCard_two_click()

    def yueyue_Cancle(self, type=0):
        self.mLog.log(self.mTag, "取消预约")
        if type == 0:
            self.yuyueCancel_click()
            if self.yuyueCancel_confrim_exist():
                self.dialog.confirm_click()
        elif type == 1:
            self.yuyueCancel_daily_click()
            self.dialog.cancel_click()  # 二次确认弹框-点击取消订单
            self.operater.sleep(5)
            self.dialog.confirm_click()  # 首页-我知道了
            self.operater.sleep(5)


    def wholeRPage_enter(self):
        self.mLog.log(self.mTag, "点击【车辆图片】进入整租预定页面")
        self.wholeRCar_click()
        self.operater.sleep(5)
        if self.wholeReserve_exist():
            return True
        else:
            return False
            
    def wholeR_reserveSuc(self):
        self.mLog.log(self.mTag, "整租下单")
        # 同意整租规则说明
        self.wholeRAgree_click()
        self.operater.sleep(5)
        #预定整租
        self.wholeReserve_click()
        self.operater.sleep(4)
        if self.dialog.warmTipContent_exist():
            self.dialog.confirm_click()
            self.operater.sleep(2)
        if self.wholeRSuc_exist():
            return True
        else:
            return False
            
    def wholeR_cancel(self):
        self.mLog.log(self.mTag, "取消整租预定")
        self.wholeRCancel_click()
        self.operater.sleep(3)
        if self.wholeRCancel_exist():
            self.wholeRCancel_click()
            self.operater.sleep(2)
        if self.dialog.confirmCancel_exist():
            self.dialog.confirmCancel_click()
            self.operater.sleep(2)
            if self.dialog.confirm_exist():
                self.dialog.confirm_click()
                self.operater.sleep(1)
