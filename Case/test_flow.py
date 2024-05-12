import pytest

from Utils.AssertUtil_v1 import assert_res
from Utils.ExcelUtil import get_params, get_params_value
from Utils.GlobalUtil import global_v
from Utils.LogUtil import log
from Utils.MysqlUtil import dbMysql
from Utils.ParamUtil import params_replace
from Utils.RequestUtil import send_request
from Utils.YamlUtil import config_item

params = get_params('data.xlsx', 'flow', 1)
params_values = get_params_value('data.xlsx', 'flow')


@pytest.mark.parametrize(params, params_values)
def test_flow(project, module, caseid, casename, description, path, method, headers, param, contenttype, assertres, globalVars, aftersql):
    url = config_item['url']
    url = url + path
    transUrl = params_replace(url)
    res = send_request(url=transUrl, params=param, headers=headers, method=method, content_type=contenttype)
    log.info(res)
    if assertres:
        assert_res(assertres, res)

    if globalVars:
        global_v.save_globalVars(globalVars, res)


if __name__ == '__main__':
        pytest.main(['-vs', 'test_flow.py'])