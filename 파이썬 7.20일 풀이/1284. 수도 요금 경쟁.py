import sys

sys.stdin = open("1284.txt", "r")

T = int(input())

for test_case in range(1, T+1) :
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    B = Q
    if W > R :
        B += (W-R)*S

    print("#" + str(test_case), end=" ")

    if A > B :
        print(B)
    else :
        print(A)