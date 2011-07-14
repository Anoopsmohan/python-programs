
# Return True if n is a factorial number
# Examples of factorial numbers: 2, 6, 24, 120, ....
def is_factorial(n): 
  f=i=1
  while i<=n:
    f=f*i
    if f == n:
      return 1
    if f > n:
      return 0
    i=i+1


print '\n\n**************OUTPUT*****************\n'
assert(is_factorial(6))

assert(not is_factorial(100))
 
assert(is_factorial(1307674368000L))

assert(is_factorial(120))

print'\nAll conditions are verified..\n'
  
