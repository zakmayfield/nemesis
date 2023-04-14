# n = 5

# while n > 0:
#     print(n)
#     n = n - 1

# print('Blast Off!')


# x = 40

# if x > 50:
#     print('greater than 50')
#     if x <= 100:
#         print('less than 100')


# x = 11

# if x < 3:
#     print('small')
# elif x < 7:
#     print('medium')
# elif x <= 10:
#     print('large')
# else:
#     print('gargantuan')

# print('finished')



# my_var = 'Hello there, General Kenobi.'

# try:
#     to_int = int(my_var)
# except:
#     print('Invalid, try again.')




# nbr = 42

# try:
#     meaning_of_life = int(nbr)

#     if meaning_of_life == 42:
#         print('This is correct')
# except:
#     print('Invalid, try again.')



temp = 27

try:
    fahr = float(temp)
    cell = (fahr - 32.0) * 5.0 / 9.0
    
    # f-string : this syntax allows me to embed expressios that are evaluated at runtime via f'{ }'.
        #  similar to js template literal `${}`
    print(f'Temperature in C: {cell:.2f}')
except:
    print('Probably an error in your temp input')


