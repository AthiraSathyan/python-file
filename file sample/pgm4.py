def pgm4(a):
    return a[0].upper()+a[1:]
try:
    inf=open("pgm4.txt")
    word=inf.read().split()
    b=""
    for i in word:
        out=pgm4(i)
        b=b+" "+out
    print(b)
    inf.close()
except IOError as io:
    print(io)
