def divide():
    return 5/0
try:
    divide()
except ZeroDivisionError as ze:
    print("division by zero!")
except:
    print("any other exception") 
            