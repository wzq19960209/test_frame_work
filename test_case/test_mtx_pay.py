from test_framework.api.api_login import api_login
from test_framework.api.api_order import api_order
from test_framework.api.api_pay import api_pay
import requests
class Test_pay():
    def setup_class(self):
        # 创建session
        self.session=requests.Session()
        #先调用成功的登录接口
        api_login().login_success(self.session)
        #调用下订单接口
        api_order().order(self.session)
        #创建支付对象
        self.pay_obj = api_pay()

    def test_pay(self):
        resp_pay = self.pay_obj.pay(self.session)

        assert '支付成功' in resp_pay.text