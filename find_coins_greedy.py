def find_coins_greedy(amount):
  """
  Ця функція реалізує жадібний алгоритм для визначення оптимального набору монет для видачі решти.
  Args:     amount: Сума, яку потрібно видати покупцеві (ціле число).
  Returns:  Словник, де ключі - номінали монет, а значення - їх кількість.
  """

  coins = [50, 25, 10, 5, 2, 1]  # Список монет у порядку їх номіналу
  coin_counts = {}  # Словник для зберігання кількості монет кожного номіналу

  # Ітерація по монетах у порядку їх номіналу
  for coin in coins:
    while amount >= coin:
      amount -= coin  # Вирахувати з суми решти номінал монети
      if coin not in coin_counts:
        coin_counts[coin] = 0  # Додати номінал до словника, якщо його ще немає
      coin_counts[coin] += 1  # Збільшити кількість монет цього номіналу

  return coin_counts

# Приклад використання
# amount = 113
# coin_counts = find_coins_greedy(amount)
# print(f"Для суми {amount} оптимальний набір монет: {coin_counts}")