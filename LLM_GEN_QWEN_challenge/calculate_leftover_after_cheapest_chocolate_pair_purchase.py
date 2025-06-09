def buyChoco(prices, money):
    # Initialize variables to store the minimum prices
    min_price1 = float('inf')  # Minimum price of the first chocolate
    min_price2 = float('inf')  # Minimum price of the second chocolate
    
    # Iterate over the prices to find the two smallest prices
    for price in prices:
        if price < min_price1:
            min_price2 = min_price1  # Update the second minimum to old minimum
            min_price1 = price         # Update the first minimum to new minimum
        elif price < min_price2:
            min_price2 = price         # Update the second minimum if current price is lower
            
    # Calculate the total cost of the two cheapest chocolates
    total_cost = min_price1 + min_price2
    
    # Check if the total cost can be paid without going into debt
    if total_cost <= money:
        return money - total_cost  # Return the leftover money
    else:
        return money               # Return the original money if purchase is not possible

# Example usage:
prices1 = [1, 2, 2]
money1 = 3
print(buyChoco(prices1, money1))  # Output: 0

prices2 = [3, 2, 3]
money2 = 3
print(buyChoco(prices2, money2))  # Output: 3