
# Insert an integer into a sorted list in such a way that
# after insertion, the list again remains sorted.

# Return the new list

def insert_into(a, n):
  if len(a)==0 or n>a[-1]: 
    a.append(n)
  else:
    for num in a:
      if num > n:
        ind=a.index(num)   
        a.insert(ind,n)
        break  
  print a
  return a      


print '\n\n***************OUTPUT*************'
assert(insert_into([10, 20, 30], 24) == [10,20,24,30])

assert(insert_into([5, 10, 20], 3) == [3,5,10,20])

assert(insert_into([1, 10, 20], 30) == [1,10,20,30])

assert(insert_into([], 10) == [10])

assert(insert_into([1, 4, 18, 24, 27, 35, 87], 19) == [1,4,18,19,24,27,35,87])

print '\nAll conditions are verified.\n'
