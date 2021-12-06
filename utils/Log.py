import datetime
from functools import wraps


class Log:
    def __init__(self, path=None):
        self._output = path

    def __call__(self, f):  # 相当于原来的 inner_decorator
        @wraps(f)
        def wrap_func(*args, **kwargs):  # 增加了输入参数
            now = datetime.datetime.now()
            msg = now.strftime("%Y-%m-%d %H:%M:%S")  # 运行时刻
            msg += f" {f.__name__}()\n"  # 运行的函数名

            ret = f(*args, **kwargs)  # 透传了输入参数，并记录了输出

            aft = datetime.datetime.now()
            time_cost = aft - now
            ms = time_cost.total_seconds() * 10 ** 3  # 毫秒
            msg += now.strftime("%Y-%m-%d %H:%M:%S")
            msg += f" {f.__name__}() return, cost {ms} ms"
            if self._output is None:
                print(msg)
            else:
                print(f"print logs into {self._output}")
                with open(self._output, 'a+') as fp:
                    fp.write(msg + '\n')

        return wrap_func