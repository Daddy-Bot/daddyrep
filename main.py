sum = 0
for i in range(8, -1, -1):
    sum += 1 / (2 ** i)
    print("cnt is:", i)
    print("i is:", 2 ** i)
    print("div is 1/{:} = {:}".format(2 ** i, 1 / (2 ** i)))
    print("sum is: {:} + next({:})".format(sum - 1 / (2 ** i), 1 / (2 ** i)))
    print("\n")
