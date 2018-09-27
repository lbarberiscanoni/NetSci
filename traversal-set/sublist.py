a = [1, 2, 4, 5]
b = [2, 5]


subL = [ [ a[i], a[i +1] ] for i in range(len(a) - 1) ]

print(subL)
print(b in subL)