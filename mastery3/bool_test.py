def func1(b):
    print(str(b))
    print(int(b))
    print(float(b))


def func2(i, j):
    if(j % i == 0):
        return True
    else:
        return False


def func3(i, j):
    if(type(i) == type(j)):
        return True
    else:
        return False


def boolean_test(x, y):
    if(x or y):
        print(x, "or", y, "is True")
    else:
        print(x, "or", y, "is False")
    
    if(not(x and y)):
        print("not (" + str(x) + " and " + str(y) + ") is True")
    else:
        print("not (" + str(x) + " and " + str(y) + ") is False") 

print("func1 ------")
func1(True)
func1(False)
print("func2 ------")
print(func2(3, 6))
print(func2(3, 4))
print("func3 ------")
print(func3(3, 3))
print(func3(3, "3"))
print("func4 ------")
boolean_test(True, False)
boolean_test(True, True)