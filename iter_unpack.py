a = [1, 2, 3]
b = [4, 5, 6]
print([*a, *b])

# tuple
c = *a, 4, 5
print(c)

# only unpack error
d = *a
print(d)