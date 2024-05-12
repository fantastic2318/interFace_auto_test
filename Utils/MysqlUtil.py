import re

import jsonpath
import pymysql

from Utils.LogUtil import log
from Utils.YamlUtil import config_item


class DbMysql:
    _conn = ''
    _cursor = ''

    def __init__(self, info):
        try:
            self._conn = pymysql.connect(host=info['host'], port=info['port'], user=info['user'],
                                         password=info['password'],
                                         db=info['db'], charset='utf8', cursorclass=pymysql.cursors.DictCursor)
            self._cursor = self._conn.cursor()
        except pymysql.Error as e:
            log.exception(f'Mysql connect error {e}')

    # def close(self):
    #     self._cursor.close()
    #     self._conn.close()

    def execute(self, res='', sqls=''):
        if sqls is None or len(sqls) == 0:
            log.error('sqls is empty or sqls == '' ')
            return False
        if 'where' in sqls and res != '':
            afterSqls = self.comSql(res, sqls)
        else:
            afterSqls = sqls
        for sql in afterSqls.split(';'):
            operator = sql[:6].lower()
            if operator == 'select':
                dbRes = self.query(sql)
            elif operator == 'delete' or 'update':
                dbRes = self.operate(sql)
            elif operator == 'insert':
                dbRes = self.insert(sql)
            else:
                 log.error(f'mysql operator is not supported: {sqls}')
        self._cursor.close()
        self._conn.close()
        return dbRes

    def insert(self,sql):
        log.info(f'insert sql: {sql}')
        try:
            rows = self._cursor.execute(sql)
            db_id = int(self._conn.insert_id())
            self._conn.commit()
            log.info(f'db insert {rows} with id {db_id}')
            return db_id
        except pymysql.Error as e:
            self._conn.rollback()
            log.error(f'mysql insert error {e}')

    def query(self, sql):
        log.info(f'query sql: {sql}')
        try:
            self._cursor.execute(sql)
            result = self._cursor.fetchall()
            log.info(f'query res: {result}')
            return result
        except pymysql.Error as e:
            log.exception(f' Mysql query error {e}')
            return False

    def operate(self, sql):
        log.info(f'delete sql: {sql}')
        try:
            rows = self._cursor.execute(sql)
            self._conn.commit()
            log.info(f'affect: {rows}')
            return rows
        except pymysql.Error as e:
            self._conn.rollback()
            log.error(f'Mysql operate error: {e}')
            return False

    def comSql(self, res, sqls):
        """
        组合SQL
        :param res: case execute result
        :param sqls: 要执行的sqls
        :return:
        """
        # param = sqls.split('=')[0].split(' ')[-2]
        # print(param)
        resultSqls = []
        for sql in sqls.split('\n'):
            if sql != '':
                value = sql.split('=')[1].strip()
                paramValue = jsonpath.jsonpath(res['data'][0], value)[0]
                # 组合SQL
                afterSql = sql.split('=')[0] + '=' + ' ' + str(paramValue)
                resultSqls.append(afterSql)
        return resultSqls


dbMysql = DbMysql(config_item['dbInfo'])


if __name__ == '__main__':
    sqls = ("select * from cat where id = $.id;\ndelete from cat where id = $.id;")
    res = {'code': 200, 'data': [{'age': 60, 'id': 2655, 'name': '韩佳'}], 'success': True}
    # s = sqls.split('\n')
    # print(s)
    # afterSqls = dbMysql.comSql(res, sqls)
    # print(afterSqls)
    print(dbMysql.execute(res, sqls))

