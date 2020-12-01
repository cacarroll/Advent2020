def add(x, y, z=0):
    return x + y + z

def multiply(x, y, z=0):
    if z == 0:
        result = x * y
    else:
        result =  x * y * z
    return result
