l=[1,2,3,4,5,6,7,8,9]
def demo_fun(n):
    if n>5:
        return True
    else:
        return False
data=list(filter(demo_fun,l))
print(data)