l=[23,59,8,7,5]
t=[1,2,59,8,7,6]
# 1 
l.append(t[0])
print(l)
l.append(t[0]+t[3])
print(l)


t.extend(l)
print(t)



h=[1,2,3,4,5,6,7,8,9]
h.pop()
h.pop()
print(h)
