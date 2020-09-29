"""PAVAN SAI . V
   121910313028"""
# Linear search of an array using dynamical input
n=int(input())
ar=[]
print("enter the elements:")
#taking array inputs dynamically
for i in range(n):
    a=int(input())
    ar.append(a)
#search element    
s=int(input("enter an ele to search:"))
l=len(ar)
for i in range(l):
    if(ar[i]==s):
        print("ele found in",i)
        