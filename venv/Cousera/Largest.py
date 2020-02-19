'''This is used to find the largest of few numbers'''

largest = -1
counter = 0
print("Before, the largest is", largest)
for num in [34, 45, 67, 34,23, 48, 99,2,35, 23, 19]:
    if num > largest:
        largest = num
        counter += 1
print(counter)
print("The largest of all is", largest)

