from JLC_AutoTest.model.base import Base


class Snb_LoginPageUI(Base):
    """
        页面UI对象（PUO）：登陆页面的UI
    """

    def get_login_close_button_Loc(self):
        """
            定位登录页面的关闭按钮
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="关闭"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.TextView[1]',
        })

    def get_login_title_Loc(self):
        """
            定位登录页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="注册/登录"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })
    def get_login_input_phone_Loc(self):
        """
            定位登录页面的输入手机号码的输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入手机号码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入手机号码"]',
        })

    def get_login_regist_button_Loc(self):
        """
            定位登录页面的注册按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '注 册',
            'android_by': 'xpath',
            'android_value': '//*[@text="注 册"]',
        })
    def get_login_regist_agree_Loc(self):
        """
            定位登录页面的协议文案
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '注册即同意',
            'android_by': 'xpath',
            'android_value': '//*[@text="注册即同意《拾年保服务协议》和《拾年保隐私条款》"]',
        })


    def get_login_loginbutton_Loc(self):
        """
            定位登录页面的登录按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '登录',
            'android_by': 'xpath',
            'android_value': '//*[@text="登录"]',
        })
    def get_login_jlcloginbutton_Loc(self):
        """
            定位登录页面的简理财登录按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '简理财登录',
            'android_by': 'xpath',
            'android_value': '//*[@text="简理财登录"]',
        })

    def get_login_registbutton_Loc(self):
        """
            定位注册页面的注册按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '注册',
            'android_by': 'xpath',
            'android_value': '//*[@text="注册"]',
        })

    def get_login_verficode_Loc(self):
        """
            获取注册页面的输入短信验证码的输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入短信验证码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入短信验证码"]',
        })

    def get_login_reverficode_Loc(self):
        """
            获取注册页面的再次输入正确的短信验证码的输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入短信验证码',
            'android_by': 'xpath',
            'android_value': '//*[@text="111111"]',
        })

    def get_login_error_verficode_Loc(self):
        """
            获取注册页面的输入错误短信验证码提示语
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="短信验证码有误，请重新输入"]',
        })

    def get_login_verficode_click_Loc(self):
        """
            获取注册页面的重新发送按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '重新发送',
            'android_by': 'xpath',
            'android_value': '//*[@text="重新发送"]',
        })
    def get_login_Registered_Loc(self):
        """
            如果手机号已注册，给与提示"该号码已注册"
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '该号码已注册',
            'android_by': 'xpath',
            'android_value': '//*[@text="该号码已注册"]',
        })

    def get_login_icon_Loc(self):
        """
            清除手机号码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACUAAAAlCAMAAADyQNAxAAAAtFBMVEVHcEzw3bLw3bLw3bLw3bLIpVbKp1nIpVbw3bLw3bLexIrLqFvIpVbNvYvw3bKmkl2ypm6vlVnEtoLIpVbw3bK0mFi7rXjw3bKtm2fw3bKkjlmtnWjIpVbw3bKljlncwYWsklmpkVnIpVa2qXPp06HIpVbw3bLIpVbIpVa/sHzw3bLWuHXw3bKzom+xoGy4q3Xw3bKllF/IpVbw3bK8nVfPr2aokFmnj1jw3bLaypqsllvYxpi/6iO2AAAAPHRSTlMAKS0Sa2QvampkAykSmUXl4KmrVxyYwFXeTODnPDvUCrXBH9RYR14XQrUjaDLL1MtC/iVZhU/KzDGFvYUOzJhEAAACCElEQVQ4y3WUiZKrIBBFcQwKRo37FjUuZaJZJnteZub//+shLhFjqEKK5nC53QUCMGiSFflrPMNrP9pKYLrxJ6w4uZYfSXcUfOInmJWKHM34wa6v+i7+MTQHqasxtMVVrlz33X5+f1XyCnMsFCma4VpMyHINTYmGkZNxRM+xX+mJjoY6UDIcbE14tbBj9Gpb5Yj56bTxUdm22WENWR+qYyENN5mqlbGnG5mMpEb9aVTUGo9ytzbOr2dfA4pD1JHk5qjmT45Cz+NmywHGIY2uAktxTgTGy2uz8DXAaqg1cF1iibDVHoyxAQSeFUkzcv76KnQYh7weAvyfEwH/G78sNxgDAYC/fbD2XMBiKgsB11tTksHOhzMD0dNmB5Wptno4v0VmYy0OES2mvFSL9VUbV5nyNr7u3u4VmO8WuzkQyFd4BXfeHYS/N7mHxIU4J6NAxh6Tb78hyGxdGEEsJuh2BiS4MDsoaCEGMxeQXJkyJSxpmwHUYHSW2WlZnyvGjVg4gGoMUr9mLNKxSFpnG6aYc7lxlRTNvYeBuPlw74kN2L7wi/2A8iQkw4d96SahnsIptQ1M9fA1LfWHKLy9bUF86OUwEuqBbmYMlJkkFrIbLzCJbVPo7MmCaccJvLz9vwoxDZIbNIuiMOEtCVKxWE0lVEI7jYP4H+mpDUv5Q3WkLLxDKEJ4DzMml/9H8iwcJSSfLQAAAABJRU5ErkJggg==',
            'android_by': 'xpath',
            'android_value': '//*[@text="9H8iwcJSSfLQAAAABJRU5ErkJggg=="]',
        })
    # 获取设置登录密码页面的元素
    def get_login_set_passwd_title_Loc(self):
        """
            获取设置登录密码页面的title
        :return:
        """
        return self.selector({
            'ios_by': 'xpath',
            'ios_value': '//*[@name="设置登录密码"]',
            'android_by': 'xpath',
            'android_value': '//*[@resource-id="com.laijin.simplefinance:id/layout_widget_title_bar"]/android.widget.LinearLayout[1]/android.widget.TextView[1]',
        })

    def get_login_set_passwd_requi_Loc(self):
        """
            获取设置密码的要求
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '8-20位英文与数字组合并区分大小写',
            'android_by': 'xpath',
            'android_value': '//*[@text="8-20位英文与数字组合并区分大小写"]',
        })

    def get_login_input_passwd_Loc(self):
        """
            获取输入密码的输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请设置登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请设置登录密码"]',
        })

    def get_login_input_passwd_icon_Loc(self):
        """
            获取密码输入框是明文还是密文
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="X1WsOAAAAAElFTkSuQmCC"]',

        })
    #

    def get_login_input_passwd_icon1_Loc(self):
        """
            获取密码输入框是明文还是密文
        :return:
        """
        return self.selector({
            'ios_by': '',
            'ios_value': '//XCUIElementTypeApplication[1]/XCUIElementTypeWindow[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeOther[1]/XCUIElementTypeTable[1]/XCUIElementTypeCell[2]/XCUIElementTypeButton[1]',
            'android_by': 'xpath',
            'android_value': '//*[@text="rlWKJaAFcv111nEAMt9IBhASs862x1FEDFjZ4xSgN0ilkkx9IB2BzoPaq4fv4goIswfSt+AGCzEn+gPjAnAAAAAElFTkSuQmCC"]',

        })
    def get_login_input_passwd_confirm_Loc(self):
        """
            获取确定按钮
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '确 定',
            'android_by': 'xpath',
            'android_value': '//*[@text="确 定"]',
        })


    #确认登录密码的页面

    def get_login_reinput_passwd_Loc(self):
        """
            获取再次输入登录密码的输入框
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请再次输入登录密码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请再次输入登录密码"]',
        })

    def get_login_input_error_phone_Loc(self):
        """
            输入错误的手机号码，提示请输入正确的手机号码
        :return:
        """
        return self.selector({
            'ios_by': 'name',
            'ios_value': '请输入正确手机号码',
            'android_by': 'xpath',
            'android_value': '//*[@text="请输入正确手机号码"]',
        })