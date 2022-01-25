# Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().


spisok = input("Введите желаемое количество элементов списка: ").split(",")

kolich_el = len(spisok) - 1

for index in range(0, kolich_el, 2):
    sosednyi_index = index + 1
    spisok[index], spisok[sosednyi_index] = spisok[sosednyi_index], spisok[index]
    print(spisok)