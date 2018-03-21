try:
    x = int("zero")
    print(10 / x)
except ZeroDivisionError:
    print("div")
except NameError:
    print("name")
except ValueError:
    print("value")
except:
    print("other")

def fn(x, y):
    z = x + y

print(fn(1, 2))