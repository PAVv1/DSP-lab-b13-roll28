"""PAVAN SAI . V
   121910313028"""
#Binary search using array input
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
        else:
            print("ele not found")
            break
#array input
ar=[1,2,3,4,9,76,90,12,133,1345,135]
ar.sort()
s=int(input("enter an ele to search:"))
l=len(ar)
low=0
high=l
mid=low+high//2
binary_search(s)