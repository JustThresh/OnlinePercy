"""
    本文件方法为本项目公用工具方法
    The method of this document is the public tool method of this project
    @Author: WangFeng
    @date: 2019-11-13
    @software: Pycharm
"""
import datetime
import time


# datetime格式转换为字符串格式
def datetime_to_str(dt):
    data = dt.strftime("%Y-%m-%d %H:%M:%S")
    return data


# 把字符串格式转换成datetime格式
def string_to_datetime(st):
    data = datetime.datetime.strptime(st, "%Y-%m-%d %H:%M:%S")
    return data


# 把字符串转成时间戳形式
def string_to_timestamp(st):
    data = time.mktime(time.strptime(st, "%Y-%m-%d %H:%M:%S"))
    return data


# 把时间戳转成字符串形式
def timestamp_to_string(sp):
    data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(sp))
    return data


# 把时间戳格式转换成datetime格式
def timestamp_to_datetime(tp):
    publish_date = datetime.datetime.fromtimestamp(tp)
    return publish_date


# 把datetime类型转外时间戳形式
def datetime_to_timestamp(dt):
    data = time.mktime(dt.timetuple())
    return data


# 当前时间
now = datetime.datetime.now()


# 求当前时间的一天之前的时间点
def get_one_day_before():
    one_day_before = now - datetime.timedelta(days=1)
    return one_day_before
