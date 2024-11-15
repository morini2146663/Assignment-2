'''
Maximum Perimeter Triangle exercise

Given an array of stick lengths, use  of them to construct a non-degenerate triangle with the maximum possible perimeter. 
Return an array of the lengths of its sides as  integers in non-decreasing order.

If there are several valid triangles having the maximum perimeter:

Choose the one with the longest maximum side.
If more than one has that maximum, choose from them the one with the longest minimum side.
If more than one has that maximum as well, print any one them.
If no non-degenerate triangle exists, return [-1]
'''

def maxPerimeterTriangle(sticks):
    sticks.sort()                                                           # we sort the stick lenghts in ascending order 
    
    # a non degenerate triangle is found if a + b > c (with c as its longest side)
    # the loop basically tries the largest possible set of sticks first and then goes backward
    for element in range(len(sticks) - 3, -1, -1):                         
        if sticks[element] + sticks[element+1] > sticks[element+2]:         
            return [sticks[element], sticks[element+1], sticks[element+2]]  # if a valid triangle is found, the 3 sides of the triangle are returned 
    return [-1]                                                             # if no valid triangle is found return [-1]


sticks = [1, 1, 1, 3, 3]
print(maxPerimeterTriangle(sticks))

sticks2 = [1, 2, 3]
print(maxPerimeterTriangle(sticks2))

sticks3 = [1, 1, 1, 2, 3, 5]
print(maxPerimeterTriangle(sticks3))