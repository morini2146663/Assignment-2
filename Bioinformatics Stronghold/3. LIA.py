'''
LIA exercise

Given: Two positive integers k(k≤7) and N(N≤2k). In this problem, we begin with Tom, who in the 0th generation has genotype Aa Bb. 
Tom has two children in the 1st generation, each of whom has two children, and so on. 
Each organism always mates with an organism having genotype Aa Bb.

Return: The probability that at least N Aa Bb organisms will belong to the k-th generation of Tom's family tree 
        (don't count the Aa Bb mates at each level). Assume that Mendel's second law holds for the factors.
'''

import math     
                                                               
k = 2                                                                       
n = 1                                                                                   
p = 2**k                                   # total number of individual in the k-th generation                                          
probability = 0                            # we initialize the cumulative probability as 0 
                                                             
for element in range(n, p + 1):            # for every element form n to p+1                                            
    prob = (math.factorial(p) /            # binomial coefficient   
                                           
            (math.factorial(element) * math.factorial(p - element))) * (0.25**element) * (0.75**(p - element))                                                        
    # (0.25**element) caluclates the probability of individuals being Aa Bb
    # (0.75**element) calculates the probaility of individuals being different from Aa Bb

    probability += prob                   # sums the calculated probability to the cumulative probability                                                   

print(round(probability, 3))              # we round the result to its 3rd decimanl number 