string = input()
Num = int(input())
Index = len(string)
Len = len(string)

for i in range(Num):
    Line = input()
    if Line == "L":
        if Index > 0:
            Index -= 1
    elif Line == "D":
        if Index < Len:
            Index += 1
    elif Line == "B":
        if Index != 0:
            if Index == 1:
                string = string[1:Len]
                Index -= 1
                Len -= 1
            elif Index == Len:
                string = string[0:Len-1]
                Index -= 1
                Len -= 1
            else:
                string = string[0:Index-1] + string[Index:Len]
                Index -= 1
                Len -= 1
    else:
        Line = Line.split()
        p = Line[1]
        if Index == 0:
            string = p + string
        elif Index == Len:
            string = string + p
        else:
            string = string[0:Index] + p + string[Index:Len]
        Index += 1
        Len += 1

print(string)