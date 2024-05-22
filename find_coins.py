from collections import defaultdict


def find_min_coins(amount, coins=[1, 2, 5, 10, 25, 50]):
    K = [0] + [float("inf")] * (amount)
    coin_used = [0] * (amount + 1)

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                if K[i - coin] + 1 < K[i]:
                    K[i] = K[i - coin] + 1
                    coin_used[i] = coin

    result = defaultdict(int)
    while amount > 0:
        coin = coin_used[amount]
        result[coin] += 1
        amount -= coin

    return dict(result)


print(find_min_coins(113))


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    result = defaultdict(int)
    current_value = 0
    index = 0

    while current_value != amount:
        if current_value + coins[index] <= amount:
            current_value += coins[index]
            result[coins[index]] += 1
        else:
            index += 1

    return dict(result)


print(find_coins_greedy(113))
