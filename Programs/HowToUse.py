def mul(a, b):
    return a * b

mul(3, 4)
#12

def mul5(a):
    return mul(5,a)

mul5(2)
#10

def mul(a):
    def helper(b):
        return a * b
    return helper

mul(5)(2)
#10

def fun1(a):
    x = a * 3
    def fun2(b):
        nonlocal x
        return b + x
    return fun2

test_fun = fun1(4)

test_fun(7)
#19
