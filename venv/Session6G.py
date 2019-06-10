# Keyword Arguments which is **kwargs: kwargs represents a dictionary
def marks(**kwargs):
    print(kwargs)
    print(type(kwargs))

marks(physics=90, maths=92, chemistry=70, name="John")


def fun(*a, **b):
    print(a)
    print(b)


fun(10, 20, 30, 40, 50, a=10, b=20, c=30)