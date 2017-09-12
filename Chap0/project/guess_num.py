import random

tag=random.randint(0,20)
i=0
j=0
while i<10 and j==0:
    in1=input("could you guess the number?\n")
    if in1.isdigit():
        g=int(in1)
        if g<tag:
             print("What you guess is too small\n")
             i+=1
        elif g>tag:
             print("What you guess is too large\n")
             i+=1
        elif g==tag:
            j=1
            print("OK, you got it!")
    else:
        print("Please input a integer number!")
