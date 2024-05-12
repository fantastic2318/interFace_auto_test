import jsonpath

from Utils.LogUtil import log


class GlobalVariables:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '__instance'):
            cls.__instance = super(GlobalVariables, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.globalVars = {}

    def setVar(self, key, value):
        self.globalVars[key] = value
        log.info(f'当前全局变量{self.globalVars}')

    def getVar(self, key):
        return self.globalVars.pop(key)

    def save_globalVars(self, globalVars, res):
        for temp in globalVars.split(';'):
            if temp != '':
                key = temp.split('=')[0]
                value11 = temp.split('=')[1]
                value = jsonpath.jsonpath(res, value11)[0]
                if value is not False:
                    self.setVar(key, value)
                else:
                    log.error(f'{res} do not contain {value11}')


global_v = GlobalVariables()


if __name__ == '__main__':
    # global_v.getVar()
    # s = global_v.getVar(['host', 'cat_id'])
    # print(s)
    global_v = GlobalVariables()
    res = {'code': 200, 'data': 8, 'success': True}
    globalval = 'cat_id=$.data;'
    global_v.save_globalVars(globalval, res)
