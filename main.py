import logging
import time

import mysql.connector

logger = logging.getLogger()

config_master = {
    'user': 'root',
    'password': 'your-password',
    'host': 'mysql-master.default.svc.cluster.local',
    'port': '3306'
}

config_slave = {
    'user': 'root',
    'password': 'your-password',
    'host': 'mysql-slave.default.svc.cluster.local',
    'port': '3306'
}


class MysqlUtil:

    def __init__(self):
        pass

    def query_from_master(self):
        sql = "select * from test.users"
        conn = mysql.connector.connect(**config_master)
        cursor = conn.cursor()
        cursor.execute(sql)
        raws = cursor.fetchall()
        print("query result from master:")
        for raw in raws:
            print(raw)
        conn.close()

    def query_from_slave(self):
        sql = "select * from test.users"
        conn = mysql.connector.connect(**config_slave)
        cursor = conn.cursor()
        cursor.execute(sql)
        raws = cursor.fetchall()
        print("query result from slave:")
        for raw in raws:
            print(raw)
        conn.close()

    def insert(self):
        sql = f"""
                INSERT INTO 
                    test.users (username, email, birthdate, is_active)
                VALUES
                    ('xxx', 'xxx@runoob.com', '1998-07-10', true)
               """
        conn = mysql.connector.connect(**config_master)
        cursor = conn.cursor()
        cursor.execute(sql)
        conn.commit()
        conn.close()
        print("insert master succeed")


mysql_util = MysqlUtil()
print("===========")
logger.info("*************")
mysql_util.insert()
mysql_util.query_from_master()
mysql_util.query_from_slave()
time.sleep(10)
