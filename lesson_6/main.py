# array = 'is2 th1is 3a t4est'.split()
# res = []
# for word in array:
#     for symbol in word:
#         if symbol.isdigit():
#             res.append({symbol: word})
# for k in range(len(res)):
#     for n in range(len(res) - k - 1):
#         if list(res [n].keys())[0] > list(res[n + 1].keys())[0]:
#             res [n], res[n +1] = res [n + 1], res[n]
# res = [list(x.values())[0] for x in res]
# print(' '.join(res))



#
# array = 'is2 th1is 3a t4est'.split()
# def get_num(word: str) -> int:
#     for symbol in word:
#         if symbol.isdigit():
#             return int(symbol)
# print(' '.join(sorted(array, key=get_num)))



# arr = ['vdfgdtb', 'dtbdtdgd', 'egger', 'rvrrg']
# def get_min_len(list_str: list) -> list:
#     min_len = len(min(list_str, key = len))
#     result = [x for x in list_str if len(x) == min_len]
#     return result
# print(get_min_len(arr))


# 1
#
# nums = [1, 2, 3, 4, 5, 6, 7, 8]
# def square_nums(nums):
#     squared_nums = []
#     for num in nums:
#         squared_nums.append(num * num)
#     return squared_nums
# print(square_nums(nums))


# 2
#
# stroki = ['343234'], ['64'], ['6563456'], ['35637'], ['35737'], ['863268'], ['2'], ['543']
# dlinnye = []
#

# 3
#
# numbers = [23, 45, 67, 56, 89, 43, 22, 13, 46]
# def get_even_numbers(numbers):
#   even_numbers = []
#   for number in numbers:
#     if number % 2 == 0:
#       even_numbers.append(number)
#   return even_numbers
# print(get_even_numbers(numbers))


# 4
#
# spisok = [23, 65, 78, 2, 4, 6, 12, 14, 45, 33]
# def summa_kvadratov_chetnykh(spisok):
#     summa_kvadratov = 0
#     for chislo in spisok:
#         if chislo % 2 == 0:
#             summa_kvadratov += chislo ** 2
#     return summa_kvadratov
# print(summa_kvadratov_chetnykh(spisok))


# 5
#
# strings = ['argd', 'yeyhd', 'svsvdfg', 'rttb', 'axcr', 'awer']
# def starts_with_a(strings):
#     a_strings = []
#     for string in strings:
#         if string.startswith('a'):
#             a_strings.append(string)
#     return a_strings
# print(starts_with_a(strings))


# 6
#
# lista = [12, 34, 56, 23, 11, 15, 17, 14]
# def filtruj_liczby(lista):
#     otfiltrowany_lista = []
#     for liczba in lista:
#         if 10 < liczba < 20:
#             otfiltrowany_lista.append(liczba)
#     return otfiltrowany_lista
# print(filtruj_liczby(lista))


# 7
#
# list_of_strings = ['rsggewe', 'ethhjgv', 'dnvireb,', 'rbddrbd']
# def contains_e(list_of_strings):
#     e_strings = []
#     for string in list_of_strings:
#         if "e" in string:
#             e_strings.append(string)
#     return e_strings
# print(contains_e(list_of_strings))


# 8
#
# nums = [352, 4564, 676, 3356, -3456]
# def all_num(nums):
#     if not nums:
#         return True
#     else:
#         if all(num > 0 for num in nums):
#             return True
#         else:
#             return False
# print(all_num(nums))


# 9
#
# strings = [3456, 4543, True]
# digit_strings = []
