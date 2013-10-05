import sys

lines = []

for line in sys.stdin:
     lines.append(line)

items = lines[1].split(" ")
items = map(int, items)
items.sort()

mx = 0
idx = 0
for item in reversed(items):
  sm = idx+item+1
  if sm > mx:
    mx = sm
  idx += 1

print mx+1
