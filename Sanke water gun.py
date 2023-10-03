import random
player = ["Snake" , "Water" , "Gun"]
computer = random .choice(player)
computer_point=0
player_point=0



while True:
    u=input("You have to chose Play a game or Exit a game : ")
    if "play" == u.lower():
        playerin = int(input("Snake : 1 ,Water : 2 , Gun : 3 = "))
        if playerin == 1:
            playerin = "Snake"
        elif playerin == 2:
            playerin = "Water"
        elif playerin == 3:
            playerin = "Gun"
        else:
            print("Enter valid input?")
        print(computer)
        if playerin == computer:
            print("Draw")
        if playerin != computer:
            if playerin =="Gun":
                if computer !="Water":
                    print("You won the  One point : 1")
                    player_point+=1
                else:
                    print("Computer get the point")
                    computer_point+=1
        if playerin != computer:
            if playerin =="Snake":
                if computer !="Gun":
                    print("You won the  One point : 1")
                    player_point+=1
                else:
                    print("Computer get the point")
                    computer_point+=1
        if playerin != computer:
            if playerin =="Water":
                if computer !="Snake":
                    print("You won the  One point : 1")
                    player_point+=1
                else:
                    print("Computer get the point")
                    computer_point+=1
    else:
        print("Play soon😊")
        print(player_point)
        print(computer_point)
        exit()

