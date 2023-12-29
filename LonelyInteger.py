def lonelyinteger(a):
    arr = sorted(a)
    for i in range(0, len(arr) - 1, 2):
        if arr[i] != arr[i + 1]:
            return arr[i]
    
    return arr[-1]

arr = [1, 2, 3, 2, 1]
result = lonelyinteger(arr)
print(f"The lonely integer is: {result}")
