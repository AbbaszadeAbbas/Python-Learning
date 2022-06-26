weight = input("Weight : ")
l_k = input("(L)bs or (K)g : ")

if l_k == "k" or l_k == "K":
  print("You are", int(weight) * 2.20462, "pounds")
elif l_k == "l" or l_k == "L":
  print("You are", int(weight) * 0.453592, "kilograms")
else:
  print("Please enter (L)bs or (K)g")