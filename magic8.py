import random

question = "Will i become a millionaire?"
random_number = random.randint(1, 9)

print(question)

if question == "":
  print("Please provide a question")
elif random_number == 1:
 print("Magic 8-ball's answer: Yes - definitely")
elif random_number == 2:
  print("Magic 8-ball's answer: It is decidedly so")
elif random_number == 3:
  print("Magic 8-ball's answer: Without a doubt")
elif random_number == 4:
  print("Magic 8-ball's answer: Reply hazy, try again")
elif random_number == 5:
  print("Magic 8-ball's answer: Ask again later")
elif random_number == 6:
  print("Magic 8-ball's answer: Better not tell you now")
elif random_number == 7:
  print("Magic 8-ball's answer: My sources say no")
elif random_number == 8:
  print("Magic 8-ball's answer: Outlook not so good")
elif random_number == 9:
  print("Magic 8-ball's answer: Very doubtful")
else:
  answer = "Error"


