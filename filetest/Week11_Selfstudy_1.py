inFp = None
inStr = ""
i=1

inFp = open("C:\\PythonProgramming\\Python-Programming\\filetest\\datal.txt", "r", encoding="utf-8")

while True:
    inStr = inFp.readline()
    if inStr == "":
        break
    print("%d: %s" % (i, inStr), end="")
    i+= 1

inFp.close()