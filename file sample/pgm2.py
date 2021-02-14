try:
    inf=open("pgm2.txt","r+")
    lines=inf.readlines()
    inf.write("\n Output:\n")
    for line in lines:
        if not(line.startswith("#")):
            inf.write(line)
    inf.close()
    print("program completed successfully")
except IOError as io:
    print(io)
    
