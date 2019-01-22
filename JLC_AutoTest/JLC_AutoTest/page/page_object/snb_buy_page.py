from JLC_AutoTest.page.page_ui_object.snb_buy_page_ui import Snb_Buy_Now_PageUI
# from JLC_AutoTest.model.utils import JianlcTools



#登录页面的元素
class SNB_Buy_now_page(Snb_Buy_Now_PageUI):
    """
        页面对象(PO): 立即买入页面
    """

    def get_buy_now_button_loc_page(self):
        """
            点击立即买入按钮
        :return:
        """
        return self.get_buy_now_button_loc().click()

    def get_buy_now_title_loc_page(self):
        """
            获取立即买入页面的title为买入
        :return:
        """
        return self.get_buy_now_title_loc().text

    def get_buy_now_pay_method_loc_page(self):
        """
            获取支付方式文本
        :return:
        """
        return self.get_buy_now_pay_method_loc().text

    def get_buy_now_pay_method_click_loc_page(self):
        """
            点击一下文本元素
        :return:
        """
        return self.get_buy_now_pay_method_loc().click()

    def get_buy_now_pay_amount_loc_page(self):
        """
            获取买入金额的文本
        :return:
        """
        return self.get_buy_now_pay_amount_loc().text

    def get_buy_now_pay_amount_text_loc_page(self):
        """
            获取买入金额输入框中的提示语:最小买入金额1，000.00
        :return:
        """
        return self.get_buy_now_pay_amount_text_loc().text

    def get_buy_now_pay_amount_click_page(self):
        """
           点击买入金额输入框
        :return:
        """
        return self.get_buy_now_pay_amount_text_loc().click()

    def get_buy_now_pay_amount_input_page(self):
        """
           输入金额小于1000元
        :return:
        """
        return self.get_buy_now_pay_amount_text_loc().send_keys("900")

    def get_buy_now_pay_amount_input_pay_page(self):
        """
           输入金额大于1000元
        :return:
        """
        return self.get_buy_now_pay_amount_text_loc().send_keys("3000")
    def get_buy_now_pay_amount_inputmore_page(self):
        """
           输入金额大于1000元
        :return:
        """
        return self.get_buy_now_pay_amount_click_loc().send_keys("3000")

    def get_buy_now_pay_amount_inputmoreios_page(self):
        """
           输入金额大于1000元
        :return:
        """
        return self.get_buy_now_pay_amount_click_loc().send_keys("3")
    def get_buy_now_pay_amount_click1_page(self):
        """
           点击一下输入框
        :return:
        """
        return self.get_buy_now_pay_amount_click_loc().click()

    def get_buy_now_confirm_button_loc_page(self):
        """
            获取确认买入按钮元素
        """
        return self.get_buy_now_confirm_button_loc().click()

    def get_buy_now_single_box_loc_page(self):
        """
            点击单选框
        """
        return self.get_buy_now_single_box_loc().click()

    def get_buy_now_bus_rules_loc_page(self):
        """
            获取业务规则文本
        """
        return self.get_buy_now_bus_rules_loc().text

    def get_buy_now_ms_jg_loc_page(self):
        """
            获取民生监管的文本
        """
        return self.get_buy_now_ms_jg_loc().text

    def get_buy_now_ms_jg_loc_click_page(self):
        """
            点击民生监管的文本
        """
        return self.get_buy_now_ms_jg_loc().click()

    def get_buy_now_yf_jr_loc_page(self):
        """
            获取奕丰金融文本
        """
        return self.get_buy_now_yf_jr_loc().click()

    def get_buy_now_error_msg_loc_page(self):
        """
            获取输入的金额小于1000时，显示提示语的文本，买入金额不能小于最小买入金额1000.00元文本
        """
        return self.get_buy_now_error_msg_loc().text

    def get_buy_now_evaluation_loc_page(self):
        """
            点击风险测评中确认并进行测评的按钮
        """
        return self.get_buy_now_evaluation_loc().click()

    def get_buy_now_evaluation01_loc_page(self):
        """
            获取风险测评中的第一个问题
        """
        return self.get_buy_now_evaluation01_loc().click()

    def get_buy_now_evaluation02_loc_page(self):
        """
            获取风险测评中的第二个问题
        """
        return self.get_buy_now_evaluation02_loc().click()

    def get_buy_now_evaluation03_loc_page(self):
        """
            获取风险测评中的第三个问题
        """
        return self.get_buy_now_evaluation03_loc().click()

    def get_buy_now_evaluation04_loc_page(self):
        """
            获取风险测评中的第四个问题
        """
        return self.get_buy_now_evaluation04_loc().click()

    def get_buy_now_evaluation05_loc_page(self):
        """
            获取风险测评中的第五个问题
        """
        return self.get_buy_now_evaluation05_loc().click()

    def get_buy_now_evaluation06_loc_page(self):
        """
            获取风险测评中的第六个问题
        """
        return self.get_buy_now_evaluation06_loc().click()

    def get_buy_now_evaluation_button_loc_page(self):
        """
            点击风险测评中完成按钮
        """
        return self.get_buy_now_evaluation_button_loc().click()

    def get_buy_now_evaluation_confirmbutton_loc_page(self):
        """
            点击风险测评中的确认无误按钮
        """
        return self.get_buy_now_evaluation_confirmbutton_loc().click()

    def get_buy_now_evaluation_confirmres_loc_page(self):
        """
            点击风险测评中的确认评测结果按钮
        """
        return self.get_buy_now_evaluation_confirmres_loc().click()

    def get_buy_now_pay_pass_text_loc_page(self):
        """
            获取支付密码弹层中的请输入基金支付密码的文本
        """
        return self.get_buy_now_pay_pass_text_loc().text

    def get_buy_now_pay_pass_close_loc_page(self):
        """
            获取支付密码弹层中的关闭按钮
        """
        return self.get_buy_now_pay_pass_close_loc().click()

    def get_buy_now_pay_pass_yf_text_loc_page(self):
        """
            获取支付密码弹层中文本基金销售服务由奕丰金融提供文本
        """
        return self.get_buy_now_pay_pass_yf_text_loc().text

    def get_buy_now_complete_loc_page(self):
        """
            获取买入完成页面的title
        """
        return self.get_buy_now_complete_loc().text

    def get_buy_now_complete_button_loc_page(self):
        """
            点击买入完成页面的完成按钮
        """
        return self.get_buy_now_complete_button_loc().click()

    def get_set_passwd_01Loc_page(self):
        """
            输入支付密码1
        :return:
        """
        return self.get_set_passwd_01Loc().click()
    def get_set_passwd_02Loc_page(self):
        """
            输入支付密码2
        :return:
        """
        return self.get_set_passwd_02Loc().click()
    def get_set_passwd_03Loc_page(self):
        """
            输入支付密码3
        :return:
        """
        return self.get_set_passwd_03Loc().click()
    def get_set_passwd_04Loc_page(self):
        """
            输入支付密码4
        :return:
        """
        return self.get_set_passwd_04Loc().click()
    def get_set_passwd_05Loc_page(self):
        """
            输入支付密码5
        :return:
        """
        return self.get_set_passwd_05Loc().click()
    def get_set_passwd_06Loc_page(self):
        """
            输入支付密码6
        :return:
        """
        return self.get_set_passwd_06Loc().click()

    def get_set_passwd_07Loc_page(self):
        """
            输入支付密码7
        :return:
        """
        return self.get_set_passwd_07Loc().click()

    def get_buy_now_verficode_Loc_page(self):
        """
            获取短信验证码输入框的文本,请输入验证码
        :return:
        """
        return self.get_buy_now_verficode_Loc().text

    def get_buy_now_errorverficode_input_Loc_page(self):
        """
            输入错误的验证码：111111
        :return:
        """
        return self.get_buy_now_verficode_Loc().send_keys('111111')

    def get_buy_now_verficode_input_Loc_page(self):
        """
            输入错误的验证码：111111
        :return:
        """
        return self.get_buy_now_errorverficode_Loc().send_keys('888888')

    def get_buy_now_verficode_resendLoc_page(self):
        """
            点击重新发送按钮
        :return:
        """
        return self.get_buy_now_verficode_resendLoc().click()

    def get_buy_now_verficode_cancel_Loc_page(self):
        """
            点击取消按钮
        :return:
        """
        return self.get_buy_now_verficode_cancel_Loc().click()

    def get_buy_now_verficode_confirm_Loc_page(self):
        """
            点击确认按钮
        :return:
        """
        return self.get_buy_now_verficode_confirm_Loc().click()

    def get_buy_now_error_password_input_Loc_page(self):
        """
            点击输入错误支付密码弹窗中重新输入按钮
        :return:
        """
        return self.get_buy_now_error_password_input_Loc().click()

    def get_buy_now_error_password_retri_Loc_page(self):
        """
            点击输入错误支付密码弹窗中找回支付密码按钮
        :return:
        """
        return self.get_buy_now_error_password_retri_Loc().click()

    def get_buy_now_single_buy_Loc_page(self):
        """
            点击持有页面单笔买入的按钮
        :return:
        """
        return self.get_buy_now_single_buy_Loc().click()

    def get_buy_now_big_buy_cancelLoc_page(self):
        """
            点击大额买入弹层中的取消按钮
        :return:
        """
        return self.get_buy_now_big_buy_cancelLoc().click

    def get_buy_now_big_buy_buttonLoc_page(self):
        """
            点击大额买入弹层中的大额买入按钮
        :return:
        """
        return self.get_buy_now_big_buy_buttonLoc().click()

    def get_buy_now_big_buy_titleLoc_page(self):
        """
            获取大额买入页面的title
        :return:
        """
        return self.get_buy_now_big_buy_titleLoc().text

    def get_buy_now_big_buy_apply_Loc_page(self):
        """
            获取大额买入页面的申请转账按钮
        :return:
        """
        return self.get_buy_now_big_buy_apply_Loc().click()

    def get_buy_now_big_buy_apply_pop_Loc_page(self):
        """
            点击大额买入页面的提交成功的我知道了按钮
        :return:
        """
        return self.get_buy_now_big_buy_apply_pop_Loc().click()

    def get_buy_now_big_buy_apply_submit_title_Loc_page(self):
        """
            获取大额买入页面的提交申请完成页面的Title
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_title_Loc().text

    def get_buy_now_big_buy_apply_submit_account_Loc_page(self):
        """
            获取大额买入页面的提交申请完成页面的银行户名
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_account_Loc().text

    def get_buy_now_big_buy_apply_submit_account_bank_Loc_page(self):
        """
            获取大额买入页面的提交申请完成页面的银行户名
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_account_bank_Loc().text

    def get_buy_now_big_buy_apply_submit_account_bankname_Loc_page(self):
        """
            获取大额买入页面的提交申请完成页面的开户银行
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_account_bankname_Loc().text

    def get_buy_now_big_buy_apply_submit_account_sys_Loc_page(self):
        """
            获取大额买入页面的提交申请完成页面的大额支付系统账号
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_account_sys_Loc().text

    def get_buy_now_big_buy_apply_submit_account_copy_Loc_page(self):
        """
            点击大额买入页面的提交申请完成页面的复制按钮
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_account_copy_Loc().click()


    def get_buy_now_big_buy_apply_submit_complete_Loc_page(self):
        """
            点击大额买入页面的提交申请完成页面的完成按钮
        :return:
        """
        return self.get_buy_now_big_buy_apply_submit_complete_Loc().click()


