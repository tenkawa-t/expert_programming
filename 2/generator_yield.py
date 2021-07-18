def fibonacci():
    a, b = 0, 1
    while True:
        yield b
        a, b = b, a + b

fib = fibonacci()
a = [next(fib) for i in range(20)]
print(a)
