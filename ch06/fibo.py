# Fibonacci numbers module




def f():
    value = "toto"
    print(value)

def fib(n):
    """Write Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):
    """Return Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result



if __name__ == "__main__":
    print("__name__",__name__)
    fib(2000)
    r = fib2(4000)
    print(r)



