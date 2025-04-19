print("""
                       ===================================================================================         
                       =      ===   ===     =======     ======     =======     =======      =======      =
                       =      =   ==  =     =     =     =             =        =            =      =     =
                       =      =       =     =     =     =             =        =            =    =       =
                       =      =       =     =======     ======        =        =======      ====         =
                       =      =       =     =     =          =        =        =            =    =       =
                       =      =       =     =     =          =        =        =            =     =      =
                       =      =       =     =     =     ======        =        =======      =      =     =
                       =                                                                                 =
                       =                                                                                 =
                       =                                                                                 =
                       =                    ===   ===   =======     ==       =    =======                =
                       =                    =   ==  =      =        =  =     =     =     =               =
                       =                    =       =      =        =   =    =     =       =             =
                       =                    =       =      =        =    =   =     =        =            =
                       =                    =       =      =        =     =  =     =       =             =
                       =                    =       =      =        =      = =     =      =              =
                       =                    =       =   =======     =       ==    =======                =
                       =                                                                                 =
                       =                                                                                 =
                       ===================================================================================   """)


print('''                                                       WELCOME TO MASTERMIND


''')
def startup():
    
    print('''                                                       Start---------------->s                                                     ''')
    print('''                                                       How To Play---------->h                                                     ''')
    print('''                                                       About --------------->a                                                     ''')
    print('''                                                       Credits-------------->c                                                     ''')
    print('''                                                       Exit----------------->x                                                     ''')
    
def how():
    e='''					Game Protocols:
			1)At first the four colours will be set in an order.
			2)Player Has to Guess the Combination Of Colours.
			3)You will get to know your progess at the end of each trial.
			4)You have to complete this challenge in a total of 10 trials.
			5)Available colours are red,green,blue,orange,yellow,violet,pink,white,black,grey
						Enjoy The Gaming Experience                                      '''
    return(e)
def crhow():
    cc=['e','n','c']
    print("""Hit
                            c----------------->Continue
                            n----------------->Main Menu
                            e----------------->Exit""")
                     
    j=input("Hit a key to move forward:")
    if j=='c':
        print(level())
    elif j=='e':
        exit()
    elif j=='n':
        startup()
        ch=input("Enter your Choice:---------->")
        minimain(ch)
    elif j not in cc:
        print("Please Enter Correct Choice")
        crhow()

def about():
    
    q='''The modern game with pegs was invented in 1970 by Mordecai Meirowitz, an Israeli postmaster and telecommunications expert.
         It resembles an earlier pencil and paper game called Bulls and Cows that may date back a century or more.
         '''
    return(q)
def cred():
    c='''                                                            CODE CREDITS


                                                        Karthik Mohan, Vasanth Manne
         '''
    return(c)
def correction():
        jj=['m','q']
        p=input("Hit m for main Menu or Hit q to exit:")
        if p=='m':
            startup()
            ch=input("Enter your Choice:---------->")
            minimain(ch)
        elif p=='q':
            exit()
        elif p not in jj:
            print("Please Enter Correct Choice")
            correction()
def easy():
    global n1,n2,n3,n4
    import random
    s=['red','green','blue','orange','yellow','violet','pink','white','black','grey']
    n1 = random.choice(s)
    n2 = random.choice(s)
    n3 = random.choice(s)
    n4 = random.choice(s)
    c = 0
    while True:
    
        colwrong = 0
        guess1 = str(input("guess the first Colour:"))
        guess2 = str(input("guess the second Colour:"))
        guess3 = str(input("guess the third Colour:"))
        guess4 = str(input("guess the fourth Colour:"))
        if guess1 not in s:
            print("Please Enter colour1 Correctly")
        if guess2 not in s:
            print("Please Enter colour2 Correctly")
        if guess3 not in s:
            print("Please Enter colour3 Correctly")
        if guess4 not in s:
            print("Please Enter colour4 Correctly")
            print(easy())
  
        if guess1 != n1:
            colwrong += 1

        if guess2 != n2:
            colwrong += 1

        if guess3 != n3:
            colwrong += 1

        if guess4 != n4:
            colwrong += 1

        if colwrong == 0:
            print('Well Done!')
            print('It took you ' + str(c) + ' ries to guess the number!')
            break
        else:
            print('You got ' + str(4-colwrong) + ' Colour right.')
        c += 1
        if c==5:
            print(lose())
            return(urchoice())

