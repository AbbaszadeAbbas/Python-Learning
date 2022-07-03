list = [1,2,3,4,3,2,1,345,46,537,3,8,6,4,45,4]
second_list = []

for lis in list:
  if lis not in second_list:
    second_list.append(lis)

print(second_list)