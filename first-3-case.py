
def search_pairs(array, k):
    min_array = []

    for num in array:
        if num < k and num not in min_array:
            min_array.append(num)

    sorted_array = []

    # Мне кажется так алгоритм быстрее всего

    i = 1

    for num1 in min_array:
        for num2 in min_array[i:len(min_array)]:
            if num1 + num2 == k:
                sorted_array.append((num1, num2))
        i += 1

    return sorted_array


# То же самое что и во второй случае, но вместо математичкских операций,
# питоновские функции. Я не уверен что меньше ест памяти, числовые операция или что то другое.
# Этот алгоритм выглядет наиболее красиво, как мне кажется, хотя его можно улучшить.
# Сложность n + ((1 -- 0.almostinfinity, в зависимости от размера массива) * 2n)

print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
