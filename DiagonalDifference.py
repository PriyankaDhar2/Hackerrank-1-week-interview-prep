
#without using numpy array

def DifferenceDiagonal(n,arr):

    diag= [arr[i][i] for i in range(min(n,n))]
    oppdiag= [arr[i][n - 1 - i] for i in range(min(n,n))]
    
    sumofd1= sum(diag)
    sumofd2 = sum(oppdiag)
    if sumofd1 > sumofd2:
        return sumofd1 - sumofd2
    else:
        return sumofd2 - sumofd1

n = int(input("Enter the number of rows n columns: "))
arr = []

for i in range(n):
    row = list(map(int, input(f"Enter the {i+1}th column: ").split()))
    arr.append(row)



print(DifferenceDiagonal(n,arr))