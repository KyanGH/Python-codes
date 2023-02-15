a = list(("Apple","Car","Phone","Pad","Watch"))
print(a[1], end=" ")

b = ["Car","apple","watch"]
print(a[0],b[2], sep=" has ")
b.insert(1,'wash')
print(b)
b.extend(a)
print(b)