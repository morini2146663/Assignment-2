'''
PERM exercise

Given: A positive integer n≤7.

Return: The total number of permutations of length n, followed by a list of all such permutations (in any order).
'''

permutations = []

def gen_permutations(current_permutation):
    if len(current_permutation) == n:                       # if the current permutation lenght equals given n 
        permutations.append(current_permutation[:])         # we append a copy of the permutation to the empty list 
        return

    for i in range(1, n + 1):
        if i not in current_permutation:                    # if the element is not already in current permutation
            current_permutation.append(i)                   # we append it to the current permutation
            gen_permutations(current_permutation)           # and recursively do the same thing for all the permutation
            current_permutation.pop()                       # lastly we backtrack by removign the last element

n = 6

gen_permutations([])

print(len(permutations))

for perm in permutations:
    print(" ".join(map(str, perm)))
