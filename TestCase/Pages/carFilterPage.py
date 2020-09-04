# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class CarFilterPage(Element_Operation):
    appConfig = GoFunConfiguration.GoFunConfiguration()
    carFilter = appConfig.get("HOME.FILTER")
    brand_list = appConfig.get_list("BRAND.LIST")
    seat_list = appConfig.get_list("SEAT.LIST")
    power_list = appConfig.get_list("POWER.TYPE")
    mileScroll = appConfig.get("MILE.SCROLL")
    filterConfirm = appConfig.get("FILTER.CAR.CONFIRM")
    filterReset = appConfig.get("FILTER.RESET")
    operater = Element_Operation()
    
    def __init__(self):
        pass     
        
    #主页-车辆筛选
    def carFilter_exist(self):
        return self.operater.exist(self.carFilter, "homepage car filter")
        
    def carFilter_click(self):
        self.operater.find_click_element(self.carFilter, des="homepage car filter")
        
    #主页-车辆筛选-车型
    def getBrandList(self):
        return self.brand_list

    def brand_exist(self, brand):
        return self.operater.exist(brand, "%s"%brand)
        
    def brand_click(self, brand):
        self.operater.find_click_element(brand, des="%s"%brand)
        
    #主页-车辆筛选-座位数
    def getSeatList(self):
        return self.seat_list

    def seat_exist(self, seat):
        return self.operater.exist(seat, "%s"%seat)
        
    def seat_click(self, seat):
        self.operater.find_click_element(seat, des="%s"%seat)
        
    #主页-车辆筛选-动力类型
    def getPowerList(self):
        return self.power_list

    def power_exist(self, power):
        return self.operater.exist(power, "%s"%power)
        
    def power_click(self, power):
        self.operater.find_click_element(power, des="%s"%power)
 
    #主页-车辆筛选-滑轮
    def mileScroll_exist(self):
        return self.operater.exist(self.mileScroll, "存在【滑轮】")
        
    def mileScroll_find(self):
        return self.operater.find_element(self.mileScroll)

    #主页-车辆筛选-确认按钮
    def confirm_exist(self):
        return self.operater.exist(self.filterConfirm, "confirm")
        
    def confirm_click(self):
        self.operater.find_click_element(self.filterConfirm, des="confirm")
        
    #主页-车辆筛选-重置按钮
    def reset_exist(self):
        return self.operater.exist(self.filterReset, "reset icon")
        
    def reset_click(self):
        self.operater.find_click_element(self.filterReset, des="reset icon")
