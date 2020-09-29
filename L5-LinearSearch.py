"""PAVAN SAI . V
   121910313028"""
#linear search using inputs
#array input
ar=[1,2,3,4,5,7,9]
l=len(ar)
#element to search
s=int(input("Enter element to search:"))
#comparing elements with search
for i in range(l):
    if(ar[i]==s):
        print("element is found in",i)