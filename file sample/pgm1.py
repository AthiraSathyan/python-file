try:
    word=input("Enter your text:")
    inf=open("pgm1.txt","r+")
    lines=inf.readlines()
    inf.write("\n Output:\n")
    for line in lines:
        if word not in line.strip("\n"):
            inf.write(line)
    inf.close()
    print("program completed successfully")
except IOError as io:
    print(io)
    
