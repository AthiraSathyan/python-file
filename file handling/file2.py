try:
    a=open("appendpgm.txt","a")
    x=input("Enter a text:")
    while x:
        a.write(x+"\n")
        x=input("Enter a text:")
    a.close()
except IOError as io:
    print(io)
