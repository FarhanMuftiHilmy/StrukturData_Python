sample = {0: 10, 1: 20}
sample[2] = 30
print(sample)
#print using for loop
for i in sample:
  print(i, sample[i])
#sum all the values
for i in sample:
  sum += sample[i]
print("sum =", sum)