import sys

def split(str, num):
    return [ str[start:start+num] for start in range(0, len(str), num) ]

lines = []
valids = [['***', '* *', '* *', '* *', '***'], ['  *', '  *', '  *', '  *', '  *'], ['***', '  *', '***', '*  ', '***'], ['***', '  *', '***', '  *', '***'], ['* *', '* *', '***', '  *', '  *'], ['***', '*  ', '***', '  *', '***'], ['***', '*  ', '***', '* *', '***'], ['***', '  *', '  *', '  *', '  *'], ['***', '* *', '***', '* *', '***'], ['***', '* *', '***', '  *', '***']]

for line in sys.stdin:
     line = line.rstrip("\n")
     line = split(line, 4)
     lines.append(line)

chars = []

for idx, line in enumerate(lines):
  for idx2, number in enumerate(line):
    if len(chars) <= idx2:
      chars.append([])
    chars[idx2].append(number[0:3])

# print chars
nums = []

valid = True
for char in chars:
  char_valid = False
  for idx,valid in enumerate(valids):
    if valid == char:
      char_valid = True
      nums.append(idx)
      break

  if not char_valid:
    valid = False
    break

if not valid:
  print "BOOM!!"
else:
  string = ""
  for num in nums:
    string += str(num)

  val = int(string)
  # print val

  if val%6 == 0:
    print "BEER!!"
  else:
    print "BOOM!!"