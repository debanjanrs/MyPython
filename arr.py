a=[1,2,3,4,5]
b=[6,7,8,9,10]
a[3]=10
print(a[2])
b[0]+=1 # b[0] = b[0] + 1
print(a)
print(b)




b[1]=a[1]
print (b)





K=[1,2,3,4,5,6]
M=[0,0,0,0,0,0]


for m in range(0,len(K)):
    M[m]+=K[m] 
print (M)