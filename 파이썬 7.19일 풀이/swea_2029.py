import sys

sys.stdin = open("swea_2029.txt", "r")

t = int(input())
for i in range(1,t+1):
    a,b = map(int,input().split())
    print("#{} {} {}".format(i, a//b,a%b))

