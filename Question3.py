def findSteppingNumbers(N, M):
    stepping_numbers = []
    
    def bfs(start):
        queue = [start]
        while queue:
            num = queue.pop(0)
            
            if num >= N and num <= M:
                stepping_numbers.append(num)
            
            last_digit = num % 10
            
            if last_digit > 0:
                next_num = num * 10 + (last_digit - 1)
                if next_num <= M:
                    queue.append(next_num)
            
            if last_digit < 9:
                next_num = num * 10 + (last_digit + 1)
                if next_num <= M:
                    queue.append(next_num)
    
    for i in range(10):
        bfs(i)
    
    stepping_numbers.sort()
    for number in stepping_numbers:
        print(number, end=' ')
    print()

N, M = [int(x) for x in input().split()]
findSteppingNumbers(N, M)
