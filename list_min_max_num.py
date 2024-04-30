# find max and min number of list in python
numbers = [635,1,2,5,6,4,5,123,900,4]
max = numbers[0]
min = numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max:
        max = numbers[i]
    elif numbers[i] < min:
        min = numbers[i]

print("max:",max)
print("min:",min)