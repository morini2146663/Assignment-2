'''
FIBD exercise 

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.
'''

# n represents the number of rabbit pairs
# k represents the number of months after which the rabbits die

def rabbits(n, k):
  rabbits_list=[0] * k                                 # rabbits_list represents the number of rabbit pairs in each age group 
                                                       # initially, there are no rabbits in each age group, so all values are set to zero

  rabbits_list[0] = 1                                  # we specify that there is 1 pair of newborn rabbits at the beginning (age 0)

  fib = [rabbits_list[0]]                              # fib will be used to keep a running total of the population across months

  for i in range(n):
    rabbits_list.insert(0, sum(rabbits_list[1:]))      # we adds a new pair of rabbits to the start of rabbits_list
                                                       # the number of new pairs is calculated as the sum of all rabbits aged 1 to k−1 months
    rabbits_list.pop()                                 # we removes the last element of rabbits_list, (rabbits dying after k months)
    fib.append(sum(rabbits_list))                      # we add the total number of rabbits for the current month to the fib list

  return fib[n-1]                                      # returns the count at the end of the n-th month

print(rabbits(83,20))