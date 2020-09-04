# coding=utf-8

import time
import random
from Lib.Util import log
from Lib.per import per_app
from Lib.Stability.Framework import testrunner
#from Lib.Stability.Framework import element_operation
from TestCase.Controller import loginController, homePageController, dialogController, \
walletController, personalCenterController, tripDetailController, customServiceController, settingController, \
hasCarNotiController, carFilterController, reserveController, goingController, payController, pickingController
from TestCase.Pages import loginPage, homePage, dialog, goingPage, pickingPage, \
walletPage, personalCenterPage, tripDetailPage, customServicePage, settingPage, hasCarNotiPage, \
carFilterPage, reservePage, payPage
import sys
reload(sys)
sys.setdefaultencoding("utf8")

class TestCase(testrunner.TestRunner):
    mAdvanced_insurance = False
    mUnder_or_multistory = False
    mFree_return = True
    mLog = log.Log()
    percent = 10
    new_time = time
    case_random = random.Random()

    loginCtrl = loginController.LoginController()
    homePageCtrl = homePageController.HomePageController()
    dialogCtrl = dialogController.DialogController()
    pickingCtrl = pickingController.PickingController()
    walletCtrl = walletController.WalletController()
    personalCtrl = personalCenterController.PersonalCenterController()
    tripdCtrl = tripDetailController.TripDetailController()
    custserviceCtrl = customServiceController.CustomServiceController()
    settingCtrl = settingController.SettingController()
    hascarCtrl = hasCarNotiController.HasCarNotiController()
    carFilterCtrl = carFilterController.CarFilterController()
    reserveCtrl = reserveController.ReserveController()
    goingCtrl = goingController.GoingController()
    payCtrl = payController.PayController()
    
    loginpage = loginPage.LoginPage()
    homepage = homePage.HomePage()
    dialog = dialog.Dialog()
    pickingpage = pickingPage.PickingPage()
    walletpage = walletPage.WalletPage()
    perscenpage = personalCenterPage.PersonalCenterPage()
    tripdetailpage = tripDetailPage.TripDetailPage()
    settingpage = settingPage.SettingPage()
    hascarpage = hasCarNotiPage.HasCarNotiPage()
    carfilterpage = carFilterPage.CarFilterPage()
    reservepage = reservePage.ReservePage()
    goingpage = goingPage.GoingPage()
    paypage = payPage.PayPage()
    custservpage =customServicePage.CustomServicePage()
    
    def login(self):
        self.sleep(2)
        self.addCaseStep("检测账号是否登录")
        if self.homepage.menu_exist():
            self.homepage.menu_click()
            self.sleep(4)
            if not self.loginpage.unlogin_exist(): 
                self.addCaseStep("账号已登录，点击地图，返回应用首页")
                self.atx_d.click([0.95, 0.5])
                self.sleep(2)  
            else:
                self.loginCtrl.login()              
                self.homePageCtrl.tip_close()
                self.homePageCtrl.ad_close()
                if self.loginpage.unlogin_exist():
                    self.addCaseStep("登录失败")
                    self.fail("login fail")
                else:
                    self.addCaseStep("成功登录")
                    self.atx_d.click([0.95, 0.5])

    def environment_init(self):
        self.login()
        # 进行脸部识别
        self.dialogCtrl.faceRec_skip()
        self.sleep(2)
        # 上次行程处于【取车超时已结单】
        self.dialogCtrl.takeCarOverTime_close()
        self.sleep(2)
        # 上次行程处于【去还车】界面
        if self.goingpage.toReturnCar_exist() or self.homepage.accident_exist() or self.homepage.clean_exist():
            self.addCaseStep("上次订单未完成，去还车")
            self.return_car()
            self.commmit_evaluation()
        # 免费还车
        if self.pickingpage.freeReturn_exist():
            self.addCaseStep("上次订单未完成，免费还车")
            self.free_return()
        # 上次行程处于【取车中】界面
        if self.pickingpage.pickingCar_exist():
            if self.pickingpage.cancleOrder_exist():
                self.addCaseStep("上次订单未完成，取消订单")
                self.cancel_order()
                self.sleep(4)
            elif self.pickingpage.settleOrder_exist():
                self.addCaseStep("上次订单未完成，结算订单")
                self.pickingCtrl.settleOrder()
        # 上次行程处于【行程账单】界面
        if self.paypage.tripBill_exist():
            self.settle_order()
            self.commmit_evaluation()
        # 预约界面
        if self.homepage.yuyue_waitDistribute_exist():
            self.cancel_maa()

    def app_init(self):
        self.addCaseStep("Test start")
        if self.dialog.agree_exist():
            self.dialog.agree_click()
        self.addCaseStep("等待广告出现")
        for i in range(2):
            self.sleep(15)
            if self.homepage.adClose_exist():
                self.homePageCtrl.ad_close()
                self.sleep(4)
                if self.homepage.adClose_exist():
                    self.addCaseStep("点击【关闭广告按钮】，等待15秒，广告依然存在")
                    self.homePageCtrl.ad_close()
                    self.sleep(4)
                break
            elif self.homepage.menu_exist():
                break
            elif self.homepage.accident_exist() or self.homepage.clean_exist():
                break
            else:
                self.mLog.log(self.mCaseTag, "wait")
                self.t_stop(self.gofun_package)
                self.sleep(4)
                self.t_start(self.gofun_package)
                self.sleep(8)
        else:
            self.addCaseStep("广告未出现")
        self.environment_init()

    def search_park(self):
        self.xml_address = self.h5_element_path
        list_element = ["p_num_1", "p_num_2", "p_num_3", "p_num_4", "", "p_num_5add"]
        num_result = []
        for i, i_data in enumerate(list_element):
            if i_data == "":
                continue
            num_pos = self.xml_pic_pos(i_data)
            if num_pos != "False":
                self.mLog.log(self.mCaseTag, "select park, %s cars in the park" % (i + 1))
                self.click(num_pos)
                self.sleep(12)
                self.find_click_element_by_id(self.appConfig.get("HOME.CARD"), "[Homepage]:card")
                self.t_sleep(30)
            else:
                num_result.append("False")
        if len(num_result) == 6:
            self.fail("No change park!!!")

    def homapge_check_parking_type(self):
        self.addCaseStep("检测首页地图中取车网点气泡")
        if self.xml_pic_pos("homepage_parking_bubble") == "False":
            self.fail("[Parking Bubble] not exist")
        else:
            self.addCaseStep("首页地图中取车网点气泡存在")
        self.sleep(8)

    def refresh(self):
        if not self.homepage.location_exist():
            self.fail("[Location] not exist")
        self.addCaseStep("双击首页【位置刷新】")
        # click location button 2 times
        self.homePageCtrl.location_refresh(2)
        if not self.homePageCtrl.go_click():
            self.fail("未找到go按钮")

    def goto_reserve_homepage(self):
        self.refresh()
        if self.homepage.noCar_exist():
            self.addCaseStep("附近无车")
            return False
        else:
            self.addCaseStep("附近有车，开始用车")
            if self.homepage.ivGuess_exist():
                self.homepage.ivGuess_click()
            #同取同还
            if self.homepage.returnSameTak_exist():
                self.homepage.returnSameTak_click()
            self.sleep(4)
            # 添加途径点525
            # if self.exist_text(self.appConfig.get("ADD.WAY.POINT")):
            #     current_city = self.find_element(self.appConfig.get("HOME.CITY"), "").get_text()
            #     self.sleep(4)
            #     if current_city == "济南":
            #         way_point_name = "大明湖"
            #     elif current_city == "北京":
            #         way_point_name = "天安门"
            #     self.find_click_element_by_id(self.appConfig.get("ADD.WAY.POINT"), "")
            #     self.sleep(4)
            #     self.find_click_element_by_id(self.appConfig.get("WAY.POINT.NAME"), "")
            #     self.sleep(4)
            #     if self.exist_text(self.appConfig.get("SEARCH.ADDRESS.EDIT")):
            #         self.find_element(self.appConfig.get("SEARCH.ADDRESS.EDIT"),"").set_text(way_point_name)
            #         self.sleep(4)
            #         self.find_click_element_by_id(self.appConfig.get("WAY.NAME.RESULT"), "")
            self.addCaseStep("点击【车辆卡片】")
            self.homePageCtrl.click_carCard()
            self.sleep(15)
            return True

    def goto_reserve_make_an_app(self):
        self.sleep(3)
        self.refresh()
        if not self.homePageCtrl.yuyueTab_switch():
            self.fail("未找到【预约】")
        self.sleep(4)
        #if self.xml_pic_pos("maa_icon") != 'False':
        #    self.xml_pic_click("maa_icon")
        # 同取同还
        if self.homepage.returnSameTak_yuyue_exist():
            self.homepage.returnSameTak_yuyue_click()
        self.sleep(4)
        self.addCaseStep("点击【车辆卡片】")
        self.homePageCtrl.click_carCard()
        self.sleep(10)
        if not (self.reservepage.commit_exist() or self.reservepage.commit1_exist()):
            self.fail("fail to go to [reserve] page")           
        title_text_list = [["基础服务协议", "Dialog:Advanced insurance"], ["本地已开通\"超停\"服务", "over parking"]]
        self.dialogCtrl.dialog_traversal_close(title_text_list)
        self.addCaseStep("检测是否有【三者无忧】")
        self.reserve_check_advanced_insurance()
        #若取车点非同取同还，设置还车点同取车点
        self.reserveCtrl.returnSameTak_set()
        #
        self.sleep(8)
        self.reservepage.yuyueTime_button_click()
        self.sleep(2)
        # 选择预约时间
        if self.reservepage.selectTime_exist():
            time_element = self.reservepage.getTimeOption()
            [top, right, bottom, left] = time_element.get_bounds()
            y1 = bottom - (bottom - top)*0.1
            y2 = bottom - (bottom - top)*0.9
            x = right + (left - right)*0.5
            self.addCaseStep("划定范围：y1:%s,y2:%s,x:%s" %(y1, y2,x))
            self.atx_d.swipe((x, y1), (x, y2), duration=0.5)
            self.sleep(3)
            self.reservepage.yuyueTime_confirm_click()

    def cancel_maa(self):
        self.addCaseStep("开始取消预约订单流程")
        title = self.homepage.yuyue_getTitle()
        if title == "支付":
            self.fail("进入【支付】界面")
        self.sleep(2)
        if not self.homepage.yuyue_waitDistribute_exist():
            self.fail("未进入【等待派送】界面")
        self.sleep(2)
        #取消预约
        self.homePageCtrl.yueyue_Cancle(type=0)
        self.addCaseStep("完成取消预约订单流程")

    # 日租预约
    def cancel_maa_two(self):
        self.addCaseStep("开始取消预约订单流程")
        # title = self.get_text(self.appConfig.get("NATIVE.TITLE.TRIP"), "获取标题")
        # if title == "支付":
        if self.homepage.yuyueDaily_pay_exist():
            self.addCaseStep("进入【支付】界面")
        self.sleep(2)
        self.homePageCtrl.yueyue_Cancle(type=1)
        self.addCaseStep("完成取消预约订单流程")

    def reserve_check_advanced_insurance(self):
        if self.reservepage.advInsurance_exist():
            self.addCaseStep("【三者无忧】存在")
            self.mAdvanced_insurance = True
        else:
            self.addCaseStep("【三者无忧】不存在")

    # test_gofun_MTBF_other01_navigation
    def navigation(self):
        self.addCaseStep("取车界面导航测试")
        self.pickingpage.nevigate_click()
        self.sleep(4)
        #站内导航
        if self.pickingpage.nevigate1_exist():
            self.pickingpage.nevigate1_click()
        #内置导航
        elif self.pickingpage.builtInNevigate_exist():
            self.pickingpage.builtInNevigate_click()
        self.sleep(4)
        # 判断是否显示
        #选择导航距离过远
        if self.dialog.nevigateTooFar_exist() or self.dialog.nevigateTipTitle_exist():
            self.dialog.iKnowText_click()
        else:
            self.pickingpage.nevLogout_click()
            self.sleep(3)
            self.pickingpage.nevLogoutConfirm_click()

    def reserve_car(self,commit_button=1):
        self.mAdvanced_insurance = False
        self.sleep(2)
        title_text_list = [["基础服务协议", "Dialog:Advanced insurance"], ["本地已开通\"超停\"服务", "over parking"]]
        self.dialogCtrl.dialog_traversal_close(title_text_list)
        self.addCaseStep("检测是否有【三者无忧】")
        self.reserve_check_advanced_insurance()
        if not (self.reservepage.commit_exist() or self.reservepage.commit1_exist()):
            self.fail("fail to go to [reserve] page")
        #若取车点非同取同还，设置还车点同取车点
        self.reserveCtrl.returnSameTak_set()
        self.sleep(2)
        # 预定车辆
        self.reserveCtrl.car_reserve()
        #检查温馨提示
        self.reserveCtrl.warmTip_check()
        #检查车辆被他人预定        
        if self.reserveCtrl.reserveByOther_check():
            self.fail("车辆被他人预定！！！")            
        ok_list = ["仍然预定", "确认预定"]
        for item in ok_list:
            if self.homepage.item_exist(item, item):
                self.homepage.item_click(item, item)
                self.sleep(8)
        # 判断是否需要重新点击预定按钮
        if self.dialog.confirm_exist():
            #确认预定
            self.dialog.confirm_click()
        self.dialogCtrl.faceRec_skip()
        #成功预定提示
        self.reserveCtrl.reserveSuc_check()
        if self.reservepage.noteTitle_exist():
            #点击继续下单
            self.dialog.confirm_click()

    def pick_up_car(self):
        if self.dialog.iKnowText_exist():
            self.dialog.iKnowText_click()
        if not self.pickingpage.pickingCar_exist():
            self.fail("Go to [Pick-up car] fail")
        self.addCaseStep("检测【取车中】网点信息显示是否正常")
        self.addCaseStep("取车中：点击【声音寻车】")
        self.pickingpage.pickingVoice_click()
        self.sleep(4)
        # 判断人脸识别是否开启
        if self.pickingpage.faceRecButton_exist():
            self.addCaseStep("人脸识别开关开启，无法用车")
            return False
        else:
            self.addCaseStep("取车中：点击【开始用车】")
            self.pickingpage.useCar_click()
            self.sleep(8)
            # 车损操作
            # self.car_damage_commit()
            if self.pickingpage.reportFinish_exist():
                self.pickingpage.reportFinish_click()
            self.sleep(4)
            #【准备就绪】-开门提示
            if self.dialog.openDoorTip_exist():
                self.dialog.confirm_click()
                self.sleep(8)
            return True

    def car_damage_commit(self):
        num_pos = self.xml_pic_pos("shot")
        if num_pos != "False":
            num_pos = list(num_pos)
            num_pos.reverse()
            num_pos = self.click(num_pos)
            self.addCaseStep("num_pos：%s" % str(num_pos))
            for i in range(3):
                self.atx_d.click([0.52, 0.92])
                self.sleep(8)
            self.addCaseStep("拍照结束，等待10秒")
            self.sleep(8)
        if self.exist_text("PICKING.APPRAISE", "评价停车技术"):
            self.find_click_element_by_text(self.appConfig.get("PICKING.APPRAISE"))
        if self.exist_text("车损拍照", "【车损拍照】界面"):
            self.sleep(3)
            self.find_click_element_by_text("验伤完毕", "点击【验伤完毕】按钮")
        if self.exist_text("将面部置于取景框内", "开启人脸识别"):
            self.addCaseStep("【人脸识别】开启，无法用车")
            self.fail("Face recognition exist!!!")

    def goging_set_destination(self):
        self.addCaseStep("点击【设置还车点】")
        self.find_click_element_by_id(self.appConfig.get("SET.DESTINATION"), "set destination")
        self.sleep(8)
        if self.exist_text("停车位类型", "[Dialog] parking type"):
            self.addCaseStep("【停车位类型】：点击【我知道了】")
            self.find_click_element_by_id(self.appConfig.get("DIALOG.POSITIVE.ID"), "我知道了")
            self.sleep(2)

    def change_car(self):
        if self.goingpage.changeCar_exist():
            self.sleep(12)
            if self.dialog.dialog_exist("如何换车", "Dialog:How to change car?"):
                if not self.goingpage.changeCar_exit():
                    self.fail("换车 返回 行程中 失败")

    def power_not_enough(self):
        if not self.goingpage.powerNotEnough_exist():
            self.addCaseStep("无【电量不足】图标")
            return
        self.mLog.log(self.mCaseTag, "power not enough, please change other car")
        self.dialog.iKnowText_click()
        self.sleep(3)
        #首次体验该车型
        self.goingCtrl.firstExperienceTip_close()
        if not self.goingpage.guessParking_exist():
            self.mLog.log(self.mCaseTag, "[Guess where you want to go] not exist")
            icon_name = "guess_you_like.png"
            self.getTemImage(icon_name)
        self.change_car()

    def going_open_close_find_car_check(self):
        self.addCaseStep("点击【开门】、【关门】、【寻车】")
        self.goingpage.openDoor_click()
        self.sleep(8)
        self.goingpage.closeDoor_click()
        self.sleep(8)
        self.goingpage.voiceFind_click()
        self.sleep(8)

    def swipe_map(self):
        device_size = self.appConfig.get_x_y("DEVICE.SIZE")
        left_x = int(device_size[0] * 0.2)
        right_x = int(device_size[0] * 0.8)
        center_x = int(device_size[0] * 0.5)
        center_y = int(device_size[1] * 0.5)
        top_y = int(device_size[1] * 0.2)
        bottom_y = int(device_size[1] * 0.8)
        self.addCaseStep("左滑")
        for i in range(2):
            self.swipe([right_x, center_y], [left_x, center_y])
        self.addCaseStep("上滑")
        for i in range(2):
            self.swipe([center_x, bottom_y], [center_x, top_y])
        self.addCaseStep("右滑")
        for i in range(2):
            self.swipe([left_x, center_y], [right_x, center_y])
        self.addCaseStep("下滑")
        for i in range(2):
            self.swipe([center_x, top_y], [center_x, bottom_y])

    def cancel_order(self):
        if not self.pickingpage.pickingCar_exist():
            self.fail("Go to [Going] fail")
        #点击取消订单
        if not self.pickingCtrl.cancle_order():
            self.fail("[Cancel order] not exist")
        #确认取消订单
        if not self.pickingCtrl.cancelOrder_confirm():
            self.fail("[Confirm cancel order] not exist!")
        #订单已经取消
        if not self.pickingpage.cancleOrderSuc_exist():
            self.fail("Dialog:[have canceled order] not exist")
        self.addCaseStep("【已为您取消订单】：点击【返回】")
        # 提交取消原因
        if self.pickingpage.specificReason_exist():
            self.pickingCtrl.specificReason_submit()
        else:
            if self.pickingpage.reasonArrow_exist():
                self.self.pickingpage.reasonArrow_click()
                if self.pickingpage.specificReason_exist():
                    self.pickingCtrl.specificReason_submit()
                else:
                    self.sleep(2)
                    self.dialog.backArrow1_click()
            else:
                self.sleep(2)
                self.dialog.backArrow1_click()
        self.sleep(6)
        if not self.homepage.menu_exist():
            self.fail("back to homepage fail!")
        self.addCaseStep("成功返回应用首页")

    def daily_cancel_order(self):
        if not self.paypage.dailyPay_exist():
            self.fail("Go to 【日租账单】 fail")
        self.sleep(3)
        self.paypage.dailyPayBackArrow_click()
        self.sleep(8)

        self.dialog.cancel_click()#二次确认弹框-点击取消订单
        self.sleep(8)
        self.dialog.confirm_click()#首页-我知道了
        self.sleep(8)

        if self.homepage.menu_exist():
            self.addCaseStep("返回首页面")

    def trip_up_img(self):
        # 判断开门、锁门等按钮在页面下方
        self.sleep(6)
        self.addCaseStep("判断免费还车或去还车未出现，向上滑动屏幕")
        if self.goingpage.issueReport_exist() and self.homepage.location_exist():
            self.addCaseStep("准备向上滑动屏幕")
            [top, right, bottom, left] = self.goingpage.getTripCarImage().get_bounds()
            self.addCaseStep("top, right, bottom, left:%s,%s,%s,%s"%(top, right, bottom, left))
            self.sleep(2)
            self.atx_d.swipe((left,top),(left,0.2), duration=0.5)
            self.sleep(4)

    def drive_car(self):
        self.addCaseStep("进入【行程中】")
        self.homepage.clever_wait(self.goingpage.carHealth,num=8)
        self.goging_car_health()
        #首次体验该车型
        self.goingCtrl.firstExperienceTip_close()
        # 车辆太远找不到
        self.goingCtrl.soFar_close()
        # 判断电量是否充足
        self.power_not_enough()
        self.trip_up_img()
        self.going_open_close_find_car_check()
        self.sleep(2)

    def goging_car_health(self):
        self.goingCtrl.goging_car_health()
        
    def free_return(self):
        self.addCaseStep("【免费还车过程】")
        self.goging_car_health()
        # 判定是否存在免费还车选项
        # if not self.title_exist(id="com.gvsoft.gofun:id/tv_return_car", name="免费还车"):
        if self.goingpage.freeReturnTime_exist():
            self.mFree_return = True
            self.addCaseStep("行程中：点击【免费还车】")
            self.goingpage.freeReturn_click()
            self.sleep(2)
            # 免费还车提示框
            if not self.dialogCtrl.freeReturnTip_close():
                self.fail("Dialog [Free return car?] not exist")
            self.sleep(2)
            # 免费还车后出现提示框
            if not self.dialog.finishFreeReturnTitle_exist():
                self.fail("Dialog [Free return car?] not exist")
            self.addCaseStep("已为您免费还车：点击【我知道了】")
            self.dialog.confirm_click()
        else:
            self.addCaseStep("无免费还车按钮，进行收费还车")
            self.return_car()
            self.commmit_evaluation()

    def going_check_auto_fee(self):
        self.addCaseStep("点击【费用预估】")
        if self.exist_text(self.appConfig.get("GOING.AUTO.FEE"), "[Going]: Auto fee icon"):
            self.find_click_element_by_id(self.appConfig.get("GOING.AUTO.FEE"), "[Going]: Auto fee icon")
        else:
            self.find_click_element_by_id(self.appConfig.get("GOING.DAILY.FEE"), "[Going]: Auto fee icon")
        self.sleep(4)
        if not self.exist_id(self.appConfig.get("GOING.FEE.ESTIMATE"), "Basic insurance"):
            self.fail("Auto Fee dialog not exist")

        self.mLog.log(self.mCaseTag, "self.mAdvanced_insurance is %s" % self.mAdvanced_insurance)
        if self.mAdvanced_insurance:
            if self.mFree_return == self.exist_id(self.appConfig.get("GOING.FEE.ADVANCED.INSURANCE"),
                                                  "GOING.FEE.ADVANCED.INSURANCE"):
                self.addCaseStep("费用预估中：保险费用与预定车时不匹配")
                icon_name = "auto_fee_dialog.png"
                icon_address = self.tem_img_path + icon_name
                self.n_screen(icon_address)
                self.tem_img_list.append(icon_name)
            else:
                self.addCaseStep("费用预估中：保险费用正常")
        self.addCaseStep("点击【我知道了】，关闭【费用预估】对话框")
        self.find_click_element_by_id(self.appConfig.get("DIALOG.POSITIVE.ID"), "I have known")
        self.sleep(4)

    def wait_to_return_car(self):
        self.addCaseStep("行程中：点击【去还车】")
        self.sleep(2)
        # 车辆太远找不到
        self.goingCtrl.soFar_close()
        self.trip_up_img()
        for i in range(24):
            if not self.goingpage.toReturnCar_exist():
                self.sleep(5)
            else:
                self.mFree_return = False
                # self.going_check_auto_fee()
                self.addCaseStep("点击【去还车】")
                self.goingpage.toReturnCar_click()
                self.sleep(8)
                break
        else:
            self.fail("wait 120s, [Return car] bottom button not exist")
        #点击：确定
        if self.dialog.confirmText_exist():
            self.dialog.confirmText_click()
        self.sleep(4)
        #选择车辆停放位置
        if self.goingpage.selectParkLoc_exist():
            self.goingpage.nextButton_click()
        self.sleep(4)
        #锁车停止计费
        if self.goingpage.closeInterfaceTitle_exist():
            self.goingpage.closeDoorToPay_click()
            self.sleep(8)
        else:
            self.fail("no closeDoorToPay button")

    def select_park_area(self):
        self.payCtrl.litiParking_return()
        self.payCtrl.NonLitiParking_return()

    def advance_insurance_in_order(self):
        insurance_list = self.paypage.get_insuranceList()
        if insurance_list != None:
            insurance_num = len(insurance_list.child("type=android.widget.LinearLayout"))
            if insurance_num == 1:
                self.addCaseStep("还车结算：费用明细只包含【基础保险】")
            elif insurance_num == 2:
                self.addCaseStep("还车结算：费用明细只包含【三者无忧】")
            if self.mAdvanced_insurance == True and insurance_num == 1:
                self.addCaseStep("预定车时包含三者无忧，还车结算中费用明细不包含【三者无忧】")
                icon_name = "settle_order.png"
                self.getTemImage(icon_name)

    def settlement_cost_key(self):
        self.addCaseStep("还车并结算：点击【合计费用】")
        self.find_click_element_by_id(self.appConfig.get("SETTLEMENT.COST.KEY"), "还车并结算-合计费用")
        self.sleep(4)
        if not self.exist_id(self.appConfig.get("SETTLEMENT.COST.KEY.DATA"), "合计费用-费用明细"):
            self.fail("还车并结算页面，费用明细不存在")
        self.addCaseStep("还车并结算：再次点击【合计费用】，隐藏费用明细")
        self.find_click_element_by_id(self.appConfig.get("SETTLEMENT.COST.KEY"), "还车并结算-合计费用")
        self.sleep(4)
        if self.exist_id(self.appConfig.get("SETTLEMENT.COST.KEY.DATA"), "合计费用-费用明细"):
            self.fail("费用明细未隐藏")

    def settle_order(self):
        self.sleep(8)
        self.addCaseStep("账单页面，检查费用明细")
        self.advance_insurance_in_order()
        self.addCaseStep("账单页面，点击【余额支付】")
        self.paypage.pay_click()
        self.sleep(8)
        self.select_park_area()
        #选择优惠券
        self.payCtrl.useCoupons()
        #请完成以下事项
        self.dialogCtrl.finishBelowItem()
        #锁车前请确认以下事项
        self.dialogCtrl.confirmBeforeReturn()
        #确认还车
        self.dialogCtrl.confirmReturn()

    def return_car(self):
        self.wait_to_return_car()
        self.settle_order()
        self.sleep(8)

    def commmit_evaluation(self):
        self.goging_car_health()
        if self.paypage.evaluateOrder_exist():
            self.paypage.evaluateClose_click()
            self.sleep(3)
        if self.paypage.byCarIntTitle_exist():
            self.t_keyevent("BACK")
            self.sleep(3)
        if self.paypage.byCarIntTitle2_exist():
            self.t_keyevent("BACK")
            self.sleep(3)
        if not self.paypage.travelFinish_exist():
            self.fail("Go to 行程完成 fail")
        self.addCaseStep("评价完成页面：点击【返回首页】")
        if self.paypage.backToHome_exist():
            self.paypage.backToHome_click()
        if self.dialog.backArrow1_exist():
            self.dialog.backArrow1_click()
        self.sleep(4)

    def zoom_in(self, percent=0.3, duration=0.3, dead_zone=0.2):
        self.atx_d.pinch(direction="in", percent=percent, duration=duration, dead_zone=dead_zone)

    def zoom_out(self, percent=0.3, duration=0.3, dead_zone=0.2):
        self.atx_d.pinch(direction="out", percent=percent, duration=duration, dead_zone=dead_zone)

    def service_function_check(self):
        self.xml_address = self.h5_element_path

    # MTBF_PersonalCenter01_wallet
    def wallet_title_coupon(self):
        self.addCaseStep("钱包主页，点击【优惠券】")
        if not self.walletCtrl.coupon_open():
            self.fail("Go to [Coupon] fail")
        self.addCaseStep("优惠券页面，点击【兑换】")
        if not self.walletCtrl.exchange_open():
            self.fail("Go to [Exchange coupon] fail")
        if not self.walletCtrl.backTo_wallet():
            self.fail("Back to [wallet] fail")

    # MTBF_PersonalCenter01_wallet 免密支付
    def wallet_pay_without_password(self):
        self.addCaseStep("钱包主页，点击【免密支付】")
        if not self.walletCtrl.payWithoutPassword_open():
            self.fail("Go to [Pay without password] fail")
        if not self.walletCtrl.backTo_wallet():
            self.fail("Back to [wallet] fail")

    # MTBF_PersonalCenter01_wallet 鼓励金
    def wallet_encouragement(self):
        if self.walletpage.encouragement_exist():
            self.addCaseStep("钱包主页，点击【鼓励金】")
            if not self.walletCtrl.encouragement_open():
                self.fail("Go to [Encouragement] fail")
            self.walletpage.encouragementBack_click()
            self.sleep(4)
            if not self.walletCtrl.backTo_wallet():
                self.fail("返回【钱包】主页失败")
        else:
            self.addCaseStep("钱包主页，未找到【鼓励金】")

    # MTBF_PersonalCenter01_wallet 履约保证金
    def wallet_deposit(self):
        self.addCaseStep("钱包主页，点击【履约保证金】")
        if not self.walletCtrl.deposit_open():
            self.fail("Go to [Deposit] fail")
        if not self.walletCtrl.backTo_wallet():
            self.fail("Back to [wallet] fail")

    # MTBF_PersonalCenter01_wallet---发票与报销
    def wallet_receipt(self):
        self.addCaseStep("钱包主页，点击【发票与报销】")
        if not self.walletCtrl.receipt_open():
            self.fail("Go to [Receipt&Reimbursement] fail")
        if not self.walletCtrl.backTo_wallet():
            self.fail("Back to [wallet] fail")

    # MTBF_PersonalCenter01_wallet---钱包->出行卡
    def travel_card(self):
        if self.walletpage.travelCard_exist():
            self.addCaseStep("钱包主页，点击【出行卡】")
            if not self.walletCtrl.travelCard_open():
                self.fail("进入【出行卡】界面失败")
            self.sleep(2)
            if not self.walletCtrl.travelCardHis_open():
                self.fail("进入【购卡历史】界面失败")
            self.back()
            if not self.walletpage.travelCardTitle_exist():
                self.fail("【购卡历史】后退，未进入【出行卡】界面")
            if not self.walletCtrl.backTo_wallet():
                self.fail("Back to [wallet] fail")
        else:
            self.addCaseStep("钱包主页，未找到【出行卡】")

    # MTBF_PersonalCenter08_setting---接近还车网点提示开关
    def setting_switch_button(self):
        self.addCaseStep("接近还车网点提示")
        if not self.settingpage.switchButton_exist():
            self.fail("切换开关不存在")
        #2: 点击切换2次
        self.settingCtrl.switchButton_switch(2)

    # MTBF_PersonalCenter08_setting---给GoFun好评
    def setting_gofun_valuation(self):
        self.addCaseStep("点击【给GoFun好评】")
        if not self.settingCtrl.appStore_open():
            self.fail("Go to app store fail")
        self.addCaseStep("【应用商店】页面，点击back键")
        # self.xml_pic_click("appstore_back")
        if not self.settingCtrl.backTo_gofunGood():
            self.fail("未回退至【给GoFun好评】")

    def setting_about_us(self):
        self.addCaseStep("点击【关于我们】")
        if not self.settingCtrl.aboutUs_open():
            self.fail("Go to [关于我们] fail")
        self.addCaseStep("成功进入【关于我们】，点击back返回应用首页")
        if not self.settingCtrl.backTo_setting():
            self.fail("Back to 设置 fail")

    def setting_membership_agreement(self):
        self.addCaseStep("点击【法律条款与平台规则】")
        if not self.settingCtrl.legalProvision_open():
            self.fail("Go to [法律条款与平台规则] fail")
        self.addCaseStep("成功进入【会员协议】，点击back返回应用首页")
        if not self.settingCtrl.backTo_setting():
            self.fail("Back to 设置 fail")

    def setting_logoff(self):
        self.addCaseStep("点击【注销账户】")
        if not self.settingCtrl.logoff_open():
            self.fail("Go to 申请注销账户 fail")
        self.addCaseStep("成功进入【注销账户】页面，点击back键")
        if not self.settingCtrl.backTo_setting():
            self.fail("Back to 设置 fail")

    # MTBF_PersonalCenter02_trip
    def trip_detail_car_picture(self):
        self.addCaseStep("点击【验车照片】")
        if self.tripdCtrl.carStatus_open():
            self.addCaseStep("点击back键")
            if not self.tripdCtrl.backTo1_tripDetail():
                self.fail("[Car picture] back to [trip detail] fail")
            self.addCaseStep("成功返回【费用详情】页面")
        else:
            self.fail("Go to [Trip detail] fail")

    # MTBF_PersonalCenter02_trip
    def trip_detail_report(self):
        self.addCaseStep("费用详情页面，点击【问题上报】")
        if self.tripdCtrl.report_open():
            self.addCaseStep("点击back图标")
            if not self.tripdCtrl.backTo1_tripDetail():
                self.fail("[Report] back to [trip detail] fail")
            self.addCaseStep("成功返回【费用详情】页面")
        else:
            self.fail("Go to [Trip detail] fail")

    # MTBF_PersonalCenter02_trip
    def trip_detail_auto_service(self):
        self.addCaseStep("点击【自助服务】")
        if self.tripdCtrl.autoService_open():
            self.addCaseStep("自助服务页面，点击【取消】")
            if not self.tripdCtrl.backTo_tripDetail():
                self.fail("[autoService] back to [trip detail] fail")
            self.addCaseStep("成功返回【费用详情】页面")
        else:
            self.addCaseStep("未成功打开【自助服务】")
            self.fail("error in [Auto service] content")

    # MTBF_PersonalCenter02_trip
    def trip_detail_fee_detail(self):
        self.addCaseStep("费用详情页面，点击【费用明细】")
        if self.tripdCtrl.feeDetail_open():
            self.addCaseStep("点击【查看计费规则】")
            if not self.tripdCtrl.feeRule_open():
                self.fail("Go to [Fee Rule] fail")
            self.addCaseStep("返回【行程详情】页面")
            #self.t_keyevent("BACK")
            #self.sleep(4)
            if not self.tripdCtrl.backTo1_tripDetail():
                self.fail("[feeDetail] back to [trip detail] fail")
            self.addCaseStep("成功返回【费用详情】页面")
        else:
            self.fail("Go to [Fee Detail] fail")

    # MTBF_PersonalCenter02_trip
    def trip_detail_invoice(self):
        self.addCaseStep("费用详情页面，点击【开发票】")
        if not self.tripdCtrl.invoice_open():
            self.fail("Go to [Invoice] fail")
        self.addCaseStep("点击back，返回【行程详情】")
        if not self.tripdCtrl.backTo1_tripDetail():
            self.fail("[invoice] back to [trip detail] fail")
        self.addCaseStep("成功返回【费用详情】页面")			            

    def coupon_seckill(self):
        if self.xml_pic_pos("1_gotokill_button") == "False":
            self.addCaseStep("【Go券商城】页面，不存在【去秒杀 GO】")
            return
        self.addCaseStep("【Go券商城】页面，点击【去秒杀 GO】")
        self.xml_pic_click("1_gotokill_button")
        self.sleep(8)
        if not self.title_exist(text="秒杀详情"):
            self.fail("进入【秒杀详情】失败")
        self.addCaseStep("成功进入【秒杀详情】")
        self.addCaseStep("点击back键，返回【Go券商城】首页")
        self.find_click_element_by_id(self.appConfig.get("COUPON.BACK"), "秒杀详情页面返回键")
        self.sleep(4)
        if not self.title_exist(text="Go券商城"):
            self.fail("返回【Go券商城】失败")
        self.addCaseStep("成功返回【Go券商城】")

    def coupon_seckill_list(self):
        self.addCaseStep("【Go券商城】页面，向上滑动")
        self.atx_d.swipe([0.5, 0.8], [0.5, 0.3])
        self.sleep(4)
        if self.xml_pic_pos("2_manykill_button") == "False":
            self.addCaseStep("未找到【更多秒杀】按钮")
            return
        self.addCaseStep("点击【更多秒杀】")
        self.xml_pic_click("2_manykill_button")
        self.sleep(4)
        if not self.title_exist(text="秒杀列表"):
            self.fail("返回【秒杀列表】失败")
        self.addCaseStep("点击back键，返回【Go券商城】首页")
        self.find_click_element_by_id(self.appConfig.get("COUPON.BACK"), "秒杀列表页面返回键")
        self.sleep(4)
        if not self.title_exist(text="Go券商城"):
            self.fail("返回【Go券商城】失败")
        self.addCaseStep("成功返回【Go券商城】")

    def coupon_bug_history(self):
        '''if not self.exist_text("购买记录", "判定是否存在【购买记录】"):
            return
        self.sleep(3)
        self.find_click_element_by_text("购买记录", "点击【购买记录】")
        self.sleep(4)
        if not self.title_exist(text1="购买记录"):
            self.fail("未进入【购买记录】界面")'''
        if not self.personalCtrl.couponHisroty_open():
            self.fail("未进入【购买记录】界面")
        self.t_keyevent("BACK")

    def find_num_park(self, img_park):
        self.addCaseStep("首页，双击【位置刷新】，点击%s，若不存在，则右滑寻找，最多右滑10次" % img_park)
        self.homePageCtrl.location_refresh(2)
        num_pos = self.xml_pic_pos(img_park)
        if num_pos != "False":
            return num_pos
        elif num_pos == "False":
            for i in range(1):
                self.atx_d.swipe([0.500, 0.4000], [0.500, 0.8555])
                self.sleep(5)
                pos = self.xml_pic_pos(img_park)
                if pos != "False":
                    self.addCaseStep("找到%s" % img_park)
                    return pos
            else:
                return False

    def MTBF_PersonalCenter01_wallet(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        self.addCaseStep("个人中心页面，点击【钱包】")
        if not self.personalCtrl.wallet_open():
            self.fail("[Title][My wallet] not exist")
        self.wallet_title_coupon()
        self.wallet_pay_without_password()
        # 511去除鼓励金功能
        self.wallet_encouragement()
        self.wallet_deposit()
        self.wallet_receipt()
        # 出行卡532
        self.travel_card()
        self.mLog.log(self.mCaseTag, "back to homepage")
        self.t_keyevent("BACK")
        self.sleep(3)
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)
        if not self.homepage.menu_exist():
            self.fail("Back to homepage fail")
        self.addCaseStep("返回应用主页")

    def MTBF_PersonalCenter02_trip(self):
        self.addCaseStep("首页，点击【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        self.addCaseStep("个人中心页面，点击【行程】")
        if not self.personalCtrl.trip_open():
            self.fail("[Title][My trip] not exist")   
        if self.perscenpage.tripList_exist():
            self.addCaseStep("点击行程列表中第二个行程")
            self.perscenpage.tripList2_click()
            self.sleep(4)
        else:
            self.addCaseStep("行程列表内容为空")
            return
        self.trip_detail_car_picture()
        self.trip_detail_report()
        self.trip_detail_auto_service()
        self.trip_detail_fee_detail()
        self.trip_detail_invoice()

    def MTBF_PersonalCenter03_customer_service(self):
        self.addCaseStep("首页，点击【客服】图标")
        if not self.custserviceCtrl.myService_open():
            self.fail("未进入【我的客服】")
        # 我的行程
        if self.custservpage.allTrip_exist():
            if not self.custserviceCtrl.allTrip_open():
                self.fail("点击全部行程失败，未进入【我的行程】")
            else:
                self.t_keyevent("BACK")
        self.sleep(5)
        # 我的咨询
        if self.custservpage.complain_exist():
            if not self.custserviceCtrl.complain_open():
                self.fail("点击投诉失败，未进入【处理进度】")
            else:
                self.t_keyevent("BACK")
        self.sleep(5)
        self.custserviceCtrl.autoService_traversal()
        self.addCaseStep("点击【联系客服】")
        if not self.custserviceCtrl.callService_open():
            self.fail("Go to [致电热线客服] fail")
        self.addCaseStep("成功进入【致电热线客服-选择电话】页面")
        self.t_keyevent("BACK")
        self.sleep(5)    
        '''if not self.custserviceCtrl.speed_cs_open():
            self.fail("Go to [Xiao Fun] fail")
        self.addCaseStep("成功进入【小Fun】页面")
        self.t_keyevent("BACK")
        self.sleep(6)'''
        if not self.custservpage.myServiceTitle_exist():
            self.fail("Back to [Service] fail")

    def MTBF_PersonalCenter04_activity(self):
        self.addCaseStep("点击首页【个人中心】菜单图标")
        self.find_click_element_by_id(self.appConfig.get("HOME.MENU"), "homepage menu")
        self.sleep(4)
        for i in range(5):
            if not self.exist_text("活动中心", "[Activity]"):
                self.addCaseStep("【个人中心】list中，活动中心不存在，向上滑动")
                self.atx_d.swipe([0.388, 0.838], [0.388, 0.454], duration=0.5)
                self.sleep(4)
            else:
                break
        self.addCaseStep("点击【活动中心】")
        self.find_click_element_by_text("活动中心", "[Activity]")
        self.sleep(8)
        if not self.title_exist(text="活动中心"):
            self.fail("Go to [Activity] fail")
        self.addCaseStep("成功进入【活动中心】，按back建，返回应用首页")
        self.t_keyevent("BACK")
        self.sleep(4)
        if not self.exist_id(self.appConfig.get("HOME.MENU"), "HOME.MENU"):
            self.fail("[Activity] back to homepage fail")

    def MTBF_PersonalCenter05_invitation(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        #如果没找到"邀请有礼"，向上滑动页面
        if not self.personalCtrl.swipe_up([0.388, 0.838], [0.388, 0.454], "邀请有礼"):
            self.fail("未找到【邀请有礼】")
        self.addCaseStep("点击【邀请有礼】")
        if not self.personalCtrl.invitation_open():
            self.fail("Go to [Invitation] fail")
        self.addCaseStep("成功进入【邀请有礼】，点击back返回应用首页")
        self.t_keyevent("BACK")
        self.sleep(4)
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)
        if not self.homepage.menu_exist():
            self.fail("[邀请有礼] back to homepage fail")

    def MTBF_PersonalCenter06_illegal_traffic(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        if not self.personalCtrl.swipe_up([0.388, 0.838], [0.388, 0.454], "交通违法"):
            self.fail("未找到【交通违法】")
        if not self.personalCtrl.illegalTraffic_open():
            self.fail("Go to [Illegal traffic] fail")
        self.addCaseStep("成功进入【交通违法】页面，点击back返回应用首页")
        self.t_keyevent("BACK")
        self.sleep(4)
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)
        if not self.homepage.menu_exist():
            self.fail("[交通违法] back to homepage fail")

    def MTBF_PersonalCenter08_setting(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        self.addCaseStep("【个人中心】页面，点击【设置】")
        if not self.personalCtrl.swipe_up([0.388, 0.838], [0.388, 0.454], "设置"):
            self.fail("未找到【设置】")
        if not self.personalCtrl.setting_open():
            self.fail("Go to [Setting] fail")
        #
        self.setting_switch_button()
        self.setting_logoff()
        # self.setting_gofun_valuation()
        self.setting_about_us()
        self.setting_membership_agreement()
        self.t_keyevent("BACK")
        self.sleep(3)
        #gxq
        self.t_keyevent("BACK")
        self.sleep(3)
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)
        if not self.homepage.menu_exist():
            self.fail("Go to homepage fail")

    def MTBF_PersonalCenter09_recommendBuildPoint(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.find_click_element_by_id(self.appConfig.get("HOME.MENU"), "homepage menu")
        self.sleep(4)
        self.addCaseStep("【个人中心】页面，点击【推荐建点】")
        self.find_click_element_by_text(self.appConfig.get("BUILD.POINT.MENU"), "点击【推荐建点】")
        self.sleep(4)
        if (not self.exist_text("推荐建点", "判断是否出现【推荐建点】")) or \
                (not self.exist_text(self.appConfig.get("SHARE.BUTTON.BUILD"), "是否存在【分享提升热力】")):
            self.fail("未进入到【推荐建点】界面")
        self.sleep(3)
        self.find_click_element_by_text(self.appConfig.get("ADD.BUTTON.BUILD"),"点击ADD按钮")
        self.sleep(4)
        if not self.exist_text("选择推荐位置","判断是否出现【选择推荐位置】"):
            self.fail("未进入【选择推荐位置】界面")
        self.t_keyevent("BACK")
        self.sleep(4)
        if (not self.exist_text("推荐建点", "判断是否出现【推荐建点】")) or \
                (not self.exist_text(self.appConfig.get("SHARE.BUTTON.BUILD"), "是否存在【分享提升热力】")):
            self.fail("返回时未进入到【推荐建点】界面")
        self.t_keyevent("BACK")

    def MTBF_PersonalCenter10_my_medal(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        self.addCaseStep("【个人中心】页面，点击【我的勋章】")
        if not self.personalCtrl.medal_open():
            self.fail("未进入【我的勋章】界面")
        self.sleep(3)
        self.t_keyevent("BACK")
        self.sleep(3)
        self.t_keyevent("BACK")
        self.sleep(1)

    def MTBF_PersonalCenter11_wmf(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        self.addCaseStep("【个人中心】页面，点击【文明用车分】")
        if not self.personalCtrl.wmf_open():
            self.fail("未进入【文明用车分】界面")
        self.sleep(3)
        self.t_keyevent("BACK")
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)

    def MTBF_PersonalCenter12_coupon(self):
        self.addCaseStep("点击首页【个人中心】图标")
        self.homepage.menu_click()
        self.sleep(4)
        '''for i in range(5):
            if not self.exist_text("Go券商城", "判定是否存在【Go券商城】"):
                self.addCaseStep("【Go券商城】list中，Go券商城不存在，向上滑动")
                self.atx_d.swipe([0.388, 0.838], [0.388, 0.454], duration=0.5)
                self.sleep(4)
            else:
                break
        self.addCaseStep("点击【Go券商城】")
        self.find_click_element_by_text("Go券商城", "点击【Go券商城】")
        self.sleep(8)
        if not self.exist_text("Go券商城", "判定是否进入【Go券商城】界面"):
            self.fail("未进入【Go券商城】")'''
        if not self.personalCtrl.coupon_open():
            self.fail("未进入【Go券商城】")
        self.coupon_bug_history()
        #self.coupon_seckill()
        #self.coupon_seckill_list()
        self.addCaseStep("点击返回键，返回应用主页")
        #self.find_click_element_by_id(self.appConfig.get("COUPON.BACK"), "【Go券商城】主页返回键")
        self.dialog.backArrow1_click()
        self.sleep(4)
        self.atx_d.click([0.95, 0.5])
        self.sleep(2)
        
    def MTBF_home01_zoomRandom(self):
        if not self.homepage.location_exist():
            self.fail("No [Location] ")
        self.addCaseStep("首页，双击【位置刷新】")
        self.homePageCtrl.location_refresh(2)
        # 第一步
        self.addCaseStep("随机缩放160次，偶数时缩小，奇数时放大")
        for j in range(4):
            self.sleep(1)
            for i in range(40):
                self.sleep(1)
                if int(i) % 2 == 0:
                    self.zoom_in(percent=0.4, duration=0.5, dead_zone=0.1)
                else:
                    self.zoom_out(percent=0.4, duration=0.5, dead_zone=0.1)
        self.sleep(3)
        if self.homepage.locationSimulate_exist():
            self.back()
            self.sleep(3)
        if not self.homepage.menu_exist():
            self.fail("TestCase: MTBF_home01_zoomRandom--homepage menu not exist.")
        # 第二步
        for j in range(4):
            self.addCaseStep("双击【位置刷新】")
            self.homePageCtrl.location_refresh(2)
            self.addCaseStep("先缩小4次，后放大4次")
            for i in range(8):
                self.sleep(1)
                if i < 5:
                    self.zoom_in(percent=0.4, duration=0.5, dead_zone=0.1)
                else:
                    self.zoom_out(percent=0.4, duration=0.5, dead_zone=0.1)
        self.sleep(4)
        if self.homepage.locationSimulate_exist():
            self.back()
            self.sleep(3)
        if not self.homepage.menu_exist():
            self.fail("TestCase: MTBF_home01_zoomRandom--menu not exist.")  # ####

    def MTBF_home02_Swipe(self):
        if not self.homepage.location_exist():
            self.fail("No [location] icon")
        else:
            self.sleep(2)
            self.addCaseStep("首页，双击【位置刷新】")
            self.homePageCtrl.location_refresh(2)
        # 第一步
        self.addCaseStep("顺时针滑动20次")
        for i in range(20):
            self.atx_d.swipe([0.277, 0.325], [0.926, 0.325])
            self.atx_d.swipe([0.926, 0.325], [0.926, 0.667])
            self.atx_d.swipe([0.926, 0.667], [0.277, 0.667])
            self.atx_d.swipe([0.277, 0.667], [0.277, 0.667])
        # 第二步
        [device_width, device_height] = self.appConfig.get_x_y("DEVICE.SIZE")
        x_min = int(0.277 * device_width)
        x_max = int(0.926 * device_width)
        y_min = int(0.325 * device_height)
        y_max = int(0.667 * device_height)
        self.addCaseStep("随机滑动100次")
        for j in range(100):
            self.sleep(1)
            x1 = self.case_random.randint(x_min, x_max)
            x2 = self.case_random.randint(x_min, x_max)
            y1 = self.case_random.randint(y_min, y_max)
            y2 = self.case_random.randint(y_min, y_max)
            self.swipe([x1, y1], [x2, y2])
        if not self.homepage.menu_exist():
            self.fail("TestCase: MTBF_home01_zoomRandom--main_pic not exist.")

    def MTBF_home03_Num(self):
        num_time = self.new_time.strftime("%H%M%S", self.new_time.localtime())
        list_element = ["p_num_0", "p_num_1", "p_num_2", "p_num_3", "p_num_4", "", "p_num_5add"]
        num_result = []
        for i, i_data in enumerate(list_element):
            if i_data == "":
                continue
            result = self.find_num_park(i_data)
            if result is not False:
                self.addCaseStep("点击%s,坐标：%s" % (i_data, result))
                self.click(result)
                self.sleep(6)
                if i == 0 and not self.homepage.openCarNoti_exist():
                    num_result.append("False")
                    icon_name = str(i_data) + "_" + str(num_time) + ".png"
                    self.getTemImage(icon_name)
                elif i == 0 and self.homepage.openCarNoti_exist():
                    self.addCaseStep("有车提醒存在")
                if i > 1:
                    if not self.homepage.homeCard_exist():
                        self.addCaseStep("车辆卡片列表不存在")
                        self.fail("card list not exist")
                    self.addCaseStep("向上滑动，展开车辆卡片列表")
                    self.atx_d.swipe([0.277, 0.800], [0.277, 0.100], duration=0.5)
                    self.sleep(8)
                    card_list = self.homepage.getCardList()
                    self.addCaseStep("停车场车辆数 %s，列表内容 %s" % (i, len(card_list)))
                    if (i >= 4 and len(card_list) < 4) or (i < 4 and len(card_list) != i):
                        self.addCaseStep("网点显示车辆数量与列表显示车辆数量 不一致，截图保存")
                        num_result.append("False")
                        icon_name = str(i_data) + "_" + str(num_time) + ".png"
                        self.getTemImage(icon_name)
                    self.addCaseStep("向下滑动，隐藏车辆列表")
                    self.atx_d.swipe([0.277, 0.277], [0.277, 0.950], duration=0.5)
                    self.sleep(8)
        if num_result.count("False") > 0:
            self.fail("MTBF_home03_Num fail")
        if not self.homepage.menu_exist():
            self.fail("TestCase: MTBF_home01_zoomRandom--menu not exist.")

    def getTemImage(self, icon_name):
        icon_address = self.tem_img_path + icon_name
        self.n_screen(icon_address)
        self.tem_img_list.append(icon_name)

    def MTBF_home04_Zoom_in(self):
        self.xml_address = self.h5_element_path
        self.addCaseStep("首页，单击【位置刷新】")
        self.homePageCtrl.location_refresh(1)
        i = 1
        while True:
            self.zoom_in(percent=0.2, duration=0.1, dead_zone=0.1)
            i += 1
            self.sleep(3)
            if self.homepage.homeCityPic_exist != "False":
                self.addCaseStep("已缩小%s次，匹配到本地图片" % i)
                break
            if i > 10:
                self.addCaseStep("已缩小20次，未匹配到本地图片")
                self.fail("test_gofun_MTBF_home04_Zoom_in-assert01 not exist")

    def MTBF_home05_filter(self):
        if not self.carfilterpage.carFilter_exist():
            self.fail("Homepage [car filter] not exist")
        self.addCaseStep("点击首页【车辆筛选】图标")
        self.carfilterpage.carFilter_click()
        self.sleep(6)
        # 点击各个车型
        total_exist_brand = self.carFilterCtrl.brand_traversal()
        if total_exist_brand ==0:
            self.addCaseStep("未找到任何车型")
        self.addCaseStep("共点击车型：%s种" %str(total_exist_brand))
        # 点击座位数
        self.carFilterCtrl.seat_traversal()
        # 点击车辆动力类型
        self.carFilterCtrl.power_traversal()
        # 2.操作滑轮
        if not self.carfilterpage.mileScroll_exist():
            self.addCaseStep("车辆里程滑轮不存在")
            self.fail("mile scroll not exist")
        self.carFilterCtrl.mileScroll_oper()
        self.sleep(3)
        self.addCaseStep("点击【确认】")
        self.carfilterpage.confirm_click()
        self.sleep(8)
        #重置
        self.carFilterCtrl.carFilter_reset()
        if not self.homepage.menu_exist():
            self.fail("未回到【主页】")

    def MTBF_home08_switch_city(self):
        self.addCaseStep("首页，点击当前城市")
        self.homepage.localCity_click()
        self.sleep(4)
        if not self.homepage.cityList_exist():
            self.fail("Go to [city list] fail")
        self.addCaseStep("上下滑动城市列表共50次，奇数向上，偶数向下")
        self.homePageCtrl.cityList_swipe(50)
        self.sleep(3)
        city_name = self.homepage.getcityName()
        self.addCaseStep("点击城市%s" % city_name)
        self.homepage.cityName_click(city_name)
        self.sleep(4)
        self.homePageCtrl.ad_close()
        self.homepage.clever_wait(self.homepage.location)
        if not self.homepage.location_exist():
            self.addCaseStep("等待20秒，未成功返回应用首页")
            self.fail("Go to homepage fail")
        if not self.homepage.cityName_exist(city_name):
            self.addCaseStep("等待20秒，切换城市至%s失败" % city_name)
            self.fail("设置 %s fail" % city_name)
        self.addCaseStep("点击【位置刷新】按钮，恢复至当前位置")
        self.homepage.location_click()
        # self.sleep(12)
        self.homepage.clever_wait(self.homepage.localCity)
        if not self.homepage.localCity_exist():
            self.addCaseStep("恢复至当前位置失败")
            self.fail("位置刷新失败")

    def MTBF_home09_search(self):
        self.addCaseStep("点击首页搜索图标")
        self.find_click_element_by_id(self.appConfig.get("HOME.SEARCH"), "homepage search")
        self.sleep(4)
        search_content = self.appConfig.get("SEARCH.CONTENT")
        self.addCaseStep("编辑框输入%s" % search_content)
        self.set_text_by_id(self.appConfig.get("SEARCH.ADDRESS.EDIT"), search_content, "搜索页面,地址输入框")
        self.sleep(4)
        if not self.exist_id(self.appConfig.get("SEARCH.RESULT.LIST"), "搜索结果"):
            self.fail("搜素结果为空")
        self.addCaseStep("点击搜索结果列表中第一个")
        result_list = self.find_element(self.appConfig.get("SEARCH.RESULT.LIST"), "搜索结果列表")
        result_list.child("android.widget.LinearLayout")[0].click()
        self.sleep(4)
        if not self.exist_id(self.appConfig.get("HOME.GO"), "[Go] in homepage"):
            self.addCaseStep("未进入目的地页面")
            self.fail("未进入目的地页面")
        self.addCaseStep("成功显示目的地")
        self.addCaseStep("点击取消")
        self.find_click_element_by_id(self.appConfig.get("SEARCH.DESTINATION.CANCEL"), "取消")
        self.sleep(8)
        if self.exist_id(self.appConfig.get("HOME.SEARCH"), "首页搜索图标"):
            self.addCaseStep("成功返回首页")
        else:
            self.fail("点击取消未返回首页")

    def MTBF_home10_car_reminder(self):
        self.app_init()
        self.addCaseStep("主页面有车提醒测试")
        if not self.hascarCtrl.reminderSetting_open():
            self.fail("未进入【设置有车提醒】页面")
        # 搜索范围
        # [top, right, bottom, left] = self.find_element("com.gvsoft.gofun:id/mile_slide_seek_bar").get_bounds()
        # self.sleep(2)
        # swip_left = [left,(bottom-top)/2+top]
        # swip_right = [left+(right-left)/2, (bottom-top) / 2 + top]
        # self.atx_d.click(swip_left)
        # self.sleep(2)
        # self.atx_d.swipe(swip_left, swip_right)
        # # 找车时间
        self.addCaseStep("点击找车时间【重复】按钮")
        if not self.hascarCtrl.repeatDate_open():
            self.fail("未找到【选择重复日期】")
        self.sleep(2)
        self.dialog.confirm_click()
        self.sleep(4)
        if not self.hascarCtrl.startTime_open():
            self.fail("未找到【选择找车开始时间】")
        self.hascarpage.selectTimeConfirm_click()
        self.sleep(6)
        if not self.hascarpage.endTimeTitle_exist():
            self.fail("未找到【选择找车结束时间】")
        self.hascarpage.selectTimeConfirm_click()
        self.sleep(4)
        # 车型筛选
        if not self.hascarCtrl.carType_open():
            self.fail("未进入【选择车型】")
        self.sleep(2)
        self.dialog.confirm_click()
        self.sleep(4)
        # 点击确定，开启有车提醒
        self.dialog.confirm_click()
        self.sleep(4)
        # 0-20语音提醒
        if self.hascarpage.confirmText_exist():
            self.hascarpage.confirmText_click()
        # 关闭有车提醒
        self.addCaseStep("关闭有车提醒")
        self.hascarpage.carReminder_click()
        self.sleep(6)
        self.dialog.cancel_click()

    def MTBF_home11_message(self):
        self.addCaseStep("点击首页【个人中心】图标")
        # 532消息在首页显示
        # self.find_click_element_by_id(self.appConfig.get("HOME.MENU"), "homepage menu")
        # self.sleep(4)
        self.addCaseStep("点击【消息】")
        if not self.homePageCtrl.message_open():
            self.fail("未进入【消息流】")
        self.sleep(3)
        if not self.homePageCtrl.messageNoti_open():
            self.addCaseStep("消息列表为空")
        else:
            self.addCaseStep("消息列表上下滑动5次")
            for i in range(5):
                self.atx_d.swipe([0.500, 0.8555], [0.500, 0.4000])
                self.sleep(4)
                self.atx_d.swipe([0.500, 0.4000], [0.500, 0.8555])
                self.sleep(4)
            if self.homepage.checkDetail_exist():
                self.addCaseStep("点击【查看详情】")
                if not self.homePageCtrl.messageDetail_open():
                    self.fail("Go to 消息详情失败")
        if not self.homePageCtrl.backToHome():
            self.fail("[Push] back to homepage fail")

    def MTBF_rent_01_screen(self):
        self.addCaseStep("整租界面测试")
        self.homepage.wholeR_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        if self.homepage.wholeRCar_exist():
            if self.homePageCtrl.wholeRPage_enter():
                self.addCaseStep("存在【预定整租】按钮")
                # self.back()
                # self.sleep(5)
                # if not self.exist_id(self.appConfig.get("HOME.MENU"), "homepage, [Menu]"):
                #     self.fail("back to homepage fail!")
            else:
                self.fail("不存在【预定整租】按钮")

            '''if not self.exist_text("预约取车"):
                self.fail("未进入【预约取车】页面")
            self.sleep(3)
            # 预约取车 确定按钮
            self.find_click_element_by_id("com.gvsoft.gofun:id/tv_WholeRent")
            self.sleep(5)
            self.find_click_element_by_id("com.gvsoft.gofun:id/imgArgee")
            self.sleep(5)
            # 预定整租
            self.find_click_element_by_id("com.gvsoft.gofun:id/tv_WholeRent")
            if self.exist_text("确定"):
                self.find_click_element_by_text("确定")'''

            if not self.homePageCtrl.wholeR_reserveSuc():
                self.fail("整租未成功！")
            # 取消预定
            self.homePageCtrl.wholeR_cancel()
            if not self.homepage.menu_exist():
                self.fail("back to homepage fail!")
        else:
            self.addCaseStep("未找到整租车辆图片")

    def MTBF_preferentialCar_01_screen(self):
        self.addCaseStep("特惠车界面测试")
        self.homepage.tehui_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        if not (self.homepage.tehui_exist() or self.homepage.tehui_exist1()):
            self.fail("fail to enter [tehui] tab")
        # if self.exist_text("顺路用车超划算", "判断是否存在【顺路用车超划算】提示"):
        #     self.addCaseStep("存在【顺路用车超划算】提示")
        # else:
        #     self.fail("不存在【特惠车】")

    def test_gofun_MTBF_other01_navigation(self):
        self.app_init()
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        if not self.goto_reserve_homepage():
            return
        self.reserve_car()
        self.navigation()
        self.cancel_order()

    def test_gofun_MTBF_other02_time_makeAnApp01(self):
        self.app_init()
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        self.goto_reserve_make_an_app()
        self.reserve_car()
        self.cancel_maa()

    def test_gofun_MTBF_other03_daily_makeAnApp01(self):
        self.app_init()
        self.homepage.daily_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        self.goto_reserve_make_an_app()
        self.reserve_car()
        self.cancel_maa_two()

    def test_gofun_MTBF_home01_zoomRandom(self):
        self.app_init()
        self.MTBF_home01_zoomRandom()

    def test_gofun_MTBF_home02_Swipe(self):
        self.app_init()
        self.MTBF_home02_Swipe()

    def test_gofun_MTBF_home03_Num(self):
        self.app_init()
        self.MTBF_home03_Num()


    def test_gofun_MTBF_home04_Zoom_in(self):
        self.app_init()
        self.MTBF_home04_Zoom_in()

    def test_gofun_MTBF_home05_filter(self):
        self.app_init()
        self.MTBF_home05_filter()


    # 已无此功能418
    def test_gofun_MTBF_home06_report(self):
        self.app_init()
        self.addCaseStep("点击首页【问题上报】")
        self.find_click_element_by_id(self.appConfig.get("HOME.USER.REPORT"), "[User Report] icon")
        self.sleep(12)
        if not self.title_exist(text="问题上报"):
            self.fail("Go to [User Report] fail")
        if not self.exist_text("上报内容一经核实可得", "问题上报：能量方块"):
            self.fail("问题上报页面无获得能量方块提示")
        self.addCaseStep("【问题上报】页面存在获得【能量方块】提示")
        problem_list = self.appConfig.get_list("USER.REPORT.PROBLEM")
        for problem in problem_list:
            self.addCaseStep("点击 %s" % problem)
            self.find_click_element_by_text(problem, problem)
            self.sleep(8)
            if not self.title_exist(text=problem):
                self.fail("Go to %s fail" % problem)
            self.addCaseStep("点击back图标，返回【问题上报】主页")
            self.t_keyevent("BACK")
            self.sleep(8)
            if not self.title_exist(text="问题上报"):
                self.fail("Back to [User Report] fail")

    def test_gofun_MTBF_home08_switch_city(self):
        self.app_init()
        self.MTBF_home08_switch_city()

    def test_gofun_MTBF_home09_search(self):
        self.app_init()
        self.MTBF_home09_search()

    def test_gofun_MTBF_home10_car_reminder(self):
        self.app_init()
        self.MTBF_home10_car_reminder()

    def test_gofun_MTBF_home11_message(self):
        self.app_init()
        self.MTBF_home11_message()

    def test_gofun_MTBF_PersonalCenter01_wallet(self):
        self.app_init()
        self.MTBF_PersonalCenter01_wallet()

    def test_gofun_MTBF_PersonalCenter02_trip(self):
        self.app_init()
        self.MTBF_PersonalCenter02_trip()

    def test_gofun_MTBF_PersonalCenter03_customer_service(self):
        self.app_init()
        self.MTBF_PersonalCenter03_customer_service()

    def test_gofun_MTBF_PersonalCenter04_activity(self):
        self.app_init()
        self.MTBF_PersonalCenter04_activity()

    def test_gofun_MTBF_PersonalCenter05_invitation(self):
        self.app_init()
        self.MTBF_PersonalCenter05_invitation()

    def test_gofun_MTBF_PersonalCenter06_illegal_traffic(self):
        self.app_init()
        self.MTBF_PersonalCenter06_illegal_traffic()

    # def test_gofun_MTBF_PersonalCenter07_push(self):
    #     self.app_init()
    #     self.MTBF_PersonnalCenter07_push()

    def test_gofun_MTBF_PersonalCenter08_setting(self):
        self.app_init()
        self.MTBF_PersonalCenter08_setting()

    def test_gofun_MTBF_PersonalCenter09_recommendBuildPoint(self):
        self.app_init()
        self.MTBF_PersonalCenter09_recommendBuildPoint()

    def test_gofun_MTBF_PersonalCenter10_my_medal(self):
        self.app_init()
        self.MTBF_PersonalCenter10_my_medal()

    def test_gofun_MTBF_PersonalCenter11_wmf(self):
        self.app_init()
        self.MTBF_PersonalCenter11_wmf()
        
    def test_gofun_MTBF_PersonalCenter12_coupon(self):
        self.app_init()
        self.MTBF_PersonalCenter12_coupon()


    def test_gofun_MTBF_main_01_order_car(self):
        self.app_init()
        self.addCaseStep("点击【分时】按钮")
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        if not self.goto_reserve_homepage():
            self.fail("no reserve page")
        self.reserve_car()
        face_recongnization = self.pick_up_car()
        if face_recongnization:
            self.drive_car()
            self.return_car()
            self.commmit_evaluation()
        else:
            self.cancel_order()

    def test_gofun_MTBF_main_02_free_return(self):
        self.app_init()
        self.xml_address = self.h5_element_path
        self.addCaseStep("点击【分时】按钮")
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        if not self.goto_reserve_homepage():
            self.fail("no reserve page")
        self.reserve_car()
        face_recongnization = self.pick_up_car()
        if face_recongnization:
            self.free_return()
        else:
            self.cancel_order()

    def test_gofun_MTBF_main_03_cancel_order(self):
        self.app_init()
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        if not self.goto_reserve_homepage():
            self.fail("no reserve page")
        self.reserve_car()
        self.cancel_order()

    def test_gofun_MTBF_Daily_main_03_cancel_order(self):
        self.app_init()
        self.homepage.daily_click()
        self.sleep(6)
        self.homePageCtrl.ad_close()
        if not self.goto_reserve_homepage():
            self.fail("no reserve page")
        self.reserve_car(commit_button=2)
        self.daily_cancel_order()

    def test_gofun_MTBF_rent_01_screen(self):
        self.app_init()
        self.MTBF_rent_01_screen()

    def test_gofun_MTBF_preferentialCar_01_screen(self):
        self.app_init()
        self.MTBF_preferentialCar_01_screen()

    @per_app
    def test_gofun_PERF_home01_zoomRandom(self):
        self.app_init()
        for i in range(2):
            self.MTBF_home01_zoomRandom()

    @per_app
    def test_gofun_PERF_home02_Swipe(self):
        self.app_init()
        for i in range(2):
            self.MTBF_home02_Swipe()

    @per_app
    def test_gofun_PERF_main_01_order_car(self):
        for i in range(2):
            self.app_init()
            self.homepage.timeD_click()
            self.sleep(5)
            self.homePageCtrl.ad_close()
            self.sleep(2)
            if not self.goto_reserve_homepage():
                self.fail("no reserve page")
            self.reserve_car()
            self.pick_up_car()
            self.drive_car()
            self.return_car()
            self.commmit_evaluation()

    @per_app
    def order_car_part(self):
        self.reserve_car()
        self.pick_up_car()
        self.drive_car()

    def test_gofun_PERF_main_02_order_car_part(self):
        self.app_init()
        self.homepage.timeD_click()
        self.sleep(5)
        self.homePageCtrl.ad_close()
        self.sleep(2)
        if not self.goto_reserve_homepage():
            self.fail("no reserve page")
        self.order_car_part()
        self.return_car()
        self.commmit_evaluation()
