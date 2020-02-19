total = 0
counter = 0
print('At first', total,counter)
for things in [4,3,54,6,23,45,24,12,26,13,15]:
    counter += 1
    total += things
    print("total, counter", total, counter)
   
print('The average is',total/counter)