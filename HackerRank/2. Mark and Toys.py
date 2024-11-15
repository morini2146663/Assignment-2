'''
Mark and Toys exercise

Mark and Jane are very happy after having their first child. 
Their son loves toys, so Mark wants to buy some. 
There are a number of different toys lying in front of him, tagged with their prices. 
Mark has only a certain amount to spend, and he wants to maximize the number of toys he buys with this money. 

Given a list of toy prices and an amount to spend
Return the maximum number of gifts he can buy
'''

def maxToys(prices, k):
    prices.sort()                      # sort the prices in ascending order 

    spent = 0                          # initialize both spend and count as 0
    count = 0
    
    for price in prices:               # for every element in prices
        if spent + price <= k:         # if spent + prince is smaller than the maximum expendable amount 
            spent += price             # add price to spent
            count += 1                 # and increase the toy count of 1
        else:                          # if spent + price is bigger than the maximum expendable amount
            break                      # stop the loop
    return count                       # return the final toys count 

prices = [1, 2, 3, 4]
budget = 7
maxToys (prices, budget)

prices2 = [1, 12, 5, 111, 200, 1000, 10]
budget2 = 50
maxToys (prices2, budget2)