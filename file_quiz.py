import random
def load(filename):
    q=[]
    with open(filename,'r') as file :
        for x in file:
            a=x.strip().split(';')
            qt=a[0]
            op=a[1:-1]
            ca=a[-1]
            q.append((qt,op,ca))
    return q    
def eva(a,name):
    points=0
    k=random.shuffle(a)
    f=open(f"{name}.txt",'w')
    l=random.sample(a,4)
    for x,y,z in l:
           print(f"{x}\n")
           f.write(f"{x}\n")
           for i in y:
               print(f"{i}\n")
               f.write(f"{i}\n")
           b=input("Enter your option here : ")
           print(f"Your choose {b}\n")
           f.write(f"Your choose {b}\n")
           print(f"correct option --> {z}\n")
           f.write(f"correct option --> {z}\n")
           if b==z:
               points+=1
    f.write(f"Total score {points}")
    print(f"Total score {points}")
    f.close()
                
            
name=input("Welcome to quiz..\nEnter your name: ")
print(f"\nHello {name} please Choose your subject\n")
while True:
    print("\n1 -> History\n2 -> Science\n3 -> Geography",end=': ')
    x=int(input()) 
    if 1<=x<=3 :
        break
if x==1:
    p=load('his.txt')
    eva(p,name)
elif x==2:
    p=load('sci.txt')
    eva(p,name)
elif x==3:
    p=load('geo.txt')
    eva(p,name)
    
