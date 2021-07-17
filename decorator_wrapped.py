def mydecorator(function):
    def wrapped(*args, **kwargs):
        # 前処理
        result = function(*args, **kwargs)
        # 後処理
        return result
    return wrapped
