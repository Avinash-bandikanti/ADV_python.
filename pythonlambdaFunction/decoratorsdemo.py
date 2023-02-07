def outer():
    print("hello in outer function")
    def inner():
        print("hello in inner function")
    inner()
    return inner
d=outer()
d()