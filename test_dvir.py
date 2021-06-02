# itmes = [2,4,5,9,8,5,7]
#
# y =list(filter(lambda x : x <6,itmes))
# print(y)
#
# number = ['a','s','d','f','g','k','h']
# zipped = zip(number,itmes)
# print(dict(zipped))
matrex = [[x for x in range(5)] for j in range(5)]
cuomt = 0

names = " moshe", 'david', 'chaim', 'shira', 'arial', 'chaim', 'shira', 'arial'
name = set(names)
print(name)

list = []
for name in names:
    if name not in list:
        list.append(name)
print(list)

#
#
#
# def dask (colour):
#     return lambda obj : print("this",obj,"is colour",colour)
# itmes=dask("green")
# itmes("table")
#
#
# def double (arg):
#     return arg*2
# lam = lambda x : x +2
#
# print(lam(9))
#
# for i in itmes:
#     print(double(i))

y = map(lam,itmes)
print(list(y))
#list comprehsion
### matrix
y = [[i * j for i in range(5)] for j in range(6)]

### list dictionary
dollar = {"backpack": 100,
          "caes": 200,
          "bag": 20}
shekel = {product: price * 3.4 for (product, price) in dollar.items()}
print(dollar)
print(shekel)
#
s = "h,e,l,o,p,y,t,h,o,n,7.6"
# print(s.find("y"))
# print(s.index("y"))
s = s.replace(",", "")
print(s)
y = float(s[10:])
s = s.capitalize()
s = s[0:4] + " " + s[4:10], y / 2
#
print(s)
'''for _ in range(10):
    txt = input("enter string : ")
    print(txt.index(" "))
    i = txt.find(" ")

    print(txt[i + 1:], '?')'''


#
#
# txt ="dear you ard whdre "
# print(txt)
# i = txt.find(" ")
# txt1 =txt[:i]
# str = txt[i + 1:]
#
# for t in txt1:
#     w = ""
#     for j in str:
#         if t == j:
#             j= j.replace(j, "e")
#         w=w+j
# print(txt1,w)
#
#
#
#
#
#
# '''
# def som(*num):
#     for i in num:
#         print(type(i))
#
#
# num = [5,7,9],[9,5,44]
# som(*num)

def my_decorator(function):
    def wrapper(x):
        print("we have a wrapper")
        function(x)
        print("and still in wrapper")

    return wrapper


@my_decorator
def inner(x):
    print(x * x)


def plos(x):
    print(x + x)


my_decorat = my_decorator(plos)
my_decorat(6)
#
#
# inner(9)'''
