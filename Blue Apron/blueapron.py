# Flatten an array
# Input: [[1],[2,3],[4]]
# Output: [1, 2, 3, 4]

def flatten(array):
  try:
    it_is = iter(array)
  except TypeError:
    yield array
  else:
    for x in it_is:
      for y in flatten(x):
        yield y

# arr = [[1],[2,3,[4]],[4], [1]]
# result = list(set(flatten(arr)))
# print result

# Resource:
# https://www.codecademy.com/en/forum_questions/52cc75f0631fe98640001510


# Simple generator implementation
def simple_generator_fxn():
  yield 1
  yield 2
  yield 3 # how is this different from "yield 1 print 2 print 3" ??

# for x in simple_generator_fxn():
#   print x

# g = simple_generator_fxn()

# while True:
#   try:
#     print next(g)
#   except StopIteration:
#     print 'End of iterable'
#     break


# Implement an iterator in Python

# This class to implements an iterator of powers of two
class PowTwo:
  def __init__(self, max=0):
    self.max = max

  def __iter__(self):
    self.n = 0
    return self

  def next(self):
    if self.n <= self.max:
      result = 2 ** self.n 
      self.n += 1
      return result

    else:
      raise StopIteration

# Create an iterator and iterate as follows
a = PowTwo(4) # 2 ** 4 = 16
i = iter(a)

# print next(i) # 1
# print next(i) # 2
# print next(i) # 4
# print next(i) # 8
# print next(i) # 16
# print next(i) # StopIteration

# Can also use for loop to iterate over iterator class
for i in PowTwo(5):
  print i # 1 2 4 8 16 32




def is_prime(n):
  if n > 1:
    if n == 2:
      return True
    elif n % 2 == 0:
      return False
    for i in range(3, int(math.sqrt(n) + 1) , 2):
      if num % i == 0:
        return False
      else:
        return True
  return False

# n = 16
# 1 2 4 8 16


# A prime is defined as any counting number that is divisible by
# exactly two distinct counting numbers: 1 and itself.
# Therefore: 1 is not prime, because it is divisible by only one
# distinct counting number: 1. 2 is prime because it is
# divisible by two distinct counting numbers: 1 and 2.

# Return iterable with elements which are prime numbers
# Input: List of ints
# Output: Iterable of elements that are prime numbers
def return_primes(input):
  primes = list()
  for e in input:
    if is_prime(e):
      primes.append(e)


def get_primes(input_list):
  for e in input_list:
    if is_prime(e):
      return e
  # return e for e in input_list if is_prime(e)


def is_prime(num):
  if num > 1:
    if num == 2:
      return True
    elif num % 2 == 0:
      return False
    for i in range(3, int(math.sqrt(num) + 1) , 2):
      if num % i == 0:
        return False
    else:
      return True
  return False



# Resources:

# https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
# http://www.programiz.com/python-programming/iterator
# https://docs.python.org/3/tutorial/classes.html

