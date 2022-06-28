s = '07:05:45PM'

def timeConversion(s):
  hour = int(s[0]) + 1
  minute = int(s[1]) + 2

  watch = f'{hour}{minute}:{s[3]}{s[4]}:{s[6]}{s[7]}'

  if int(s[0]) != 1 and int(s[1]) != 2 and s[8] != "A" or s[8] != "P":
    print(watch)

  if s[8] == "A":
    if int(s[0])==1 and int(s[1]) == 2:
      print(f'00:{s[3]}{s[4]}:{s[6]}{s[7]}')

  if s[8] == "P":
    if int(s[0])==1 and int(s[1]) == 2:
      print(f'12:{s[3]}{s[4]}:{s[6]}{s[7]}')


timeConversion(s)