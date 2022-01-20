def operate(symbol, *args):
    list_of_numbers = [int(x) for x in args]

    if symbol == '+':
        return sum(list_of_numbers)

    elif symbol == '-':
        result = list_of_numbers[0]
        for i in range(1, len(list_of_numbers)):
            result -= list_of_numbers[i]
        return result

    elif symbol == '*':
        result = 1
        for i in range(len(list_of_numbers)):
            result *= list_of_numbers[i]
        return result

    elif symbol == '/':
        not_possible = False
        result = list_of_numbers[0]
        for i in range(1, len(list_of_numbers)):
            if list_of_numbers[i] == 0:
                not_possible = True
                break
            result /= list_of_numbers[i]
        if not_possible:
            return None
        else:
            return result


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
