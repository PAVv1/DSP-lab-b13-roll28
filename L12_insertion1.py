def insertion(arr1):
  for i in range(1, len(arr1)):
    k = arr1[i]
    j = i - 1
    while j >= 0 and k < arr1[j]:
      arr1[j + 1] = arr1[j]
      j -= 1
    arr1[j + 1] = k

arr1 = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
  ele = int(input())
  arr1.append(ele)

insertion(arr1)
print ("Sorted array is:")
for i in range(len(arr1)):
    print (arr1[i])
