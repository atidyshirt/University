#  def fibonacci(n):
    #  if n < 2:
        #  return n
    #  else:
        #  return fibonacci(n-1) + fibonacci(n-2)

#  def recur_fibo(n):
    #  if n <= 1:
         #  return n
    #  else:
        #  return(recur_fibo(n-1) + recur_fibo(n-2))
#  # take input from the user
#  #  nterms = int(input("How many terms? "))
#  #  # check if the number of terms is valid
#  #  if nterms <= 0:
    #  #  print("Plese enter a positive integer")
#  #  else:
    #  #  print("Fibonacci sequence:")
    #  for i in range(nterms):
        #  print(recur_fibo(i))
#  print(fibonacci(5))
#  print(fibonacci(6))
#  print(fibonacci(7))
#  print(fibonacci(100))


#  """ Fibonacci sequence using memoisation"""


#  seq = {0:0, 1:1}  # Cache of memoised answers

#  def fib(num):
    #  if num not in seq:
        #  seq[num] = fib(num-1) + fib(num-2)
    #  return seq[num]

#  print(fib(100))


#fib matrix
def mult(x,y):
    if ( len(y) == 2 ):
        a = x[0]*y[0]+x[1]*y[1]
        b = x[2]*y[0]+x[3]*y[1]
        return [a,b]
    a = x[0]*y[0] + x[1]*y[2]
    b = x[0]*y[1] + x[1]*y[3]
    c = x[2]*y[0] + x[3]*y[2]
    d = x[2]*y[1] + x[3]*y[3]
    return [a,b,c,d]

# Only works for positive powers!
def matrix_power( x, n ):
    if ( n == 1 ):
        return x
    if ( n%2 == 0 ):
        return matrix_power( mult(x, x), n//2 )
    return mult(x, matrix_power( mult(x, x), n//2 ) )

# fibonacci example:
A = [1,1,1,0]
v = [1,0]

x = 1000000
print mult(matrix_power(A,x-1),v)[0]

