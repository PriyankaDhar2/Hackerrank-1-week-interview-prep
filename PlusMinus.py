def plusMinus(arr):
    z, n, p = 0, 0, 0
    total = len(arr)

    for i in arr:
        if i == 0:
            z += 1
        elif i < 0:
            n += 1
        else:
            p += 1

    print("{:.6f}".format(p / total))
    print("{:.6f}".format(n / total))
    print("{:.6f}".format(z / total))

arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
