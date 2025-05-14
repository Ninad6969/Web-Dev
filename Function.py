def GM():
    print("Hello")
    print("Good Morning!")



def GN():
    print("Good Night")

def GE():
    print("Good Evening")

 # GM()
 # GN()
 # GE()

#Arguments / Parameter

def GM(name):
    print("Good Morning",name)

    GM("Tahseenul")

    def Chat(f1,f2,f3):
        print(f1," : Hey Everyone! How are you?")
        print(f2, " : Yeah. I'm DOing great. WHat about you?")
        print(f3, " : I'm also doing good ")
        print(f1, " Okay,bye")
        print(f2, "Bye Bye")
        print(f3, " Take Care!")

("Tahseenul","Orion","Aohon") 

def Add(a,b):
    print(a+b)

def Sub(a,b):
    print(a-b)

def Mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)


p = 7
q = 5
Add(p,q) #Add(7,5)
Sub(p,q)
Mul(p,q)
div(p,q)

def A():
    print("Inside A Function")
    B()

def B():
    print("Inside B Function")
    C()

def C():
    print("Inside C Function")
    A()

    def wish():
        return "Happy Birthday"
    
   a = wish()

def Square(a):
    return a**2

a = Square(2)
b = Square(3)
c = Square(3)

print(a,b,c)