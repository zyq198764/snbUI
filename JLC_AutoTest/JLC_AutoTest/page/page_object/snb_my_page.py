from JLC_AutoTest.page.page_ui_object.snb_my_page_ui import Snb_My_Page_UI
# from JLC_AutoTest.model.utils import JianlcTools
from JLC_AutoTest.common.settings import OLD_PHONE
from JLC_AutoTest.model.utils import OpMysql

#获取老用户登录的身份证号
opmysql=OpMysql('10.103.27.54','root','123123',3306,'snb_test2_live')
opmysql.connect_mysql()
userid=opmysql.op_db_select("SELECT user_id FROM `snb_test2_live`.`user_info`  WHERE phone='%s'"%OLD_PHONE)[0][0]
id_nums=opmysql.op_db_select("SELECT identity_number FROM `user_bank_card` WHERE user_id='%s'"%userid)[0][0]




#登录页面的元素
class SNB_My_page(Snb_My_Page_UI):
    """
        页面对象(PO): 我的页面
    """
    def get_my_tab_Loc_page(self):
        """
            点击我的页面
        :return:
        """
        return self.get_my_tab_Loc().click()

    def get_my_retreat_safely_Loc_page(self):
        """
            点击我的页面的安全退出按钮
        :return:
        """
        return self.get_my_retreat_safely_Loc().click()

    def get_my_retreat_safely_confirm_button_Loc_page(self):
        """
            点击退出弹层中确认按钮
        :return:
        """
        return self.get_my_retreat_safely_confirm_button_Loc().click()

    def get_login_switch_account_Loc_page(self):
        """
            点击登录注册页面的切换账号按钮
        :return:
        """
        return self.get_login_switch_account_Loc().click()

    def get_login_input_phone_Loc_page(self):
        """
            输入登录的手机号码
        :return:
        """
        return self.get_login_input_phone_Loc().send_keys(OLD_PHONE)

    def get_login_input_phone_next_button_Loc_page(self):
        """
            点击下一步按钮
        :return:
        """
        return self.get_login_input_phone_next_button_Loc().click()

    def get_login_verficode_input_Loc_page(self):
        """
            输入短信验证码
        :return:
        """
        return self.get_login_verficode_input_Loc().send_keys("123456")

    def get_login_button_Loc_page(self):
        """
            点击登录按钮
        :return:
        """
        return self.get_login_button_Loc().click()

    def get_login_password_login_Loc_page(self):
        """
            点击登录密码登录
        :return:
        """
        return self.get_login_password_login_Loc().click()

    def get_login_password_input_Loc_page(self):
        """
            输入密码
        :return:
        """
        return self.get_login_password_input_Loc().send_keys("q1234567890")

    def get_login_forget_password_Loc_page(self):
        """
            定位忘记密码
        :return:
        """
        return self.get_login_forget_password_Loc().click()

    def get_login_forget_password_Loc_page(self):
        """
            定位我的页面的title
        :return:
        """
        return self.get_login_forget_password_Loc().click()

    def get_my_discount_coupon_Loc_page(self):
        """
            点击我的页面的我的优惠券
        :return:
        """
        return self.get_my_discount_coupon_Loc().click()

    def get_my_discount_coupon_Loc_page(self):
        """
            点击我的页面的我的优惠券
        :return:
        """
        return self.get_my_discount_coupon_Loc().click()

    def get_my_discount_coupon_close_Loc_page(self):
        """
            点击我的页面的我的优惠券页面的关闭按钮
        :return:
        """
        return self.get_my_discount_coupon_close_Loc().click()

    def get_my_trans_record_Loc_page(self):
        """
            点击我的页面的交易记录
        :return:
        """
        return self.get_my_trans_record_Loc().click()

    def get_my_trans_record_all_Loc_page(self):
        """
            点击我的页面的交易记录页面的全部
        :return:
        """
        return self.get_my_trans_record_all_Loc().click()

    def get_my_trans_record_buy_Loc_page(self):
        """
            点击我的页面的交易记录页面的买入
        :return:
        """
        return self.get_my_trans_record_buy_Loc().click()

    def get_my_trans_record_redeem_Loc_page(self):
        """
            点击我的页面的交易记录页面的赎回
        :return:
        """
        return self.get_my_trans_record_redeem_Loc().click()

    def get_my_trans_record_ware_Loc_page(self):
        """
            点击我的页面的交易记录页面的调仓
        :return:
        """
        return self.get_my_trans_record_ware_Loc().click()

    def get_my_trans_record_buy01_Loc_page(self):
        """
            点击我的页面的交易记录页面的买入的记录
        :return:
        """
        return self.get_my_trans_record_buy01_Loc().click()

    def get_my_trans_record_redeem01_Loc_page(self):
        """
            点击我的页面的交易记录页面的赎回记录
        :return:
        """
        return self.get_my_trans_record_redeem01_Loc().click()

    def get_my_trans_record_buy_detail_type_Loc_page(self):
        """
            点击我的页面的交易记录页面的买入交易详情的交易类型
        :return:
        """
        return self.get_my_trans_record_buy_detail_type_Loc().text

    def get_my_trans_record_buy_detail_type1_Loc_page(self):
        """
            点击我的页面的交易记录页面的买入交易详情的交易类型为买入
        :return:
        """
        return self.get_my_trans_record_buy_detail_type1_Loc().text

    def get_my_trans_record_redeem_detail_type1_Loc_page(self):
        """
            点击我的页面的交易记录页面的赎回交易详情的交易类型为赎回
        :return:
        """
        return self.get_my_trans_record_redeem_detail_type1_Loc().text
    #以下是修改支付密码的操作

    def get_my_modify_payment_password_Loc_page(self):
        """
            点击我的页面的修改支付密码元素
        :return:
        """
        return self.get_my_modify_payment_password_Loc().click()

    def get_my_modify_payment_password_title_Loc_page(self):
        """
            获取我的页面的修改支付密码页面的title
        :return:
        """
        return self.get_my_modify_payment_password_title_Loc().text

    def get_my_retrieve_payment_password_Loc_page(self):
        """
            点击我的页面的找回支付密码
        :return:
        """
        return self.get_my_retrieve_payment_password_Loc().click()

    def get_my_retrieve_payment_password_title_Loc_page(self):
        """
            获取我的页面的找回支付密码页面的title
        :return:
        """
        return self.get_my_retrieve_payment_password_title_Loc().text

    def get_my_retrieve_payment_password_name_Loc_page(self):
        """
            获取我的页面的找回支付密码页面的真实姓名文本
        :return:
        """
        return self.get_my_retrieve_payment_password_name_Loc().text

    def get_my_retrieve_payment_password_idnuminput_Loc_page(self):
        """
            输入我的页面的找回支付密码页面的身份证号
        :return:
        """
        return self.get_my_retrieve_payment_password_idnuminput_Loc().send_keys(id_nums)

    def get_my_retrieve_payment_password_idnum_verficode_Loc_page(self):
        """
            输入我的页面的找回支付密码页面的输入短信验证码
        :return:
        """
        return self.get_my_retrieve_payment_password_idnum_verficode_Loc().send_keys("123456")

    def get_my_retrieve_payment_password_idnum_confirm_Loc_page(self):
        """
            点击我的页面的找回支付密码页面的确认按钮
        :return:
        """
        return self.get_my_retrieve_payment_password_idnum_confirm_Loc().click()

    def get_retrieve_payment_password_nextbutton_Loc_page(self):
        """
            点击我的页面的找回支付密码页面的确认按钮
        :return:
        """
        return self.get_retrieve_payment_password_nextbutton_Loc().click()
    #以下是修改登录密码的操作

    def get_my_modify_login_password_Loc_page(self):
        """
            点击我的页面的修改登录密码
        :return:
        """
        return self.get_my_modify_login_password_Loc().click()

    def get_my_modify_login_password_input_Loc_page(self):
        """
            输入我的页面的修改登录密码页面的当前登录密码
        :return:
        """
        return self.get_my_modify_login_password_input_Loc().send_keys("q1234567890")
    def get_my_modify_login_password_inputnew_Loc_page(self):
        """
            输入我的页面的修改登录密码页面的新密码
        :return:
        """
        return self.get_my_modify_login_password_inputnew_Loc().send_keys("q1234567890")

    def get_my_modify_login_password_inputnewconfirm_Loc_page(self):
        """
            输入我的页面的修改登录密码页面的确认新密码
        :return:
        """
        return self.get_my_modify_login_password_inputnewconfirm_Loc().send_keys("q1234567890")

    def get_my_modify_login_password_confirmbutton_Loc_page(self):
        """
            点击我的页面的修改登录密码页面的确认修改按钮
        :return:
        """
        return self.get_my_modify_login_password_confirmbutton_Loc().click()



