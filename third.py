import sys

def get_zeros(num: int):
    factorial = 1

    while num > 1:
        factorial *= num
        num -= 1

    factorial_list = list(str(factorial))

    print(factorial)
    print(factorial_list)

    iterator = -1
    while factorial_list[iterator] == str(0):
        iterator -= 1

    return (iterator * -1) - 1


# Не уверен о сложности, количество операций будет равно
# len(num) + len(количество нулей в конце номера) + операции конвертации
# из одного типа в другой + пара математических операций.


if len(sys.argv) == 2:
    print(get_zeros(int(sys.argv[1])))
else:
    print('Введите любое число, пример: ./python3 third.py 13')
