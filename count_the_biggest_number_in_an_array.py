array = [1,2,3,4,5,6,7,7,7,8,8,8,8,9,9,9,9]
max = array[0]

for arr in array:
  while arr > max:
    max = arr

print(array.count(max))