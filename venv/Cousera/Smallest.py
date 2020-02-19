'''This is used to find the smallest of few numbers'''

smallest = 0
counter = 0
print("Before, the smallest is", smallest)
for num in [34, 45, 67, 34,23, 48, 99,2,35, 23, 19]:
    if smallest is 0:
        smallest = num
    if num < smallest:
        smallest = num
    counter += 1
print(counter)
print("The smallest of all is", smallest)