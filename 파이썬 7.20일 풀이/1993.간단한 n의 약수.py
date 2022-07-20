inputValue = int(input("정수를입력하세요" ))
for resultValue in range(1,inputValue+1):
    if inputValue % resultValue == 0:
        print(resultValue,end=" ")