def buy_choco(prices, money):
    """
    Calculate the leftover money after buying the two cheapest chocolates.
    
    Args:
    prices (List[int]): List of chocolate prices.
    money (int): Initial amount of money.
    
    Returns:
    int: Leftover money after purchase. Returns original money if cannot afford two chocolates.
    """
    # Find the two smallest prices in the list
    min1 = min2 = float('inf')
    for price in prices:
        if price < min1:
            min2 = min1
            min1 = price
        elif price < min2:
            min2 = price
    
    total_cost = min1 + min2
    
    # Check if the total cost is affordable
    if total_cost <= money:
        return money - total_cost
    else:
        return money