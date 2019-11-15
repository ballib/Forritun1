def is_float(s):
    try:
        if float(s):
            return True
        else:
            return False
    except ValueError:
        return False

# Do not change the lines below
print(is_float('3.45'))
print(is_float('3e4'))
print(is_float('abc'))
print(is_float('4'))
print(is_float('.5'))