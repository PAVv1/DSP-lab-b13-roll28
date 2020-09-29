"""PAVAN SAI . V
   121910313028"""
#Binary search using dynamic inputs nd functions
def dynamic_input():
    print("enter the elements:")
    for i in range(n):
        a=int(input())
        ar.append(a)
    return ar
def binary_search(s):
    if(ar[mid]==s):
        print("ele is found in",mid)
#comparing search value with elements from starting to mid    
    for i in range(low,mid-1):
        if(ar[i]==s):
            print("ele found in",i)
#comparing search value with elements from mid to last       
    for i in range(mid+1,high):
        if(ar[i]==s):
            print("ele found in",i) 
n=int(input())
ar=[]
ar=dynamic_input()
ar.sort()
s=int(input("enter an ele to search:"))
l=len(ar)
low=0
high=l
mid=low+high//2
binary_search(s)