def power(values):
    for value in values:
        print(f'{value}を供給')
        yield value

def adder(values):
    for value in values:
        print(f'{value}に値を追加')
        if value % 2 == 0:
            yield value + 3
        else:
            yield value + 2

elements = [1, 4, 7, 9, 12, 19]
results = adder(power(elements))
for i in range(3):
    print(next(results))
