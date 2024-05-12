import os.path

URL = 'http://119.3.223.250:5000/'
# 文件夹路径
BASE = os.path.dirname(os.path.dirname(__file__))

# 日志文件地址
LOG_PATH = os.path.join(BASE, 'Log')

# 测试数据路径
TEST_DATA_PATH = os.path.join(BASE, 'Data')

# 测试用例路径
TEST_CASE_DIR = os.path.join(BASE, 'Case')

# 环境配置路径
CONFIG_PATH = os.path.join(BASE, 'Config')
#print(LOG_PATH)

# 测试报告路径
TEST_REPORT_PATH = os.path.join(BASE, 'Reports')

SIGNMAP = {'equal': '==', 'not_equal': '!=', 'contain': 'in', 'not_contain': 'not in'}


