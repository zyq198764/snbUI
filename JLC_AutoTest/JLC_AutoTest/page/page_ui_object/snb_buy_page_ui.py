from JLC_AutoTest.model.base import Base


class Snb_Buy_Now_PageUI(Base):
    """
        页面UI对象（PUO）：立即买入的页面
    """

    def get_buy_now_button_loc(self):
        """
            定位立即买入按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '立即买入',
            'android_by': 'xpath',
            'android_value': '//*[@text="立即买入"]',
        })

    def get_buy_now_title_loc(self):
        """
            定位立即买入页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="买入"]',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入"]',
        })

    def get_buy_now_pay_method_loc(self):
        """
            定位立即买入页面的支付方式文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '支付方式',
            'android_by': 'xpath',
            'android_value': '//*[@text="支付方式"]',
        })

    def get_buy_now_pay_amount_loc(self):
        """
            定位立即买入页面的买入金额文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '买入金额',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入金额"]',
        })

    def get_buy_now_pay_amount_text_loc(self):
        """
            定位立即买入页面的买入金额提示框中文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '最小买入金额1,000.00',
            'android_by': 'xpath',
            'android_value': '//*[@text="最小买入金额1,000.00"]',
        })
    def get_buy_now_pay_amount_click_loc(self):
        """
            定位立即买入页面的买入金额输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '最小买入金额1,000.00',
            'android_by': 'xpath',
            'android_value': '//*[@text="900"]',
        })

    def get_buy_now_confirm_button_loc(self):
        """
            定位确认买入按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认买入',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认买入"]',
        })

    def get_buy_now_single_box_loc(self):
        """
            定位单选框（默认是选中状态，点击后变为不可选中状态）
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="animation-wrapper"]/android.view.View[7]',
        })

    def get_buy_now_bus_rules_loc(self):
        """
            定位业务规则文本
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="同意《拾年保基金组合交易业务规则》"]',
        })

    def get_buy_now_ms_jg_loc(self):
        """
            定位民生监管文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '民生银行监管',
            'android_by': 'xpath',
            'android_value': '//*[@text="民生银行监管"]',
        })

    def get_buy_now_yf_jr_loc(self):
        """
            定位奕丰金融文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '奕丰金融',
            'android_by': 'xpath',
            'android_value': '//*[@text="奕丰金融"]',
        })

    def get_buy_now_error_msg_loc(self):
        """
            定位输入的金额小于1000时，显示提示语的文本，买入金额不能小于最小买入金额1000.00元
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '买入金额不能小于最小买入金额1,000.00元',
            'android_by': 'xpath',
            'android_value': '//*[@text="买入金额不能小于最小买入金额1,000.00元"]',
        })


    # def get_buy_now_error_msg_loc(self):
    #     """
    #         定位输入的金额小于1000时，显示提示语的文本，买入金额不能小于最小买入金额1000.00元
    #     :return:
    #     """
    #     return self.selector({
    #         'ios_by': '',
    #         'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
    #         'android_by': 'xpath',
    #         'android_value': '//*[@text="买入金额不能小于最小买入金额1,000.00元"]',
    #     })

    def get_buy_now_evaluation_loc(self):
        """
            定位风险测评中确认并进行测评的按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认并进行测评',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认并进行测评"]',
        })

    def get_buy_now_evaluation01_loc(self):
        """
            定位风险测评中第一个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '闲赋在家',
            'android_by': 'xpath',
            'android_value': '//*[@text="闲赋在家"]',
        })

    def get_buy_now_evaluation02_loc(self):
        """
            定位风险测评中第二个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '5万及以下',
            'android_by': 'xpath',
            'android_value': '//*[@text="5万及以下"]',
        })

    def get_buy_now_evaluation03_loc(self):
        """
            定位风险测评中第三个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '有时需要使用投资资金',
            'android_by': 'xpath',
            'android_value': '//*[@text="有时需要使用投资资金"]',
        })
    def get_buy_now_evaluation04_loc(self):
        """
            定位风险测评中第四个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '保证本金安全',
            'android_by': 'xpath',
            'android_value': '//*[@text="保证本金安全"]',
        })

    def get_buy_now_evaluation05_loc(self):
        """
            定位风险测评中第五个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '<5%（精打细算型）',
            'android_by': 'xpath',
            'android_value': '//*[@text="<5%（精打细算型）"]',
        })

    def get_buy_now_evaluation06_loc(self):
        """
            定位风险测评中第六个问题
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '从事金融行业多年',
            'android_by': 'xpath',
            'android_value': '//*[@text="从事金融行业多年"]',
        })

    def get_buy_now_evaluation_button_loc(self):
        """
            定位风险测评中完成按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '完成',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })

    def get_buy_now_evaluation_confirmbutton_loc(self):
        """
            定位风险测评中的确认无误按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认无误提交',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认无误提交"]',
        })

    def get_buy_now_evaluation_confirmres_loc(self):
        """
            定位风险测评中的确认评测结果按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认测评结果',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认测评结果"]',
        })

    def get_buy_now_pay_pass_text_loc(self):
        """
            定位支付密码弹层中的请输入基金支付密码的文本
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入基金支付密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入基金支付密码"]',
        })

    def get_buy_now_pay_pass_close_loc(self):
        """
            定位支付密码弹层中的关闭按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@text="关闭"]',
            'android_by': 'xpath',
            'android_value': '//*[@text="关闭"]',
        })

    def get_buy_now_pay_pass_yf_text_loc(self):
        """
            定位支付密码弹层中文本基金销售服务由奕丰金融提供
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '基金销售服务由奕丰金融提供',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/web_root_ll"]/android.webkit.WebView[1]/android.webkit.WebView[1]/android.view.View[2]/android.view.View[1]/android.view.View[5]',
        })

    def get_buy_now_complete_loc(self):
        """
            定位买入完成页面的title
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '买入完成',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_buy_now_complete_button_loc(self):
        """
            定位买入完成页面的完成按钮
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '完成',
            'android_by': 'xpath',
            'android_value': '//*[@text="完成"]',
        })

    def get_set_passwd_title_Loc(self):
        """
            定位设置支付密码的title
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
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

    def get_set_passwd_07Loc(self):
        """
            定位支付密码键盘中的7数字
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '7',
            'android_by': 'xpath',
            'android_value': '//*[@text="7"]',
        })
    #以下是短信验证码支付的元素定位：以招商银行为例，第一笔是3000，第二笔+第一笔超过5000，就弹出短信验证码支付
    def get_buy_now_verficode_Loc(self):
        """
            定位短信验证码输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入验证码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入验证码"]',
        })

    def get_buy_now_errorverficode_Loc(self):
        """
            定位短信验证码输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '111111',
            'android_by': 'xpath',
            'android_value': '//*[@text="111111"]',
        })

    def get_buy_now_verficode_resendLoc(self):
        """
            定位重新发送按钮，必须过了60秒后，才能进行点击
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '重新发送',
            'android_by': 'xpath',
            'android_value': '//*[@text="重新发送"]',
        })

    def get_buy_now_verficode_cancel_Loc(self):
        """
            定位取消按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '取消',
            'android_by': 'xpath',
            'android_value': '//*[@text="取消"]',
        })

    def get_buy_now_verficode_confirm_Loc(self):
        """
            定位确认按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确认',
            'android_by': 'xpath',
            'android_value': '//*[@text="确认"]',
        })

    def get_buy_now_error_password_input_Loc(self):
        """
            定位输入错误支付密码弹出的弹窗中的重新输入按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '重新输入',
            'android_by': 'xpath',
            'android_value': '//*[@text="重新输入"]',
        })

    def get_buy_now_error_password_retri_Loc(self):
        """
            定位输入错误支付密码弹出的弹窗中的找回密码按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '找回密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="找回密码"]',
        })

    def get_buy_now_single_buy_Loc(self):
        """
            定位持有页面单笔买入的按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '单笔买入',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })
    #大额买入页面元素定位

    def get_buy_now_big_buy_cancelLoc(self):
        """
            定位第一次买入3000，第二次再买入3000的话，就提示大额买入
            点击取消按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '取消',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_buttonLoc(self):
        """
            定位第一次买入3000，第二次再买入3000的话，就提示大额买入
            定位大额买入按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '大额买入',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_titleLoc(self):
        """

            定位大额买入页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="大额买入"]',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_Loc(self):
        """

            定位大额买入页面的申请转账按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '申请转账',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_pop_Loc(self):
        """

            定位大额买入页面的申请转账按钮后，弹出提交成功的弹窗，定位我知道了按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '我知道了',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_title_Loc(self):
        """

            定位大额买入提交申请完成页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="提交申请完成"]',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_account_Loc(self):
        """

            定位大额买入提交申请完成页面的大额专用账户的信息中的银行户名是奕丰基金销售有限公司
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '奕丰基金销售有限公司',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_account_bank_Loc(self):
        """

            定位大额买入提交申请完成页面的大额专用账户的信息中的银行账号是633038888
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '633038888',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_account_bankname_Loc(self):
        """

            定位大额买入提交申请完成页面的大额专用账户的信息中的银行名称是中国民生银行深圳分行海岸城支行
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '中国民生银行深圳分行海岸城支行',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_account_sys_Loc(self):
        """

            定位大额买入提交申请完成页面的大额专用账户的信息中的大额支付系统账号是305584018301
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '305584018301',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })
    def get_buy_now_big_buy_apply_submit_account_copy_Loc(self):
        """

            定位大额买入提交申请完成页面的大额专用账户的信息中的复制按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '复制',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })

    def get_buy_now_big_buy_apply_submit_complete_Loc(self):
        """

            定位大额买入提交申请完成页面的完成按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '完成',
            'android_by': 'xpath',
            'android_value': '//*[@text="单笔买入"]',
        })
