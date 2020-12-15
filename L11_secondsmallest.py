def second_smallest(n):
  if (len(n)<2):
    return
  if ((len(n)==2)  and (n[0] == n[1]) ):
    return
  dup = set()
  unq = []
  for x in n:
    if x not in dup:
      unq.append(x)
      dup.add(x)
  unq.sort()
  return  unq[1]

print(second_smallest([1,10,5,9,3,43]))