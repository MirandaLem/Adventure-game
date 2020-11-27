#game beginning
have_ruler = False
print("Welcome to When the Leaves Fall in the Spring")
print("...")
name = input("Please Enter your Name: ")
print()
print(f"Nice to meet you, {name} ")

print("Are you ready to start the game?")

print()

print("[yes] lets start the game!")
print("[no] maybe another day")

choice = input("Enter choice: ")
if choice == "yes":
    print("Let's get going then!")
elif choice == "no":
    print("Too bad so sad, see you next time then")
print()
print("Day 1: First day of school")
print("Your tired...")
choice = input("[1] Get up or [2] go back to bed? : ")
if choice == "1":
    print("you made it to school early")
    happiness = 1
    likeability = 1
elif choice == "2":
    print("your 10 mins late to class and made a bad impression")
    happiness = -1
    likeability = -1

print()
print("Your stats updated!:")
print(f"happiness:{happiness}")
print(f"Likeability:{likeability}")
print()
print(
    "Note --> Some questions will upgrade your stats depending on your response! If you have high stats the mystery level will be easier to get through! -"
)

print("...")

print("Its hard being the new kid...")
print(
    "you miss your old friends and dread meeting new ones.  But who knows this time may be different"
)
print()
print("Room 253...Homeroom")

if choice == "1":
    print(
        "You walk into the classroom and notice one student looking out the window and your new teacher typing something on her computer"
    )

    print()
    print("Who would you like to talk to?")
    print()
    print("[1] The teacher")
    print("[2] The student")
    choice2 = input("Enter choice: ")
    if choice2 == "1":
        print("You walk over to the teachers desk and greet her")
    elif choice2 == "2":
        print("You walk over to your new classmate and to say hello")
        print(
            "you notice she is mumbling to herself, you cant quite makeout what shes saying and only hear"
        )
        print("< unknown classmate > ...I don't want...")
        print(
            "you lightly tap her on the shoulder and she jumps up. You've surpised her."
        )
        print(f"< {name} > I'..m sorry, I didn't mean to surprise you >")
        print("< unknown classmate > Who are you? Your not in this class.")
        print(f"< {name} > I'm..I'..m {name}, I'm the new transfer student")
        print("< Rebecca > I'm Rebecca...Welcome to hell >")
        print("< Teacher > REBECCA!")
        print("Rebecca quickly sits down and turns towards the class")
        print(
            f"< Teacher > Welcome {name}, you'll be in the last window seat. Ummm you will be next to Carter, he'll show you around the school and be sure to bother him if you have any questions."
        )
        print(
            "You walk to your seat and slowly students start filling up the class"
        )
        happiness = 1
        likeability = 2
        print()
        print("Your stats update!: ")
        print(f"happiness: {happiness}")
        print(f"likeability: {likeability}")

    if choice2 == "1":
        print("You walk over to the teachers desk")
        print(
            f"< {name} > Hello, I'm {name} I'm the new transfer student. I'll be joining your class."
        )
        print(
            "She looks up from her computer, looks up and down your body, and then sits up"
        )
        print(
            "< Teacher > Your in the last window seat, you'll be next to Carter he'll be giving you a tour of the school after class. Please bother him if you have any questions"
        )
        print("You walk over to your desk and sit down")
        print("The class slowly starts filling up with students")
    elif choice == "2":
        print("You walk into class and everyone turns around to look at you")
        print(
            f"< Teacher > You must be the new student, your late miss {name}. Please sit in the last window seat please so we can start class."
        )
        print("You walk over to your seat and sit down")

print()

print(
    "< Carter > Hi I'm Carter! I'll be your class buddy to get you aquainted here"
)
print("[1] Ignore him")
print("[2] Tell carter to be quiet or you guys might get in trouble")
print("[3] Introduce yourself and thank him")
choice3 = input("Enter choice: ")
print()

if choice3 == "1":
    print("You ignore him and look away")
    print("Carter is offended and turns back to the front of the desk")
    happiness = -1
    likeability = -2
    print("Your stats update!: ")
    print(f"happiness: {happiness}")
    print(f"likeability: {likeability}")
    print("Oh no! you gained -1 likeability")
