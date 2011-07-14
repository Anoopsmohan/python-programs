# flatten a list

def flatten(a):
  b=[]
  for num in a:
    if isinstance(num,list):
      c= flatten(num) 
      b.extend(c)
    else:
      b.append(num)
#  print b
  return b


print'\n\n************ OUTPUT************'
assert(flatten([[1,[2,3]]]) == [1,2,3])

assert(flatten([[[1,2]]]) == [1, 2])

assert(flatten([[[]]]) == [])

assert(flatten([1, [2, [3, [4]]]]) == [1,2,3,4])

print'\nAll conditions are verified..\n'
