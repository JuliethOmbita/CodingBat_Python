'''
Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'
'''

def string_bits(str):
  # I want to star ar 0 and go up by 2
  # Initialization: 0 
  # Condition: Length of the string  
  # Incrementation: by 2 
  return str[::2]