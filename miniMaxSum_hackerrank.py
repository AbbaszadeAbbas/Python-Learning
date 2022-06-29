def miniMaxSum(arr):
  arr.sort()
  first = arr[:-1]
  total1 = 0
  for fir in first:
    total1+=fir


  second = arr[1:]
  total2 = 0

  for sec in second:
    total2+=sec

  print(total1,total2)


miniMaxSum([1,3,5,7,9])