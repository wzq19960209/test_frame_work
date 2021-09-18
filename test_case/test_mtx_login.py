import pytest
import requests
from test_framework.tools import readExcel
from test_framework.api.api_login import api_login
import allure

# ids = ['正向用例','反向用例','反向用例']   #用例说明的个数要与用例执行的次数一致，否则会报错
yaml_data = readExcel.ReadeExcel().get_yaml('login_data','test_login')
class TestMtx:
    #在所以的测试用例之前做创建session，实例化登录接口对象  ->setup.class
    def setup_class(self):
        # 创建一个session对象
        self.session=requests.Session()
        #实例化登录接口对象
        self.login_object = api_login()

    @pytest.mark.parametrize('dic',yaml_data )
    @allure.title('登录的测试用例')
    @allure.feature('登录功能')
    @allure.story('登录的参数：正向和逆向')
    def test_login_list(self,dic):
        #读取数据，进行构造data，然后发起请求
        data = {'accounts':dic['accounts'],'pwd':dic['pwd']}
        res=self.login_object.login(self.session,data)
        assert res['msg'] == dic['exp']