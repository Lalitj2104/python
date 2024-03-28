import time
import pyfiglet
word=pyfiglet.figlet_format("welcome To The Quiz")
print(word)
print()

name=input("Enter your name:")
email=input("Enter your mail id: ")
score=0
question=0
cq=0
wq=0
while True:
    time.sleep(1)
    print("starting......")
    time.sleep(1)
    
    print('''Q1) What will be the output of the following Python code snippet?

                a={1:"A",2:"B",3:"C"}
                print(a.setdefault(3))

                a) {1: ‘A’, 2: ‘B’, 3: ‘C’}
                b) C
                c) {1: 3, 2: 3, 3: 3}
                d) No method called setdefault() exists for dictionary''')
    ans1=input("Enter your answer:")
    if ans1=="b":
        print("correct answer")
        score=score + 2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
        
    time.sleep(1)
    print('''Q2) Who developed Python Programming Language?
                a) Wick van Rossum
                b) Rasmus Lerdorf
                c) Guido van Rossum
                d) Niene Stom''')
    ans2=input("Enter your answer:")
    if ans2=="c":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
        
    time.sleep(1)
    print('''Q3)Is Python code compiled or interpreted?
                a) Python code is both compiled and interpreted
                b) Python code is neither compiled nor interpreted
                c) Python code is only compiled
                d) Python code is only interpreted''')
    ans3=input("Enter your answer:")
    if ans3=="a":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
        
    time.sleep(1)
    print('''Q4)Which of the following is the correct extension of the Python file?
                a) .python
                b) .pl
                c) .py
                d) .p ''')
    ans4=input("Enter your answer:")
    if ans4=="c":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)   
    print('''Q5)What will be the output of the following Python code?

                            i = 1
                            while True:
                                if i%3 == 0:
                                        break
                                print(i)
 
                            i + = 1

            a) 1 2 3
            b) error
            c) 1 2
            d) none of the mentioned ''')
    ans5=input("Enter your answer:")
    if ans5=="b":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)   
    print('''Q6)Which of the following is the correct extension of the Python file?
                a) .python
                b) .pl
                c) .py
                d) .p ''')
    ans6=input("Enter your answer:")
    if ans6=="c":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)   
    print('''Q7)What is the maximum possible length of an identifier in Python?
            a) 79 characters
            b) 31 characters
            c) 63 characters
            d) none of the mentioned''')
    ans7=input("Enter your answer:")
    if ans7=="d":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)
    print('''Q8)Which of the following statements is used to create an empty set in Python?
            a) ( )
            b) [ ]
            c) { }
            d) set()''')
    ans8=input("Enter your answer:")
    if ans8=="d":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)
    print('''Q9)Which function is called when the following Python program is executed?

                f = foo()
                format(f)

            a) str()
            b) format()
            c) __str__()
            d) __format__()''')
    ans9=input("Enter your answer:")
    if ans9=="c":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    time.sleep(1)
    print('''Q10)What will be the output of the following Python function?
    min(max(False,-3,-4), 2,7)

            a) -4
            b) -3
            c) 2
            d) False''')
    ans10=input("Enter your answer:")
    if ans10=="d":
        print("correct answer")
        score=score+2
        question+=1
        cq+=1
    else:
        print("wrong answer")
        question+=1
        wq+=1
        break
    
   
else:
    print("pls try again")
print("Total question attempted:",question)
print("number of correct answer:",cq)
print("number of wrong answer",wq)
print("total score:",score)
