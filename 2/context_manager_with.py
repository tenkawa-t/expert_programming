hosts = open('/etc/hosts')
try:
    for line in hosts:
        if line.startswith('#'):
            continue
        print(line.strip())
finally:
    hosts.close()


class ContextIllustration:
    def __enter__(self):
        print('enter context')
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit context')

        if exc_type is None:
            print('No error')
        else:
            print(f'error raise{exc_val}')

with ContextIllustration():
    print('in context')

with ContextIllustration():
    raise RuntimeError('"with"内で発生')
