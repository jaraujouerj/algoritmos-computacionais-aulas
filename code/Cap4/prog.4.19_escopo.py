global_y = 1

def foo(par):  #par existe somente dentro de foo()
    local_y = 20
    print('local_y =', local_y)
    print('global_y =', global_y)
    for i in range(1, 2):
        print('i =', i)
    print('i =', i)

foo(global_y)
