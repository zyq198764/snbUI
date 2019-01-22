from JLC_AutoTest.page.page_ui_object.snb_redeem_page_ui import Snb_Redeem_Page_UI
# from JLC_AutoTest.model.utils import JianlcTools


#登录页面的元素
class SNB_Redeem_page(Snb_Redeem_Page_UI):
    """
        页面对象(PO): 赎回页面
    """

    def get_redeem_button_Loc_page(self):
        """
            点击持有页面的赎回按钮
        :return:
        """
        return self.get_redeem_button_Loc().click()

    def get_redeem_title_Loc_page(self):
        """
            获取赎回页面的title
        :return:
        """
        return self.get_redeem_title_Loc().text

    def get_redeem_total_assets_Loc_page(self):
        """
            获取赎回页面的总资产文本
        :return:
        """
        return self.get_redeem_total_assets_Loc().text

    def get_redeem_amount_Loc_page(self):
        """
            获取赎回页面的赎回金额的文本
        :return:
        """
        return self.get_redeem_amount_Loc().text

    def get_redeem_amount_inputnt_Loc_page(self):
        """
           赎回金额输入整数且大于最小赎回金额小于总资产
        :return:
        """
        return self.get_redeem_amount_input_Loc().send_keys("100")

    def get_redeem_amount_input_click_Loc_page(self):
        """
           点击赎回金额输入框
        :return:
        """
        return self.get_redeem_amount_inputq_Loc().click()

    def get_redeem_amount_inputdecimal_Loc_page(self):
        """
           赎回金额输入小数且大于最小赎回金额小于总资产
        :return:
        """
        return self.get_redeem_amount_input_Loc().send_keys("200.01")
    def get_redeem_all_Loc_page(self):
        """
            点击全部赎回
        :return:
        """
        return self.get_redeem_all_Loc().click()

    def get_redeem_single_box_Loc_page(self):
        """
            点击单选框
        :return:
        """
        return self.get_redeem_single_box_Loc().click()

    def get_redeem_confrim_button_Loc_page(self):
        """
            点击确认赎回按钮
        :return:
        """
        return self.get_redeem_confrim_button_Loc().click()
    def get_redeem_compele_title_Loc_page(self):
        """
            获取赎回完成页面的title
        :return:
        """
        return self.get_redeem_compele_title_Loc().text
    def get_redeem_compele_button_Loc_page(self):
        """
            点击赎回页面的完成按钮
        :return:
        """
        return self.get_redeem_compele_button_Loc().click()

    def get_redeem_not_first_Loc_page(self):
        """
            点击赎回弹窗中的先不赎了的按钮
        :return:
        """
        return self.get_redeem_not_first_Loc().click()

    def get_redeem_continue_Loc_page(self):
        """
            点击赎回弹窗中的继续赎回的按钮
        :return:
        """
        return self.get_redeem_continue_Loc().click()

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

    def get_redeem_question_loc_page(self):
        """
           定位全部赎回弹窗中的问题
        :return:
        """
        return self.get_redeem_question_loc().click()

    def get_redeem_question_submit_loc_page(self):
        """
           定位全部赎回弹窗中的提交按钮
        :return:
        """
        return self.get_redeem_question_submit_loc().click()
