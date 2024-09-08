def minimize_ticket_price(price, K):
    stack = []
    for i in range(len(price)):
        while K > 0 and stack and stack[-1] > price[i]:
            stack.pop()
            K -= 1
        stack.append(price[i])
    
    while K > 0:
        stack.pop()
        K -= 1
    
    minimized_price = ''.join(stack).lstrip('0')
    return minimized_price if minimized_price else '0'

Tickets = input().strip()
K = int(input().strip())

result = minimize_ticket_price(Tickets, K)

print(result)
