"""
Given n as input, print the following pattern. Note that the number of # keep on increasing by 1.
Input-> n=3
Output-> 1#2##3###
"""

n = 3
pt = "#"
st = ""
for i in range(1,n+1):
  st = st + str(i) + pt*i
print(st)