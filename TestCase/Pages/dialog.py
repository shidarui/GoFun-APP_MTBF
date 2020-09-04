# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class Dialog:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    positive = appConfig.get("DIALOG.POSITIVE.ID")
    dismiss = appConfig.get("DIALOG.DISMISS")
    cancel = appConfig.get("DIALOG.CANCEL")
    content = appConfig.get("DIALOG.CONTENT")
    backArrow = appConfig.get("BACK.ARROW")
    freeReturnTitle = appConfig.get("NATIVE.TITLE.TRIP")
    lockToPay =appConfig.get("DIALOG.CLOSEDOOR.ID")
    backArrow1 = appConfig.get("COUPON.BACK")
        
    def __init__(self):
        pass
        
    def confirm_exist(self):
        return self.operater.exist(self.positive, "存在【确认/确认预定/仍然预定/我知道了/继续下单/确认开门/确认免费还车】按钮")
        
    def confirm_click(self):
        self.operater.find_click_element(self.positive, des="点击【确认/确认预定/仍然预定/我知道了/继续下单/确认开门/确认免费还车】按钮")
        
    def dismiss_exist(self):
        return self.operater.exist(self.dismiss, "存在【我知道了】按钮")
        
    def dismiss_click(self):
        self.operater.find_click_element(self.dismiss, des="点击【我知道了】按钮")
        
    def cancel_exist(self):
        return self.operater.exist(self.cancel, "存在【继续用车/取消/停止找车】按钮")
        
    def cancel_click(self):
        self.operater.find_click_element(self.cancel, des="点击【继续用车/取消/停止找车】按钮")
        
    def agree_exist(self):
        return self.operater.exist("同意", "存在【同意】按钮")
        
    def agree_click(self):
        self.operater.find_click_element("同意", des="点击【同意】按钮")
        
    def faceRec_exist(self):
        return self.operater.exist("请完成面部识别", "存在【请完成面部识别】提示")
        
    def later_click(self):
        self.operater.find_click_element("稍后再说", des="点击【稍后再说】按钮")
 
    def takeCarOverTime_exist(self):
        return self.operater.exist("取车已超时", "存在【取车已超时】提示") 
        
    def dialog_exist(self, dialogTitle, des):
        return self.operater.exist(dialogTitle, des)

    def iKnowText_exist(self):
        return self.operater.exist("我知道了", "存在【我知道了】")
        
    def iKnowText_click(self):
        self.operater.find_click_element("我知道了", des="点击【我知道了】")
        
    def confirmText_click(self):
        self.operater.find_click_element("确定", des="点击【确定】")
        
    def confirmText_exist(self):
        return self.operater.exist("确定", "存在【确定】")
        
    #dialog-温馨提示 
    def warmTipContent_exist(self):
        return self.operater.exist(self.content, "【温馨提示】-内容")

    def getWarmTipContent(self):
        return self.operater.get_text(self.content, "【温馨提示】-内容")
        
    #dialog-开门用车提示
    def openDoorTip_exist(self):
        return self.operater.exist("准备就绪", "提示框：【准备就绪】-关于开门提示")

    #dialog-首次用车提示
    def firstExperience_exist(self):
        return self.operater.exist("您首次体验该车型", "[Dialog]First Experience")

    #后退箭头
    def backArrow_click(self):
        self.operater.find_click_element(self.backArrow, des="点击后退按钮")
        
    #dialog-免费还车提示框
    def freeReturnTitle_exist(self):
        return self.operater.title_exist(id = self.freeReturnTitle, text1="免费还车")
        
    #dialog-已经免费还车提示框
    def finishFreeReturnTitle_exist(self):
        return self.operater.title_exist(id = self.freeReturnTitle, text1="免费还车成功")
        
    #账单页-请完成以下事项
    def finishBelowItem_exist(self):
        return self.operater.exist("请完成以下事项", "[Dialog]Please finish bellow items")

    #账单页-锁车前请确认以下事项
    def confirmBeforeReturn_exist(self):
        return self.operater.exist("锁车前请确认以下事项", "Dialog[Confirm return]")
        
    #账单页-确认还车
    def confirmReturn_exist(self):
        return self.operater.exist("确认还车", "Dialog[Confirm return]")
 
    #锁车并结算 
    def closeDoor_click(self):
        self.operater.find_click_element(self.lockToPay, des="锁车并结算")
        
    #后退箭头
    def backArrow1_exist(self):
        return self.operater.exist( self.backArrow1, "判定是否存在：返回按钮")
        
    def backArrow1_click(self):
        self.operater.find_click_element(self.backArrow1, "点击【<】按钮")
        
    def nevigateTipTitle_exist(self):
        return self.operater.title_exist(id=self.freeReturnTitle, text1="提示")  
        
    def nevigateTooFar_exist(self):
        return self.operater.title_exist(id=self.content, text1="选择导航距离过远，请重试！")

    #543,整租取消订单-“确认取消”
    def confirmCancel_exist(self):
        return self.operater.exist("确认取消", "存在[确认取消]按钮")
    
    def confirmCancel_click(self):
        self.operater.find_click_element("确认取消", "点击[确认取消]按钮")
