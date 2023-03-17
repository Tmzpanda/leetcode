"""
Imagine you are creating an algorithm for currency trading. Now you have a prototype which handles trading of a single currency. Each day, it can sell or buy exactly one unit of the currency or do nothing.

You are given rates, an array of positive integers where rates[i] represents the currency price on the ith day. You're also given strategy, an array of -1s, 0s, and 1s, where strategy[i] represents what operation the algorithm should perform on the ith day:
-1 represents the buy operation,
0 represents the hold operation, meaning nothing is bought or sold,
1 represents the sell operation.
You're also given an integer k, which is guaranteed to be even.

In order to improve the algorithm's performance, you may change the strategy in the following way:
Choose a range of exactly k consecutive elements,
Set elements of the first half of the chosen range to 0,
Set elements of the second half of the chosen range to 1.
Your task is to choose the range optimally to maximize the algorithm's total profit. The profit is defined as the sum of all selling rates minus the sum of all buying rates (in other words, the difference between the end and start amount). The profit may be negative in case the end amount is lower than the start amount.

NOTE: Assume it is always possible to perform buy and sell operations, meaning you always have enough currency and budget.

Example:
For rates = [2, 4, 1, 5, 10, 6], strategy = [-1, 1, 0, 1, -1, 0], and k = 4, the output should be solution(rates, strategy, k) = 18.

First, let's calculate the profit if the algorithm is left as it is with no changes.

Before the trades start, the profit is 0;
Day 0: strategy[0] = -1, so the algorithm buys currency at price rates[0] = 2, and the profit becomes 0 - 2 = -2;
Day 1: strategy[1] = 1, so the algorithm sells currency at price rates[1] = 4, and the profit becomes -2 + 4 = 2;
Day 2: strategy[2] = 0, so the algorithm holds currency, and the profit doesn't change;
Day 3: strategy[3] = 1, so the algorithm sells currency at price rates[3] = 5, and the profit becomes 2 + 5 = 7;
Day 4: strategy[4] = -1, so the algorithm buys currency at price rates[4] = 10, and the profit becomes 7 - 10 = -3;
Day 5: strategy[5] = 0, so the algorithm holds currency, and the profit doesn't change;
Thus, the total profit is -3.

We may change exactly k = 4 consecutive elements of the strategy to be equal to [0, 0, 1, 1]. Thus, we have three variants of the new strategy:

strategy = [0, 0, 1, 1, -1, 0] resulting in profit = -4
strategy = [-1, 0, 0, 1, 1, 0] resulting in profit = 13
strategy = [-1, 1, 0, 0, 1, 1] resulting in profit = 18.
So, the maximum achievable profit is 18.

"""

# O(n*k)
def solution(rates, strategy, k):
    n = len(rates)
    max_profit = sum(rate * strategy for rate, strategy in zip(rates, strategy))
    
    for i in range(n - k + 1):
        new_strategy = strategy[:i] + [0]*(k//2) + [1]*(k//2) + strategy[i+k:]
        profit = sum(rate * strategy for rate, strategy in zip(rates, new_strategy))
   
        if profit > max_profit:
            max_profit = profit
    
    return max_profit
    
    
