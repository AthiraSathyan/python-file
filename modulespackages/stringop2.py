def StrRev(str):
    l=len(str)
    r=str[l::-1]
    return r
def UCount(str):
    u=0
    for i in str:
        if i.isupper():
            u+=1
    return u
def LCount(str):
    l=0
    for i in str:
        if i.islower():
            l+=1
    return l
def IsPalindrome(str):
    p=str[::-1]
    if str==p:
        return 'True'
    else:
        return 'False'
def IsPangram(str):
    a="abcdefghijklmnopqrstuvwxyz"
    for i in a:
        if i not in str.lower():
            return 'False'
    return 'True'

    
