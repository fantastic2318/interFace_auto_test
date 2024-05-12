from Utils.MysqlUtil import dbMysql


# def query_value(checksql):
#     dbRes = dbMysql.execute(res, checksql)
#     print(dbRes)
#     # if isinstance(assertRes, list):
#     #     assert assertRes[0] == res['data'][0]
#     #     return

# def checkSql(checksql):
#     sqls = checksql.split(',')[-1]
#     params = checksql.split(',')[:-1]

# if __name__ == '__main__':
#     query_value('')

def checkSql(checksql, id):
    db_conn = dbMysql
    sql = "select * from cat where id = '%d'" % (id)
    result = db_conn.execute('', sql)[0]
    valueDict = eval(checksql)
    for k, v in valueDict.items():
        if k in result:
            assert v == result[k], str(v) + " is not equal to" + str(result[k])

# 就是数据库和assert 结合


if __name__ == '__main__':

    checkSql("{'id': 2928, 'name': '唐凤兰', 'age': 24}", 2928)