#121910313028
def quicksort(arr):
  k=len(arr)
  if k<2:
    return arr

  cur_pos=0
  for i in range(1,len(arr)):
    if arr[i]<=arr[0]:
      cur_pos+=1
      arr[cur_pos],arr[i]=arr[i],arr[cur_pos]
  arr[cur_pos],arr[0]=arr[0],arr[cur_pos]
  
  left=quicksort(arr[0:cur_pos])
  middle=[arr[cur_pos]]
  right=quicksort(arr[cur_pos+1:])
  return left+middle+right

l=list(map(int,input().split()))
print(quicksort(l))