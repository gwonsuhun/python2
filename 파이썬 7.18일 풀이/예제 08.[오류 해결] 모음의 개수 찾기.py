#아래 코드는 문자열에서 모음의 개수를 찾는 코드입니다. 
#코드에서 오류를 찾아 원인을 적고, 수정하세요.

word = "HappyHacking"

count = 0
 
for char in word:
    if char in [ "a" or "e" or "i" or "o" or "u"]:
        count += 1
print(count)