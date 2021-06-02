s = "h,e,l,o,p,y,t,h,o,n,7.6"

# print(s.find("y"))
# print(s.index("y"))
s = s.replace(",", "")
print(s)
y = float(s[10:])
s = s.capitalize()
s = s[0:4] + " " + s[4:10], y / 2

import functools as f


def stm(x, y):
    return y + " " + x


numrer = [3, 5, 76]
r = f.reduce(stm, ["chaim", 'david', 'moshe'])
print(r)
m = 'yoel'
# s= .join(reversed(m))
print(m[::-1])
