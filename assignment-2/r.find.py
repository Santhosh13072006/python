def function(s,a):
    A=-1
    for i in range(0,len(s)):
       if s[i]==a[0]:
            k=i
            c=0
            for j in range(0,len(a)):
                if k+j<len(s) and s[k+j]==a[j]:
                    c=c+1
            if c==len(a):
                A=i
    return A 
s=input ("enter a string\n")
a=input("enter a string to be found\n")
d=function(s,a)
if d==-1:
    print("error not found!\n")
else :
    print(d)
     
