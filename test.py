def func1(a):
    a += 1
    def funct2(b):
        val = 1+b
        return val
    return funct2(a)

print(func1(5))