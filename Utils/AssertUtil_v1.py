import jsonpath

from Config.settings import SIGNMAP
from Utils.LogUtil import log
'''
@todo比较方式写成变量  灵活比较 不只是使用‘等于’“包含”
'''


def assert_res(assertRes, res):
    try:
        if res is None:
            raise Exception('res is None')
        #
        # if isinstance(assertRes, list):
        #     assert assertRes[0] == res['data'][0]
        #     return
        for tmp_res in assertRes.split(';'):
            # EXPRESS 整体表达式
            express = tmp_res.split(',')
            if len(express) == 2:
                sign = express[0]
                if sign in SIGNMAP:
                    signal = SIGNMAP[sign]
                except_value = express[1].split('=')[1]
                actual_value_express = express[1].split('=')[0]
                actual_value = jsonpath.jsonpath(res, actual_value_express)
                if actual_value is False:
                    log.exception(f'{actual_value_express} is not contained in {res}')
                else:
                    actual_value = actual_value[0]
                    assert eval(str(actual_value) + ' ' + signal + ' ' + except_value), f"assert {str(actual_value)}{signal}{except_value}"
    except Exception as e:
        log.exception(e)


if __name__ == '__main__':
    #assert 1 == 1
    assert_res('equal,$.success=True;equal,$.code=200', {'code': 200, 'data': 5, 'success': True})