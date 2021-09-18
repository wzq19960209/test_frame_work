'''
前提：依赖登录接口
下订单的所有场景
step1：先调用登录接口
2.下订单接口
宗旨：设计测试用例的时候，接口调用之间没有依赖关系(降到最低)
举例：存在依赖关系的接口，失败了，并不会影响下游接口的调用
'''

from test_framework.api.api_order import api_order
from test_framework.api.api_login import api_login
import requests
class TestOrder:
    def setup_class(self):
        #创建session对象
        self.session=requests.Session()
        #创建order对象
        self.order_obj= api_order()
        #调用成功的登录接口
        api_login().login_success(self.session)

    def test_order(self):
        res_order=self.order_obj.order(self.session)

        assert res_order['msg'] == '提交成功'