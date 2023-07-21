# TASK №1

# def quote(author):
#     quote = '''"Don't compare yourself with anyone in this world…
# if you do so, you are insulting yourself."
# {}'''.format(author)

#     print(quote)

# quote("Bill Gates")

# TASK №2

def evennumber(start, end):
    even_numbers = []
    for i in range(start, end + 1):
        if i % 2 == 0:
            even_numbers.append(i)
    print(even_numbers)

evennumber(1, 10)