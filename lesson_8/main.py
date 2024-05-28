# from random import randint
#
# a = list(range(1, 101))
# guess = randint(1, 100)
# print(guess)
#
# def bin_search(num: int, nums: list):
#     for i in range(1, 8):
#         print(f'try {i}')
#         end = len(nums) // 2
#         if num[end] == num:
#             return num
#         if num > nums[end]:
#             nums = nums[end:]
#         elif num < nums[end]:
#             nums = nums[:end]
#         else:
#             return num
#     print(bin_search( 87, nums))



# def sum_list(a:list, b:list):
#     if len(a) >len(b):
#         a, b = b, a
#     for n in range(len(a)):
#         b[n] += a[n]
#     return b
#
# print(sum_list(a = [1, 3, 1, 4, 5], b = [3, 2, 1]))


# [2, 46, 68, 45, 12, 34, 56]
# [11, 35, 67, 89, 33, 55, 22, 13]

def find_outlier(integers):
    odds = list(filter(lambda x: x% 2 == 1,  integers))
    if len(odds) == 1:
        return odds
    return list(set(integers).difference(odds))[0]