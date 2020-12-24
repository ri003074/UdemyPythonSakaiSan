def say_something():
    print('hi')
    s = 'hi'
    return s

def return_hello():
    s = 'hellow'
    return s

say_something()

print(return_hello())


def menu(entree, drink, dessert):
    print('entree  = ', entree)
    print('drink   = ', drink)
    print('dessert = ', dessert)


menu('beef', 'beer', 'ice')
menu(entree='beef', drink='beer', dessert='ice')

def menu2(entree='salada', drink='orange', dessert='cookie'):
    print('entree  = ', entree)
    print('drink   = ', drink)
    print('dessert = ', dessert)

menu2()
menu2(dessert='banana')


#デフォルト引数で空のリストを扱うときは気を付ける

def test_func(x, l=[]):
    l.append(x)
    return l

y = [1,2,3]
r = test_func(100, y)
print(r)

y = [1,2,3]
r = test_func(200, y)
print(r)


r = test_func(100)
print(r)
r = test_func(100)
print(r)

def test_func2(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l


r = test_func2(100)
print(r)
r = test_func2(100)
print(r)






def say_something(word,*args):
    print(word)
    print(args)
    for arg in args:
        print(arg)


say_something('Hi','Mike','Nancy')



def menu2(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)
            
menu2(entree='beef', drink='coffee')





d = { 
    'entree':'beef', 
    'drink':'coffee',
    'dessert':'ice',
}

menu2(**d)







def menu3(food, *args, **kwargs):
    print(food)
    print(args)
    print(kwargs)


menu3('banana','apple', 'orange', entree='beef', drink='coffee')











