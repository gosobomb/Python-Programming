inFp = None
inList, inStr = [], ""
i=1

inFp = open("C:\\PythonProgramming\\Python-Programming\\filetest\\datal.txt", "r", encoding="utf-8")

inList = inFp.readlines()
for inStr in inList:
    print("%d: %s" % (i, inStr), end="")
    i += 1

inFp.close()
