from JLC_AutoTest.model.base import Base


class Snb_My_Page_UI(Base):
    """
        页面UI对象（PUO）：我的页面的元素
    """
    def get_my_tab_Loc(self):
        """
            定位"我的"tab
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '我的',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[2]/android.view.View[3]/android.view.View[1]',
        })

    def get_my_retreat_safely_Loc(self):
        """
            定位安全退出按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '安全退出',
            'android_by': 'xpath',
            'android_value': '//*[@text="安全退出"]',
        })

    def get_my_retreat_safely_confirm_button_Loc(self):
        """
            定位退出弹窗中的确认按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认"]',
        })

    def get_login_switch_account_Loc(self):
        """
            定位登录注册页面的切换账号按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '切换账号',
            'android_by': 'xpath',
            'android_value': '//*[@text="切换账号"]',
        })

    def get_login_input_phone_Loc(self):
        """
            定位登录注册页面的输入手机号输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入手机号码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入手机号码"]',
        })

    def get_login_input_phone_Loc(self):
        """
            定位登录注册页面的输入手机号输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入手机号码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入手机号码"]',
        })

    def get_login_input_phone_next_button_Loc(self):
        """
            定位登录注册页面的输入手机号页面的下一步按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '下 一 步',
            'android_by': 'xpath',
            'android_value': '//*[@text="下 一 步"]',
        })

    def get_login_input_phone_next_button_Loc(self):
        """
            定位登录注册页面的输入手机号页面的下一步按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '下 一 步',
            'android_by': 'xpath',
            'android_value': '//*[@text="下 一 步"]',
        })

    def get_login_verficode_input_Loc(self):
        """
            定位登录注册页面的短信验证码输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入短信验证码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入短信验证码"]',
        })

    def get_login_button_Loc(self):
        """
            定位登录注册页面的登录按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '登 录',
            'android_by': 'xpath',
            'android_value': '//android.widget.FrameLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.view.View[3]',
        })

    def get_login_password_login_Loc(self):
        """
            定位登录注册页面的登录密码登录
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '登录密码登录',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[1]/android.view.View[1]/android.view.View[2]/android.view.View[1]/android.widget.ListView[1]/android.view.View[2]',
        })
    def get_login_password_input_Loc(self):
        """
            定位输入登录密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入登录密码"]',
        })

    def get_login_forget_password_Loc(self):
        """
            定位忘记密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '忘记密码?',
            'android_by': 'xpath',
            'android_value': '//*[@text="忘记密码?"]',

        })

    def get_login_forget_password_Loc(self):
        """
            定位忘记密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '忘记密码?',
            'android_by': 'xpath',
            'android_value': '//*[@text="忘记密码?"]',
        })

    def get_my_title_Loc(self):
        """
            定位我的页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="忘记密码?"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_my_discount_coupon_Loc(self):
        """
            定位我的页面的我的优惠券
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '我的优惠券',
            'android_by': 'xpath',
            'android_value': '//*[@text="我的优惠券"]',
        })

    def get_my_discount_coupon_close_Loc(self):
        """
            定位我的页面的我的优惠券页面的关闭按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="关闭"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]',
        })

    def get_my_trans_record_Loc(self):
        """
            定位我的页面的我的交易记录
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '交易记录',
            'android_by': 'xpath',
            'android_value': '//*[@text="交易记录"]',
        })
    def get_my_trans_record_all_Loc(self):
        """
            定位我的页面的交易记录页面的全部
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '全部',
            'android_by': 'xpath',
            'android_value': '//*[@text="全部"]',
        })

    def get_my_trans_record_buy_Loc(self):
        """
            定位我的页面的交易记录页面的买入
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '买入',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入"]',
        })
    def get_my_trans_record_redeem_Loc(self):
        """
            定位我的页面的交易记录页面的赎回
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '赎回',
            'android_by': 'xpath',
            'android_value': '//*[@text="赎回"]',
        })

    def get_my_trans_record_ware_Loc(self):
        """
            定位我的页面的交易记录页面的调仓
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '调仓',
            'android_by': 'xpath',
            'android_value': '//*[@text="调仓"]',
        })

    def get_my_trans_record_buy01_Loc(self):
        """
            定位我的页面的交易记录页面的买入的记录
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '交易完成',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="all"]/android.view.View[1]/android.widget.ListView[1]/android.view.View[3]',
        })

    def get_my_trans_record_redeem01_Loc(self):
        """
            定位我的页面的交易记录页面的赎回记录
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '提交申请',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="all"]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]',
        })

    # def get_my_trans_record_redeem01_Loc(self):
    #     """
    #         定位我的页面的交易记录页面的赎回记录
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': '',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
    #         'android_by': 'xpath',
    #         'android_value': '//*[@resource-id="all"]/android.view.View[1]/android.widget.ListView[1]/android.view.View[1]',
    #     })

    def get_my_trans_record_buytitle_Loc(self):
        """
            定位我的页面的交易记录页面的买入交易详情的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="交易详情"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_my_trans_record_buy_detail_type_Loc(self):
        """
            定位我的页面的交易记录页面的买入交易详情的交易类型
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '交易类型',
            'android_by': 'xpath',
            'android_value': '//*[@text="交易类型"]',
        })
    # def get_my_trans_record_buy_detail_type1_Loc(self):
    #     """
    #         定位我的页面的交易记录页面的买入交易详情的交易类型为买入
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': '',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
    #         'android_by': 'xpath',
    #         'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.ListView[1]/android.view.View[1]/android.view.View[2]',
    #     })
    def get_my_trans_record_buy_detail_type1_Loc(self):
        """
            定位我的页面的交易记录页面的买入交易详情的交易类型为买入
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '买入',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.ListView[1]/android.view.View[1]/android.view.View[2]',
        })

    def get_my_trans_record_redeem_detail_type1_Loc(self):
        """
            定位我的页面的交易记录页面的赎回交易详情的交易类型为赎回
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '赎回',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.widget.ListView[1]/android.view.View[1]/android.view.View[2]',
        })

    #以下是修改支付密码的元素

    def get_my_modify_payment_password_Loc(self):
        """
            定位我的页面的修改支付密码元素
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '修改支付密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="修改支付密码"]',
        })

    def get_my_modify_payment_password_title_Loc(self):
        """
            定位我的页面的修改支付密码页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="修改支付密码"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_my_retrieve_payment_password_Loc(self):
        """
            定位我的页面的找回支付密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '找回支付密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="找回支付密码"]',
        })

    def get_my_retrieve_payment_password_title_Loc(self):
        """
            定位我的页面的找回支付密码页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="找回支付密码"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_my_retrieve_payment_password_name_Loc(self):
        """
            定位我的页面的找回支付密码页面的真实姓名文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '真实姓名',
            'android_by': 'xpath',
            'android_value': '//*[@text="真实姓名"]',
        })

    def get_my_retrieve_payment_password_idnum_Loc(self):
        """
            定位我的页面的找回支付密码页面的身份证号文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '身份证号',
            'android_by': 'xpath',
            'android_value': '//*[@text="身份证号"]',
        })

    def get_my_retrieve_payment_password_idnuminput_Loc(self):
        """
            定位我的页面的找回支付密码页面的身份证号输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入身份证号码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入身份证号码"]',
        })

    def get_my_retrieve_payment_password_idnum_verficode_Loc(self):
        """
            定位我的页面的找回支付密码页面的输入短信验证码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入短信验证码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入短信验证码"]',
        })

    def get_my_retrieve_payment_password_idnum_confirm_Loc(self):
        """
            定位我的页面的找回支付密码页面的确认按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认"]',
        })

    def get_my_modify_login_password_Loc(self):
        """
            定位我的页面的修改登录密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '修改登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="修改登录密码"]',
        })

    def get_my_modify_login_password_title_Loc(self):
        """
            定位我的页面的修改登录密码页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="修改登录密码"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]',
        })

    def get_my_modify_login_password_input_Loc(self):
        """
            定位我的页面的修改登录密码页面的当前登录密码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入当前登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入当前登录密码"]',
        })

    def get_my_modify_login_password_inputnew_Loc(self):
        """
            定位我的页面的修改登录密码页面的新密码输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入新登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入新登录密码"]',
        })

    def get_my_modify_login_password_inputnewconfirm_Loc(self):
        """
            定位我的页面的修改登录密码页面的确认新密码输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请再次输入新登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请再次输入新登录密码"]',
        })

    def get_my_modify_login_password_confirmbutton_Loc(self):
        """
            定位我的页面的修改登录密码页面的确认修改按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认修改',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认修改"]',
        })

    def get_retrieve_payment_password_nextbutton_Loc(self):
        """
            定位找回支付密码的下一步按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '下一步',
            'android_by': 'xpath',
            'android_value': '//*[@text="下一步"]',
        })