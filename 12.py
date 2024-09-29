def prt(l):
    if 0<l:
        print("positive")
    else:
        print("negative")
j = prt (10)
print(j)


for i in range (10):
    print("Debanjan")


















for i in [5,10,11,1,3]:
    print(i)

for h in range(0,6):
    print(h)

x=[15,20,25,30,35,40]

for h in range(0,6):
    print(h)
    print(x[h]) 








def replace(arr):
    for m in range(0,len(arr)):
        if (arr[m] % 2 == 0):
           arr[m] = 0
        else:
            arr[m]= 1
    return arr

x=[1,2,3,4,5]
y = replace (x)
print ( y)


k=[1,5,6,9,8,6,45,7]
k[5]  = 225
print (k)