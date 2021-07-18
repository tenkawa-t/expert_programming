class User(object):
    def __init__(self, roles):
        self.roles = roles


class Unauthorized(Exception):
    pass


def protect(role):
    def _protect(function):
        def __protect(*args, **kw):
            user = globals().get('user')
            if user is None or role not in user.roles:
                raise Unauthorized('あなたには内緒です')
            return function(*args, **kw)
        return __protect
    return _protect


tarek = User(('admin', 'user'))
bil = User(('user',))
class MySecrets(object):
    @protect('admin')
    def waffle_recipe(self):
        print('バターを数トン用意してください')


these_are = MySecrets()
user = tarek
these_are.waffle_recipe()

user = bil
these_are.waffle_recipe()
