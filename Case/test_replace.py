import pytest

from Lib.mysql import checkSql
from Utils.AssertUtil_v1 import assert_res
from Utils.ExcelUtil import get_params, get_params_value
from Utils.GlobalUtil import global_v
from Utils.LogUtil import log
from Utils.MysqlUtil import dbMysql
from Utils.ParamUtil import params_replace
from Utils.RequestUtil import send_request
from Utils.YamlUtil import config_item

params = get_params('data.xlsx', 'repalce', 1)
params_values = get_params_value('data.xlsx', 'repalce')


@pytest.mark.parametrize(params, params_values)
def test_replace(project, module, caseid, casename, description, path, method, headers, param, contenttype, assertres, globalVars, checksql, aftersql):
    url = config_item['url']
    url = url + path
    transUrl = params_replace(url)
    transParam = params_replace(param) if param is not None else None
    res = send_request(url=transUrl, params=transParam, headers=headers, method=method, content_type=contenttype)
    log.info(res)
    if assertres:
        assert_res(assertres, res)

    if globalVars:
        global_v.save_globalVars(globalVars, res)

    # 验证返回值是否同数据库中存储的数据一致
    print(global_v.globalVars)
    if checksql:
        checkSql(checksql, global_v.globalVars['cat_id'])
        # dbRes = dbMysql.execute(res, checksql)
        # assert_res(dbRes, res['data'][0])

    # if aftersql:
    #     dbMysql.execute(res, aftersql)


if __name__ == '__main__':
        pytest.main(['-vs', 'test_replace.py'])