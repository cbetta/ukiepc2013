import sys

lines = []

for line in sys.stdin:
     lines.append(line)

before = lines[1].strip()
after = lines[2].strip()

expected = int(lines[0])%2

idx = 0
for char in list(before):
  before_val = int(char)
  after_val = int(after[idx])
  sm = before_val + after_val
  if sm % 2 != expected:
    print "Deletion failed"
    exit(0)
  idx += 1

print "Deletion succeeded"
