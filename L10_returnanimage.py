#121910313028
st=input("Enter string: ")
s=[]
f=0
count=0
o="("
c=")"
def checkclose(k):
    if c.index(k)!=o.index(s[-1]):
        return False
    return True
for i in st:
    if i in o:
        s.append(i)
    else:
        if len(s)==0:
            f=1
            break
        if checkclose(i):
            count+=1
            s.pop()
if f==1 or len(s)!=0:
    print(-1,":Not safe")
else:
    print(count)