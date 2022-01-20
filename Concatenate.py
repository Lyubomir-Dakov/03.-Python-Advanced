def concatenate(*args):
    result = ''
    for x in args:
        result += x
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))


