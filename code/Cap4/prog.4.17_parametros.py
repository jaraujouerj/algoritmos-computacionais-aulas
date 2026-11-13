def foo(n):
    print('n - id:', id(n), 'valor:', n, 'em foo ')
    n = 0
    print('n - id:', id(n), 'valor:', n, 'em foo ')

n = 42
print('foo - id:', id(foo))
print('n - id:', id(n), 'valor:', n)
foo(n)
print('n - id:', id(n), 'valor:', n)
