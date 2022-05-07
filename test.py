import sys
num = int(sys.stdin.readline())
inlist = []
for i in range(1, num+1):
    inlist.append(i)
inlist.reverse()

for i in range(len(inlist)):
    print(inlist[i])