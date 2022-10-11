print("Welcome to SQL (BASIC) Quiz")

playing = input("Do you want to play?  ")

if playing.lower()!= "yes":
    quit()
print("Okay !Let's play :) ")
score = 0 
answer = input("Q1) What does SQl stand for? ")
if answer.lower() =='structured query language':
    print('Correct! :)')
    score +=1
else :
    print('WRONG!')

answer = input("Q2) What does DML stand for? ")
if answer.lower() =='data manapulation language' :
    print('Correct! :)')
    score +=1
else :
    print('WRONG!')

answer = input("Q3) What does TCL stand for? ")
if answer.lower() =='transaction control language' :
    print('Correct! :)')
    score +=1
else :
    print('WRONG!')

answer = input("Q4) CURD stands for ? ")
if answer.lower() =='create update read delete' :
    print('Correct! :)')
    score +=1
else :
    print('WRONG!')

answer = input("Q5) What does RDMS stand for? ")
if answer.lower() =='relational database management system' :
    print('Correct! :)')
    score +=1
else :
    print('WRONG!')


print("You got " + str(score) + " Questions correct !")
print("You got " + str((score/4)*100) + "%.")