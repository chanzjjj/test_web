from pages.MaiLingLingYunCheng import Mailinglingyuncheng
import time
import re

class TestMaiLingLingYunCheng():

    def test_01(self, mllyc:Mailinglingyuncheng):
        '''输入中文姓名太短是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.short_name()
        acturl_tips = mllyc.get_tips()
        expect_tips = "姓名最少2个字"
        assert acturl_tips == expect_tips

    def test_02(self, mllyc:Mailinglingyuncheng):
        '''输入中文姓名太长是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.long_name()
        acturl_tips = mllyc.get_tips()
        expect_tips = "姓名不超过5个字"
        assert acturl_tips == expect_tips

    def test_03(self, mllyc:Mailinglingyuncheng):
        '''输入英文姓名太短是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.short_english_name()
        acturl_tips = mllyc.get_tips()
        expect_tips = "英文姓名最少3个字母"
        assert acturl_tips == expect_tips

    def test_04(self, mllyc:Mailinglingyuncheng):
        '''输入英文姓名太长是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.long_english_name()
        acturl_tips = mllyc.get_tips()
        expect_tips = "英文姓名不超过10个字母"
        assert acturl_tips == expect_tips

    def test_05(self, mllyc:Mailinglingyuncheng):
        '''输入正常的信息是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.normal_information()
        current_url = mllyc.get_url()
        acturl_url = re.findall("https://(.+?)order_id", current_url)[0]
        expect_url = "cs.lingbz.com/pay/mllyuncheng?"
        assert  acturl_url == expect_url

    def test_06(self, mllyc:Mailinglingyuncheng):
        '''调起微信支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.wechat_pay()
        acturl_title = mllyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_07(self, mllyc:Mailinglingyuncheng):
        '''调起支付宝支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.zfb_pay()
        acturl_title = mllyc.get_title()
        expect_title = "支付宝 - 网上支付 安全快速！"
        assert acturl_title == expect_title

    def test_08(self, mllyc:Mailinglingyuncheng):
        '''调起银联支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.yl_pay()
        acturl_title = mllyc.get_title()
        expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
        assert acturl_title == expect_title

    def test_09(self, mllyc:Mailinglingyuncheng):
        '''调起paypal支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.pp_pay()
        acturl_title = mllyc.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title

    def test_10(self, mllyc:Mailinglingyuncheng):
        '''跳转到历史订单是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.lsdd()
        current_url = mllyc.get_url()
        acturl_url = re.findall("https://(.+?)/index?", current_url)[0]
        expect_url = "cs.lingbz.com/orderquery"
        assert acturl_url == expect_url

    def test_11(self,mllyc:Mailinglingyuncheng):
        '''调起历史订单的微信支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.dd_wechat_pay()
        acturl_title = mllyc.get_title()
        expect_title = "灵机支付 - 微信扫码支付"
        assert acturl_title == expect_title

    def test_12(self, mllyc:Mailinglingyuncheng):
        '''调起历史订单的支付宝支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.dd_zfb_pay()
        acturl_title = mllyc.get_title()
        expect_title = "支付宝 - 网上支付 安全快速！"
        assert acturl_title == expect_title

    def test_13(self, mllyc:Mailinglingyuncheng):
        '''调起历史订单的银联支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.dd_yl_pay()
        acturl_title = mllyc.get_title()
        expect_title = "银联在线支付-银行卡综合性网上交易转接清算平台！"
        assert acturl_title == expect_title

    def test_14(self, mllyc:Mailinglingyuncheng):
        '''调起历史订单的paypal支付是否正常'''
        mllyc.open("/mllyuncheng/index?channel=online_paytest")
        mllyc.dd_pp_pay()
        acturl_title = mllyc.get_title()
        expect_title = "登录您的PayPal账户"
        assert acturl_title == expect_title