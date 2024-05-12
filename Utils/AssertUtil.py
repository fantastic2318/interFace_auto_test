import jsonpath

from Utils.LogUtil import log
'''
@todo比较方式写成变量  灵活比较 不只是使用‘等于’“包含”
'''


def assert_res(assertRes, res):
    try:
        if res is None:
            raise Exception('res is None')
        for tmp_res in assertRes.split(';'):
            except_value = tmp_res.split('=')[1]
            actual_value_express = tmp_res.split('=')[0]
            actual_value = jsonpath.jsonpath(res, actual_value_express)
            if actual_value is False:
                log.exception(f'{actual_value_express} is not contained in {res}')
            else:
                actual_value = actual_value[0]
                assert str(actual_value) == except_value, f"Expected {except_value}, got {str(actual_value)}"
    except Exception as e:
        log.exception(e)


if __name__ == '__main__':
    assert_res('$.success=True', {'code': 200, 'data': 5, 'success': True})


    #assert_res('$.success=True;$.code=200', {'code': 200, 'data': 5})