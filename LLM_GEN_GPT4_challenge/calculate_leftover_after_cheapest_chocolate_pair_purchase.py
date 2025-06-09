def buy_chocolates(prices, money):
    # Sort the prices in non-decreasing order
    prices.sort()
    
    # The two cheapest chocolates will be the first two in the sorted list
    min_cost = prices[0] + prices[1]
    
    # If we have enough money to buy them, return the leftover
    if min_cost <= money:
        return money - min_cost
    else:
        # Cannot afford any two chocolates, return original money
        return money
```