def medium():
    global n1,n2,n3,n4
    import random
    s=['red','green','blue','orange','yellow','violet','pink','white','black','grey']
    n1 = random.choice(s)
    n2 = random.choice(s)
    n3 = random.choice(s)
    n4 = random.choice(s)
    c = 0
    while True:
    
        guess1 = str(input("guess the first Colour:"))
        guess2 = str(input("guess the second Colour:"))
        guess3 = str(input("guess the third Colour:"))
        guess4 = str(input("guess the fourth Colour:"))
        colwrong = 0
        if guess1 not in s:
            print("Please Enter colour1 Correctly")
        if guess2 not in s:
            print("Please Enter colour2 Correctly")
        if guess3 not in s:
            print("Please Enter colour3 Correctly")
        if guess4 not in s:
            print("Please Enter colour4 Correctly")
            print(medium())
    
        if guess1 != n1:
            colwrong += 1

        if guess2 != n2:
            colwrong += 1

        if guess3 != n3:
            colwrong += 1

        if guess4 != n4:
            colwrong += 1

        if colwrong == 0:
            print('Well Done!')
            print('It took you ' + str(c) + ' ries to guess the number!')
            break
        else:
            print('You got ' + str(4-colwrong) + ' Colour right.')
        c += 1
        if c==3:
            print(lose())
            return(urchoice())
def hard():
    global n1,n2,n3,n4
    import random
    s=['red','green','blue','orange','yellow','violet','pink','white','black','grey']
    n1 = random.choice(s)
    n2 = random.choice(s)
    n3 = random.choice(s)
    n4 = random.choice(s)
    c = 0
    while True:
    
        guess1 = str(input("guess the first Colour:"))
        guess2 = str(input("guess the second Colour:"))
        guess3 = str(input("guess the third Colour:"))
        guess4 = str(input("guess the fourth Colour:"))
        colwrong = 0
        if guess1 not in s:
            print("Please Enter colour1 Correctly")
        if guess2 not in s:
            print("Please Enter colour2 Correctly")
        if guess3 not in s:
            print("Please Enter colour3 Correctly")
        if guess4 not in s:
            print("Please Enter colour4 Correctly")
            print(hard())

    
        if guess1 != n1:
            colwrong += 1

        if guess2 != n2:
            colwrong += 1

        if guess3 != n3:
            colwrong += 1

        if guess4 != n4:
            colwrong += 1

        if colwrong == 0:
            print('Well Done!')
            print('It took you ' + str(c) + ' ries to guess the number!')
            break
        else:
            print('You got ' + str(4-colwrong) + ' Colour right.')
        c += 1
        if c==1:
            print(lose())
            return(urchoice())

def lose():
    a='''                                                         Tough time...........Better Luck Next Time
         Hit                                            k------------>To Check exact combinaion
                                                        m------------>Main Menu
                                                        z------------>Exit                              '''
    return(a)
def urchoice():
    p=input("Enter your Choice:")
    zzz=['k','z','m']
    if p=='k':
        crct=['f','m']
        print(n1,n2,n3,n4)
        t='''Hit f to quit the game or Hit m for main menu:'''
        print(t)
        y=input("Enter your Choice:")
        if y=='f':
            exit()
        elif y=='m':
             startup()
             ch=input("Enter your Choice:---------->")
             minimain(ch)
        elif y not in crct:
            print("Please Enter choice correctly")
            urchoice()
    elif p=='z':
        exit()
    elif p=='m':
         startup()
         ch=input("Enter your Choice:---------->")
         minimain(ch)
    elif p not in zzz:
        print("Please enter choice Correctly")
        return(urchoice())
def level():
    print("""EASY--------------->e""")
    print("""Medium------------->m""")
    print("""HARD--------------->h""")
    ll=['e','m','h']
    inp=input("Enter your Choice:")
    if inp=='e':
        print(easy())
    elif inp=='m':
        print(medium())
    elif inp=='h':
        print(hard())
    elif inp not in ll:
        print("Plese enter Correct Choice")
        return level()
    
def minimain(ch):
    kk=['s','a','h','c','x']
    if ch=='s':
        print(level())
    elif ch=='a':
        print(about())
        print(correction())
    elif ch=='h':
        print(how())
        print(crhow())
    elif ch=='c':
        print(cred())
        print(crhow())
    elif ch=='x':
        exit()
    elif ch not in kk:
        print("Please Enter choice Correctly")
        ch=input("Enter your Choice:---------->")
        minimain(ch)
        
startup()
ch=input("Enter your Choice:---------->")
minimain(ch)
