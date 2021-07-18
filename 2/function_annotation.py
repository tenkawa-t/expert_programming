def f(ham: str, eggs: str = 'eggs') -> str:
    pass

print(f.__annotations__)

# 型情報の提供
# 型チェック
# IDEが関数が期待する引数の型や返り値の方を表示
# 関数オーバーロード/ジェネリック関数
# 外部の言語のコードとの接続
# アダプタ
# ...