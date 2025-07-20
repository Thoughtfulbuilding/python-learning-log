# Devide by zero error code:
# def spam(divide_by):
    #return 42 / divide_by
#print(spam(2))
#print(spam(12))
#print(spam(0))
#print(spam(1))

#try and except clause
def spam(divide_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divide_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print('Error: Invalid argument.')

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
