def insertionRecursive(arr, n):
    if n <= 1:
        return
    insertionRecursive(arr, n - 1)
    l = arr[n - 1]
    j = n - 2
    while (j >= 0 and arr[j] > l):
        arr[j + 1] = arr[j]
        j = j - 1
    arr[j + 1] = l
def printArray(arr, n):
    for i in range(n):
        print(arr[i])

arr1 = []
n = int(input("Enter range: "))
for i in range(0, n):
  ele = int(input())
  arr1.append(ele)

insertionRecursive(arr1, n)
printArray(arr1, n)