
def search_pairs(array, k):
    min_array = []

    for num in array:
        if num < k and num not in min_array:
            min_array.append(num)

    sorted_array = []
    for num1 in min_array:
        for num2 in min_array:
            if num1 + num2 == k and (num2, num1) not in sorted_array:
                sorted_array.append((num1, num2))

    return sorted_array

# Это самый простой алгоритм в плане написания кода,
# сложность n + ((1 -- 0.almostinfinity, в зависимости от размера массива) * n ^ 2)


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
