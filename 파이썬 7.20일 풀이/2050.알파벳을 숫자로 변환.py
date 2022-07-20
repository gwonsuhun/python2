import sys

sys.stdin = open("2050.txt", "r")

alphabet = str(input())
for result in range(len(alphabet)):
    print(ord(alphabet[result])-64, end = " ")