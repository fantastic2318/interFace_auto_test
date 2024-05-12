import re

from Utils.GlobalUtil import global_v
from Utils.LogUtil import log
from Utils.YamlUtil import config_item
from Utils.KeyWordUtil import get_id, get_name, get_age


def params_replace(content):
    # keys = re.findall(config_item['pattern'], content)
    Pattern = '\$\{(.*?)\}'
    keys = re.findall(Pattern, content)
    for key in keys:
        if key in global_v.globalVars.keys():
            value = global_v.getVar(key)
            content = content.replace('${' + key + '}', str(value))
        else:
            log.debug(f'"{key}" is not contained in {global_v.globalVars.keys()}')
            if str(key).endswith(')'):
                value = eval(key)
                content = content.replace('${' + key + '}', str(value))

    return content


if __name__ == '__main__':
    #Pattern = '\$\{(.*?)\}'
    global_v.setVar('host', '127.0.0.1')
    global_v.setVar('id', 99)
    contents = 'http://${host}/cat_detail/${id}'
    print(params_replace(contents))