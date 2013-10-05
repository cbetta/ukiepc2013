import sys

lines = []

for line in sys.stdin:
     lines.append(line.strip())

after = list(lines[1])
before = list(lines[0])

before_cnt = 0
for idx,char in enumerate(after):
  if len(before)<idx+1:
    break
  elif char == before[idx]:
    before_cnt += 1
  else:
    break

after = list(lines[1][::-1])
before = list(lines[0][::-1])

after_cnt = 0
for idx,char in enumerate(after):
  if len(before)<idx+1:
    break
  elif char == before[idx]:
    after_cnt += 1
  else:
    break

df = len(after)-before_cnt-after_cnt
if df <= 0 and len(after) > len(before):
  df = len(after) - len(before)
print max(df, 0)