def dp(coins, amount):
    minCoins = [float('inf')]*(amount+1)

    minCoins[0] = 0;

    for coin in coins:
        for i in range(amount+1):
            if i - coin >= 0:
                minCoins[i] = min(minCoins[i], minCoins[i - coin]+1)

    return minCoins[amount]
    
