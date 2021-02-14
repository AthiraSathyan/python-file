try:
    inf=open("pgm3.txt","r")
    word=inf.read().split()
    maxm=len(max(word,key=len))
    for i in word:
        if len(i)==maxm:
            print("Longest word is:",i)
    inf.close()
except IOError as io:
    print(io)
