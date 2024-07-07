a = [1, 3, 5, 7, 6, 12]
for i in range(0, len(a) - 1):
    print(a[i], '-', a[i + 1])
    if a[i] < a[i + 1]:
        print("good")
    else:
        print("BAD")
