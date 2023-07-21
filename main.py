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