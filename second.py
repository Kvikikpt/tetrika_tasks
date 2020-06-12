
with open('./names.txt') as file:
    array = str(file.read()).replace('"', '').split(',')

    array.sort()

    alphabet_sum = []

    for word in array:
        summ = 0
        for w in word:
            summ += ord(w) - 64
        alphabet_sum.append(summ)

    a = 1
    summ = 0
    while a <= len(alphabet_sum):
        alphabet_sum[a - 1] = alphabet_sum[a - 1] * a
        summ += alphabet_sum[a - 1]
        a += 1


    # 871853874
    print(f'The answer is: {str(summ)}')
