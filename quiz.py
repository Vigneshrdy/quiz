import random
print("Welcome to quiz..")
name=input("Enter your name: ")
print(f"\nHello {name} please Choose your subject\n")
while True:
    print("\n1 -> History\n2 -> Science\n3 -> Geography",end=': ')
    x=int(input()) 
    if 1<=x<=3 :
        break
        
fname=name+'.txt'
f=open(fname,'w')
history = [
    ("Who was the first President of the United States?\na-->George Washington\nb-->Thomas Jefferson\nc-->Abraham Lincoln\nd-->John Adams", "a"),
    ("What year did World War I begin?\na-->1914\nb-->1939\nc-->1920\nd-->1945", "a"),
    ("Which civilization is known for building the Colosseum?\na-->Greeks\nb-->Romans\nc-->Egyptians\nd-->Aztecs", "b"),
    ("Who was the first person to step on the moon?\na-->Neil Armstrong\nb-->Buzz Aldrin\nc-->Yuri Gagarin\nd-->Alan Shepard", "a"),
    ("What was the name of the ship that carried the Pilgrims to America in 1620?\na-->Mayflower\nb-->Santa Maria\nc-->Titanic\nd-->Endeavour", "a"),
    ("What was the main cause of the Cold War?\na-->Communism vs. Capitalism\nb-->World War I\nc-->The French Revolution\nd-->The Industrial Revolution", "a"),
    ("Who was the longest reigning monarch in British history?\na-->Queen Elizabeth II\nb-->Queen Victoria\nc-->King George III\nd-->King Henry VIII", "a"),
    ("What event triggered the start of World War II?\na-->The assassination of Archduke Franz Ferdinand\nb-->The invasion of Poland\nc-->The bombing of Pearl Harbor\nd-->The signing of the Treaty of Versailles", "b")
]
sci =[
    ("What is the speed of light in a vacuum?\na-->300,000 km/s\nb-->150,000 km/s\nc-->450,000 km/s\nd-->1,000,000 km/s", "a"),
    ("Who developed the laws of motion?\na-->Isaac Newton\nb-->Albert Einstein\nc-->Galileo Galilei\nd-->Nikola Tesla", "a"),
    ("What is the unit of force?\na-->Joule\nb-->Newton\nc-->Watt\nd-->Pascal", "b"),
    ("What is the acceleration due to gravity on Earth?\na-->10 m/s²\nb-->9.8 m/s²\nc-->8.5 m/s²\nd-->12 m/s²", "b"),
    ("Which subatomic particle has a positive charge?\na-->Electron\nb-->Neutron\nc-->Proton\nd-->Quark", "c"),
    ("What is the energy stored in an object due to its motion called?\na-->Potential Energy\nb-->Kinetic Energy\nc-->Thermal Energy\nd-->Chemical Energy", "b"),
    ("Who formulated the theory of special relativity?\na-->Isaac Newton\nb-->Albert Einstein\nc-->Niels Bohr\nd-->Max Planck", "b"),
    ("What is the SI unit of electric current?\na-->Volt\nb-->Ampere\nc-->Ohm\nd-->Tesla", "b")
]


geography = [
    ("What is the capital of France?\na-->London\nb-->Paris\nc-->Berlin\nd-->Madrid", "b"),
    ("Which country is the largest by land area?\na-->China\nb-->United States\nc-->Russia\nd-->Canada", "c"),
    ("What is the longest river in the world?\na-->Amazon River\nb-->Nile River\nc-->Yangtze River\nd-->Mississippi River", "b"),
    ("Which continent is known as the 'Dark Continent'?\na-->Asia\nb-->Africa\nc-->Australia\nd-->South America", "b"),
    ("Mount Everest is located in which mountain range?\na-->Andes\nb-->Himalayas\nc-->Rockies\nd-->Alps", "b"),
    ("What is the largest ocean on Earth?\na-->Atlantic Ocean\nb-->Indian Ocean\nc-->Arctic Ocean\nd-->Pacific Ocean", "d"),
    ("Which desert is the largest in the world?\na-->Sahara Desert\nb-->Gobi Desert\nc-->Kalahari Desert\nd-->Atacama Desert", "a"),
    ("What is the smallest country in the world?\na-->Monaco\nb-->Vatican City\nc-->Nauru\nd-->San Marino", "b")
]

score = 0

if x==1:
    random.shuffle(history)
    for i in range(5):
        print(history[i][0])
        f.write(history[i][0]+'\n')
        ans=input("Enter your option here :")
        if ans==history[i][1]:
            f.write(f"Your answer is {ans}\n")
            f.write("Congrats your answer is correct\n")
            score+=1
            print(f"Your answer is {ans}\n")
            print("Congrats your answer is correct\n")
        else :
            f.write("Better luck next time\n")
            print("Better luck next time\n")
        f.write(f"Correct option is {history[i][1]}\n")
        print(f"Correct option is {history[i][1]}\n")
elif x==2:
    random.shuffle(sci)
    for i in range(5):
        print(sci[i][0])
        f.write(sci[i][0]+'\n')
        ans=input("Enter your option here :")
        if ans==sci[i][1]:
            f.write(f"Your answer is {ans}\n")
            f.write("Congrats your answer is correct\n")
            score+=1
            print(f"Your answer is {ans}\n")
            print("Congrats your answer is correct\n")
        else :
            f.write("Better luck next time\n")
            print("Better luck next time\n")
        f.write(f"Correct option is {sci[i][1]}\n")
        print(f"Correct option is {sci[i][1]}\n")
elif x==3:
    random.shuffle(geography)
    for i in range(5):
        print(geography[i][0])
        f.write(geography[i][0]+'\n')
        ans=input("Enter your option here :")
        if ans==geography[i][1]:
            f.write(f"Your answer is {ans}\n")
            f.write("Congrats your answer is correct\n")
            score+=1
            print(f"Your answer is {ans}\n")
            print("Congrats your answer is correct\n")
        else :
            f.write("Better luck next time\n")
            print("Better luck next time\n")
        f.write(f"Correct option is {geography[i][1]}\n")
        print(f"Correct option is {geography[i][1]}\n")
f.write('\n')
print('\n')
f.write(f"Score:{score}")
print(f"Score:{score}")
f.close()
