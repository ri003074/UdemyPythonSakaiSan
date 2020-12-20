d = {'x': 10, 'y': 20}
print(type(d))
print(d['x'])

d['x'] = 100
print(d['x'])

d = {'x': 10, 'y': 20}
print(d.keys())
print(d.values())

d2 = {'x': 1000, 'j': 500}

d.update(d2)
print(d)
d.pop('x')
print(d)
del d['y']
print(d)

print( 'j' in d )

x = {'a':1}
y = x
y['a'] = 2
print(x)
print(y)

x = {'a':1}
y = x.copy()
y['a'] = 2
print(x)
print(y)


fruits = {
    'apple' :1000,
    'banana' :2000,
    'orange' :3000,
}
print(fruits['apple'])

