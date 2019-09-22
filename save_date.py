import sys,os
# import MySQLdb
import pymysql
import random
from datetime import *
import time
import re
import glob


def save_s821_data():
    for i in range(0, 300):
        # time.sleep(1)
        UA = random.uniform(0, 0.3)
        UB = random.uniform(0, 0.3)
        UC = random.uniform(0, 0.3)
        IA = random.uniform(0, 0.3)
        IB = random.uniform(0, 0.3)
        IC = random.uniform(0, 0.3)
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
    cursor.execute('select * from myapp_s821')
    data = cursor.fetchall()
    print(data)


def save_picture():
    path = glob.glob(r"H:\django-test\mytest\static\picture/*/*")
    s = len('H:\django-test\mytest\\')
    # stt = os.path.basename(path[100])
    # print(stt)
    for picture in path:
        picture_name=os.path.basename(picture)
        dates = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        picture_url=picture[s:].replace('\\','/')
        SQL = "INSERT INTO myapp_picture(" \
              "name,date, image_path) VALUES ('%s','%s','%s')" % \
              (picture_name, dates, picture_url)
        try:
            # 执行sql语句
            cursor.execute(SQL)
            # 提交到数据库执行
            db.commit()
        except:
            # Rollback in case there is any error
            db.rollback()
    cursor.execute('select * from myapp_picture')
    data = cursor.fetchall()
    print(data)
# 这个程序是向MYSQL服务器里写数据的
# 数据库连接
db = pymysql.connect('localhost', 'root', '000000', 'test')
cursor = db.cursor()  # 光标

# save_s821_data()

save_picture()

# # 关闭数据库连接
db.close()

# path = glob.glob("H:\django-test\mytest\static\picture/*/*")
# s=len('H:\django-test\mytest\\')
# for i in path:
#     print(i[s:].replace('\\','/'))