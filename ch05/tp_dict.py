
user = {
    "name":"GAURAT",
    "firstName":"Fred",
    "job":"Dev",
    "age":22
}
# ["name","firstName","job",'age'] # Keys
# ["GAURAT","Fred","Dev",22] # Values

print(user)
print(user['name'])
user["age"] = 49
user['languages'] = ["Python","Javascript"]
print(user)


for k in user:
    print(k,user[k])

all_keys = user.keys()
all_values  = user.values()

print(all_values)

for v in user.values():
    print(v)

t = (0,1)
a,b = (0,1)


# ('name', 'GAURAT')
# ('firstName', 'Fred')
# ('job', 'Dev')
# ('age', 49)
# ('languages', ['Python', 'Javascript'])
for the_key,the_value in user.items():
    print(the_key,the_value)

for k in user:
    print(k,user[k])

l = ["Valeur 01", "Valeur 02", "Valeur 03", "Valeur 04" ]

for i,v in enumerate(l):
    print(i,v)