#
# print('#x:',['#'+str(x) for x in range(10)],'\n','x/2:',[x/2 for x in range(10)],'\n','x**2:',[x**2 for x in range(10)])
# # matrex
#


for row in range(9):
    for index in range(17):
        if index == row:
            index = "0"
        elif index == 16 - row:
            index = "0"
        else:
            index = "-"

        print(index, end='\t')
    print()



print("main question")
f = {"#x": lambda x: f"#{x}","x/2": lambda x: x/2,"x**2": lambda x: x**2}
[print(k + ": " + str([v(i) for i in range(10)])) for k,v in f.items()]

# shorter alternative using map
#[print(k + ": " + str(list(map(v,range(10))))) for k,v in f.items()]

print("\n\nbonus question no lambda")
f = {"x"+g: "x" + g for g in ["*5","/2","**2","%3","+3","-1"]}
[print(k + ": " + str([eval(v) for x in range(10)])) for k,v in f.items()]

#reduce
from functools import reduce
s = input("reverse\ntype string to reverse: ")
print(s + " <-> " + reduce(lambda x,y: y+x, s))


class ColourError(Exception):
    pass


class NonColour(ColourError):
    def __init__(self, colour):
        self.message = str(colour) + " is not a colour"


class NonBaseColour(ColourError):
    def __init__(self):
        self.message = "Only base colours allowed"


def print_base_colour(c):
    colours = ["red", "green", "blue", "yellow", "brown", "purple"]
    if c in colours[:3]:
        print(c + " is printed")
    elif c in colours:
        raise NonBaseColour()
    else:
        raise NonColour(c)


def colour_interface():
    while True:
        try:
            print_base_colour(input("choose base colour"))
            break
        except NonColour as n:
            print(n.message)
            raise
        except NonBaseColour as nb:
            print(nb.message)
            print("try again")
        finally:
            print("printing colour request handled...")


colour_interface()
