def actual_divison(func):
    def wrapper(a,b):
        result = func(a,b)
        if a < b:
            return 1
        return result
    return wrapper


@actual_divison
def output(a,b):
    if a % b == 0:
        return int(a // b)
    else: 
        return int(a / b)

print(output(10,3))
print(output(5,2)) 