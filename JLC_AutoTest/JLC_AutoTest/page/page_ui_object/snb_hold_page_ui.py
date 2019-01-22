from JLC_AutoTest.model.base import Base


class Snb_Hold_PageUI(Base):
    """
        页面UI对象（PUO）：持有页面
    """

    def get_hold_title_loc(self):
        """
            定位持有页面title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="拾年宝"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_open_cast_loc(self):
        """
            定位开启定投元素
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '开启定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="开启定投"]',
        })

    def get_hold_open_cast_title_loc(self):
        """
            定位开启定投的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="设置定投"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_open_cast_amount_loc(self):
        """
            定位定投金额文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '定投金额',
            'android_by': 'xpath',
            'android_value': '//*[@text="定投金额"]',
        })

    def get_hold_open_cast_amount_inputloc(self):
        """
            定位定投金额输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '最低定投金额1,000.00',
            'android_by': 'xpath',
            'android_value': '//*[@text="最低定投金额1,000.00"]',
        })

    def get_hold_open_cast_date_loc(self):
        """
            定位定投日期文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '定投日期',
            'android_by': 'xpath',
            'android_value': '//*[@text="定投日期"]',
        })

    def get_hold_open_cast_defaultdate_loc(self):
        """
            定位默认的定投日期
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '每月15日',
            'android_by': 'xpath',
            'android_value': '//*[@text="每月15日"]',
        })

    def get_hold_open_cast_openbutton_loc(self):
        """
            定位开启定投的按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '开启定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="开启定投"]',
        })

    def get_hold_confirm_title_loc(self):
        """
            定位确认定投title
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="确认定投"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_confirm_text1_loc(self):
        """
            定位确认定投页面的文本"您的拾年保定投"
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '您的拾年宝定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="您的拾年宝定投"]',
        })

    def get_hold_confirm_text2_loc(self):
        """
            定位确认定投页面的文本"定投期间附赠保额10万元众安人身意外险"
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '定投期间附赠保额10万元众安人身意外险',
            'android_by': 'xpath',
            'android_value': '//*[@text="定投期间附赠保额10万元众安人身意外险"]',
        })

    def get_hold_confirm_amount_text_loc(self):
        """
            定位确认定投页面的定投金额为1000元
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '1,000.00',
            'android_by': 'xpath',
            'android_value': '//*[@text="1,000.00"]',
        })

    def get_hold_confirm_date_text_loc(self):
        """
            定位确认定投页面的定投金额日期
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '15',
            'android_by': 'xpath',
            'android_value': '//*[@text="15"]',
        })

    def get_hold_confirm_hint_loc(self):
        """
            定位确认定投页面的提示语"每月按定投设置从银行卡自动扣款，定投手续费由基金公司收取，以实际为准。"
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '每月按定投设置从银行卡自动扣款，定投费用由基金公司收取，以实际为准。',
            'android_by': 'xpath',
            'android_value': '//*[@text="每月按定投设置从银行卡自动扣款，定投费用由基金公司收取，以实际为准。"]',
        })

    def get_hold_confirm_button_loc(self):
        """
            定位确认开启定投的按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认开启定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认开启定投"]',
        })

    def get_hold_confirm_single_box_loc(self):
        """
            定位确认定投页面的单选框
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[5]',
        })

    def get_hold_confirm_rule_text_loc(self):
        """
            定位确认定投页面的规则文本
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="同意《基金组合交易业务规则》"]',
        })

    def get_hold_confirm_tips_text_loc(self):
        """
            定位确认定投页面的小贴士文案"应证监会要求：持有7天内赎回费率为1.20%，8-30天赎回费率0.32%，30天后赎回费率0.00%。"
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '应证监会要求：持有7天内赎回费率为1.20%，8-30天赎回费率0.32%，30天后赎回费率0.00%。',
            'android_by': 'xpath',
            'android_value': '//*[@text="应证监会要求：持有7天内赎回费率为1.20%，8-30天赎回费率0.32%，30天后赎回费率0.00%。"]',
        })

    def get_hold_confirm_carry_out_title_loc(self):
        """
            定位开启完定投页面的title"开启定投"
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="开启定投"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_confirm_carry_out_button_loc(self):
        """
            定位开启完定投页面的完成按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '完成',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })
    #已经开启定投后，定投页面的管理

    def get_hold_confirm_manage_button_loc(self):
        """
            定位"定投管理"
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '定投管理',
            'android_by': 'xpath',
            'android_value': '//*[@text="定投管理"]',
        })

    def get_hold_confirm_manage_title_loc(self):
        """
            定位定投管理页面的title"定投管理"
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="定投管理"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_confirm_manage_stop_loc(self):
        """
            定位定投管理页面的暂停定投
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '暂停定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="暂停定投"]',
        })

    def get_hold_confirm_manage__adjustment_loc(self):
        """
            定位定投管理页面的调整定投
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '调整定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="调整定投"]',
        })

    def get_hold_confirm_manage__adjustmentbutton_loc(self):
        """
            定位定投管理页面的确认调整按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认调整',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认调整"]',
        })

    def get_hold_confirm_manage__adjustmentbutton1_loc(self):
        """
            定位定投管理页面的确认调整按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认调整定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认调整定投"]',
        })

    def get_hold_confirm_manage__adjustmenttitle_loc(self):
        """
            定位定投管理页面的调整定投页面的title
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })
    def get_hold_confirm_manage__adjustmentsettitle_loc(self):
        """
            定位定投管理页面的调整定投页面设置页面的title
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })
    def get_hold_confirm_manage__adjustment_carry_out_title_loc(self):
        """
            定位定投管理页面的调整定投页面完成页面的title
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_confirm_manage__open_loc(self):
        """
            定位定投管理页面的开启定投
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '开启定投',
            'android_by': 'xpath',
            'android_value': '//*[@text="开启定投"]',
        })

    def get_hold_jcrdu_loc(self):
        """
            定位持有页面的加仓热度
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '加仓热度',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[14]/android.widget.ListView[1]',
        })

    #总资产页面元素的定位

    def get_hold_total_assetsloc(self):
        """
            定位持有页面总资产元素
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '总资产(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="总资产(元)"]',
        })

    def get_hold_total_assets_title_loc(self):
        """
            定位总资产页面的title为总资产
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })
    def get_hold_total_assets_redeemable_text_loc(self):
        """
            定位总资产页面的可赎回资产文本
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '可赎回资产(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="可赎回资产(元)"]',
        })

    def get_hold_total_assets_income_text_loc(self):
        """
            定位总资产页面的可待收收益文本
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '待收收益(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="待收收益(元)"]',
        })

    def get_hold_total_assets_income_icon_loc(self):
        """
            定位总资产页面的可待收收益旁边的图标
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.Image[1]',
        })

    def get_hold_total_assets_income_pop_knowbutton_loc(self):
        """
            定位总资产页面的可待收收益弹窗中的我知道了按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '我知道了',
            'android_by': 'xpath',
            'android_value': '//*[@text="我知道了"]',
        })

    def get_hold_total_assets_pend_divid_text_loc(self):
        """
            定位总资产页面的待分红文本
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '待收分红(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="待收分红(元)"]',
        })

    def get_hold_total_assets_confirmed_text_loc(self):
        """
            定位总资产页面的待确认文本
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '待确认资产(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="待确认资产(元)"]',
        })

    def get_hold_total_assets_pend_divid_icon_loc(self):
        """
            定位总资产页面的分红旁边的图标
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.Image[2]',
        })

    def get_hold_total_assets_confirmed_icon_loc(self):
        """
            定位总资产页面的待确认资产旁边的图标
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.Image[3]',
        })
    def get_hold_total_assets_hold_detail_loc(self):
        """
            定位总资产页面的持有详情
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '持有详情',
            'android_by': 'xpath',
            'android_value': '//*[@text="持有详情"]',
        })

    def get_hold_total_assets_confirming_loc(self):
        """
            定位总资产页面的确认中详情
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认中详情',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认中详情"]',
        })


    #累计收益页面元素的定位

    def get_hold_total_assets_cumulative_income_loc(self):
        """
            定位总资产页面累计收益
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '累计收益(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="累计收益(元)"]',
        })

    def get_hold_total_assets_cumulative_income_title_loc(self):
        """
            定位累计收益页面的title
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="收益记录"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_hold_total_assets_cumulative_income_tab_loc(self):
        """
            定位累计收益页面的累计收益tab
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '累计收益',
            'android_by': 'xpath',
            'android_value': '//*[@text="累计收益"]',
        })

    def get_hold_total_assets_cumulative_income_ratio_loc(self):
        """
            定位累计收益页面的历史收益天数比元素
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '历史正收益天数比',
            'android_by': 'xpath',
            'android_value': '//*[@text="历史正收益天数比"]',
        })

    def get_hold_total_assets_cumulative_income_maximum_loc(self):
        """
            定位累计收益页面的单日最高收益
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '单日最高收益(元)',
            'android_by': 'xpath',
            'android_value': '//*[@text="单日最高收益(元)"]',
        })

    def get_hold_total_assets_cumulative_income_leaderboard_loc(self):
        """
            定位累计收益页面的收益排行榜
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '收益排行榜',
            'android_by': 'xpath',
            'android_value': '//*[@text="收益排行榜"]',
        })
    def get_hold_total_assets_cumulative_income_monthly_loc(self):
        """
            定位累计收益页面的月收益
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '月收益',
            'android_by': 'xpath',
            'android_value': '//*[@text="月收益"]',
        })


