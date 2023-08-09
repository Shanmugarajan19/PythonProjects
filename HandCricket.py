import math
import random as rd

user = 0
c1 = "dash"
c2 = "dash"
computer = 0
toss = int(input('''

      Enter your toss choice :

      1.Odd
      2.Even


      '''))
res = [1, 2]
cpu = rd.choice(res)
if cpu == toss:
    print("You have won toss")
    c1 = input('''
                    Enter your choice : (Bat/Bowl)
                        ''')
else:
    ch = ["Bat", "Bowl"]
    c2 = rd.choice(ch)
    print(f"Opponent won and Chose to {c2}")
if c1 == "Bat":
    flag = 1
elif c2 == "Bat":
    flag = 2
elif c1 == "Bowl":
    flag = 2
elif c2 == "Bowl":
    flag = 1

if flag == 1:
    while True:
        print("Start To Strike")
        play = int(input("Your Input :     "))
        if play == rd.randint(1, 6):

            target = user + 1
            print(f"You are out and target was {target}")
            break
        else:
            user += play
            print("Current runs : ")
            print(f"USER :  {user}")
            print(f"Computer : {computer}")
    while True:
        print("Start to Bowl")
        cpu = rd.randint(1, 6)
        play = int(input("Your Input : "))
        if cpu == play:
            print("You have won the match")

            break
        else:
            computer += cpu
            if user < computer:
                ("Computer Have Won the Match")
                break
            else:
                run = user - computer + 1
                print("Current runs : ")
                print(f"USER :  {user}")
                print(f"Computer : {computer}")
                print(f"computer needs {run} runs")
else:

    while True:
        print("Start to Bowl")
        cpu = rd.randint(1, 6)
        play = int(input("Your Input : "))
        if cpu == play:

            target = computer + 1
            print(f"Computer was out and target was {target}")
            break
        else:
            computer += cpu
            print("Current runs : ")
            print(f"USER :  {user}")
            print(f"Computer : {computer}")

    while True:
        print("Start to Bat")
        play = int(input("Your Input : "))
        if play == rd.randint(1, 6):
            print("You are out!!!")
            break
        else:
            user += play
            if user > computer:
                ("You Have Won the Match")
                break
            else:
                run = computer - user + 1
                print(f"You need {run} runs")
                print("Current runs : ")
                print(f"USER :  {user}")
                print(f"Computer : {computer}")
