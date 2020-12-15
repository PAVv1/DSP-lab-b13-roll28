arr1 = []
n = int(input("Enter range: "))
for i in range(0, n):
  ele = int(input())
  arr1.append(ele)

print('unsorted list',arr1)

for i in range(n):
  min=i
  for j in range(i+1,n):
    if arr1[min]>arr1[j]:
      min=j
  arr1[i],arr1[min]=arr1[min],arr1[i]

print("sorted array:",arr1)
