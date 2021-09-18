import logging.handlers
from test_framework import setting
##单例模式的思想：通过逻辑控制，只生成一个对象
class GetLogger():
    '''
    当已经创建了logger对象的适合，那么之后就不在创建了，也就是只创建一次对象
    '''

    #把logger对象的初始值设置为None
    logger=None

    #创建logger，并且返回这个logger
    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            cls.logger = logging.getLogger()
            # 设置总的级别    级别都需要大写
            cls.logger.setLevel(logging.INFO)
            # 2.获取格式器
            # 2.1  给格式器设置要输出的样式
            fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
            # 2.2 创建格式器，并且
            fm = logging.Formatter(fmt)

            # 3.创建处理器，按照时间进行切割文件
            tf = logging.handlers.TimedRotatingFileHandler(filename=setting.DIR_NAME+'/logger/test.log',
                                                           when='S',  # 间隔多长时间把日志存放到新的文件中
                                                           interval=1,
                                                           backupCount=3,  # 除了原日志，还有3个备份
                                                           encoding='utf-8')
            # 在处理器中添加格式器
            tf.setFormatter(fm)
            # 在日志器中添加处理
            cls.logger.addHandler(tf)
        return cls.logger



if __name__ == '__main__':
    logger=GetLogger()

#学习完本文件内容可至pymysqltools.py文件学习简单的如何用python链接数据库，执行一些sql语句



























#1.获取日志器(日记本)
logger = logging.getLogger()
#设置总的级别    级别都需要大写
logger.setLevel(logging.ERROR)
# 2.获取格式器
# 2.1  给格式器设置要输出的样式
fmt='%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
# 2.2 创建格式器，并且
fm=logging.Formatter(fmt)

# 3.创建处理器，按照时间进行切割文件
tf =logging.handlers.TimedRotatingFileHandler(filename='./test.log',
                                          when='S',    #间隔多长时间把日志存放到新的文件中
                                          interval=1,
                                          backupCount=3,   #除了原日志，还有3个备份
                                          encoding='utf-8')
#在处理器中添加格式器
tf.setFormatter(fm)
#在日志器中添加处理器
logger.addHandler(tf)