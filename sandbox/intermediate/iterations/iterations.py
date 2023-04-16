import array
import random

# while
x = 1
can_submit = False

while x < 5:
    if x == 3:
        can_submit = True
        print('Submitted!')  
        break
    print(x)
    x += 1

# for
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in numbers:
  if num == 7:
    print('Found!')
    print('Adding random number to the list')
    numbers.append(random.randint(10, 1000))
    print(numbers)
    break