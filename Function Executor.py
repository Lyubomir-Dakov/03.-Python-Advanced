def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def func_executor(*args):
    result = []
    for (func_name, arguments) in args:
        num_1, num_2 = arguments
        if func_name == sum_numbers:
            result.append(sum_numbers(num_1, num_2))
        elif func_name == multiply_numbers:
            result.append(multiply_numbers(num_1, num_2))
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))




