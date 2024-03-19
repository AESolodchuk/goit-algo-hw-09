def find_min_coins(sum, coins):
    min_coins_required = [0] + [float("inf")] * sum
    coin_used = [0] * (sum + 1)

    for i in range(1, sum + 1):
        for coin in coins:
            if i >= coin and min_coins_required[i - coin] + 1 < min_coins_required[i]:
                min_coins_required[i] = min_coins_required[i - coin] + 1
                coin_used[i] = coin

    coins_count = {}
    current_sum = sum
    while current_sum > 0:
        coin = coin_used[current_sum]
        coins_count[coin] = coins_count.get(coin, 0) + 1
        current_sum -= coin

    coins_count_ordered = {
        coin: coins_count.get(coin, 0) for coin in coins if coin in coins_count
    }
    return coins_count_ordered, coin_used


if __name__ == "__main__":
    cases = [([50, 25, 10, 5, 2, 1], 137), ([10, 6, 1], 12)]

    functions = [find_min_coins]

    for coins, cash_amount in cases:
        print(f"\n\tCase for {coins} and sum: {cash_amount}")
        for fun in functions:

            result, coin_used = fun(cash_amount, coins)
            print("Result for sum {}: {}".format(fun.__name__, result))

            print("\tShow calculated table of best coins for each amount")
            for calculated_sum, best_coin in enumerate(coin_used):
                print(f"Best coin to use for {calculated_sum} is {best_coin}")

            print("\tShow how best result was calculated")
            current_sum = cash_amount
            while current_sum > 0:
                print(f"Current sum is {current_sum}")
                coin = coin_used[current_sum]
                print(
                    f"Found that for the sum {current_sum} the best coin to use is {coin}"
                )
                current_sum -= coin
                print("Calculating next value of sum to search...")
