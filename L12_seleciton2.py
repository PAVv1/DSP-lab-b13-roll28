def selectionrecursion(a,i,n):
    min_i=i
    for j in range(i+1,n):
        if a[j]<a[min_i]:
            min_i=j
    a[i],a[min_i]=a[min_i],a[i]
    if i+1<n:
        selectionrecursion(a,i+1,n)


a = []
n = int(input("Enter range: "))
for i in range(0, n):
  ele = int(input())
  a.append(ele)

  
selectionrecursion(a,0,len(a))
print(a)
