import array as arr

eg1 = arr.array('i', [12, 3, 45, 3, 12, 6, 3])
print(eg1)
eg1.reverse()
print(eg1)
count = eg1.count(12)
print("The Number 12 occurs", count, "number of times")