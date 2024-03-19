def find_coins_greedy(sum, coins):
    # sum = 137
    coins_count = {}

    # coins = [50, 25, 10, 5, 2, 1]
    for coin in coins:
        # coin = 50
        count = sum // coin
        # count = 2
        if count > 0:
            coins_count[coin] = count  # coins_count.get(coin, count)
        sum -= coin * count
        # sum = 37, більше монета 50 не підходить, використовуємо наступну найбільшу доступну монету
    return coins_count


if __name__ == "__main__":

    cases = [
        ([50, 25, 10, 5, 2, 1], 137),
        ([10, 6, 1], 12),
        ([25, 10, 5, 2, 1], 543210),
    ]
    functions = [find_coins_greedy]

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:
            print("Result for {}: {}".format(fun.__name__, fun(cash_amount, coins)))
