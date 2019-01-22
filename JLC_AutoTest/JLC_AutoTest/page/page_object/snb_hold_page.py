from JLC_AutoTest.page.page_ui_object.snb_hold_page_ui import Snb_Hold_PageUI
# from JLC_AutoTest.model.utils import JianlcTools



#登录页面的元素
class SNB_hold_page(Snb_Hold_PageUI):
    """
        页面对象(PO):持有页面
    """
    def get_hold_title_loc_page(self):
        """
           获取持有页面title
        :return:
        """
        return self.get_hold_title_loc().text

    def get_hold_open_cast_loc_page(self):
        """
           点击开启定投按钮
        :return:
        """
        return self.get_hold_open_cast_loc().click()

    def get_hold_open_cast_title_loc_page(self):
        """
          获取开启定投页面的title
        :return:
        """
        return self.get_hold_open_cast_title_loc().text

    def get_hold_open_cast_amount_loc_page(self):
        """
          获取定投金额文本
        :return:
        """
        return self.get_hold_open_cast_amount_loc().text

    def get_hold_open_cast_amount_inputtextloc_page(self):
        """
          获取定投金额输入框中的文本
        :return:
        """
        return self.get_hold_open_cast_amount_inputloc().text

    def get_hold_open_cast_amount_inputloc_page(self):
        """
          输入定投金额为1000元
        :return:
        """
        return self.get_hold_open_cast_amount_inputloc().send_keys("1000")
    def get_hold_open_cast_date_loc_page(self):
        """
          获取定投日期文本
        :return:
        """
        return self.get_hold_open_cast_date_loc().text

    def get_hold_open_cast_defaultdate_loc_page(self):
        """
          获取默认的定投日期为每月15日
        :return:
        """
        return self.get_hold_open_cast_defaultdate_loc().text

    def get_hold_open_cast_defaultdateclick_loc_page(self):
        """
          点击默认的定投日期为每月15日
        :return:
        """
        return self.get_hold_open_cast_defaultdate_loc().click()

    def get_hold_open_cast_openbutton_loc_page(self):
        """
          点击开启定投的按钮
        :return:
        """
        return self.get_hold_open_cast_openbutton_loc().click()

    def get_hold_confirm_title_loc_page(self):
        """
          获取确认定投title
        :return:
        """
        return self.get_hold_confirm_title_loc().text

    def get_hold_confirm_text1_loc_page(self):
        """
          获取确认定投页面的文本"您的拾年保定投"
        :return:
        """
        return self.get_hold_confirm_text1_loc().text

    def get_hold_confirm_text2_loc_page(self):
        """
          获取确认定投页面的文本"定投期间附赠保额10万元众安人身意外险"
        :return:
        """
        return self.get_hold_confirm_text2_loc().text

    def get_hold_confirm_amount_text_loc_page(self):
        """
          获取确认定投页面的定投金额为1000元
        :return:
        """
        return self.get_hold_confirm_amount_text_loc().text

    def get_hold_confirm_date_text_loc_page(self):
        """
          获取确认定投页面的定投金额日期
        :return:
        """
        return self.get_hold_confirm_date_text_loc().text

    def get_hold_confirm_hint_loc_page(self):
        """
          获取确认定投页面的提示语"每月按定投设置从银行卡自动扣款，定投手续费由基金公司收取，以实际为准。"
        :return:
        """
        return self.get_hold_confirm_hint_loc().text

    def get_hold_confirm_button_loc_page(self):
        """
          点击确认开启定投的按钮
        :return:
        """
        return self.get_hold_confirm_button_loc().click()

    def get_hold_confirm_single_box_loc_page(self):
        """
          点击确认定投页面的单选框
        :return:
        """
        return self.get_hold_confirm_single_box_loc().click()

    def get_hold_confirm_rule_text_loc_page(self):
        """
          获取确认定投页面的规则文本
        :return:
        """
        return self.get_hold_confirm_rule_text_loc().text

    def get_hold_confirm_tips_text_loc_page(self):
        """
          获取确认定投页面的小贴士文案"应证监会要求：持有7天内赎回费率为1.20%，8-30天赎回费率0.32%，30天后赎回费率0.00%。"
        :return:
        """
        return self.get_hold_confirm_tips_text_loc().text

    def get_hold_confirm_carry_out_title_loc_page(self):
        """
          获取开启完定投页面的title"开启定投"
        :return:
        """
        return self.get_hold_confirm_carry_out_title_loc().text

    def get_hold_confirm_carry_out_button_loc_page(self):
        """
        点击开启完定投页面的完成按钮
        :return:
        """
        return self.get_hold_confirm_carry_out_button_loc().click()

    def get_hold_confirm_manage_button_loc_page(self):
        """
        点击定投管理
        :return:
        """
        return self.get_hold_confirm_manage_button_loc().click()

    def get_hold_confirm_manage_title_loc_page(self):
        """
        获取定投管理页面的title"定投管理"
        :return:
        """
        return self.get_hold_confirm_manage_title_loc().text

    def get_hold_confirm_manage_stop_loc_page(self):
        """
            点击定投管理页面的暂停定投
        :return:
        """
        return self.get_hold_confirm_manage_stop_loc().click()

    def get_hold_confirm_manage_adjustment_loc_page(self):
        """
            点击定投管理页面的调整定投
        :return:
        """
        return self.get_hold_confirm_manage__adjustment_loc().click()

    def get_hold_confirm_manage__open_loc_page(self):
        """
            点击定投管理页面的开启定投
        :return:
        """
        return self.get_hold_confirm_manage__open_loc().click()

    def get_hold_confirm_manage__adjustment_loc_page(self):
        """
            点击定投管理页面的开启定投
        :return:
        """
        return self.get_hold_confirm_manage__adjustment_loc_page().click()

    def get_hold_confirm_manage__adjustment_loc_page(self):
        """
            点击定投管理页面的开启定投
        :return:
        """
        return self.get_hold_confirm_manage__adjustment_loc_page().click()

    def get_hold_confirm_manage__adjustmentbutton_loc_page(self):
        """
            点击定投管理页面的确认调整按钮
        :return:
        """
        return self.get_hold_confirm_manage__adjustmentbutton_loc().click()

    def get_hold_confirm_manage__adjustmentbutton1_loc_page(self):
        """
            点击定投管理页面的确认调整按钮
        :return:
        """
        return self.get_hold_confirm_manage__adjustmentbutton1_loc().click()

    def get_hold_confirm_manage__adjustmenttitle_loc_page(self):
        """
            获取定投管理页面的调整定投页面的title
        :return:
        """
        return self.get_hold_confirm_manage__adjustmenttitle_loc().text

    def get_hold_confirm_manage__adjustment_carry_out_title_loc_page(self):
        """
            获取定投管理页面的调整定投页面完成页面的title
        :return:
        """
        return self.get_hold_confirm_manage__adjustment_carry_out_title_loc().text

    def get_hold_jcrdu_loc_page(self):
        """
            点击持有页面的加仓热度
        :return:
        """
        return self.get_hold_jcrdu_loc().click()

    #以下是总资产页面的元素操作

    def get_hold_total_assetsloc_page(self):
        """
            点击持有页面的总资产
        :return:
        """
        return self.get_hold_total_assetsloc().click()

    def get_hold_total_assets_title_loc_page(self):
        """
            获取总资产页面的title为总资产
        :return:
        """
        return self.get_hold_total_assets_title_loc().text

    def get_hold_total_assets_redeemable_text_loc_page(self):
        """
            获取可赎回资产的文本
        :return:
        """
        return self.get_hold_total_assets_redeemable_text_loc().text

    def get_hold_total_assets_pend_divid_text_loc_page(self):
        """
            获取待分红的文本
        :return:
        """
        return self.get_hold_total_assets_pend_divid_text_loc().text

    def get_hold_total_assets_confirmed_text_loc_page(self):
        """
            获取待确认文本
        :return:
        """
        return self.get_hold_total_assets_confirmed_text_loc().text

    def get_hold_total_assets_income_text_loc_page(self):
        """
            获取待收收益的文本
        :return:
        """
        return self.get_hold_total_assets_income_text_loc().text

    def get_hold_total_assets_income_icon_loc_page(self):
        """
            点击待收益旁边的图标
        :return:
        """
        return self.get_hold_total_assets_income_icon_loc().click()
    def get_hold_total_assets_pend_divid_icon_loc_page(self):
        """
            点击待分红旁边的图标
        :return:
        """
        return self.get_hold_total_assets_pend_divid_icon_loc().click()

    def get_hold_total_assets_confirmed_icon_loc_page(self):
        """
            点击确认中资产旁边的图标
        :return:
        """
        return self.get_hold_total_assets_confirmed_icon_loc().click()

    def get_hold_total_assets_income_pop_knowbutton_loc_page(self):
        """
            点击弹层中的我知道了按钮
        :return:
        """
        return self.get_hold_total_assets_income_pop_knowbutton_loc().click()

    def get_hold_total_assets_hold_detail_loc_page(self):
        """
            点击持有中详情tab
        :return:
        """
        return self.get_hold_total_assets_hold_detail_loc().click()

    def get_hold_total_assets_confirming_loc_page(self):
        """
            点击确认中的详情
        :return:
        """
        return self.get_hold_total_assets_confirming_loc().click()
    #以下是累计收益
    def get_hold_total_assets_cumulative_income_loc_page(self):
        """
            点击持有页面的累计收益
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_loc().click()

    def get_hold_total_assets_cumulative_income_title_loc_page(self):
        """
            获取累计收益页面的Title --收益记录
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_title_loc().text

    def get_hold_total_assets_cumulative_income_tab_loc_page(self):
        """
           点击累计收益页面的累计收益tab
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_tab_loc().click()

    def get_hold_total_assets_cumulative_income_ratio_loc_page(self):
        """
           获取历史收益天数比元素
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_ratio_loc()

    def get_hold_total_assets_cumulative_income_maximum_loc_page(self):
        """
           获取单日最高收益元素
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_maximum_loc()

    def get_hold_total_assets_cumulative_income_leaderboard_loc_page(self):
        """
           点击收益排行榜
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_leaderboard_loc().click()

    def get_hold_total_assets_cumulative_income_monthly_loc_page(self):
        """
           点击月收益
        :return:
        """
        return self.get_hold_total_assets_cumulative_income_monthly_loc().click()
