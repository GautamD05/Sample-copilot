def calculate_total(prices, discount =0):
    total = 0
    for price in prices:
        total += price

    if discount > 0:
        total -= (total * discount / 100)

    return total