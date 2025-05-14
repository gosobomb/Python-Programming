inFp = None
inStr = ""

inFp = open("C:\\pp\\Python-Programming\\filetest\\datal.txt", "r", encoding="utf-8")

inStr = inFp.read()
print(inStr, end = "")

inStr = inFp.readline()
print(inStr, end = "")

inSTr = inFp.readlines()
print(inSTr, end = "")

inFp.close()