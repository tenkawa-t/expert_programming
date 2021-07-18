from contextlib import contextmanager
@contextmanager
def context_illustration():
    print('コンテキストに入ります')
    try:
        yield
    except Exception as e:
        print('コンテキストから出ます')
        print(f'エラーが発生しました{e}')
        raise
    else:
        print('コンテキストから出ます')
        print('エラーはありません')