elif choice3 == "2":
    print(
        f"< {name} > please don't talk to me during the lesson I don't wanna get in more get in trouble "
    )
    print("< Carter > Oh ok sorry to bother to you, talk to you after class")
    happiness = -1
    likeability = -0.5
    print("your stats updated!: ")
    print(f"happiness: {happiness}")
    print(f"likeability: {happiness}")
    print("You only gained half a likeability point")
elif choice3 == "3":
    print(
        f"< {name} > Nice to meet you Carter, I'm {name}. Happy to have you help me"
    )
    print("< Carter > Anytime, *winks*.")
    happiness = 1
    likeability = 1
    print("Your stats update!: ")
    print(f"happiness: {happiness}")
    print(f"likeability: {likeability}")
    print("Congrats! You gained 2 happiness and 2 likeability points")
print()
print(
    "Carter takes you on a tour of the school you and Carter talk and find out you guys have lots in common."
)
print()
#day1completion
print("Congrats you finished Day 1: First day of school!")
print("Now on to the next chapter of your adventure...")

print()

question = input("Please Type [yes] if you would like to continue the game: ")
print()
if question == "yes":
    print("Day 2: The Dread of Meeting New people")
print(
    "Note --> Today you will have to interact and meet the whole class! You can also use today to improve your relationship with the classmate you met yesterday! Goodluck you'll need it hehe"
)

print()

print(
    "As you enter the school you notice Carter waiting for you in front of the class, Carter notices you and waves to you"
)
print(f"< Carter > Good Morning {name}!")
choice4 = input(
    "Do wish to ask Carter why he he is waiting outside the door? [yes] or [no]: "
)
print()
if choice4 == "yes":
    print(f"<{name}> Good morning Carter!")
    print(f"Why are you out here? Is the class door locked?")
    print(
        "<Carter> I was waiting for you I thought I'd walk in with you *smiles*"
    )
else:
    print(f"<{name}> Good morning Carter!")
    print(
        "Your curious as to why hes waiting here for you but were to nervous to ask"
    )
    print("<Carter> Shall we go in?")

print()

print(
    "You follow Carter into the class...but you notice the classroom is empty...where are all the desks...the teacher...the students"
)
print(
    "You hear the door slam behind you and turn around to find Carter with his head drooped down, his bag slowly slip from his shoulder down to the gound. \n He bends down and opens his bag revealing a knife"
)
print()
print(f"<{name}> Carter?! What are you doing?? Why do you have??")
print()
print(
    "Emergency Notification!! THE GAME HAS BEEN CORRUPTED BY AN UNKNOWN VIRUS PLEASE EXIT THE GAME IMMEDIA*&^&@^%&#$&^&"
)
print()
print(
    "<UnknownEntity> To leave the game please survive Carters attacks to the best of your ability, best of luck to you subject 09"
)
print()
print("Carter raises his hand with the knife in it")
print()
print("[1] dodge to the left or [2] dodge to right")
choice5 = input("Enter choice within 5 seconds: ")
if choice5 == "1":
    print(
        "You dodged his attack but he cuts your arm leaving a deep painful gash"
    )
    print("You need something to stop the bleed or you may bleed out!")
    print("[1] Rip your clothing, safest but most time consuming option")
    print("[2] Jump for his bag, there may be stuff to help me in there.")
    print("[3] Endure it, doing anything now may be risky")
    choice6 = input("Enter choice within 5 seconds: ")
    if choice6 == "1" or choice6 == "3" or choice6 == "2":
        print("Carter stabs you and the system wins")
        print("Game over")
else:
    print("You successfully dodged his attack")
    print()
    print
    ("You realize you need something to block his attacks with. You cannot keep on dodging forever ")
    print("You find a long metal ruler near the chalk board")
    choice7 = input("Would you like to pick it up? [yes] or [no]: ")
    if choice7 == "yes":
        print("You picked up the ruler")
        have_ruler = True
    else:
            print("Carter stabs you to death. \n The system wins. \n Game Over")

if have_ruler == True:
    print("You have blocked all of Carters attack! You have tired out the system successfully! \n You have won the game!! \n <UnknownEntity> Thank you for playing a little game with my creation Carter, it was quite fun to watch. Till next time subject 09.")
    #Game End
