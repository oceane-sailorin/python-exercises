#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. 
# We are in trouble if they are both smiling or if neither of them is smiling. 
# Return True if we are in trouble.
def monkey_trouble(monkey1,monkey2):
    return monkey1 == monkey2
  


print(monkey_trouble(True, True))
print(monkey_trouble(False, False))
print(monkey_trouble(True, False))