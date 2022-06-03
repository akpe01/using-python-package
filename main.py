
b = True
while b == True:
    h = ["R", "P", "S"]
    print("starting game")
    print("this is a rock, paper or scissors game")
    print("enter R for rock, P for paper or S for scissors")
    a = input("select R, P, or S: ")
    for letter in a:
        if letter in h:
            continue
 
        
    import random
    computer_choice = random.choice(h)
    print("your choice is: ", a)
    print("computer_choice is: ", computer_choice)
    if a == computer_choice:
        print("its tie")
    elif a == "R" and computer_choice == "P" :
        print("computer wins")
    elif a == "P" and computer_choice == "R" :
        print("congratulation you win")
    elif a == "R" and computer_choice == "S" :
        print("congratulation you win")
    elif a == "S" and computer_choice == "R" :
        print("computer wins")
    elif a == "P" and computer_choice == "S" :
        print("computer wins")
    elif a == "S" and computer_choice == "P" :
        print("congratulation you wins")
    elif a not in h:
        print("wrong input")
    print("do u want to play again, yes or no")
    c=input("enter yes to continue or no to end: ")
    if c == "yes":
        continue
    else:
        print("no to end")
    break
print("goodbye")
    
    
    
    