word = input('단어를 입력하세요')

for i in range(len(word) // 2):      
    if word[i] != word[-1 - i]:
        print()
    else:      
        print(0)       
        break
            