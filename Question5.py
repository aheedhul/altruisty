def getMaxToys(prices, money):
    start = 0
    current_sum = 0
    max_toys = 0
    
    for end in range(len(prices)):
        current_sum += prices[end]
        
        while current_sum > money:
            current_sum -= prices[start]
            start += 1
        
        max_toys = max(max_toys, end - start + 1)
    
    return max_toys

n = int(input().strip())
prices = [int(input().strip()) for _ in range(n)]
money = int(input().strip())

print(getMaxToys(prices, money))
