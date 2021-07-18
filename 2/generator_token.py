import tokenize
reader = open('hello.py').readline
tokens = tokenize.generate_tokens(reader)
a = next(tokens)
print(a)

b = next(tokens)
print(b)
