print("Welcome, this is khalid's and russel's project for IT II, our project is a quiz which tests user's on their knowlege of our school, GEMS, would you like to begin?")
print("")
start = input("type yes if you would like to begin the quiz: ")

def question_1():
    print("When was our school founded?")
    print("a: 1991")
    print("b: 2000")
    print("c: 2014")
    print("d: 2018")
    
def question_2():
    print("Who is the current principle of our school?")
    print("a: Eamonn Gregory")
    print("b: Mark Lentz")
    print("c: Engy Carniglia")
    print("d: Thomas Griffith")
    
def question_3():
    print("Who originally founded the Gems corporation")
    print("a: Engy Carniglia")
    print("b: Jeffrey Wessel")
    print("c: Mark Lentz")
    print("d: Sunny Varkey")
    
def question_4():
    print("In which city was the first Gems school built?")
    print("a: Riyadh")
    print("b: Dubai")
    print("c: Doha")
    print("d: Ranni")
    
def question_5():
    print("What does GEMS stand for?")
    print("a: Global Education Management System")
    print("b: Guiding Education in Math and Science")
    print("c: Global Enterprise Management Solutions")
    print("d: Global Expatriate Management System")
    
def question_6():
    print("How many different nationalities of students are there in GEMS")
    print("a: 50+")
    print("b: 78+")
    print("c: 126+")
    print("d: 204+")

def question_7():
    print("What curriculum does our school follow?")
    print("a: Canadian")
    print("b: American")
    print("c: British")
    print("d: Armenian")
    
def question_8():
    print("What is our schools mascot name?")
    print("a: Riaders")
    print("b: Raptors")
    print("c: Falcons")
    print("d: Eagles")
    
def question_9():
    print("Which street is our school on?")
    print("a: Mian street")
    print("b: Nasser Bin Jassim")
    print("c: Al Wakrah")
    print("d: Al Majada")
    
def question_10():
    print("What does AAQ stand for?")
    print("a: Armenian Academy Qatar")
    print("b: Azeraiani Academy Qatar")
    print("c: American Academy Qatar")
    print("d: Austrailian Academy Qatar")

if start == "yes":
    question_1()
    answer_here_1 = input("Enter Answer: ")
    if answer_here_1 == "c":
        print("Correct!")
    else:
        print("Incorrect, the answer is c, GEMS AAQ was established in 2014")

    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_2()
        answer_here_2 = input("Enter Answer: ")
        if answer_here_2 == "b":
            print("Correct")
        else:
            print("Incorrect, the answer is b, the current principle of our school is Mark Lentz")
    
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_3()
        answer_here_3 = input("Enter Answer: ")
        if answer_here_3 == "d":
            print("Correct")
        else:
            print("Incorrect, the answer is d, the original founder of the GEMS corporation is Sunny Varkey")

    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_4()
        answer_here_4 = input("Enter Answer: ")
        if answer_here_4 == "b":
            print("Correct")
        else:
            print("Incorrect, the answer is b, the fist GEMS school was founded in Dubai")
            
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_5()
        answer_here_5 = input("Enter Answer: ")
        if answer_here_5 == "a":
            print("Correct")
        else:
            print("Incorrect, the answer is a, GEMS stands for Global Education Management System")
             
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_6()
        answer_here_6 = input("Enter Answer: ")
        if answer_here_6 == "b":
            print("Correct")
        else:
            print("Incorrect, the answer is b, there are 78+ nationalities in our School")
             
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_7()
        answer_here_7 = input("Enter Answer: ")
        if answer_here_7 == "b":
            print("Correct")
        else:
            print("Incorrect, the answer is b, our schools curriculum is american")
             
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_8()
        answer_here_8 = input("Enter Answer: ")
        if answer_here_8 == "b":
            print("Correct")
        else:
            print("Incorrect, the answer is b, our school mascots are the raptors")
             
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_9()
        answer_here_9 = input("Enter Answer: ")
        if answer_here_9 == "a":
            print("Correct")
        else:
            print("Incorrect, the answer is a, our school is on Mian street")
             
    next = input("type yes if you would like to continue the quiz: ")
    if next == "yes":
        question_10()
        answer_here_10 = input("Enter Answer: ")
        if answer_here_10 == "c":
            print("Correct")
        else:
            print("Incorrect, the answer is c, AAQ stands for American Academy Qatar")
