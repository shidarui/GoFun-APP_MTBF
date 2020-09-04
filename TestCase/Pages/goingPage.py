# coding=utf-8
from Lib.Stability.Framework.element_operation import Element_Operation
from Lib.Stability.Framework import gofunconfiguration as GoFunConfiguration

class GoingPage:
    appConfig = GoFunConfiguration.GoFunConfiguration()
    operater = Element_Operation()
    toReturnCar = appConfig.get("GOING.RETURN.CAR")
    carHealth = appConfig.get("GOING.CAR.HEALTH")
    sofarClose = appConfig.get("GOING.SOFAR.CLOSE")
    healthClose = appConfig.get("GOING.HEALTH.CLOSE.BUTTON")
    powerNotEnough = appConfig.get("POWER.TIP")
    guessParking = appConfig.get("GOING.GUESS.PARKING")
    changeCar = appConfig.get("GOING.CHANGE.CAR")
    tripCarImage = appConfig.get("TRIP.CAR.IMG")
    issueReport = appConfig.get("ISSUE.REPORT")
    openDoor = appConfig.get("GOING.OPEN.DOOR")
    closeDoor = appConfig.get("GOING.CLOSE.DOOR")
    voiceFind = appConfig.get("GOING.VOICE.FIND")
    freeReturn = appConfig.get("FREE.RETURN")
    nextButton = appConfig.get("DIALOG.CLOSEDOOR.ID")
    closeInterfaceTitle = appConfig.get("CLOSE.INTERFACE")
        
    def __init__(self):
        pass 
        
    #行程中-去还车
    def toReturnCar_exist(self):
        return self.operater.exist(self.toReturnCar, "存在【去还车】按钮")
        
    def toReturnCar_click(self):
        self.operater.find_click_element(self.toReturnCar, des="点击【去还车】按钮")
 
    #行程中-车辆太远 
    def soFarClose_exist(self):
        return self.operater.exist(self.sofarClose, "存在【车辆太远关闭】按钮")
        
    def soFarClose_click(self):
        self.operater.find_click_element(self.sofarClose, des="点击【车辆太远关闭】按钮")    

    #行程中-车内卫生清洁
    def carHealth_exist(self):
        return self.operater.exist(self.carHealth, "车内卫生清洁")
        
    def healthClose_click(self):
        self.operater.find_click_element(self.healthClose, des= "点击【车内卫生清洁关闭】按钮") 

    #行程中-电量不足
    def powerNotEnough_exist(self):
        return self.operater.exist(self.powerNotEnough, "电量不足")

    #行程中-
    def guessParking_exist(self):
        return self.operater.exist(self.guessParking, "[Guess where you want to go]")
        
    #行程中-换车
    def changeCar_exist(self):
        return self.operater.exist(self.changeCar, "换车")
        
    #行程中
    def tripGoing_exist(self):
        return self.operater.exist("行程中", "[Goging]")
        
    #行程中-问题上报
    def issueReport_exist(self):
        return self.operater.exist(self.issueReport, "存在【问题上报】图标")

    def openDoor_click(self):
        self.operater.find_click_element(self.openDoor, des= "点击【开门】") 
        
    def closeDoor_click(self):
        self.operater.find_click_element(self.closeDoor, des= "点击【关门】") 
        
    def voiceFind_click(self):
        self.operater.find_click_element(self.voiceFind, des= "点击【寻车】") 
        
    #行程中-免费还车等待时间
    def freeReturnTime_exist(self):
        return self.operater.exist(self.freeReturn, "存在【免费还车等待时间】")

    #行程中-免费还车按钮
    def freeReturn_click(self):
        self.operater.find_click_element("免费还车", "[Free Return] bottom button") 
        
    #还车-选择车辆停放位置
    def selectParkLoc_exist(self):
        return self.operater.exist("选择车辆停放位置","存在：选择车辆停放位置")
 
    #还车-下一步
    def nextButton_click(self):
        self.operater.find_click_element(self.nextButton, "点击：下一步按钮") 

    #拉手刹
    def closeInterfaceTitle_exist(self):
        return self.operater.title_exist(id=self.closeInterfaceTitle,text1="拉手刹")
        
    #还车-锁车停止计费
    def closeDoorToPay_click(self):
        self.operater.find_click_element(self.nextButton, "【锁车停止计费】")

    def getTripCarImage(self):
        return self.operater.find_element(self.tripCarImage, "tripCarImage")
