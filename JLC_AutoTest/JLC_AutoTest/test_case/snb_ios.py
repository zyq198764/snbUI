from JLC_AutoTest.model.appunit import AppTest
import unittest
import time
from JLC_AutoTest.common.settings import log
from JLC_AutoTest.common.logger import Log
from JLC_AutoTest.page.page_object.snb_unlogin_page import SNB_Unlogin_page
from JLC_AutoTest.model.base import Base
from JLC_AutoTest.page.page_object.snb_login_page import SNB_login_page
from JLC_AutoTest.page.page_object.snb_bank_card_page import SNB_bank_card_page
from JLC_AutoTest.page.page_object.snb_set_password_page import SNB_set_passwd_page
from JLC_AutoTest.page.page_object.snb_buy_page import SNB_Buy_now_page
from JLC_AutoTest.page.page_object.snb_redeem_page import SNB_Redeem_page
from JLC_AutoTest.page.page_object.snb_my_page import SNB_My_page
from JLC_AutoTest.common.function import save_img
from JLC_AutoTest.page.page_object.snb_hold_page import SNB_hold_page


class Test_SNB_Regression(AppTest):
    '''拾年宝UI自动化ios测试'''
    log = Log()

    """def test_01_unlogin(self):
        '''未登陆首页测试'''

        time.sleep(3)
        self.log.info("-------------未登陆首页测试：start！-------------")
        try:
            Snb_Unlogin_po = SNB_Unlogin_page(self.driver)

            time.sleep(10)
            self.driver.element_by_name('立即买入').click()
            time.sleep(4)
            # 以下是页面元素的校验
            self.log.info("获取未登陆首页的title")
            title = Snb_Unlogin_po.get_Unlogin_Title_Loc_page()
            print(title)
            self.assertEqual('拾年保', title)
            time.sleep(1)
            #
            # self.log.info("获取文案低风险基金组合产品")
            # print(Snb_Unlogin_po.get_unlogin_lowriskfundtext_loc_page())
            # self.assertEqual('低风险基金组合产品', Snb_Unlogin_po.get_unlogin_lowriskfundtext_loc_page())
            # time.sleep(1)

            self.log.info("获取基金销售合作文案")
            print(Snb_Unlogin_po.get_unlogin_lic_fundsales_loc_page())
            self.assertEqual("与正规持牌机构奕丰金融基金销售合作", Snb_Unlogin_po.get_unlogin_lic_fundsales_loc_page())
            time.sleep(1)


            self.log.info("获取证书编码的文案")
            self.assertEqual("(证书编码：000000381)", Snb_Unlogin_po.get_unlogin_certicode_loc_page())
            time.sleep(1)
            #
            # self.log.info("获取低风险的文案")
            # self.assertEqual("低风险 低手续费 500元起投", Snb_Unlogin_po.get_unlogin_midtext_loc_page())
            # time.sleep(1)

            # self.log.info("获取历史年华收益率")
            # self.assertEqual("7.43%",Snb_Unlogin_po.get_unlogin_lssyltext_loc_page())
            # time.sleep(1)
            #
            # self.log.info("获取赎回无限制的文案")
            # self.assertEqual("赎回无限制", Snb_Unlogin_po.get_unlogin_reedmunlimited_loc_page())
            # time.sleep(1)

            # 需要执行一下向上滑动页面
            self.log.info('开始向上滑动页面')
            for i in range(3):
                Snb_Unlogin_po.swipe_up_new(duration=1)

            time.sleep(2)

            self.log.info("获取历史平均万元日收益的文案")
            self.assertEqual("历史平均万元日收益(元)", Snb_Unlogin_po.get_unlogin_Histor_loc_page())
            time.sleep(1)

            self.log.info("获取历史正收益天数占比的文案")
            self.assertEqual("历史正收益天数占比", Snb_Unlogin_po.get_unlogin_historicalpos_loc_page())
            time.sleep(1)

            self.log.info('开始向下滑动页面')
            for i in range(3):
                Snb_Unlogin_po.swipe_down_new(duration=1)

            # 以下是元素的元素的操作
            self.log.info("点击立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            self.log.info('已经点击立即买入按钮')
            time.sleep(2)
            self.log.info("点击登录页面的关闭按钮")
            self.driver.element_by_name(
                '关闭').click()
            time.sleep(2)

            # 再次进入到未登录首页
            self.driver.element_by_name('立即买入').click()
            time.sleep(2)
            self.log.info("点击你有10元奖学金可领取")
            Snb_Unlogin_po.get_unlogin_scholarship_loc_page()
            self.log.info('已经点击你有10元奖学金可领取')
            time.sleep(2)
            self.log.info('点击关闭按钮')
            self.driver.element_by_name(
                '关闭').click()
            time.sleep(2)

            # self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            # time.sleep(2)
            # self.log.info("开始点击banner")
            # Snb_Unlogin_po.get_unlogin_banner_loc_page()
            # self.log.info("已经点击banner")
            # time.sleep(2)
            # self.log.info("点击关闭按钮")
            # self.driver.element_by_xpath('//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]').click()
            # time.sleep(2)

            # 进入到未登陆首页
            time.sleep(2)
            self.driver.element_by_name('立即买入').click()
            time.sleep(4)
            self.log.info("点击立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            self.log.info('已经点击立即买入按钮')
            time.sleep(2)

        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
        self.log.info("-------------------未登陆首页测试：end!--------------------")

        # 注册脚本

    def test_02_login(self):
        ''' 注册测试'''

        self.log.info("-------------注册测试：start!-------------------")

        try:
            Snb_login_po=SNB_login_page(self.driver)

            #以下是数据的校验
            time.sleep(15)
            self.log.info("开始点击注册页面的，注册按钮")
            Snb_login_po.get_login_registbutton_Loc_page()
            self.log.info("已经点击注册按钮，进入到注册页面")
            time.sleep(2)


            self.log.info("校验登录注册页面的title是否是注册登录")
            self.assertEqual("注册/登录",Snb_login_po.get_login_title_Loc_page())
            time.sleep(2)

            self.log.info("校验输入手机号输入框中的文本是否是请输入手机号")
            self.assertEqual("请输入手机号码",Snb_login_po.get_login_input_phone_Loc_text_page())
            time.sleep(2)
            self.log.info("校验是否显示注册协议")
            self.assertEqual("注册即同意",Snb_login_po.get_login_regist_agree_Loc_page())
            time.sleep(2)

            #以下是操作
            self.log.info('开始点击登录按钮')
            Snb_login_po.get_login_loginbutton_Loc_page()
            self.log.info("已经点击登录按钮，进入到登录页面")
            time.sleep(2)
            self.log.info("开始点击注册页面的，注册按钮")
            Snb_login_po.get_login_registbutton_Loc_page()
            self.log.info("已经点击注册按钮，进入到注册页面")
            time.sleep(2)

            # self.log.info("输入错误的手机号：11111111111")
            # Snb_login_po.get_login_input_error_phone_Loc_page()
            # time.sleep(2)
            # 
            # self.log.info("获取给出的错误提示")
            # error_text=Snb_login_po.get_login_input_error_phone_text_Loc_page()
            # self.log.info("错误提示是:%s"%error_text)
            # time.sleep(2)
            # 
            # save_img(driver=self.driver,file_name='error_phone')
            # time.sleep(2)
            # 
            # self.log.info("清除输入的手机号码")
            # Snb_login_po.get_login_icon_Loc_page()
            # self.log.info("已经清除完成")
            # time.sleep(2)
            #
            #
            # self.log.info("输入已注册的手机号")
            # Snb_login_po.get_login_input_phone_Loc_page()
            # self.log.info("已经输入注册的手机号")
            # time.sleep(2)
            #
            # self.log.info("开始点击注册按钮")
            # Snb_login_po.get_login_regist_button_Loc_page()
            # self.log.info("已经点击注册按钮")
            # time.sleep(2)
            #
            # self.log.info("校验是否弹出提示语")
            # self.assertEqual("该号码已注册",Snb_login_po.get_login_Registered_Loc_page())
            # time.sleep(2)
            # #
            # # self.log.info("清除输入的手机号码")
            # # Snb_login_po.get_login_icon_Loc_page()
            # # self.log.info("已经清除完成")
            # # time.sleep(2)

            self.log.info("输入未注册的手机号")
            Snb_login_po.get_login_input_unregphone_Loc_page()
            self.log.info("已经输入未注册的手机号")
            time.sleep(2)

            self.log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            self.log.info("已经点击注册按钮")
            time.sleep(2)

            self.log.info("校验短信验证码输入框中文案")
            self.assertEqual("请输入短信验证码",Snb_login_po.get_login_verficode_Loc_text_page())
            time.sleep(2)
            # self.log.info("输入错误的短信验证码")
            # Snb_login_po.get_login_error_verficode_Loc_page()
            # time.sleep(2)
            #
            self.log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            self.log.info("已经点击注册按钮")
            time.sleep(2)
            #
            # self.log.info("获取输入错误短信验证码的提示语")
            # error_vercode=Snb_login_po.get_login_error_verficode_text_loc_page()
            # self.log.info("输入错误的我的短信验证码的提示语是：%s"%error_vercode)
            # time.sleep(2)
            #
            # save_img(driver=self.driver,file_name='error_vercode')
            # time.sleep(2)
            time.sleep(32)
            self.log.info('点击重新发送按钮')
            Snb_login_po.get_login_verficode_click_Loc_page()
            time.sleep(2)
            #

            self.log.info("输入正确的短信验证码")
            Snb_login_po.get_login_verficode_Loc_page()
            self.log.info("已经输入短信验证码")
            time.sleep(2)

            self.log.info("开始点击注册按钮")
            Snb_login_po.get_login_regist_button_Loc_page()
            self.log.info("已经点击注册按钮")
            time.sleep(2)

            # 以下是设置登录密码的操作
            self.log.info("校验设置登录密码页面的title")
            self.assertEqual("设置登录密码",Snb_login_po.get_login_set_passwd_title_Loc_page())
            time.sleep(2)

            self.log.info("检验设置密码的要求文案")
            self.assertEqual("8-20位英文与数字组合并区分大小写",Snb_login_po.get_login_set_passwd_requi_Loc_page())
            time.sleep(2)

            self.log.info("获取输入密码时，输入框中的文案")
            self.assertEqual("请设置登录密码",Snb_login_po.get_login_input_passwd_Loc_text_page())
            time.sleep(2)


            self.log.info("输入密码")
            Snb_login_po.get_login_input_passwd_Loc_page()
            time.sleep(2)

            self.log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)


            # 重新输入登录密码
            self.log.info("再次输入登录密码")
            Snb_login_po.get_login_reinput_passwd_Loc_page()
            time.sleep(2)

            self.log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)


        except Exception as msg:

            self.log.info("异常信息：%s"%msg)

        self.log.info("-----------------注册登录测试：end!-------------------")


    #添加银行卡脚本
    def test_03_add_bank_card(self):
        '''添加银行卡测试'''
        self.log.info("-------------添加银行卡测试：start!-------------------")

        try:
            Snb_add_bank_card_po = SNB_bank_card_page(self.driver)

            #点击我的tab
            time.sleep(15)
            time.sleep(4)
            self.log.info("开始点击我的tab")
            Snb_add_bank_card_po.get_my_tab_Loc_page()
            self.log.info('已经进入到我的页面')
            time.sleep(2)

            #点击我的银行卡
            self.log.info("开始点击我的银行卡")
            Snb_add_bank_card_po.get_my_bank_card_Loc_page()
            self.log.info("已经进入到我的银行卡页面")
            time.sleep(4)
            #刚进入到银行卡页面进行截图
            save_img(driver=self.driver,file_name='bank_card')
            time.sleep(2)

            # 以下是添加银行卡的操作
            self.log.info("校验添加银行卡的title是否是添加银行卡")
            self.assertEqual("添加银行卡",Snb_add_bank_card_po.get_add_bank_card_title_Loc_page())
            time.sleep(2)

            self.log.info("校验获取的持卡人文本")
            self.assertEqual("持卡人",Snb_add_bank_card_po.get_add_bank_card_name_text_Loc_page())
            time.sleep(2)

            # self.log.info("点击持卡人旁边的图标")
            # Snb_add_bank_card_po.get_add_bank_card_name_icon_Loc_page()
            # time.sleep(2)

            # save_img(driver=self.driver,file_name='bank_name')
            # time.sleep(2)
            #
            # self.log.info("点击持卡人弹层中的我知道了按钮")
            # Snb_add_bank_card_po.get_add_bank_card_name_icon_button_Loc_page()
            # time.sleep(2)

            time.sleep(2)
            Snb_add_bank_card_po.get_add_bank_card_name_clickLoc_page()
            time.sleep(2)

            self.log.info("输入持卡人姓名")
            Snb_add_bank_card_po.get_add_bank_card_name_Loc_page()
            time.sleep(10)


            self.log.info("校验身份证号的文本")
            self.assertEqual("身份证号",Snb_add_bank_card_po.get_add_bank_card_id_text_Loc_page())
            time.sleep(2)

            self.log.info("开始输入身份证号")
            Snb_add_bank_card_po.get_add_bank_card_id_Loc_page()
            self.log.info("已经输入完身份证号码")
            time.sleep(2)


            #点击弹窗中的关闭按钮

            self.log.info("校验卡号的文本")
            self.assertEqual("卡号",Snb_add_bank_card_po.get_add_bank_card_num_Loc1_page())
            time.sleep(2)

            self.log.info("输入银行卡号")
            Snb_add_bank_card_po.get_add_bank_card_num_Loc_page()
            self.log.info("已经输入了银行卡号")
            time.sleep(2)

            self.log.info("向上滑动下页面")
            Snb_add_bank_card_po.swipe_up_new_ios(duration=1)
            time.sleep(2)

            self.log.info("校验银行卡文本")
            self.assertEqual("银行卡",Snb_add_bank_card_po.get_add_bank_card_text__Loc_page())
            time.sleep(2)

            self.log.info("点击选择银行卡")
            Snb_add_bank_card_po.get_add_bank_card__Loc_page()
            time.sleep(2)

            #截图银行列表
            save_img(driver=self.driver,file_name='bank_list')
            time.sleep(2)

            self.log.info("选择招商银行")
            Snb_add_bank_card_po.get_add_bank_card_list_pop__Loc_page()
            self.log.info("已经选择招商银行")
            time.sleep(2)

            self.log.info("校验银行预留手机号文本")
            self.assertEqual("银行预留手机号",Snb_add_bank_card_po.get_add_bank_card_phone_text_Loc_page())
            time.sleep(2)

            self.log.info("输入银行预留手机号码")
            Snb_add_bank_card_po.get_add_bank_card_phone_Loc_page()
            self.log.info("已经输入完手机号码")
            time.sleep(2)

            self.log.info("校验短信验证码文本")
            self.assertEqual("短信验证码",Snb_add_bank_card_po.get_add_bank_card_vercode_text_Loc_page())
            time.sleep(2)

            self.log.info("点击获取验证码")
            Snb_add_bank_card_po.get_add_bank_card_clickvercode_Loc_page()
            time.sleep(2)

            Snb_add_bank_card_po.get_add_bank_card_vercode_click_Loc_page()
            time.sleep(2)

            self.log.info("输入短信验证码")
            Snb_add_bank_card_po.get_add_bank_card_vercode_Loc_page()
            time.sleep(2)

            self.log.info("点击确认添加按钮")
            Snb_add_bank_card_po.get_add_bank_card_confirm_button_Loc_page()
            time.sleep(2)

        except Exception as msg:
            self.log.info('异常信息：%s'%msg)
        self.log.info("---------------添加银行卡测试：end!-------------------")

    #设置支付密码
    def test_04_set_passwd(self):
        ''' 设置支付密码测试'''
        self.log.info("-------------设置支付密码测试：start!-------------------")

        try:
            Snb_set_passwd_po = SNB_set_passwd_page(self.driver)
            Snb_My_po = SNB_My_page(self.driver)

            time.sleep(10)
            time.sleep(2)
            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的")

            self.log.info("点击设置支付密码")
            Snb_set_passwd_po.get_set_passwd_Loc_page()
            self.log.info("已经点击设置支付密码")
            time.sleep(2)

            self.log.info("校验获取的页面标题")
            self.assertEqual("设置支付密码",Snb_set_passwd_po.get_set_passwd_title_Loc_page())
            time.sleep(2)

            self.log.info("输入设置的支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(2)
            self.log.info("已设置支付密码122455")

            # Snb_set_passwd_po.get_set_passwd_confirm_Loc_page()
            # time.sleep(2)

            self.log.info("再次输入设置的支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(2)
            self.log.info("已设置支付密码成功，跳转到首页")

        except Exception as msg:
            self.log.info('异常信息：%s' % msg)
        self.log.info("---------------设置支付密码测试：end!-------------------")"""

    #立即买入

    def test_05_buy_now(self):

        ''' 测试立即买入测试'''

        self.log.info("-------------立即买入测试：start!-------------------")
        try:
            Snb_buy_now_po=SNB_Buy_now_page(self.driver)
            Snb_hold_po=SNB_hold_page(self.driver)
            time.sleep(15)
            time.sleep(3)
            # self.log.info("点击首页的立即买入按钮")
            # Snb_buy_now_po.get_buy_now_button_loc_page()
            # self.log.info("已经进入到立即买入按钮")
            # time.sleep(4)
            #
            # self.log.info("校验买入页面的title")
            # self.assertEqual("买入",Snb_buy_now_po.get_buy_now_title_loc_page())
            # time.sleep(2)
            #
            # self.log.info("校验买入页面的支付方式")
            # self.assertEqual("支付方式",Snb_buy_now_po.get_buy_now_pay_method_loc_page())
            # time.sleep(2)
            #
            # self.log.info("校验买入金额的文本")
            # self.assertEqual("买入金额",Snb_buy_now_po.get_buy_now_pay_amount_loc_page())
            # time.sleep(2)
            #
            # self.log.info("校验买入金额输入框中的提示语文本")
            # self.assertEqual("最小买入金额1,000.00",Snb_buy_now_po.get_buy_now_pay_amount_text_loc_page())
            # time.sleep(2)
            #
            #
            #
            # self.log.info("点击金额输入框")
            # Snb_buy_now_po.get_buy_now_pay_amount_click_page()
            # time.sleep(2)
            #
            # self.log.info("输入买入金额小于10000")
            # Snb_buy_now_po.get_buy_now_pay_amount_input_page()
            # time.sleep(2)
            #
            # self.log.info("查看金额小于1000的提示语")
            # self.assertEqual("买入金额不能小于最小买入金额1,000.00元",Snb_buy_now_po.get_buy_now_error_msg_loc_page())
            # time.sleep(2)
            #
            # save_img(driver=self.driver, file_name='buy_tips')
            # time.sleep(2)
            #
            # self.log.info("向上滑动下页面")
            # for i in range(2):
            #     Snb_buy_now_po.swipe_up_new_ios(duration=1)
            #     time.sleep(2)
            #
            # # self.log.info("点击单选框")
            # # Snb_buy_now_po.get_buy_now_single_box_loc_page()
            # # self.log.info("点击完成后是未被选中的状态")
            # # time.sleep(2)
            # #
            # # self.log.info("再次点击单选框")
            # # Snb_buy_now_po.get_buy_now_single_box_loc_page()
            # # self.log.info("点击完成后是选中的状态")
            # # time.sleep(2)
            # #
            # # self.log.info("校验业务规则的文本")
            # # self.assertEqual("同意《拾年保基金组合交易业务规则》",Snb_buy_now_po.get_buy_now_bus_rules_loc_page())
            # # time.sleep(2)
            #
            # self.log.info("校验民生监管的文本")
            # self.assertEqual("民生银行监管",Snb_buy_now_po.get_buy_now_ms_jg_loc_page())
            # time.sleep(2)
            #
            # self.log.info("点击奕丰金融文本")
            # Snb_buy_now_po.get_buy_now_yf_jr_loc_page()
            # self.log.info("已经弹出弹层")
            # time.sleep(2)
            #
            # self.log.info("再次点击奕丰金融弹层")
            # Snb_buy_now_po.get_buy_now_ms_jg_loc_click_page()
            # self.log.info("弹层消失")
            # time.sleep(2)
            #
            # self.log.info("向下滑动下页面")
            # for i in range(2):
            #     Snb_buy_now_po.swipe_down_new(duration=1)
            #     time.sleep(2)
            #
            # self.log.info("先光标定位买入金额输入框中")
            # Snb_buy_now_po.get_buy_now_pay_amount_click1_page()
            # time.sleep(2)
            #
            # self.log.info("输入买入的金额大于1000")
            # Snb_buy_now_po.get_buy_now_pay_amount_inputmoreios_page()
            # self.log.info("已经输入买入金额")
            # time.sleep(4)
            #
            # self.log.info("点击确认买入按钮")
            # Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的确认评测按钮")
            # Snb_buy_now_po.get_buy_now_evaluation_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第一个问题")
            # Snb_buy_now_po.get_buy_now_evaluation01_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第二个问题")
            # Snb_buy_now_po.get_buy_now_evaluation02_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第三个问题")
            # Snb_buy_now_po.get_buy_now_evaluation03_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第四个问题")
            # Snb_buy_now_po.get_buy_now_evaluation04_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第五个问题")
            # Snb_buy_now_po.get_buy_now_evaluation05_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的第六个问题")
            # Snb_buy_now_po.get_buy_now_evaluation06_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的完成按钮")
            # Snb_buy_now_po.get_buy_now_evaluation_button_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击风险测评中的确认无误按钮")
            # Snb_buy_now_po.get_buy_now_evaluation_confirmbutton_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击评测结果按钮")
            # Snb_buy_now_po.get_buy_now_evaluation_confirmres_loc_page()
            # time.sleep(2)

            # self.log.info("输入买入的金额")
            # Snb_buy_now_po.get_buy_now_pay_amount_input_pay_page()
            # self.log.info("已经输入买入金额")
            # time.sleep(2)
            #
            # self.log.info("点击确认买入按钮")
            # Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            # time.sleep(2)
            #
            # self.log.info("校验支付密码输入框中的标题")
            # self.assertEqual("请输入基金支付密码",Snb_buy_now_po.get_buy_now_pay_pass_text_loc_page())
            # time.sleep(2)
            #
            # self.log.info("校验支付密码输入框下方的文本")
            # self.assertEqual("基金销售服务由奕丰金融提供",Snb_buy_now_po.get_buy_now_pay_pass_yf_text_loc_page())
            # time.sleep(2)
            #输入错误的支付密码
            # self.log.info("输入错误的支付密码")
            # Snb_buy_now_po.get_set_passwd_01Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_04Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_05Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_07Loc_page()
            # time.sleep(3)
            # self.log.info("已经输入错误的支付密码122457")
            #
            # self.log.info("弹出错误支付密码的弹窗，点击重新输入")
            # Snb_buy_now_po.get_buy_now_error_password_input_Loc_page()
            # time.sleep(3)


            # #输入正确的支付密码
            # self.log.info("输入正确的支付密码")
            # Snb_buy_now_po.get_set_passwd_01Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_04Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_05Loc_page()
            # time.sleep(3)
            # Snb_buy_now_po.get_set_passwd_05Loc_page()
            # time.sleep(3)
            # self.log.info("已经输入支付密码122455")
            # time.sleep(3)
            # self.log.info("校验买入完成页面的title")
            # self.assertEqual("买入完成",Snb_buy_now_po.get_buy_now_complete_loc_page())
            # time.sleep(2)

            # save_img(driver=self.driver,file_name='buy_complete')
            # time.sleep(2)
            #
            # self.log.info("点击买入完成页面的完成按钮")
            # Snb_buy_now_po.get_buy_now_complete_button_loc_page()
            # time.sleep(2)

            # time.sleep(15)
            # self.log.info("点击持有页面的空白处")
            # Snb_hold_po.get_hold_jcrdu_loc_page()
            # time.sleep(2)
            #
            # self.log.info("买入完成后跳转到持有页面，点击持有页面的单笔买入按钮")
            # Snb_buy_now_po.get_buy_now_single_buy_Loc_page()
            # self.log.info("已经进入到买入页面")
            # time.sleep(3)
            #
            # #以下是短信验证码买入
            #
            # self.log.info("输入买入的金额")
            # Snb_buy_now_po.get_buy_now_pay_amount_input_pay_page()
            # self.log.info("已经输入买入金额")
            # time.sleep(2)

            # self.log.info("点击确认买入按钮")
            # Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击下空白页面")
            # Snb_buy_now_po.get_buy_now_pay_method_click_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击短信验证码输入框中的取消按钮")
            # Snb_buy_now_po.get_buy_now_verficode_cancel_Loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击确认买入按钮")
            # Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            # time.sleep(2)
            #
            # save_img(driver=self.driver,file_name='buy_verficode')
            # time.sleep(2)
            #
            #
            # self.log.info("校验验证码输入框的文本")
            # self.assertEqual("请输入验证码",Snb_buy_now_po.get_buy_now_verficode_Loc_page())
            # time.sleep(62)
            #
            # self.log.info("点击重新发送按钮")
            # Snb_buy_now_po.get_buy_now_verficode_resendLoc_page()
            # time.sleep(2)
            #
            # self.log.info('输入错误的短信验证码')
            # Snb_buy_now_po.get_buy_now_errorverficode_input_Loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击下空白页面")
            # Snb_buy_now_po.get_buy_now_pay_method_click_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击确认按钮")
            # Snb_buy_now_po.get_buy_now_verficode_confirm_Loc_page()
            # time.sleep(2)
            #
            #
            #
            # self.log.info("输入正确的短信验证码888888")
            # Snb_buy_now_po.get_buy_now_verficode_input_Loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击下空白页面")
            # Snb_buy_now_po.get_buy_now_pay_method_click_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击确认按钮")
            # Snb_buy_now_po.get_buy_now_verficode_confirm_Loc_page()
            # time.sleep(2)
            #
            # #再次输入支付密码
            # self.log.info("输入正确的支付密码")
            # Snb_buy_now_po.get_set_passwd_01Loc_page()
            # time.sleep(1)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(1)
            # Snb_buy_now_po.get_set_passwd_02Loc_page()
            # time.sleep(1)
            # Snb_buy_now_po.get_set_passwd_04Loc_page()
            # time.sleep(1)
            # Snb_buy_now_po.get_set_passwd_05Loc_page()
            # time.sleep(1)
            # Snb_buy_now_po.get_set_passwd_05Loc_page()
            # time.sleep(2)
            # self.log.info("已经输入支付密码122455")
            #
            # self.log.info("校验买入完成页面的title")
            # self.assertEqual("买入完成", Snb_buy_now_po.get_buy_now_complete_loc_page())
            # time.sleep(2)
            #
            # self.log.info("点击买入完成页面的完成按钮")
            # Snb_buy_now_po.get_buy_now_complete_button_loc_page()
            time.sleep(2)

            #以下是大额买入的操作
            self.log.info("输入买入的金额")
            Snb_buy_now_po.get_buy_now_pay_amount_input_pay_page()
            self.log.info("已经输入买入金额")
            time.sleep(2)

            self.log.info("点击确认买入按钮")
            Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            time.sleep(2)

            self.log.info("点击大额买入弹层中的取消按钮")
            Snb_buy_now_po.get_buy_now_big_buy_cancelLoc_page()
            time.sleep(2)

            self.log.info("再次点击确认买入按钮")
            Snb_buy_now_po.get_buy_now_confirm_button_loc_page()
            time.sleep(2)

            self.log.info('点击大额买入按钮')
            Snb_buy_now_po.get_buy_now_big_buy_buttonLoc_page()
            time.sleep(2)

            self.log.info('校验大额买入申请的title为大额买入')
            self.assertEqual('大额买入',Snb_buy_now_po.get_buy_now_big_buy_titleLoc_page())
            time.sleep(2)

            self.log.info('点击申请转账按钮')
            Snb_buy_now_po.get_buy_now_big_buy_apply_Loc_page()
            time.sleep(2)

            self.log.info('点击申请转账成功弹层中的我知道了按钮')
            Snb_buy_now_po





        except Exception as msg:
            self.log.info("异常信息：%s"%msg)
        self.log.info("------------立即买入测试：end!------------------")

    """def test_06_login(self):
        ''' 测试登录的操作'''

        self.log.info("-------------登录测试：start!-------------------")
        try:
            Snb_My_po = SNB_My_page(self.driver)
            Snb_Unlogin_po = SNB_Unlogin_page(self.driver)
            Snb_login_po = SNB_login_page(self.driver)

            time.sleep(15)

            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的页面")
            time.sleep(2)

            self.log.info("开始点击我的页面的安全退出按钮")
            Snb_My_po.get_my_retreat_safely_Loc_page()
            time.sleep(2)

            self.log.info("点击弹窗中的确认按钮")
            Snb_My_po.get_my_retreat_safely_confirm_button_Loc_page()
            self.log.info("已经退出登录，进入到未登录的首页")
            time.sleep(2)

            self.log.info("点击未登录页面的立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            time.sleep(4)

            # 以下是验证码登录
            self.log.info("点击切换账号")
            Snb_My_po.get_login_switch_account_Loc_page()
            time.sleep(4)

            self.log.info("输入手机号")
            Snb_My_po.get_login_input_phone_Loc_page()
            time.sleep(2)

            self.log.info("点击下一步按钮")
            Snb_My_po.get_login_input_phone_next_button_Loc_page()
            time.sleep(2)

            self.log.info("输入短信验证码")
            Snb_My_po.get_login_verficode_input_Loc_page()
            time.sleep(2)

            self.log.info("点击登录按钮")
            Snb_My_po.get_login_button_Loc_page()
            self.log.info("已经登录成功")
            time.sleep(2)

            # 以下是密码登录
            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的页面")
            time.sleep(2)

            self.log.info("开始点击我的页面的安全退出按钮")
            Snb_My_po.get_my_retreat_safely_Loc_page()
            time.sleep(2)

            self.log.info("点击弹窗中的确认按钮")
            Snb_My_po.get_my_retreat_safely_confirm_button_Loc_page()
            self.log.info("已经退出登录，进入到未登录的首页")
            time.sleep(2)

            self.log.info("点击未登录页面的立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            time.sleep(2)

            self.log.info("点击登录密码登录")
            Snb_My_po.get_login_password_login_Loc_page()
            time.sleep(2)

            self.log.info("输入登录密码")
            Snb_My_po.get_login_password_input_Loc_page()
            time.sleep(2)

            self.log.info("点击登录按钮")
            Snb_My_po.get_login_button_Loc_page()
            self.log.info("已经登录成功")
            time.sleep(2)

            # 以下是忘记密码的操作
            # 1.点击忘记密码，2，输入验证码，点击下一步按钮，3设置登录密码，4，确认登录密码 5，点击登录
            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的页面")
            time.sleep(2)

            self.log.info("开始点击我的页面的安全退出按钮")
            Snb_My_po.get_my_retreat_safely_Loc_page()
            time.sleep(2)

            self.log.info("点击弹窗中的确认按钮")
            Snb_My_po.get_my_retreat_safely_confirm_button_Loc_page()
            self.log.info("已经退出登录，进入到未登录的首页")
            time.sleep(2)

            self.log.info("点击未登录页面的立即买入按钮")
            Snb_Unlogin_po.get_unlogin_buynow_button_loc_page()
            time.sleep(2)

            self.log.info("点击登录密码登录")
            Snb_My_po.get_login_password_login_Loc_page()
            time.sleep(2)
            #
            self.log.info("点击忘记密码")
            Snb_My_po.get_login_forget_password_Loc_page()
            time.sleep(2)
            #
            self.log.info("输入短信验证码")
            Snb_login_po.get_login_verficode_Loc_page()
            self.log.info("已经输入短信验证码")
            time.sleep(2)

            self.log.info("点击下一步按钮")
            Snb_My_po.get_login_input_phone_next_button_Loc_page()
            time.sleep(2)

            # 以下是设置登录密码的操作

            self.log.info("输入密码")
            Snb_login_po.get_login_input_passwd_Loc_page()
            time.sleep(2)

            self.log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)

            # 重新输入登录密码
            self.log.info("再次输入登录密码")
            Snb_login_po.get_login_reinput_passwd_Loc_page()
            time.sleep(2)

            self.log.info("点击确定按钮")
            Snb_login_po.get_login_input_passwd_confirm_Loc_page()
            time.sleep(2)

        except Exception as msg:
            self.log.info("异常信息：%s" % msg)
            self.log.info("-------------登录测试：end！------------------")

    def test_07_redeem(self):

       ''' 测试赎回的操作'''
       self.log.info("-------------赎回测试：start!-------------------")
       try:
            Snb_Redeem_po = SNB_Redeem_page(self.driver)
            Snb_buy_now_po=SNB_Buy_now_page(self.driver)

            time.sleep(15)
            time.sleep(4)
            self.log.info("点击持有页面的赎回按钮")
            Snb_Redeem_po.get_redeem_button_Loc_page()
            self.log.info("已经点击持有页面的赎回按钮，进入到赎回页面")
            time.sleep(4)

            save_img(driver=self.driver,file_name='redeem')
            time.sleep(2)

            self.log.info("校验赎回页面的title")
            self.assertEqual("赎回",Snb_Redeem_po.get_redeem_title_Loc_page())
            time.sleep(2)

            self.log.info("校验赎回页面总资产的文本")
            self.assertEqual("总资产",Snb_Redeem_po.get_redeem_total_assets_Loc_page())
            time.sleep(2)

            self.log.info("校验赎回页面赎回金额的文本")
            self.assertEqual("赎回金额",Snb_Redeem_po.get_redeem_amount_Loc_page())
            time.sleep(2)

            self.log.info("点击金额输入框")
            Snb_Redeem_po.get_redeem_amount_input_click_Loc_page()
            time.sleep(2)

            self.log.info("点击全部赎回")
            Snb_Redeem_po.get_redeem_all_Loc_page()
            time.sleep(2)

            # self.log.info("去掉勾选框")
            # Snb_Redeem_po.get_redeem_single_box_Loc_page()
            # time.sleep(2)
            #
            # self.log.info("勾选掉勾选框")
            # Snb_Redeem_po.get_redeem_single_box_Loc_page()
            # time.sleep(2)

            self.log.info("点击确认赎回按钮")
            Snb_Redeem_po.get_redeem_confrim_button_Loc_page()
            time.sleep(2)

            self.log.info("点击全部赎回调查问卷中的问题")
            Snb_Redeem_po.get_redeem_question_loc_page()
            time.sleep(2)

            self.log.info("点击全部赎回调查问卷中的确定按钮")
            Snb_Redeem_po.get_redeem_question_submit_loc_page()
            time.sleep(2)

            self.log.info("点击弹窗中的先不赎了按钮")
            Snb_Redeem_po.get_redeem_not_first_Loc_page()
            time.sleep(2)

            self.log.info("点击确认赎回按钮")
            Snb_Redeem_po.get_redeem_confrim_button_Loc_page()
            time.sleep(2)

            self.log.info("点击全部赎回调查问卷中的确定按钮")
            Snb_Redeem_po.get_redeem_question_submit_loc_page()
            time.sleep(2)

            self.log.info("点击弹窗中的继续赎回按钮")
            Snb_Redeem_po.get_redeem_continue_Loc_page()
            time.sleep(2)

            self.log.info("输入错误的支付密码")
            Snb_Redeem_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_buy_now_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("弹出错误支付密码的弹窗，点击重新输入")
            Snb_buy_now_po.get_buy_now_error_password_input_Loc_page()
            time.sleep(2)

            self.log.info("输入支付密码")
            Snb_Redeem_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_Redeem_po.get_set_passwd_05Loc_page()
            time.sleep(2)
            self.log.info("已经输入支付密码123456")

            self.log.info("校验赎回完成页面的title")
            self.assertEqual("赎回完成",Snb_Redeem_po.get_redeem_compele_title_Loc_page())
            time.sleep(2)

            self.log.info("点击赎回完成页面的完成按钮")
            Snb_Redeem_po.get_redeem_compele_button_Loc_page()
            time.sleep(2)

       except Exception as msg:
            self.log.info("异常信息：%s"%msg)
            self.log.info("------------赎回测试：end！---------------")

    def test_08_hold(self):
        ''' 测试持有页面的的操作'''

        self.log.info("-------------持有页面测试：start!-------------------")
        try:
            Snb_hold_po=SNB_hold_page(self.driver)
            Snb_set_password_po=SNB_set_passwd_page(self.driver)
            Snb_My_po = SNB_My_page(self.driver)

            # # #以下是开启定投功能
            time.sleep(20)
            self.log.info("校验持有页面的title")
            self.assertEqual("拾年宝",Snb_hold_po.get_hold_title_loc_page())
            time.sleep(2)

            self.log.info("点击开启定投")
            Snb_hold_po.get_hold_open_cast_loc_page()
            time.sleep(2)

            self.log.info("校验设置定投页面的title")
            self.assertEqual("设置定投",Snb_hold_po.get_hold_open_cast_title_loc_page())
            time.sleep(2)

            self.log.info("校验开启定投页面的定投金额文本")
            self.assertEqual("定投金额",Snb_hold_po.get_hold_open_cast_amount_loc_page())
            time.sleep(2)

            self.log.info("校验开启定投页面的定投金额输入框中的提示语")
            self.assertEqual("最低定投金额1,000.00",Snb_hold_po.get_hold_open_cast_amount_inputtextloc_page())
            time.sleep(2)

            self.log.info("输入定投金额1000")
            Snb_hold_po.get_hold_open_cast_amount_inputloc_page()
            time.sleep(2)

            Snb_hold_po.swipe_up_new_ios(duration=1)
            time.sleep(2)

            self.log.info("校验开启定投页面的定投日期文本")
            self.assertEqual("定投日期",Snb_hold_po.get_hold_open_cast_date_loc_page())
            time.sleep(2)


            self.log.info("校验定投日期是否是每月15日")
            self.assertEqual("每月15日",Snb_hold_po.get_hold_open_cast_defaultdate_loc_page())
            time.sleep(2)

            #点击定投日期
            # self.log.info("点击定投日期")
            # Snb_hold_po.get_hold_open_cast_defaultdateclick_loc_page()
            # time.sleep(2)


            self.log.info("点击确认开启的按钮")
            Snb_hold_po.get_hold_open_cast_openbutton_loc_page()
            time.sleep(2)

            self.log.info("校验开启定投设置页面的title")
            self.assertEqual("确认定投",Snb_hold_po.get_hold_confirm_title_loc_page())
            time.sleep(2)

            self.log.info("校验确认定投页面的文本1")
            self.assertEqual("您的拾年宝定投",Snb_hold_po.get_hold_confirm_text1_loc_page())
            time.sleep(2)

            self.log.info("校验确认定投页面的文本2")
            self.assertEqual("定投期间附赠保额10万元众安人身意外险",Snb_hold_po.get_hold_confirm_text2_loc_page())
            time.sleep(2)

            self.log.info("校验确认定投页面的定投金额为1000元")
            self.assertEqual("1,000.00",Snb_hold_po.get_hold_confirm_amount_text_loc_page())
            time.sleep(2)

            self.log.info("校验确认定投页面的定投金额日期")
            self.assertEqual("15",Snb_hold_po.get_hold_confirm_date_text_loc_page())
            time.sleep(2)

            self.log.info("校验确认定投页面的提示语")
            self.assertEqual("每月按定投设置从银行卡自动扣款，定投费用由基金公司收取，以实际为准。",Snb_hold_po.get_hold_confirm_hint_loc_page())
            time.sleep(2)

            # self.log.info("点击确认定投页面的单选框,为未选中状态")
            # Snb_hold_po.get_hold_confirm_single_box_loc_page()
            # time.sleep(2)
            #
            # self.log.info("点击确认定投页面的单选框，为选中状态")
            # Snb_hold_po.get_hold_confirm_single_box_loc_page()
            # time.sleep(2)

            self.log.info("校验确认定投页面小贴士的文案")
            self.assertEqual("应证监会要求：持有7天内赎回费率为1.20%，8-30天赎回费率0.32%，30天后赎回费率0.00%。",Snb_hold_po.get_hold_confirm_tips_text_loc_page())
            time.sleep(2)

            self.log.info("点击确认定投的按钮")
            Snb_hold_po.get_hold_confirm_button_loc_page()
            time.sleep(2)

            self.log.info("输入支付密码")
            Snb_set_password_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("校验定投完成的页面的title")
            self.assertEqual("开启定投",Snb_hold_po.get_hold_confirm_carry_out_title_loc_page())
            time.sleep(2)

            self.log.info("点击完成按钮")
            Snb_hold_po.get_hold_confirm_carry_out_button_loc_page()
            time.sleep(2)
           #以下是定投管理
            self.log.info("点击定投管理")
            Snb_hold_po.get_hold_confirm_manage_button_loc_page()
            time.sleep(2)

            self.log.info("点击暂停定投")
            Snb_hold_po.get_hold_confirm_manage_stop_loc_page()
            time.sleep(2)

            self.log.info("输入支付密码")
            Snb_set_password_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("点击开启定投")
            Snb_hold_po.get_hold_confirm_manage__open_loc_page()
            time.sleep(4)

            self.log.info("输入支付密码")
            Snb_set_password_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            #以下是调整定投的功能
            time.sleep(2)
            self.log.info("点击调整定投按钮")

            Snb_hold_po.get_hold_confirm_manage_adjustment_loc_page()
            time.sleep(2)

            self.log.info("进入到调整定投页面，点击确认调整按钮")
            Snb_hold_po.get_hold_confirm_manage__adjustmentbutton_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='cast1')
            time.sleep(2)

            self.log.info("进入到调整定投设置页面，点击确认调整定投按钮")
            Snb_hold_po.get_hold_confirm_manage__adjustmentbutton1_loc_page()
            time.sleep(2)

            self.log.info("输入支付密码")
            Snb_set_password_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_password_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='cast2')
            self.log.info("点击完成按钮")
            Snb_hold_po.get_hold_confirm_carry_out_button_loc_page()
            time.sleep(2)

            #以下是从总资产页面的操作
            self.log.info("点击持有页面的总资产")
            Snb_hold_po.get_hold_total_assetsloc_page()
            time.sleep(2)

            self.log.info("校验总资产页面的title为总资产")
            self.assertEqual('总资产',Snb_hold_po.get_hold_total_assets_title_loc_page())
            time.sleep(2)

            self.log.info("校验可赎回资产(元)文本")
            self.assertEqual('可赎回资产(元)',Snb_hold_po.get_hold_total_assets_redeemable_text_loc_page())
            time.sleep(2)

            self.log.info("校验待收收益(元)文本")
            self.assertEqual('待收收益(元)',Snb_hold_po.get_hold_total_assets_income_text_loc_page())
            time.sleep(2)

            self.log.info("点击待收益旁边的图标")
            Snb_hold_po.get_hold_total_assets_income_icon_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='income')
            time.sleep(2)

            self.log.info("点击弹层中的我知道了按钮")
            Snb_hold_po.get_hold_total_assets_income_pop_knowbutton_loc_page()
            time.sleep(2)

            self.log.info("校验待收分红(元)文本")
            self.assertEqual('待收分红(元)',Snb_hold_po.get_hold_total_assets_pend_divid_text_loc_page())
            time.sleep(2)

            self.log.info("点击待分红旁边的图标")
            Snb_hold_po.get_hold_total_assets_pend_divid_icon_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='divid')
            time.sleep(2)

            self.log.info("点击弹层中的我知道了按钮")
            Snb_hold_po.get_hold_total_assets_income_pop_knowbutton_loc()
            time.sleep(2)

            self.log.info("校验待确认文本")
            self.assertEqual('待确认资产(元)',Snb_hold_po.get_hold_total_assets_confirmed_text_loc_page())
            time.sleep(2)

            self.log.info("点击待确认文本旁边的图标")
            Snb_hold_po.get_hold_total_assets_confirmed_icon_loc_page()
            time.sleep(2)

            save_img(driver=self.driver, file_name='confirm')
            time.sleep(2)

            self.log.info("点击弹层中的我知道了按钮")
            Snb_hold_po.get_hold_total_assets_income_pop_knowbutton_loc()
            time.sleep(2)

            self.log.info("点击持有详情")
            Snb_hold_po.get_hold_total_assets_hold_detail_loc_page()
            time.sleep(2)

            self.log.info("点击确认中详情")
            Snb_hold_po.get_hold_total_assets_confirming_loc_page()
            time.sleep(2)


            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            time.sleep(2)
            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(4)

            #以下是累计收益页面操作
            self.log.info('点击累计收益')
            Snb_hold_po.get_hold_total_assets_cumulative_income_loc_page()
            time.sleep(2)

            self.log.info('校验累计收益页面的title')
            self.assertEqual('收益记录',Snb_hold_po.get_hold_total_assets_cumulative_income_title_loc_page())
            time.sleep(2)

            self.log.info("点击累计收益")
            Snb_hold_po.get_hold_total_assets_cumulative_income_tab_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='cumlativeincome')
            time.sleep(2)

            self.log.info("校验历史正收益天数比")
            self.assertIsNotNone(Snb_hold_po.get_hold_total_assets_cumulative_income_ratio_loc_page())
            time.sleep(2)

            self.log.info("校验单日最高收益")
            self.assertIsNotNone(Snb_hold_po.get_hold_total_assets_cumulative_income_maximum_loc_page())
            time.sleep(2)

            self.log.info("点击收益排行榜")
            Snb_hold_po.get_hold_total_assets_cumulative_income_leaderboard_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='income_leaderboard')
            time.sleep(2)

            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            time.sleep(2)
            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(4)



            #重新进入到收益记录页面

            self.log.info('点击累计收益')
            Snb_hold_po.get_hold_total_assets_cumulative_income_loc_page()
            time.sleep(2)

            self.log.info("点击月收益tab")
            Snb_hold_po.get_hold_total_assets_cumulative_income_monthly_loc_page()
            time.sleep(2)

            save_img(driver=self.driver,file_name='month-income')
            time.sleep(2)

            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            time.sleep(2)
            self.driver.element_by_id('com.laijin.simplefinance:id/plan_item_join_bt').click()
            time.sleep(4)

        except Exception as msg:
            self.log.info("异常信息：%s"%msg)
            self.log.info("--------------持有页面测试：end！-----------------")

    def test_09_my(self):
        ''' 测试我的页面的操作'''

        self.log.info("-------------我的页面测试：start!-------------------")
        try:
            Snb_My_po = SNB_My_page(self.driver)
            Snb_Unlogin_po=SNB_Unlogin_page(self.driver)
            Snb_set_passwd_po=SNB_set_passwd_page(self.driver)
            #以下是操作我的优惠券页面

            time.sleep(20)

            time.sleep(4)
            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的")

            self.log.info("点击我的优惠券")
            Snb_My_po.get_my_discount_coupon_Loc_page()
            self.log.info("已经进入到我的优惠券页面")
            time.sleep(2)
            # #截图优惠券的页面
            save_img(driver=self.driver,file_name='my_discount')
            time.sleep(2)

            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            #以下是操作交易记录页面

            self.log.info("进入到拾年宝页面")
            self.driver.element_by_name('立即买入').click()
            time.sleep(2)

            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的")
            time.sleep(2)

            self.log.info("点击交易记录页面")
            Snb_My_po.get_my_trans_record_Loc_page()
            time.sleep(2)
            # #截图
            save_img(driver=self.driver,file_name='trans_record')
            time.sleep(2)

            self.log.info("点击买入tab")
            Snb_My_po.get_my_trans_record_buy_Loc_page()
            time.sleep(2)

            self.log.info("点击赎回tab")
            Snb_My_po.get_my_trans_record_redeem_Loc_page()
            time.sleep(2)

            self.log.info("点击调仓tab")
            Snb_My_po.get_my_trans_record_ware_Loc_page()
            time.sleep(2)

            self.log.info("点击全部tab")
            Snb_My_po.get_my_trans_record_all_Loc_page()
            time.sleep(2)

            self.log.info("点击买入记录，进入到买入详情页")
            Snb_My_po.get_my_trans_record_buy01_Loc_page()
            time.sleep(2)

            self.log.info("查看买入详情页的交易类型")
            self.assertEqual("买入",Snb_My_po.get_my_trans_record_buy_detail_type1_Loc_page())
            time.sleep(2)
            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            self.log.info("进入到拾年宝页面")
            self.driver.element_by_name('立即买入').click()
            time.sleep(2)

            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的")
            time.sleep(4)

            self.log.info("点击交易记录页面")
            Snb_My_po.get_my_trans_record_Loc_page()
            time.sleep(2)

            #以下是操作赎回详情页的操作
            self.log.info("点击赎回的交易记录")
            Snb_My_po.get_my_trans_record_redeem01_Loc_page()
            time.sleep(2)

            self.log.info("校验交易类型为赎回")
            self.assertEqual("赎回",Snb_My_po.get_my_trans_record_redeem_detail_type1_Loc_page())
            time.sleep(2)

            self.log.info("点击关闭按钮")
            Snb_My_po.get_my_discount_coupon_close_Loc_page()
            time.sleep(2)

            self.log.info("进入到拾年宝页面")
            self.driver.element_by_name('立即买入').click()
            time.sleep(2)

            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            self.log.info("已经进入到我的")
            time.sleep(2)

            #以下是修改支付密码的操作

            self.log.info("点击修改支付密码")
            Snb_My_po.get_my_modify_payment_password_Loc_page()
            time.sleep(2)

            self.log.info("校验修改支付密码title")
            self.assertEqual("修改支付密码",Snb_My_po.get_my_modify_payment_password_title_Loc_page())
            time.sleep(2)

            self.log.info("输入当前支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("设置支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("设置确认支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(4)

            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            time.sleep(2)
            self.log.info("已经进入到我的")
            time.sleep(2)

            #以下是找回支付密码操作
            self.log.info("点击找回支付密码")
            Snb_My_po.get_my_retrieve_payment_password_Loc_page()
            time.sleep(2)

            self.log.info("校验找回支付密码的title")
            self.assertEqual("找回支付密码",Snb_My_po.get_my_retrieve_payment_password_title_Loc_page())
            time.sleep(2)

            self.log.info("校验真实姓名的文本")
            self.assertEqual("真实姓名",Snb_My_po.get_my_retrieve_payment_password_name_Loc_page())
            time.sleep(2)

            self.log.info("输入身份证号码")
            Snb_My_po.get_my_retrieve_payment_password_idnuminput_Loc_page()
            time.sleep(2)

            self.log.info("点击下一步按钮")
            Snb_My_po.get_retrieve_payment_password_nextbutton_Loc_page()
            time.sleep(2)

            self.log.info("输入短信验证码")
            Snb_My_po.get_my_retrieve_payment_password_idnum_verficode_Loc_page()
            time.sleep(2)

            self.log.info("点击确认按钮")
            Snb_My_po.get_my_retrieve_payment_password_idnum_confirm_Loc_page()
            time.sleep(2)

            self.log.info("设置支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(2)

            self.log.info("设置确认支付密码")
            Snb_set_passwd_po.get_set_passwd_01Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_02Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_04Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(1)
            Snb_set_passwd_po.get_set_passwd_05Loc_page()
            time.sleep(4)

            # 以下是修改登录密码的操作
            self.log.info("点击我的tab")
            Snb_My_po.get_my_tab_Loc_page()
            time.sleep(2)
            self.log.info("已经进入到我的")
            time.sleep(2)


            self.log.info("点击修改登录密码")
            Snb_My_po.get_my_modify_login_password_Loc_page()
            time.sleep(2)

            self.log.info("输入当前登录密码")
            Snb_My_po.get_my_modify_login_password_input_Loc_page()
            time.sleep(2)

            self.log.info("输入新密码")
            Snb_My_po.get_my_modify_login_password_inputnew_Loc_page()
            time.sleep(2)

            self.log.info("输入确认新密码")
            Snb_My_po.get_my_modify_login_password_inputnewconfirm_Loc_page()
            time.sleep(2)

            self.log.info("点击确认修改按钮")
            Snb_My_po.get_my_modify_login_password_confirmbutton_Loc_page()
            time.sleep(2)

        except Exception as msg:
            self.log.info("异常信息：%s"%msg)
            self.log.info("--------------我的页面测试：end！-----------------")"""

# if __name__ == '__main__':
#     unittest.main()
