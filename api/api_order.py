from test_framework import setting
from test_framework.tools.logger import GetLogger
logger = GetLogger().get_logger()
class api_order:
    def __init__(self):
        logger.info('准备初始化请求地址')
        self.url = setting.IP + '/mtx/index.php?s=/index/buy/add.html'
        logger.info(f'请求地址为{self.url}')


    def order(self,session):
        '''
        发起下订单的请求
        :param session:
        :return:
        '''
        logger.info('准备发起下订单请求')

        data = {
            'goods_id': 1,
            'stock': 1,
            'buy_type': 'goods',
            'address_id': 1290,
            'payment_id': 1,
            'spec': '',
        }
        logger.info(f'准备发起order的请求,请求的参数是{data}，header是{setting.HEADERS}')
        resp_order = session.post(self.url,data=data,headers=setting.HEADERS)
        r=resp_order.json()
        logger.info(f'请求响应值为{r}')
        # 产生数据->并把数据放到setting当中(注意)
        setting.JUMP_URL = resp_order.json().get('data').get('jump_url')
        logger.info(f'提取数据:响应值中的jump_url字段为{setting.JUMP_URL}')
        return r


if __name__ == '__main__':
    data = api_order().order().json()
    print(data)