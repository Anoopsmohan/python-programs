# partition a list using its first element
# return a list-of-partitioned-lists

def partition(a):
  b=a[0]
  lo=[]
  up=[]
  result=[]
  for num in a:
    if num<b :
      lo.append(num)
    elif num>b:
      up.append(num)
  result.append(lo)
  result.append(up)
  print result
  return result

print '\n\n****************OUTPUT*************'
assert(partition([10, 8, 2, 11, 14, 6,1, 13]) == [[8,2,6,1],[11,14,13]])

assert(partition([1,2,3,4]) == [[],[2,3,4]])

assert(partition([1]) == [[],[]])

assert(partition([4,3,2,1]) == [[3,2,1],[]])

print'\nAll conditions are verified..\n'
