y,m,d = input().split('.')
print(d,m,y,sep='-') 
# input().split(':') 를 사용하면 콜론 ':' 기호를 기준으로 자른다.
#print(?, ?, sep=':') 를 사용하면 콜론 ':' 기호를 사이에 두고 값을 출력한다.

#연습
성,이름,나이 = input("나이,이름,성을 알려주세요.").split('.')
print(나이,이름,성,sep='-')