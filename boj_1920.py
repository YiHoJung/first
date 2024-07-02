N = int(input())
Nlist = input().split()
M = int(input())
Mlist = input().split()
Answer =[0 for _ in range(M)]

for i in range(M):
    if Mlist[i] in Nlist:
        Answer[i] = 1
for i in range(M):
    print(Answer[i])