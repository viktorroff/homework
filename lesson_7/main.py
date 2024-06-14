# def get_list(array: list[int]) -> list[int]:
#     max_value, counter, max_pow_value = max(array), 1, 0
#     while max_pow_value < max_value:
#         max_pow_value = 2 ** counter
#         counter += 1
#     pows = [2 ** x for x in range(counter)]
#     return [x for x in array if x in pows]
#
#
# print(get_list([1, 3, 2, 12, 4, 12, 1024, 4325, 12, 567]))



# n = int(input('num: '))
# def is_special(n):
#     for c in str(n):
#         if c not in "012345":
#             return False
#     return True
# print(is_special(n))


# text = input('text: ').lower()
# def count_vowels(text):
#     vowels = "aeiyou"
#     word_count = 0
#     vowel_count = 0
#     for char in text:
#         if char in vowels:
#             vowel_count += 1
#         elif char.isspace() and vowel_count > 3:
#             word_count += 1
#             vowel_count = 0
#     if vowel_count > 3:
#         word_count += 1
#     return word_count
# print(count_vowels(text))


# import random
# import string
#
# def generate_password(length):
#     if length < 8 or length > 15:
#         raise ValueError("Длина пароля должна быть от 8 до 15 символов.")
#
#     password_characters = string.ascii_letters + string.digits
#     password = "".join(random.choice(password_characters) for _ in range(length))
#     return password
# for _ in range(3):
#   password = generate_password(int(input('num: ')))
#   print(password)