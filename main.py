import random
index = 0
list = []
def GRK():
  #GRK stands for generate random key
  for i in range(4):
    # Generates 4 numbers
    list.append(randint(0,9))
  key = int("".join(map(str, list)))
  # turns list into an integer and sets key to list
  return key
# ABOVE IS FOR GENERATING THE KEY
# IT IS STRUCTURED AS SUCH FOR EASIER EDITS TO BE MADE
# BELOW IS TO CREATE THE SOLUTION, AND ALSO THE LOCK ON THE USER END

def convert(key):
  if len(key) != 4:
    if len(key) > 4:
      print(f"Key Error: Length of key is too large, input was {len(key)}")
    else:
      print(f"Key Error: Length of key is too small, input was {len(key)}")
  else:
    c_list = [list(map(int, str(key)))]
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

code = grk()
convert(code)
    
    
    
    
  
  
  
