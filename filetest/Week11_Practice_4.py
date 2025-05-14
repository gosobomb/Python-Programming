inFp = None
inList, inStr = [], ""
i=1

inFp = open("C:\\pp\\Python-Programming\\filetest\\datal.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print(i,":", inStr, end = "")
    i += 1

inFp.close()
