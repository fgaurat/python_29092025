
print("Hello")


# helloWorld => camelCase => méthode, propriété
# hello_world => snake_case, var
# HELLO_WORLD => snake_case, const
# hello-world=> kebab-case

the_world_is_flat = True
if the_world_is_flat:
    print("Be careful not to fall off!")
    print("une autre ligne")
    print("encore une autre ligne")


spam = 2  # à la suite
# encore la suite
print()

t = "Une chaîne"
t2 = 'Une chaîne'
t3 = '# Une chaîne'
t4 = "# Une chaîne"

d1 = 17/3
d2 = 17//3

print(d1)
print(type(d1))
print(int(d1))
print(d2)
print(type(d2))


a = "12"
print(int(a))


p = "c:\\newproject\\test01"
p = r"c:\newproject\test01"

print(p)

m = """Une chaîne sur
plusieurs
lignes
"""

print(m)

h = """
<html>

</html>
"""


a = 1
b = 2
# a=1, b=2
s = "a="+str(a)+", b="+str(b)
print(s)


print(50*'-')

s = "toto"*12

print(s)


fname ="fred"
name = "GAURAT"
s = "Hello "+fname+" "+name
print(s)

a = 1
b = 2

print("a=",a,"b=",b)


s = "hello"

print(s[2])
print(s[len(s)-1])
print(s[-1])

print(len(s))

print(s[1:3]) # [1:3[
print(s[1:4]) # [1:4[
print(s[:4]) # [start:4[
print(s[2:]) # [2:end]

s = "hello"

s1 = s
print(hex(id(s)))
print(hex(id(s1)))

squares = [1, 4, 9, 16, 25]


print(squares)
print(squares[2])
print(type(squares))
squares.append(36)
print(squares)

l1 = ["valeur 1","valeur 2","valeur 3"]
l2 = l1 
print(l1)
print(l2)
l2.append("valeur 4")

print(l1)
print(l2)
print(50*'-')
l1 = ["valeur 1","valeur 2","valeur 3"]
l2 = l1[:] # Copy
l2.append("valeur 4")
print(l1)
print(l2)

print(50*'-')

l1 = [
    [10,20,30], # 0
    [40,50,60], # 1 
    [70,80,90] # 2
]
print(l1[1][2]) # 60

import copy 
# l2 = l1[:] # Copy
# l2 = l1.copy() # l2 = l1[:]
# l2 = copy.copy(l1)
l2 = copy.deepcopy(l1)
l1[1][2] = 2000

print(l1)
print(l2)

print(50*'-')
# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b