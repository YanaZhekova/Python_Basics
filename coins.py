coins_change = float(input())
counter_coins = 0

while coins_change > 0:
    coin = coins_change // 10
    counter_coins += 1
    coins_change -= coin
