T = int(input())

for t in range(1, T+1) :
    word = input()
    for i in range(len(word)//2) :
        if word[i] == word[-1-i] :
            result = 1
        else :
            result = 0
    print("#{} {}".format(t, result)) 
        