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


def spy_chat():
    show_menu = True
    current_status_message = None
    while show_menu:
        print("What do you want to do?")
        menu_choices = "1. Add a status update \n2. Add a friend  \n3. Exit the Application\nInput :- "
        menuchoice = input(menu_choices)
        if menuchoice == "1":
            current_status_message = add_status(current_status_message)
        elif menuchoice == "2":
            no = add_friend()# no of friends returned
            print("No of friends : %d" % no)
        elif menuchoice== '3':
            print("QUITTING....")
            show_menu = False

        else:
            print("invalid input")
            pass



def add_status(current_status_message):
    if current_status_message is not None:
        print("Your current status is  : %s" % current_status_message)
    else:
        print("You don't have any status right now")
    default =input( "Do you want to select from the previous status??(Y/N)")
    if default.upper() == 'N':
        new_status_message = input("Which status you want to set ??")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message# updates status
            STATUS_MESSAGES.append(updated_status_message) # Entered in the list
        else:
            print("Please enter a valid status...")#invalid status
            updated_status_message = current_status_message # assign previous status
    elif default.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print("%d . %s" % (item_position, message))
                item_position = item_position + 1
            menu_selection = int(input("What is your desired status?"))
            if len(STATUS_MESSAGES) >= menu_selection:
                updated_status_message = STATUS_MESSAGES[menu_selection - 1]# set desired status
            else:
                print("invalid input...")
                updated_status_message = current_status_message # assign previous status
    else:
        print("invalid input")
        pass
    return updated_status_message



def add_friend():
    new_name  = input("Whats your friend spy name?")
    new_salutation =input("what would be the salutation, Mr. or Mrs??")
    new_name = new_salutation + " " + new_name
    new_age = int(input("what is friends age?"))
    new_rating = float(input("what's your friend spy rating??"))
    if len(new_name)>0 and 12 < new_age < 50: ### add friend
        Friend_name.append(new_name)
        Friend_age.append(new_age)
        Friend_rating.append(new_rating)
        Friend_status.append(True)
    else:     ##invalid details
        print("Sorry we can't add your friend's details please try again")
    return len(Friend_name)



user = input("Do you want to continue with the default user ?(Y/N)")
new_user = 0
if user.upper() == 'Y':

    from spy_details import name
    from spy_details import salutation
    from spy_details import age
    from spy_details import rating
    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to spychat.... ' %
          (salutation, name, age, rating))
else:
    new_user = 1
    entry()
STATUS_MESSAGES =['Crazy me...', 'Mandir wahin banaenge...', 'lol']
Friend_name = []
Friend_age = []
Friend_rating = []
Friend_status = []
spy_chat()