from pages.LunHuiShu import Lunhuishu
import time
import re

class TestLunHuiShu():

    def test_01(self, lhs:Lunhuishu):
        '''不输入姓名是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.empty_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "请选择出生日期"
        assert acturl_tips == expect_tips

    def test_02(self, lhs:Lunhuishu):
        '''输入中文姓名太短是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.short_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_03(self, lhs:Lunhuishu):
        '''输入中文姓名太长是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.long_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_04(self, lhs:Lunhuishu):
        '''输入英文姓名太短是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.short_english_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_05(self, lhs:Lunhuishu):
        '''输入英文姓名太长是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.long_english_name()
        acturl_tips = lhs.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_06(self, lhs:Lunhuishu):
        '''输入正常的信息是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.normal_information()
        current_url = lhs.get_url()
        acturl_url = re.findall("https://(.+?)/pay?", current_url)[0]
        expect_url = "cs.lingbz.com/lunhuishu"
        assert  acturl_url == expect_url

    def test_07(self, lhs:Lunhuishu):
        '''调起微信支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.wechat_pay()
        acturl_title = lhs.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_08(self, lhs:Lunhuishu):
        '''调起支付宝支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.zfb_pay()
        acturl_title = lhs.get_title()
        expect_title = "支付宝 - 网上支付 安全快速！"
        assert acturl_title == expect_title

    def test_09(self, lhs:Lunhuishu):
        '''调起银联支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.yl_pay()
        acturl_title = lhs.get_title()
        expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
        assert acturl_title == expect_title

    def test_10(self, lhs:Lunhuishu):
        '''调起paypal支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.pp_pay()
        acturl_title = lhs.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title

    def test_11(self, lhs:Lunhuishu):
        '''跳转到历史订单是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.lsdd()
        current_url = lhs.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_12(self,lhs:Lunhuishu):
        '''调起历史订单的微信支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_wechat_pay()
        acturl_title = lhs.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_13(self, lhs:Lunhuishu):
        '''调起历史订单的支付宝支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_zfb_pay()
        acturl_title = lhs.get_title()
        expect_title = "支付宝 - 网上支付 安全快速！"
        assert acturl_title == expect_title

    def test_14(self, lhs:Lunhuishu):
        '''调起历史订单的银联支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_yl_pay()
        acturl_title = lhs.get_title()
        expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
        assert acturl_title == expect_title

    def test_15(self, lhs:Lunhuishu):
        '''调起历史订单的paypal支付是否正常'''
        lhs.open("/lunhuishu/index?channel=online_paytest")
        lhs.dd_pp_pay()
        acturl_title = lhs.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title




