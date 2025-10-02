import fibo as fb
from fibo import fib as the_fib,fib2
import sys

# import fibo
# fibo.fib(1000)
fb.fib(1000)

def fib(v):
    print(v)


def main():

    if len(sys.argv) > 1:
        print(sys.argv)
        user_value = int(sys.argv[1])
        print(user_value)
        the_fib(user_value)

        r = fib2(300)
        print(r)
    else:
        print("hooooooooo !")

if __name__=='__main__':
    main()
