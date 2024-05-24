def find_min_coins(coins, amount):
    # Створюємо масив для зберігання мінімальної кількості монет для кожної суми
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Нульова сума потребує нуль монет

    # Масив для зберігання монети, яка використовується для досягнення кожної суми
    used_coins = [0] * (amount + 1)

    # Заповнюємо масив dp
    for coin in coins:
        for x in range(coin, amount + 1):
            if dp[x - coin] + 1 < dp[x]:
                dp[x] = dp[x - coin] + 1
                used_coins[x] = coin

    # Якщо dp[amount] все ще нескінченність, значить неможливо видати таку суму з даними монетами
    if dp[amount] == float('inf'):
        return {}

    # Відновлюємо набір монет для видачі решти
    result = {}
    current_amount = amount
    while current_amount > 0:
        coin = used_coins[current_amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        current_amount -= coin

    return result

# Приклад використання функції
# coins = [50, 25, 10, 5, 2, 1]
# amount = 113
# print(find_min_coins(coins, amount))
