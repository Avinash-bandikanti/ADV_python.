old_price=[1,2,3,4,5,6,7,8,9]
inc_price=10
def add_price(no):
    return no+10
new_price=map(add_price,old_price)
print(list(new_price))
new_price1=list(map(lambda n:n+inc_price,old_price))
print(new_price1)