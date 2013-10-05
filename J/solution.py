import sys
import math

def chance(inner, outer, dd):
  return  _chance(outer, dd) -  _chance(inner, dd)

def _chance(r, dd):
  left = 1/(2*math.pi*math.pow(dd, 2))
  top = math.pow(r,2)/(2*math.pow(dd, 2))
  right = math.exp(-top)
  area = math.pi * r * r
  return left*right*area

lines = []

for line in sys.stdin:
  lines.append(line.strip().split(" "))

radi = []
for item in lines[0]:
  radi.append(float(item))

sd = float(lines[1][0])

print radi
print sd

# bulls_eye = chance(0, radi[0], sd)*50
# bull = chance(radi[0], radi[1], sd)*25
# inner_std = chance(radi[1], radi[2], sd)*10.5
# triple_ring = chance(radi[2], radi[3], sd)*31.5
# outer_std = chance(radi[3], radi[4], sd)*10.5
print _chance(radi[4], sd)
# double_ring = chance(radi[4], radi[5], sd)*21

# total = bulls_eye + bull + inner_std + triple_ring + outer_std + double_ring
# print total


