string = input()
list = []
Len = len(string)

for i in range(Len):
    list.append(string[i:Len])

list.sort()

for i in range(len(list)):
    print(list[i])