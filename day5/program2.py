try:
    print("i am try just started")
    print(10/2)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("i am else now alive because try is executed..")

try:
    print("i am try just started")
    print(10/0)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("i am else now alive because try is executed..")


try:
    print("i am try just started")
    print(10/0)
    print("i am try ,and done")
except ZeroDivisionError as zd:
    print(zd)
else:
    print("hi i am else now alive because try is executed..")
finally:
    print("hello there i am finally,i am going to close")



