

l = [10, 20, 30, 40, 50]
print(l)
l.append(60)
print(l)
last_value = l.pop()
print(l)
l.insert(0,-10) # insert(position,value)
print(l)
first_value = l.pop(0)
print("first_value",first_value)
print(l)

from collections import deque
d = deque(l)
print(d)
d.append(100)
d.appendleft(-20)
print(d)

print(50*'-')

# l =[0,1,2,3,4,5,6,...,99]
l=[]
for value in range(100):
    l.append(value)
print(l)

l = list(map(lambda value:value,range(100)))
print(l)

# list comprehension
# liste par intention
l=[value for value in range(100)]


# l=[]
# cpt = 0
# while cpt<100:
#     l.append(cpt)
#     cpt+=1



lines=[" ligne 01 "," ligne 02","    ligne 03" ]
clean_lines = [line.strip() for line in lines]

clean_lines =[]
for line in lines:
    clean_lines.append(line.strip())



# l=[(lambda value:value*2)(value) for value in range(100)]    
# print(l)

