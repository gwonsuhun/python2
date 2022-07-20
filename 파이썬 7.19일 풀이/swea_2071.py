from ast import Num
from posixpath import split
import sys
sys.stdin = open("swea_2071.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    sum = 0
    li = list(map(int, input().split()))
    for i in li :
        sum += i
    print("#{} {}".format(test_case, round(sum/len(li))))
