def spam(divided_by):
    try:
        # Any code in this block that causes ZeroDivisionError won't crash the program:
        return 42 / divided_by
    except ZeroDivisionError:
        # If ZeroDivisionError happened, the code in this block runs:
        print("Error: Invalid Argument.")


print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

# Note that any errors that occur in function calls in a try block will also be caught. Consider the following program, which instead has the spam() calls in the try block:

def spam(divided_by):
    return 42 / divided_by

try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print("Error: Invalid Argument.")


