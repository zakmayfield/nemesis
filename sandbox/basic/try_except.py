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
    # we pull this into a try because float might throw if temp != convertable int.
    fahr = float(temp)
    cell = (fahr - 32.0) * 5.0 / 9.0
    
    # f-string : this syntax allows me to embed expressios that are evaluated at runtime via f'{ }'.
        #  similar to js template literal `${}`
    print(f'Temperature in C: {cell:.2f}')
except:
    print('Probably an error in your temp input')