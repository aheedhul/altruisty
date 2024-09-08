def find2Numbers(arr):
    xor_sum = 0
    for num in arr:
        xor_sum ^= num
    
    set_bit = xor_sum & -xor_sum
    
    x = 0
    y = 0
    for num in arr:
        if num & set_bit:
            x ^= num
        else:
            y ^= num
    
    return sorted([x, y])

N = int(input("Enter the value of N: "))

num_elements = (2 * N) + 2

arr = []
print(f"Enter {num_elements} numbers:")
for i in range(num_elements):
    num = int(input())
    arr.append(num)

result = find2Numbers(arr)
print(result[0], result[1])
