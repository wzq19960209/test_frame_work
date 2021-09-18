import os
IP = 'http://121.42.15.146:9090/'
HEADERS = {'X-Requested-With':'XMLHttpRequest'}

#获取当前文件绝对路径的，可以和其他文件组成动态地址
AbS_PATH =os.path.abspath(__file__)
DIR_NAME = os.path.dirname(AbS_PATH)

#如果是动态产生的数据，我们直接导入文件，然后用文件.变量去使用
JUMP_URL = None