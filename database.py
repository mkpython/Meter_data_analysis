# -*- coding:utf-8 -*-

import pymysql

# 创建用来操作数据库的类
class Mysql_data():

    def __init__(self):
        self.host = 'localhost'
        self.port =3306
        self.user = 'root'
        self.password = 'root'
        self.db = 'test'
        self.charset = 'utf8'

    # 链接数据库
    def ConnectMysql(self):
        try:
            self.conn = pymysql.connect(host=self.host, port=self.port, user=self.user,
                                        passwd=self.password, db=self.db, charset=self.charset)
            self.cursor = self.conn.cursor()
        except:
            print('connect mysql error.')


    def creat_table(self):
        # 使用execute方法执行SQL语句
        self.cursor.execute("DROP TABLE IF EXISTS DATA1")
        # 创建数据表SQL语句
        sql = """CREATE TABLE DATA1(
                id  int(10) NOT NULL AUTO_INCREMENT,
                帧头  NVARCHAR(100),
                地市供电局信息  NVARCHAR(100),
                客户端类型  NVARCHAR(100),
                前置机信道  NVARCHAR(100),
                主站与集中器通讯  NVARCHAR(100),
                异常标志  NVARCHAR(100),
                功能  NVARCHAR(100),
                数据域DATA的字节数  NVARCHAR(100),
                校验位  NVARCHAR(100),
                结束符  NVARCHAR(100),
                PRIMARY KEY(id))"""
        self.cursor.execute(sql)

    def insert_data(self,tup):
        # SQL 插入语句
        sql = """INSERT INTO DATA1(帧头,地市供电局信息,客户端类型,前置机信道,主站与集中器通讯,异常标志,功能,数据域DATA的字节数,校验位,结束符)
                 VALUES ('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}')""".format(tup[0],tup[1],tup[2],
                                                                         tup[3],tup[4],tup[5],tup[6],
                                                                         tup[7],tup[8],tup[9])
        # print(sql)
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.conn.commit()
        except Exception as e:
            print(e)
            # Rollback in case there is any error
            self.conn.rollback()

    def print_data(self):
        self.cursor.execute("SELECT * FROM DATA1")
        results = self.cursor.fetchall()
        for row in results:
            id = row[0]
            FrameHeader= row[1]
            print('id={0},帧头={1}'.format(id, FrameHeader))

    def close_mysql(self):
        self.cursor.close()
        self.conn.close()

# data_test1 = Mysql_data()
# data_test1.ConnectMysql()
# data_test1.creat_table()
# a = ['正确','未知','大客户现场终端','集中器主动上报','由集中器发出的请求帧或应答帧','确认帧','集中器抄收日常综合数据','39','正确','正确',]
# b = ['正确','惠州','大客户现场终端','集中器主动上报','由集中器发出的请求帧或应答帧','确认帧','集中器抄收日常综合数据','39','正确','正确',]
# data_test1.insert_data(a)
# data_test1.insert_data(b)
# data_test1.close_mysql()
