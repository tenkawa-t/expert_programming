rpc_info = {}
def xmlrpc(in_=(), out=(type(None),)):
    def _xmlrpc(function):
        # 引数情報の登録
        func_name = function.__name__
        rpc_info[func_name] = (in_, out)
        def _check_types(elements, types):
            if len(elements) != len(types):
                raise TypeError('引数の個数が間違っています')
            typed = enumerate(zip(elements, types))
            for index, couple in typed:
                args, of_the_right_type = couple
                if isinstance(args, of_the_right_type):
                    continue
                raise TypeError(f'引数{index}は{of_the_right_type}である必要が有ります')

        def __xmlrpc(*args):
            checkable_args = args[1:]  # del self
            _check_types(checkable_args, in_)
            # do func
            res = function(*args)
            # check res
            if not type(res) in (tuple, list):
                checkable_res = (res, )
            else:
                checkable_res = res
            _check_types(checkable_res, out)
            return res
        return __xmlrpc
    return _xmlrpc


class RPCView:
    @xmlrpc((int, int))
    def meth1(self, int1, int2):
        print(f'{int1}と{int2}を受け取りました')
    @xmlrpc((str, ), (int, ))
    def meth2(self, phrase):
        print(f'{phrase}を受け取りました')
        return 12

# rpc_info
my = RPCView()
# my.meth1(1, 2)
# my.meth2('test')
my.meth2(1)
