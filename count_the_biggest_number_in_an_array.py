array = [1,2,3,4,5,6,7,7,7,88,88,9,9,9,9]
max = array[0]

for arr in array:
  while arr > max:
    max = arr

print(f'Ən böyük ədəd : {max}')
print(f'Ən böyük ədədin sayı : {array.count(max)}')