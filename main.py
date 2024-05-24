"""
Порівняйте ефективність жадібного алгоритму та алгоритму динамічного програмування, 
базуючись на часі їх виконання або О великому та звертаючи увагу на їхню продуктивність при великих сумах.
"""

import timeit
import tracemalloc

from find_coins_greedy import find_coins_greedy
from find_min_coins import find_min_coins

def measure_memory(func):
    tracemalloc.start()
    func()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return current, peak

coins = [50, 25, 10, 5, 2, 1]
test_amounts = [11, 113, 58244]

for amount in test_amounts:
    print("\n    Amount change: ", amount, "==============================")
    print("  Greedy algorythm")
    def find_change_greedy():
        find_coins_greedy(amount, coins)
    greedy_time_taken = timeit.timeit(find_change_greedy, number=100) / 100
    print(find_coins_greedy(amount, coins))
    print(f"Average greedy algorythm time: {greedy_time_taken:.6f} seconds")

    current_greedy, peak_greedy = measure_memory(find_change_greedy)
    print(f"Greedy algorythm: Peak memory usage: {peak_greedy} bytes")

    print(f"Відносно суми решти: Час - {greedy_time_taken/amount}, Пам'ять - {peak_greedy/amount}")
    


    print("  Dynamic algorythm")
    def find_change_dynamic():
        find_min_coins(coins, amount)
    dynamic_time_taken = timeit.timeit(find_change_dynamic, number=100) / 100
    print(find_min_coins(coins, amount))
    print(f"Average dynamic algorythm time: {dynamic_time_taken:.6f} seconds")

    current_dynamic, peak_dynamic = measure_memory(find_change_dynamic)
    print(f"Dynamic algorythm: Peak memory usage: {peak_dynamic} bytes")
    
    time_diff = dynamic_time_taken / greedy_time_taken
    print(f"Greedy algorythm faster dynamic in {time_diff:.2f} times")

    memory_diff = peak_dynamic / peak_greedy
    print(f"Greedy algorythm using {memory_diff:.2f} times less memory")

    print(f"Відносно суми решти: Час - {dynamic_time_taken/amount}, Пам'ять - {peak_dynamic/amount}")








