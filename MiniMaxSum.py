def miniMaxSum(arr):
    arr = sorted(arr)
    mini= sum(arr[:-1:])
    maxi= sum(arr[1::])
    return mini, maxi

arr=[1,2,3,4,5]
print(miniMaxSum(arr))