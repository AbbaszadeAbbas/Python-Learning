def staircase(n):
  i = 1
  while i <= n:
    z = n - i
    b = "#" * i
    i = i+1
    print(z * " " + b)

staircase(5)