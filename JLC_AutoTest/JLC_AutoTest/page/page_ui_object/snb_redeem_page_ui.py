from JLC_AutoTest.model.base import Base


class Snb_Redeem_Page_UI(Base):
    """
        页面UI对象（PUO）：赎回页面的元素
    """

    def get_redeem_button_Loc(self):
        """
            定位持有页面赎回的按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '赎回',
            'android_by': 'xpath',
            'android_value': '//*[@text="赎回"]',
        })

    def get_redeem_title_Loc(self):
        """
            定位赎回页面的title，赎回
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="赎回"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_redeem_total_assets_Loc(self):
        """
            定位赎回页面的总资产文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '总资产',
            'android_by': 'xpath',
            'android_value': '//*[@text="总资产"]',
        })
    def get_redeem_amount_Loc(self):
        """
            定位赎回页面的赎回金额文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '赎回金额',
            'android_by': 'xpath',
            'android_value': '//*[@text="赎回金额"]',
        })

    def get_redeem_amount_input_Loc(self):
        """
            定位赎回页面的赎回金额的输入框
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '最小赎回金额84.00',
            'android_by': 'xpath',
            'android_value': '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[2]/android.widget.EditText[1]',
        })

    def get_redeem_amount_inputq_Loc(self):
        """
            点击金额输入框
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '最小赎回金额84.00',
            'android_by': 'xpath',
            'android_value': '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[2]/android.widget.EditText[1]',
        })

    def get_redeem_all_Loc(self):
        """
            定位赎回页面的全部赎回按钮
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '全部赎回',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.widget.ListView[1]/android.view.View[2]/android.view.View[3]',
        })

    def get_redeem_confrim_button_Loc(self):
        """
            定位赎回页面的确认赎回按钮
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认赎回',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认赎回"]',
        })

    def get_redeem_single_box_Loc(self):
        """
            定位赎回页面的单选框
        :return
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[3]',
        })

    def get_redeem_tips_Loc(self):
        """
            定位赎回页面的小贴士文本
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '实际赎回金额以到账为准，根据赎回确认日净值计算，与发起赎回金额略有浮动。赎回时，由于该组合持有不同基金公司发行的基金产品，会因产品不同产生多笔到账的情况。',
            'android_by': 'xpath',
            'android_value': '//*[@text="实际赎回金额以到账为准，根据赎回确认日净值计算，与发起赎回金额略有浮动。赎回时，由于该组合持有不同基金公司发行的基金产品，会因产品不同产生多笔到账的情况。"]',
        })

    def get_redeem_not_first_Loc(self):
        """
            定位输入完赎回金额后，点击确认赎回后，显示继续赎回弹层中的先不赎了的按钮
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '先不赎了',
            'android_by': 'xpath',
            'android_value': '//*[@text="先不赎了"]',
        })

    def get_redeem_continue_Loc(self):
        """
            定位输入完赎回金额后，点击确认赎回后，显示继续赎回弹层中的继续赎回的按钮
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '继续赎回',
            'android_by': 'xpath',
            'android_value': '//*[@text="继续赎回"]',
        })
    def get_redeem_compele_title_Loc(self):
        """
            定位赎回完成页面的title
        :return
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="赎回完成"]',
            'android_by': 'xpath',
            'android_value': '//*[@text="赎回完成"]',
        })
    def get_redeem_compele_button_Loc(self):
        """
            定位赎回完成页面的完成按钮
        :return
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '完成',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })

    def get_set_passwd_01Loc(self):
        """
            定位支付密码键盘中的1数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '1',
            'android_by': 'xpath',
            'android_value': '//*[@text="1"]',
        })

    def get_set_passwd_02Loc(self):
        """
            定位支付密码键盘中的2数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '2',
            'android_by': 'xpath',
            'android_value': '//*[@text="2"]',
        })

    def get_set_passwd_03Loc(self):
        """
            定位支付密码键盘中的3数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '3',
            'android_by': 'xpath',
            'android_value': '//*[@text="3"]',
        })

    def get_set_passwd_04Loc(self):
        """
            定位支付密码键盘中的4数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '4',
            'android_by': 'xpath',
            'android_value': '//*[@text="4"]',
        })

    def get_set_passwd_05Loc(self):
        """
            定位支付密码键盘中的5数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '5',
            'android_by': 'xpath',
            'android_value': '//*[@text="5"]',
        })

    def get_set_passwd_06Loc(self):
        """
            定位支付密码键盘中的6数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '6',
            'android_by': 'xpath',
            'android_value': '//*[@text="6"]',
        })

    def get_redeem_question_loc(self):
        """
            定位全部赎回弹窗中的问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'E 不再爱了，去投其他产品',
            'android_by': 'xpath',
            'android_value': '//*[@text="E 不再爱了，去投其他产品"]',
        })

    def get_redeem_question_submit_loc(self):
        """
            定位全部赎回弹窗中的提交按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '提交',
            'android_by': 'xpath',
            'android_value': '//*[@text="提交"]',
        })