# coding=utf-8
from TestCase.Pages import personalCenterPage
from Lib.Util import log

class PersonalCenterController(personalCenterPage.PersonalCenterPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'PersonalCenterController'
        
    def wallet_open(self):
        self.mLog.log(self.mTag, "点击【钱包】，确认正常打开")
        for i in range(5):
            if not self.wallet_exist():
                self.mLog.log(self.mTag, "【个人中心】list中，钱包不存在，向下滑动")
                self.operater.atx_d.swipe([0.388, 0.454], [0.388, 0.838], duration=0.5)
                self.operater.sleep(4)
            else:
                break
        else:
            self.mLog.log(self.mTag, "钱包不存在")
            return True
        self.wallet_click()
        self.operater.sleep(4)
        if not self.walletTitle_exist():
            return False
        else:
            return True
            
    def coupon_open(self):
        self.mLog.log(self.mTag, "点击【Go券商城】，确认正常打开")
        for i in range(5):
            if not self.coupon_exist():
                self.mLog.log(self.mTag, "【个人中心】list中，Go券商城不存在，向上滑动")
                self.operater.atx_d.swipe([0.388, 0.838], [0.388, 0.454], duration=0.5)
                self.operater.sleep(4)
            else:
                break
        else:
            self.mLog.log(self.mTag, "Go券商城不存在")
            return True
        self.mLog.log(self.mTag,"点击【Go券商城】")
        self.coupon_click()
        self.operater.sleep(8)
        if not self.coupon_exist():
            return False
        else:
            return True

    def couponHisroty_open(self):
        self.mLog.log(self.mTag, "点击【Go券商城】，确认正常打开")
        if not self.couponHis_exist():
            self.mLog.log(self.mTag, "无【购买记录】")
            return True
        self.operater.sleep(1)
        self.couponHis_click()
        self.operater.sleep(4)
        if not self.couponHisTitle_exist():
            return False
        else:
            return True

    def trip_open(self):
        self.mLog.log(self.mTag, "点击【行程】，确认正常打开")
        self.trip_click()
        self.operater.sleep(4)
        if not self.tripTitle_exist():
            return False
        else:
            return True
            
    def swipe_up(self, start, end, item):
        self.mLog.log(self.mTag, "向上滑动")
        for i in range(5):
            if not self.operater.exist_text(item, "[%s]"%item):
                self.mLog.log(self.mTag, "【个人中心】list中，【%s】不存在，向上滑动"%item)
                self.operater.atx_d.swipe(start, end, duration=0.5)
                self.operater.sleep(4)
            else:
                return True
        return False

    def invitation_open(self):
        self.mLog.log(self.mTag, "点击【邀请有礼】，确认正常打开")
        self.invitation_click()
        self.operater.sleep(8)
        if self.keyboard_exist():
            self.keyboard_click()
        if self.invitateFriends_exist():
            if self.invitateRule_exist() or self.invitateRule1_exist():
                return True
            else:
                [device_width, device_height] = self.operater.appConfig.get_x_y("DEVICE.SIZE")
                y1 = int(0.325 * device_height)
                y2 = int(0.867 * device_height)
                x1 = int(0.5 * device_width)
                self.operater.swipe([x1, y1], [x1, y2], [device_width, device_height])
                self.operater.sleep(2)
                if self.invitateRule_exist() or self.invitateRule1_exist():
                    return True
                else:
                    return False
        else:
            return False
            
    def illegalTraffic_open(self):
        self.mLog.log(self.mTag, "点击【交通违法】，确认正常打开")
        self.illegalTraffic_click()
        self.operater.sleep(3)
        if self.illegalTrafficTitle_exist():
            return True
        else:
            return False
            
    def setting_open(self):
        self.mLog.log(self.mTag, "点击【设置】，确认正常打开")
        self.setting_click()
        self.operater.sleep(3)
        if self.settingTitle_exist():
            return True
        else:
            return False

    def medal_open(self):
        self.mLog.log(self.mTag, "点击【我的勋章】，确认正常打开")
        self.medal_click()
        self.operater.sleep(3)
        if self.medalTitle_exist():
            return True
        else:
            return False
            
    def wmf_open(self):
        self.mLog.log(self.mTag, "点击【文明用车分】，确认正常打开")
        self.wmf_click()
        self.operater.sleep(3)
        if self.wmfTitle_exist():
            return True
        else:
            return False
