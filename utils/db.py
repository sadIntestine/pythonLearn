from functools import wraps
import sqlite3, os


class DbCommit():
    def __init__(self, db=''):
        self.db = db;

    def __call__(self, f):
        @wraps(f)
        def wrap_func(*args, **kwargs):  # 增加了输入参数
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            ret = cursor.execute(f(*args, **kwargs))
            conn.commit()
            cursor.close()
            return cursor.rowcount

        return wrap_func


class DbQuery():
    def __init__(self, db=''):
        self.db = db;

    def __call__(self, f):
        @wraps(f)
        def wrap_func(*args, **kwargs):  # 增加了输入参数
            conn = sqlite3.connect(self.db)
            cursor = conn.cursor()
            cursor.execute(f(*args, **kwargs))
            values = cursor.fetchall()
            print(values)
            conn.commit()
            cursor.close()
            return values

        return wrap_func
