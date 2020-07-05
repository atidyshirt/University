from collections import defaultdict

def coins_reqd__(value, coinage):
    """The minimum number of coins to represent value assuming a 1-unit coin"""
    num_coins = [0] * (value + 1)
    coins_count = defaultdict(int)

    print(num_coins)
    for amt in range(min(coinage), value + 1):
        for c in coinage:
            if amt >= c:
                coins_count.append(num_coins[amt]) = 1 + min(num_coins[amt - c])

    return num_coins

def coins_reqd(value, coinage):
    """The minimum number of coins to represent value"""
    numCoins = [0] * (value + 1)
    for amt in range(min(coinage), value + 1):
          numCoins[amt] = 1 + min(numCoins[amt - c] for c in coinage if  amt >=  c)
    return numCoins[value]

print(coins_reqd(16, [1, 5, 10]))
