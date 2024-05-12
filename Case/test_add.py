import pytest

from Utils.AssertUtil_v1 import assert_res
from Utils.ExcelUtil import get_params, get_params_value
from Utils.LogUtil import log
from Utils.RequestUtil import send_request
from Utils.YamlUtil import config_item

params = get_params('data.xlsx', 'add', 1)
params_values = get_params_value('data.xlsx', 'add')

#print(params)

    # params = get_params('data.xlsx', 'data', 1)
    # params_value = get_params_value('data.xlsx', 'data')

    # def setup(self):
    #     self.params = get_params('data.xlsx', 'data', 1)
    #     self.params_value = get_params_value('data.xlsx', 'data')

@pytest.mark.parametrize(params, params_values)
def test_add(project, module, caseid, casename, description, path, method, headers, param, contenttype, assertres, globalVars):
    url = config_item['url']
    url = url + path
    res = send_request(url=url, params=param, headers=headers, method=method, content_type=contenttype)
    log.info(res)
    if assertres:
        assert_res(assertres, res)

    if globalVars:
        pass



if __name__ == '__main__':
        pytest.main(['-vs', 'test_add.py'])