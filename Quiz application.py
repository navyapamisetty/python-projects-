#Source Code For Quiz Application Using Python

questions=("1)Which type of Programming does python supports?",
          "2)All Keywords in python are ______",
          "3)What will be the value of the expression ---> 23+7%10",
          """4)           i=1
           while True:
           if i%3 == 0:
            break
            print(i)
           i + = 1
What is the output""",
          "5)What will be the output for the code --> x<<2",
          """6)What is the output of the following code-
a=[1,0,2,0,'Python','',[]]
list(filter(bool,1))""",
           """7)What will be the output of the following code if x=56.236-->
print("%.2f"%x) """,
           """8)What will be the output of the following  code-->
x='abcd'
for i in range(len(x)):
  print(i)""",
           "9)What will be the output of the following code--> round(4.576)",
           """10)What will be the output of the following code
print("Hello {0[0]} and {0[1]}".format(('foo','bin')))?""" )
options=(("A. Object Oriented Prog", "B. Structured Oriented ", "C. Functional Oriented", "D. All of mentioned"),
         ("A. Capitalized", "B.Lowercase ", "C. Uppercase" , "D. None of the mentioned"),
         ("A. 27", "B. 30", "C. 31", "D. 29"),
         ("A. 12", "B. 123", "C. Syntax error", "D.None of the above"),
         ("A. 4", "B. 2", "C. 1", "D. 8"),
         ("A. [1,0,2,'Python','',[]] " ,"B. Error" ,"C. [1,2,'Python']" , "D. [1,0,2,0,'Python','',[]]"),
         ("A. 56.236", "B. 56.23", "C. 56.0000", "D. 56.24"),
         ("A. Syntax error", "B. 0 1 2 3", "C. a b c d", "D. a b c"),
         ("A. 5", "B. 4.6", "C. 4", "D. 4.5"),
         ("A. Hello f and o", "B. Error", "C. Hello foo and bin", "D. Hello ('foo','bin') and ('foo','bin')"))
         

answers=("D", "D", "B", "C", "A" , "C" ,"D", "B" ,"A" ,"C")
guesses = []
score = 0
question_num = 0

for question in questions:
   print("---------------------------")
   print(question)
   for option in options[question_num]:
       print(option)
   guess = input("Enter (A, B, C, D):").upper()
   guesses.append(guess)
   if guess==answers[question_num]:
        score+=1
        print("CORRECT!")
   else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
   question_num += 1

print("-------------------------")
print("      RESULTS           ")
print("-------------------------")

print("answers:", end=" ")

for answer in answers:
  print(answer, end=" ")
print()

print("guesses:", end=" ")

for guess in guesses: 
  print(guess, end=" ")
print()
"""print("Your score is ",score,"/",len(questions))
if score== len(questions):
   print("Excellent.All are correct")
elif score>=len(questions)-1:
   print("Good You done a great job")
elif score>=len(questions)-3:
   print("Keep it up to get good result")
elif score>=len(questions)-5:
   print("Improve urself for better results")
elif score>=len(questions)-7:
   print("Practise daily for more improvement")
else:
   print("Your result is very low.Practise more to improve your technical skills")"""

print("Your score is ",score,"/",len(questions))
score_per=int(score/len(questions)*100)
print("Result= ",score_per,"%");
if score_per== 100:
   print("Excellent.All are correct")
elif score_per>=90:
   print("Good You done a great job")
elif score_per>=75:
   print("Keep it up to get good result")
elif score_per>=50:
   print("Improve urself for better results")
elif score_per>=30:
   print("Practise daily for more improvement")
else:
   print("Your result is very low.Practise more to improve your technical skills")
