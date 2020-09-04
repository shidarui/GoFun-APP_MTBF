# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class TripDetailPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    costDetail = appConfig.get("COAST.DETAILS")
        
    def __init__(self):
        pass

    #设置-行程-行程详情
    def tripDetail_exist(self):
        return self.operater.exist("行程详情", "存在【行程详情】")  

    #设置-行程-行程详情-自助服务
    def autoService_click(self):
        self.operater.find_click_element("自助服务", des="点击【自助服务】")
        
    def autoService_exist(self):
        return self.operater.exist("自助服务", "存在【自助服务】")  
        
    def feePayment_exist(self):
        return self.operater.exist("费用缴纳", "存在【费用缴纳】")  
 
    def illegalTraffic_exist(self):
        return self.operater.exist("交通违法处理", "存在【交通违法处理】")  
       
    def cancel_exist(self):
        return self.operater.exist("取消", "存在【取消】")  

    def cancel_click(self):
        self.operater.find_click_element("取消", des="点击【取消】")

    #设置-行程-行程详情-费用明细
    def feeDetail_exist(self):
        return self.operater.exist(self.costDetail, "存在【费用明细】")
        
    def feeDetail_click(self):
        self.operater.find_click_element(self.costDetail, des="点击【费用明细】")

    #设置-行程-行程详情-费用明细-查看计费规则
    def seeFeeRule_click(self):
        self.operater.find_click_element("查看计费规则", des="点击【查看计费规则】")
        
    def feeRule_exist(self):
        return self.operater.exist("计价规则", "存在【计价规则】")
        
    def dailyRule_exist(self):
        return self.operater.exist("日租规则", "存在【日租规则】")

    #设置-行程-行程详情-看车况
    def carStatus_click(self):
        self.operater.find_click_element("看车况", des="点击【看车况】")
        
    def carPicture_exist(self):
        return self.operater.exist("验车照片", "存在【验车照片】")
        
    def clever_wait(self, item, num = 15):
        return self.operater.clever_wait(item, num)

    #设置-行程-行程详情-开发票
    def invoice_click(self):
        self.operater.find_click_element("开发票", "点击【开发票】")
    
    def invoiceAndReimbursement_exist(self):
        return self.operater.exist("发票与报销", "存在【发票与报销】")

    #设置-行程-行程详情-报问题
    def report_click(self):
        self.operater.find_click_element("报问题", "点击【报问题】")

    def reportTitle_exist(self):
        return self.operater.exist("问题上报", "存在【问题上报】")
        
