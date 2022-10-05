list = [2, 45, 67, 67, 90, 56]
empty = []
for i in list:
    sum = 0
    for digit in str(i):
        sum += int(digit)
    empty.append(sum)
print(empty)
