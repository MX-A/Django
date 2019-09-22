import sys,os
# import MySQLdb
import pymysql
import random
from datetime import *

def save_date(A,B,C,D,E,F):
    # 这个程序是向MYSQL服务器里写数据的
    # 数据库连接
    db = pymysql.connect('localhost', 'ak47', '123456', 'test')
    cursor = db.cursor()  # 光标
    UA = A
    UB = B
    UC = C
    IA = D
    IB = E
    IC = F
    dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    name = str(dates)
    # 批量插入数据
    SQL = "INSERT INTO myapp_s821(" \
          "name,UA, UB,UC,IA,IB,IC,date) VALUES ('%s','%.2f','%.2f','%.2f','%.2f','%.2f','%.2f','%s')" % \
          (name, UA, UB, UC, IA, IB, IC, dates)
    try:
        # 执行sql语句
        cursor.execute(SQL)
        # 提交到数据库执行
        db.commit()
    except:
        # Rollback in case there is any error
        db.rollback()
    db.close()
#
# def save_s821_data(A,B,C,D,E,F,cursor,db):
#     # time.sleep(1)
#     UA = A
#     UB = B
#     UC = C
#     IA = D
#     IB = E
#     IC = F
#     dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#     name = str(dates)
#     # 批量插入数据
#     SQL = "INSERT INTO myapp_s821(" \
#           "name,UA, UB,UC,IA,IB,IC,date) VALUES ('%s','%.2f','%.2f','%.2f','%.2f','%.2f','%.2f','%s')" % \
#           (name, UA, UB, UC, IA, IB, IC, dates)
#     try:
#         # 执行sql语句
#         cursor.execute(SQL)
#         # 提交到数据库执行
#         db.commit()
#     except:
#         # Rollback in case there is any error
#         db.rollback()
#     cursor.execute('select * from myapp_s821')
#     data = cursor.fetchall()
#     print(data)
