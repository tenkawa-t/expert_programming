class WithDecorators:
    @staticmethod
    def some_static_method():
        print('これは静的なメソッドです')
    @classmethod
    def some_class_method(cls):
        print('これはクラスメソッドです')

a = WithDecorators
a.some_class_method()
a.some_static_method()