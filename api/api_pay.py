from test_framework import setting
from test_framework.tools.logger import GetLogger
logger = GetLogger().get_logger()
class api_pay():
    def __init__(self):

        self.url=setting.JUMP_URL
        logger.info(f'获取jump_url为{self.url}')
    def pay(self,session):
        #对302接口禁止重定向
        logger.info(f'准备对{self.url}发起请求，并阻止接口重定向')
        resp=session.get(self.url,allow_redirects=False)
        # 提取响应头中的location
        r=session.get(resp.headers['location'])
        logger.info(f'提取数据：请求响应头数据为{resp.headers}')
        logger.info(f'发起请求：请求响应值为{r}')
        #对location后面的地址发起请求，然后获取响应，以便testcase中做断言
        return r












