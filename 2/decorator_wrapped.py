def mydecorator(function):
    def wrapped(*args, **kwargs):
        # 前処理
        result = function(*args, **kwargs)
        # 後処理
        return result
    return wrapped


def repeat(number=3):
    """
    デコレートされた関数をnumberで指定された回数繰り返す。
    :param number:
    :return:
    """
    def actual_decorator(function):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(number):
                result = function(*args, **kwargs)
            return result
        return wrapper
    return actual_decorator


@repeat(4)
def foo():
    print("foo")

foo()