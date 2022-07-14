
word = input("문자를넣으세요")
dnada = input("찾을알파벳을 입력하세요")
cot = 0
newcot = []
for b in word: 
    cot = cot + 1
    if b == dnada:
        
        newcot.append(cot)     
print(newcot)

