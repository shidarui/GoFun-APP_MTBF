# coding=utf-8
from TestCase.Pages import carFilterPage
from Lib.Util import log

class CarFilterController(carFilterPage.CarFilterPage):
    def __init__(self):
        self.mLog = log.Log()
        self.mTag = 'CarFilterController'
        
    def brand_traversal(self):
        self.mLog.log(self.mTag, "遍历车型")
        brand_list = self.getBrandList()
        total_exist_brand = 0
        for brand in brand_list:
            self.operater.sleep(2)
            if self.brand_exist(brand):
                total_exist_brand += 1
                self.brand_click(brand)
        return total_exist_brand
        
    def seat_traversal(self):
        self.mLog.log(self.mTag, "遍历座位数")
        seat_list = self.getSeatList()
        for seat in seat_list:
            self.operater.sleep(2)
            if self.seat_exist(seat):
                self.seat_click(seat)

    def power_traversal(self):
        self.mLog.log(self.mTag, "遍历动力类型")
        power_list = self.getPowerList()
        for power in power_list:
            self.operater.sleep(2)
            if self.power_exist(power):
                self.power_click(power)

    def mileScroll_oper(self):
        self.mLog.log(self.mTag, "操作滚轮")
        mile_scroll = self.mileScroll_find()
        [top, right, bottom, left] = mile_scroll.get_bounds()
        center_y = (top + bottom) / 2.0 + 0.008
        left_pos = [left + 0.04, center_y]
        right_pos = [(left + right) / 2.0, center_y]
        self.mLog.log(self.mTag, "scroll left %s" % str(left_pos))
        self.mLog.log(self.mTag, "scroll right %s" % str(right_pos))
        self.mLog.log(self.mTag,"车辆里程滚轮滑动一半距离")
        self.operater.atx_d.swipe(left_pos, right_pos, duration=0.5)
        
    def carFilter_reset(self):
        self.mLog.log(self.mTag, "车辆筛选重置")
        self.mLog.log(self.mTag, "点击首页【车辆筛选】图标")
        self.carFilter_click()
        self.operater.sleep(4)
        self.mLog.log(self.mTag, "点击【重置】")
        self.reset_click()
        self.operater.sleep(4)
        if self.confirm_exist():
            self.mLog.log(self.mTag, "点击【确认】")
            self.confirm_click()
        self.operater.sleep(4)
