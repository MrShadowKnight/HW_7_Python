import json

# TASK №1

# def quote(author):
#     quote = '''"Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# {}'''.format(author)

#     print(quote)

# quote("Bill Gates")

# TASK №2

# def evennumber(start, end):
#     even_numbers = []
#     if end < start:
#         for i in range(end, start + 1):
#             if i % 2 == 0:
#                 even_numbers.append(i)
#     else:
#         for i in range(start, end + 1):
#             if i % 2 == 0:
#                 even_numbers.append(i)
#     print(even_numbers)

# start =int(input("Введіть перше число для масиву: "))
# end = int(input("Введіть друге число для масиву: "))
# evennumber(start, end)

# TASK №3

# def draw_square(side_length, symbol, filled):
#     if filled:
#         for _ in range(side_length):                
#             print(symbol * side_length)
#     else:
#         for i in range(side_length):                
#             if i == 0 or i == side_length - 1:
#                 print(symbol * side_length)
#             else:
#                 print(symbol + " " * (side_length - 2) + symbol)

# print("Заповнений квадрат:")                        
# draw_square(5, "#", True)
# print("\nПорожній квадрат:")
# draw_square(5, "*", False)

# TASK №4

# def find_minimum(args):
#     return min(args)

# min_value = []
# numbers = int(input("Введіть кількість цифр для списку: "))
# while numbers > 0:
#     number_fro_list = int(input("Введіть число яке хочете добавити до списку: "))
#     numbers -= 1
#     min_value.append(number_fro_list)
# print("Мінімальне число:", find_minimum(min_value))

# TASK №5

# def product_in_range(a, b):
#     if a > b:
#         a, b = b, a 
#     product = 1  
#     for num in range(a, b + 1):
#         product *= num
#     return product
# a = int(input("Введіть перше число: "))
# b = int(input("Введіть друге число: "))
# result1 = product_in_range(a, b)
# print("Добуток чисел в діапазоні:", result1)

# TASK №6

# def count_digits(number):
#     num_str = str(number)
#     return len(num_str)

# num = int(input("Введіть число(для підрахування кількості цифр в ньому): "))
# result = count_digits(num)
# print("Кількість цифр у числі", num, "дорівнює", result)


# TASK №7

# def is_palindrome(number):
#     number_str = str(number)
#     return number_str == number_str[::-1]

# numb = int(input("Введіть число(для провірки на поліндром): "))
# print(is_palindrome(numb))  

# Поліндром (слово)

# def isPolidrom(word):
#     revers_word = word[::-1]
#     if revers_word == word:
#         return True
#     else:
#         return False

# word = input("Введіть слово для провірки на поліндром: ")
# print(isPolidrom(word))

# Завдання зі списком

# def square_list(numbers):
#     squared_numbers = []

#     for num in numbers:
#         squared_numbers.append(num * num)
    
#     return squared_numbers
# numbers = int(input("Введіть кількість чисел для списку: "))
# main_list = []
# while numbers > 0:
#     number_fro_list = int(input("Введіть число для списку: "))
#     main_list.append(number_fro_list)
#     numbers -= 1
# print(square_list(main_list))

# Факторіал числа

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
# n = int(input("Введіть факторіал який хочете знайти: "))
# print(factorial(n))

# Конвертація римських чисел

# def roman_to_arabic(roman_numeral):
#     roman_dict = {
#         'I': 1,
#         'V': 5,
#         'X': 10,
#         'L': 50,
#         'C': 100,
#         'D': 500,
#         'M': 1000
#     }

#     arabic_num = 0
#     prev_value = 0

#     for symbol in reversed(roman_numeral):
#         value = roman_dict[symbol]

#         if value < prev_value:
#             arabic_num -= value
#         else:
#             arabic_num += value

#         prev_value = value

#     return arabic_num
# roman_number = input("Введіть римське число(від меншого до більшого: I, V, X, L, C, D, M): ")
# print(roman_to_arabic(roman_number))

# Підрахунок слів

