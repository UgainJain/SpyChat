def entry():
    name = input("What's your spy name??")
    if len(name) > 0:
        print("Yay, the name is good.")
        salutation = input("What would be your spy salutation, Mr. ,Mrs or Ms.")
        full_name = salutation + " " + name
        print("Alright " + full_name + ", I would like to know little more about you....")
        age = int(input("what's your age?"))
        if 20 < age < 50:
            print("Alright,")
            rating = float(input("whats ur Spy rating??"))
            if 2.5 <= rating < 3.5:
                print(" U can always do better")
            elif 3.5 <= rating < 4.5:
                print("Yup, you are one of good ones")
            elif rating >= 4.5:
                print("Ooo, thts an ace")
            else:
                print("We can always use somebody to help in the office.")
            ol = bool(input("Are u online???"))
            if ol == False:
                print("Authentication complete, welcome " + full_name + " with age " + repr(age) + " and rating of " + repr(rating) + " Proud to have u you on board")
            else:
                print("  ")
        else:
            print("Sorry you are not of the correct age to be a spy")
            exit()
    else:
        print("This name is not valid please try with a better name")


def spy_chat(new):
    i = 0
    while i < 5:
        print("What do you want to do?")
        menu_choices = "1. Add a status update \n2. Exit the Application \nInput :- "
        menuchoice = input(menu_choices)
        if menuchoice == "1":
            if new == 0:
                from spy_details import status
                print("Your current status is  : %s" % status)    # displays your current status
            elif new == 2:
                print("your status is : %s" % status) #displays status of new user
            else:
                print("Add ur status :")  # ask for a new status 
                status = input()
                print("Your status is - %s" % status)
                new = 2
            i = i+1
        elif menuchoice == "2":
            print("QUITTING....") # quits the program
            exit()
        else:
            i = i+1
            pass


user = input("Do you want to continue with the default user ?(Y/N)")
new_user = 0
if user == 'Y':

    from spy_details import name
    from spy_details import salutation
    from spy_details import age
    from spy_details import rating
    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to spychat.... ' %
          (salutation, name, age, rating))
else:
    new_user = 1
    entry() #######TAKES DETAILS OF A NEW USER

spy_chat(new_user)