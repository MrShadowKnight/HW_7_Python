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
#     for i in range(start, end + 1):
#         if i % 2 == 0:
#             even_numbers.append(i)
#     print(even_numbers)

# evennumber(1, 10)

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

# def find_minimum(*args):
#     return min(args)

# min_value = find_minimum(590, 14, 46, 56 ,2)
# print("Мінімальне число:", min_value)

# TASK №5

# def product_in_range(a, b):
#     if a > b:
#         a, b = b, a 
#     product = 1  
#     for num in range(a, b + 1):
#         product *= num
#     return product

# result1 = product_in_range(5, 25)
# print("Добуток чисел в діапазоні:", result1)

# result2 = product_in_range(10, 2)
# print("Добуток чисел в діапазоні:", result2)

# TASK №6

# def count_digits(number):
#     num_str = str(number)
#     return len(num_str)

# num = 3456
# result = count_digits(num)
# print("Кількість цифр у числі", num, "дорівнює", result)


# TASK №7

# def is_palindrome(number):
#     number_str = str(number)
#     return number_str == number_str[::-1]

# print(is_palindrome(123321))  
# print(is_palindrome(546645))  
# print(is_palindrome(421987))  

# Поліндром (слово)

# def isPolidrom(word):
#     revers_word = word[::-1]
#     if revers_word == word:
#         return True
#     else:
#         return False
    
# isPolidrom("rer")

# Завдання зі списком

# def square_list(numbers):
#     squared_numbers = []

#     for num in numbers:
#         squared_numbers.append(num * num)
    
#     return squared_numbers

# main_list = [1, 4, 7, 65, 34, 56, 78, 9]
# print(square_list(main_list))

# Факторіал числа

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)

# print(factorial(4))

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

# print(roman_to_arabic("MCIL"))

# Підрахунок слів

# def count_words(sentence):
#     words = sentence.split()
#     return len(words)

# text = "Просто текст для перевірки роботи"
# print(count_words(text))

# Шифр цезаря

import json

def casarCode(txt, key=3):
    with open("alphabet.json", "r") as file:
        alphabet_data = json.load(file)
    code_in_number = []
    for letter in txt:
        for l in alphabet_data:
            if alphabet_data[f"{l}"] == letter.lower():
                code_in_number.append(int(l) + int(key))
         
    code_word = ''
    for num in code_in_number:
        if num <= 26:    
            code_word += alphabet_data[f"{num}"]
        else:
            code_word += alphabet_data[f"{num - 26}"]
    return code_word.capitalize

print(casarCode("aple"))