# matrix = [
#   [1,2,3],
#   [4,5,6],
#   [9,8,9]
# ]

# def diagonalDifference(arr):
#   first = arr[0][0] + arr[1][1] + arr[2][2]
#   second = arr[0][2] + arr[1][1] + arr[2][0]
#   if first > second:
#     print(first - second)
#   else:
#     print(second - first)

# diagonalDifference(matrix)

# number = [1,2,3,4]
# print(number)
# number.append(5)
# print(number)
# number.remove(1)
# print(number)

# numbers = [1,2,3,4,5]

# print(0 in numbers)


array = [1,2,3,4,5,6,7,8,5,5,5,9,9,9,9]
max = array[0]

for arr in array:
  while arr > max:
    max = arr

print(array.count(max))