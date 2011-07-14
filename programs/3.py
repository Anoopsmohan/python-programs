
# Merge two sorted (ascending) lists. Return the merged list. The "merged"
# list is also sorted.

def merge(a, b):
  result = []
  for i in a:
    for j in b:
      if i<j:  
        result.append(i)
        break
      elif i>j:
        result.append(j)
  result.extend(a)
  result.extend(b)
  r=[]
  for k in result:
    if not k in r:
      r.append(k)
  print r
  return r

      

print '\n\n****************OUTPUT*******************'
assert(merge([1], [2]) == [1,2])

assert(merge([10, 20], [30]) == [10, 20, 30])

assert(merge([10, 30, 40], [32, 33, 45, 57]) == [10,30,32,33,40,45,57])

assert(merge([20, 25, 27, 34], [1, 10, 23]) == [1,10,20,23,25,27,34])

assert(merge([1], []) == [1])

assert(merge([], [1, 2]) == [1,2])

print '\nAll conditions are verified...\n'

