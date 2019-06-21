def hello(fun):
    fun()

def bye():
    print("Bye....")


hello(bye) # Passing Function in a Function