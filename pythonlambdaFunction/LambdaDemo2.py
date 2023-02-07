def demo(x):
    return lambda a:a*x
a=demo(3)
print(a(8))