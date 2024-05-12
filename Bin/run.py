'''
生成报告
对接CICD处
'''
import pytest

from Config.settings import TEST_REPORT_PATH, TEST_CASE_DIR

if __name__ == '__main__':
    pytest.main(['-vs', TEST_CASE_DIR, '--alluredir', TEST_REPORT_PATH+'/xml'])