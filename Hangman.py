import random

#Functions

#Title
def Title() :
    print ("  _    _          _   _  _____   __  __          _   _ _ ")
    print (" | |  | |   /\   | \ | |/ ____| |  \/  |   /\   | \ | | |")
    print (" | |__| |  /  \  |  \| | |  __  | \  / |  /  \  |  \| | |")
    print (" |  __  | / /\ \ | . ` | | |_ | | |\/| | / /\ \ | . ` | |")
    print (" | |  | |/ ____ \| |\  | |__| | | |  | |/ ____ \| |\  |_|")
    print (" |_|  |_/_/    \_\_| \_|\_____| |_|  |_/_/    \_\_| \_(_)")
    print ("do not use caps")
                                                         
#You Win
def You_Win() :
    print (" __     __          __          ___       _ ")
    print (" \ \   / /          \ \        / (_)     | |")
    print ("  \ \_/ /__  _   _   \ \  /\  / / _ _ __ | |")
    print ("   \   / _ \| | | |   \ \/  \/ / | | '_ \| |")
    print ("    | | (_) | |_| |    \  /\  /  | | | | |_|")
    print ("    |_|\___/ \__,_|     \/  \/   |_|_| |_(_)")

#Game Over
def Game_Over():
    print ("   _____                         ____                 ")                 
    print ("  / ____|                       / __ \                ")                
    print (" | |  __  __ _ _ __ ___   ___  | |  | |_   _____ _ __ ")
    print (" | | |_ |/ _` | '_ ` _ \ / _ \ | |  | \ \ / / _ \ '__|")
    print (" | |__| | (_| | | | | | |  __/ | |__| |\ V /  __/ |   ")
    print ("  \_____|\__,_|_| |_| |_|\___|  \____/  \_/ \___|_|   ")
                                                      
#Phase 1
def Phase_1():
    print ("__________")
    print ("        \|")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 2
def Phase_2():
    print ("__________")
    print ("    |   \|")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|" )

#Phase 3
def Phase_3():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 4
def Phase_4():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("    |    |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 5
def Phase_5():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("    |\   |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 6
def Phase_6():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("   /|\   |")
    print ("         |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 7
def Phase_7():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("   /|\   |")
    print ("    |    |")
    print ("         |")
    print ("         |")
    print ("_________|")

#Phase 8
def Phase_8():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("   /|\   |")
    print ("    |    |")
    print ("     \   |")
    print ("         |")
    print ("_________|") 


#Phase 9
def Phase_9():
    print ("__________")
    print ("    |   \|")
    print ("    0    |")
    print ("   /|\   |")
    print ("    |    |")
    print ("   / \   |")
    print ("         |")
    print ("_________|")

def Next_Phase() :
    if Phase == 1 :
        Phase_1()
    if Phase == 2 :
        Phase_2()
    if Phase == 3 :
        Phase_3()
    if Phase == 4 :
        Phase_4()
    if Phase == 5 :
        Phase_5()
    if Phase == 6 :
        Phase_6()
    if Phase == 7 :
        Phase_7()
    if Phase == 8 :
        Phase_8()
    if Phase == 9 :
        Phase_9()

#Varibles

Guess = ()
Phase = (1)
Word_Letters = ""
i = 0
Win = False

#Lists

Letters = []
Numbers = []
Random_Words = ["position","opponent"",poll","straw","fantasy","suffering","height","interest","flexible","pray","relative","passion","employ","include","egg","improve","settle","publicity","balance","coffin","herd","contrast","waste","total","thread","great","variant","increase","age","run","dilute","unfair","smell","cane","register","oh","workshop","dome","charter","am","expertise","fail","remark","lost","inside","feedback","biscuit","spread","lifestyle","systematic"]


#Code
Title()
print()
print()
print()
Word = Random_Words[random.randint(0, 49)]
Next_Phase()
while True:
    print()
    i = 0
    Word_Letters = ""
    Win = True
    while i < len(Word) :
        if Word[i] not in Letters :
            Word_Letters = Word_Letters + "_ "
            Win = False
        else:
            Word_Letters = Word_Letters + Word[i]
        i = i + 1
    print(Word_Letters)
    print()

    if Win == True :
                print()
                You_Win()
                print()
                Reply = ""
                while True:
                    print()
                    Reply = input("Do You Want To Play Again? y or n.  ")
                    print()
                    if Reply == "y" :
                        Word = Random_Words[random.randint(0, 49)]
                        Letters = []
                        Guess = ()
                        Phase = (1)
                        Next_Phase()
                        print()
                        break
                    elif Reply == "n" :
                        print()
                        print("Bye!")
                        exit()
                    else:
                        print("Please Answer y Or n!")
                    Next_Phase()
                else:
                    Next_Phase()
                    Letters.append(Guess)
                    Numbers.append(Word.find(Guess))
                    print (Letters)
                    print (Numbers)
    
    while True:
        Guess = input("Guess a Letter!  ")
        if len(Guess) == 1:
            break
        else:
            print("Please Make It One Letter!")
    if Guess not in Word or Guess in Letters :
        Phase = Phase + 1
        if Phase == 9 :
            Phase_9()
            print()
            Game_Over()
            print()
            while True:
                print()
                print("The Correct Answer Was " + Word + "!")
                print()
                Reply = input("Do You Want To Play Again? y or n.  ")
                print()
                if Reply == "y" :
                    Word = Random_Words[random.randint(0, 49)]
                    Letters = []
                    Guess = ()
                    Phase = (1)
                    #Next_Phase()
                    print()
                    break
                elif Reply == "n" :
                    print()
                    print("Bye!")
                    exit()
                else:
                    print("Please Answer y Or n!")
        Next_Phase()
    else:
        Next_Phase()
        Letters.append(Guess)
        Numbers.append(Word.find(Guess))
