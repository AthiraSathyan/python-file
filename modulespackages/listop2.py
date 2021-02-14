def unique(l):
    new=[]
    for x in l:
        if x not in new:
            new.append(x)
    for x in new:
        print (x)
def square(l):
    slist=[]
    for x in l:
        x=x*x
        slist.append(x)
    for x in slist:
        print (x)
