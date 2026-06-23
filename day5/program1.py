try:
    print(10/0)
except ZeroDivisionError:
    print("Dividind with Zero (0) is not allowed")

try:
    print(10/0)
except ZeroDivisionError as zd:
    print(zd)
