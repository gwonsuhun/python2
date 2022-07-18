a = int(input("양수입력"))
b = 1
print('와일 전a=', a)
print('와일 전b=', b)
while a/10 >= 1:
    a= a/10
    b= b+1
    print('와일 후a=', a)
    print('와일 후b=', b)
print(b)