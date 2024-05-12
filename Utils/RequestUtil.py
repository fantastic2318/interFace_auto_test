'''
Created
@author: wuf
@description:发送请求util
@time: 2024/04/14
'''
import json

import requests

from Utils.LogUtil import log
def send_request(url, method, params=None, content_type=None, headers=None):
    try:
        if method.lower() == 'get':
            r = requests.get(url=url, params=params, headers=headers)
            if params is None:
                log.info('params is None: ' + f'[{method}]:{url}')
        elif method.lower() == 'post':
            if content_type == 'application/json':
                # 将字符串转换成字典
                params = json.loads(params)
                r = requests.post(url=url, json=params, headers=headers)
            elif content_type == 'application/x-www-form-urlencoded':
                log.info(f'{method}:{url}:{params}')
                r = requests.post(url=url, data=params, headers=headers)
            else:
                log.debug('only support json and x-www-form-urlencoded')
            log.info(f'[{method}]:{url}/{params}')
        else:
            log.debug('only support method "get" or "post"')

        return r.json()
    except Exception as e:
        log.exception('http request error: {}'.format(e))


if __name__ == '__main__':
    res1 = send_request(url='http://119.3.223.250:5000/cat_list', method='get')
    # res = send_request(url='http://119.3.223.250:5000/cat_add', method='post', params={"id": 6, "name": "sss", "age": 10}, content_type='application/json')
    # print(res)
    print(res1)







