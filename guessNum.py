# Codédex :: Guess Number

guess = 0
tries = 0 # max 4 tries

while guess != 6 and tries!=4:
  guess = int(input("Guess the number:  "))
  tries +=1 

if tries == 4:
  print('You have finished all your tries!')
else:
  print("You got it!")