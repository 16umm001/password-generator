import random
char = 'abcdefghijklmnopqrstwxyz1234567890!@#$%^&*()QWERTYUIOPASDFGHJKLZXCVBNM'
length = int(input('Length of password'))
number= int(input('Number of password'))
for p in range(number):
  password=' '
  for c in range(length): 
    password += random.choice(char)
  print(password)
