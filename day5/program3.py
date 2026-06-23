try:
    a=int(input("Enter first value:"))
    b=int(input("Enter second value:"))
    print("i am just stared")
    if(b%2==0):
        raise Exception
    else:
        print(a/b)
except ZeroDivisionError as zd:
    print(zd)
except Exception as e:
    print("hi i am else now alive because try is executed")
finally:
    print("hello there i am finally, i am going to close")
    
