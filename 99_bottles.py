# Codédex :: 99 Bottles

'''                        range(start, stop, step):        
'''
''' by default: range increment by 1, to change it we specify a third argument.
    the third argument can be positive(increment) or negative(decrement)(reverse). 
    however, it can't be zero. 
'''

# using for loop 
# decrement by 1, 0 is exclusive. 
for i in range(99,0,-1): 
  print(f'{i} bottles of beer on the wall')
  print(f'{i} bottles of beer')
  print(f'Take one down, pass it around')

# using while loop 
b = 99 
while b !=0:
    print(f'{b} bottles of beer on the wall')
    print(f'{b} bottles of beer')
    print(f'Take one down, pass it around')
    b -=1 