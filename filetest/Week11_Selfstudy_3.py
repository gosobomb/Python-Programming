outFp = None
outStr = ""

outFileName = input("파일명을 입력하세요: ")
outFp = open(outFileName, "w", encoding="utf-8") 

while True:
    outStr = input("내용 입력 : ")
    if outStr != "":
        outFp.writelines(outStr + "\n")
    else:
        break

outFp.close()
print("--- 정상적으로 파일에 씀 ---")