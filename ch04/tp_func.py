
def fib(n):    # write Fibonacci series less than n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()



def fib2(n=100):    # write Fibonacci series less than n
    """Return a Fibonacci series less than n."""
    
    a, b = 0, 1
    result =[]
    while a < n:
        result.append(a)
        a, b = b, a+b
    
    return result



# Now call the function we just defined:
fib(2000)
r = fib2(10) # [0,1,1,2,3,5,8]
print(r)
r = fib2()
print(r)
r = fib2(n=23)

print(50*'-')
# i=50
# for i in range(32):
#     print(i)

# print(i)
# def f(param=i):
#     print("param",param)

# i=1000
# f()




def hello(name,firstName,job,age):
    print("hello",name,firstName)


hello("gaurat",'fred','dev',49)
# hello(firstName='fred',name="gaurat")
hello("gaurat",'fred',age=49,job="dev")


print("valeur 1","valeur 2","valeur 3")



print(50*'-')

# emballage
# *values <- 10,20,30,40,50,60,70
# *values = 10,20,30,40,50,60,70

def add(*values):
    print(values)
    result = 0
    for i in values:
        result = result+i # result+=i  
    return result

l = [10,20,30,40,50]
r = add(*l,150,432)
print(l)
# print(r) # 150


# r = add(10,20,30,40,50,60,70)
# print(r) # 150

a,b,c,d,e = [*l]
print(a)


# print(*l)


# print(sum([10,20,30,40]))



# l = [10,20,30] # Liste
# t = (10,20,30) # Tuple
# l[0] = 1000
# print(l,type(l))
# print(t,type(t))
# t[0] = 1000



line = "10;20;30;40;50"
data = line.split(";")
print(*data,sep="-")


a,b,*c = [0,1,2,3,4]
print(a,b,c)


# {'name': 'gaurat', 'firstName': 'fred', 'age': 49, 'job': 'dev'}



def hello(**kwargs):
    print(kwargs)
    print("hello",kwargs['name'],kwargs['firstName'])


hello(name="gaurat",firstName='fred',age=49,job="dev")