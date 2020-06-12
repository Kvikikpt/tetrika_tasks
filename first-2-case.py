
def search_pairs(array, k):
    min_array = []

    for num in array:
        if num < k and num not in min_array:
            min_array.append(num)

    sorted_array = []
    i = 0

    # Так бы я писал на си

    while i < len(min_array):
        b = i + 1
        while b < len(min_array):
            if min_array[i] + min_array[b] == k:
                sorted_array.append((min_array[i], min_array[b]))
            b += 1
        i += 1

    return sorted_array

# Я бы писал так на си, еще можно с циклом for, будет меньше числовых операций,
# сложность n + ((1 -- 0.almostinfinity, в зависимости от размера массива) * 2n)


print(search_pairs([1, 2, 6, 5, 3, 4, 7, 8, 3, 2], 5))
