a=int(input("enter the number"))
b=int(input("enter the number"))
c=input("enter the choice")
if(c=="+"):
    print(a+b)
elif(c=="-"):
    print(a-b)
elif(c=="*"):
    print(a*b)
elif(c=="/"):
    print(a/b)
else:
    print("invalid")
e=input("need to do other operations")
while e=="yes":
    a=int(input("enter the number"))
    b=int(input("enter the number"))
    c=input("enter the choice")
    if(c=="+"):
        print(a+b)
    elif(c=="-"):
        print(a-b)
    elif(c=="*"):
        print(a*b)
    elif(c=="/"):
        print(a/b)
    e=input("need to do other operations")
