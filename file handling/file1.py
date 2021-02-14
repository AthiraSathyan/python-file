inf=False
outf=False
try:
    inf=open('infile.txt')
    outf=open('outs.txt','w')
    line=inf.read()
    while line:
        outf.write(line)
        inf=False
        inf=open('outs.txt')
        line=inf.readline()
    print(line)
    print("copied successfully")
except IOError as io:
    print(io)
finally:
    if inf:inf.close()
    if outf:outf.close()
