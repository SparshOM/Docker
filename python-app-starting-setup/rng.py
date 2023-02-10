from random import randint

min_number = int(input('Please enter the min number: '))
max_number = int(input('Please enter the max number: '))

if (max_number > min_number): 
  print(max_number)
else:
  print(min_number)
rnd_number = randint(min_number, max_number)
print(rnd_number)
