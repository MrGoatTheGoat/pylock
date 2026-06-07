import random
index = 0
def GRK():
  listed = []
  #GRK stands for generate random key
  for i in range(4):
    # Generates 4 numbers
    listed.append(random.randint(0,9))
  key = int("".join(map(str, listed)))
  # turns list into an integer and sets key to list
  return key
# ABOVE IS FOR GENERATING THE KEY
# IT IS STRUCTURED AS SUCH FOR EASIER EDITS TO BE MADE
# BELOW IS TO CREATE THE SOLUTION, AND ALSO THE LOCK ON THE USER END

def convert(key):
  if len(str(key)) != 4:
    if len(str(key)) > 4:
      print(f"Key Error: Length of key is too large, input was {len(str(key))}")
    else:
      print(f"Key Error: Length of key is too small, input was {len(str(key))}")
  else:
    c_list = list(map(int, str(key)))
    for index in range(4):
      x = sum(c_list)
      y = c_list.pop(index)
      if y + x > 9:
        c_list.append(y)
      else:
        y = x + y
        c_list.append(y)
    result = int("".join(map(str, c_list)))
    return result

def getkey(x):
  #please note this is for decoding, do not include on user end
  if type(x) != "<class: 'int'":
    KeyResult = convert(x)
    print(f"The Lock Is {str(KeyResult)}")
  else:
    print(f"Decode Error: Expected Key Type 'integer', got {type(x)}")
    
    
    
