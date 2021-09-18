'''
接口层
登录接口的东西写在这
'''
import requests
from test_framework import setting
from test_framework.tools.logger import GetLogger
logger = GetLogger().get_logger()
class api_login():
    def __init__(self):
        '''
        日志逗号不能拼接变量
        '''
        logger.info('开始获取url地址：')
        self.url=setting.IP+'/mtx/index.php?s=/index/user/login.html'
        logger.info('url地址是',self.url)
    def  login(self,session,data):
        '''
        对登录接口进行自动化测试
        场景1：如果需要动态的传递就进行参数化，业务层传递数据
        2.如果只是验证这个功能，直接写死即可
        :param accounts:
        :param pwd:
        :return:
        '''
        logger.info(f'准备发起login的请求,请求的参数是{data}，header是{setting.HEADERS}')
        resp_login= session.post(self.url,data=data,headers=setting.HEADERS)
        r = resp_login.json()
        logger.info('获取的响应值是%s'%r)
        return r

    def  login_success(self,session):
        '''
        这个接口必过，跟其他接口进行关联，发起成功的登录请求
        :param accounts:
        :param pwd:
        :return:
        '''
        logger.info('准备发起成功的login请求：')
        data={'accounts':'yaoyao',
            'pwd':'yaoyao'}
        logger.info('成功请求的数据是{}'.format(data))
        res= session.post(url=self.url,data=data,headers=setting.HEADERS)
        r=res.json()
        logger.info('获取的响应值是%s'%r)

        return r