# def count_words(sentence):
#     words = sentence.split()
#     return len(words)

# text = input("Введіть текст для перевірки кількості слів: ")
# print(count_words(text))

# Шифр цезаря


# def cesarCode(txt, key):
#     with open("products.json", 'r') as file:
#         alphabetData = json.load(file)
#     codeInNumber = []
#     for letter in txt:
#         for l in alphabetData:
#             if alphabetData[f"{l}"] == letter.lower():
#                 codeInNumber.append(int(l) + int(key))

#     codeWord = ''
#     for num in codeInNumber:
#         if num <= 26:
#             codeWord += alphabetData[f"{num}"]
#         else:
#             codeWord += alphabetData[f"{num - 26}"]
#     return codeWord.capitalize()
# code = input("Введіть слово для шифрування(англійською): ")
# cesarCode(code)

# Пошук простих чисел

# def evennumber(start, end):
#     even_numbers = []
#     if end < start:
#         for i in range(end, start + 1):
#             if i % 2 == 0:
#                 even_numbers.append(i)
#     else:
#         for i in range(start, end + 1):
#             if i % 2 == 0:
#                 even_numbers.append(i)
#     print(even_numbers)

# start =int(input("Введіть перше число для масиву: "))
# end = int(input("Введіть друге число для масиву: "))
# evennumber(start, end)

# Калькулятор польського запису

# def polish_record_calculator(action, number_one, number_two):
#     if action == "-":
#         answer = number_one - number_two
#         print(f"{action} {number_one} {number_two}")
#         return answer
#     elif action == "+":
#         answer = number_one + number_two
#         print(f"{action} {number_one} {number_two}")
#         return answer
#     elif action == "*":
#         answer = number_one * number_two
#         print(f"{action} {number_one} {number_two}")
#         return answer
#     elif action == "/":
#         answer = number_one / number_two
#         print(f"{action} {number_one} {number_two}")
#         return answer
#     else:
#         answer = "Інших дій не існує"

# action = input("Введіть дію (+, -, *, /): ")
# number_one = float(input("Введіть перше число: "))
# number_two = float(input("Введіть друге число: "))

# print(polish_record_calculator(action, number_one, number_two))

# Cортування злиттям

# def merge_sort(arr):
#     def merge(left, right):
#         merged = []
#         left_index, right_index = 0, 0

#         while left_index < len(left) and right_index < len(right):
#             if left[left_index] < right[right_index]:
#                 merged.append(left[left_index])
#                 left_index += 1
#             else:
#                 merged.append(right[right_index])
#                 right_index += 1

#         merged += left[left_index:]
#         merged += right[right_index:]

#         return merged

#     if len(arr) <= 1:
#         return arr

#     mid = len(arr) // 2
#     left_half = merge_sort(arr[:mid])
#     right_half = merge_sort(arr[mid:])

#     return merge(left_half, right_half)

# input_list = []
# numbers = int(input("Введіть кітькість чисел для списку: "))
# while numbers > 0:
#     number_fro_list = int(input("Введіть чтисло для списку: "))
#     input_list.append(number_fro_list)
#     numbers -= 1
# sorted_list = merge_sort(input_list)
# print(sorted_list)

# Перетин списків

# def find_common_elements(list_one, list_two):
#     set1 = set(list_one)
#     set2 = set(list_two)
#     common_elements = set1.intersection(set2)
#     return list(common_elements)

# list_one = []
# list_two = []
# numbers_one = int(input("Введіть кітькість чисел для першого списку: "))
# numbers_two = int(input("Введіть кітькість чисел для другого списку: "))
# while numbers_one > 0:
#     number_fro_list_one = float(input("Введіть чтисло для першого списку: "))
#     list_one.append(number_fro_list_one)
#     numbers_one -= 1
# while numbers_two > 0:
#     number_fro_list_two = float(input("Введіть чтисло для другого списку: "))
#     list_two.append(number_fro_list_two)
#     numbers_two -= 1
# result = find_common_elements(list_one, list_two)
# print(result)