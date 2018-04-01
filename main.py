from steganography.steganography import Steganography
from datetime import datetime


def entry():
    name = raw_input("What's your spy name??")
    if len(name) > 0:
        print("Yay, the name is good.")
        salutation = raw_input("What would be your spy salutation, Mr. ,Mrs or Ms.")
        full_name = salutation + " " + name
        print("Alright " + full_name + ", I would like to know little more about you....")
        age = int(raw_input("what's your age?"))
        if 20 < age < 50:
            print("Alright,")
            rating = float(raw_input("whats ur Spy rating??"))
            if 2.5 <= rating < 3.5:
                print(" U can always do better")
            elif 3.5 <= rating < 4.5:
                print("Yup, you are one of good ones")
            elif rating >= 4.5:
                print("Ooo, thts an ace")
            else:
                print("We can always use somebody to help in the office.")
            ol = bool(raw_input("Are u online???"))
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
        menu_choices = "1. Add a status update \n2. Add a friend  \n3. Send message \n4. Read a message \n5. Exit " \
                       "the " \
                       "Application \nInput :- "

        menuchoice = raw_input(menu_choices)
        if menuchoice == "1":
            current_status_message = add_status(current_status_message)
        elif menuchoice == "2":
            no = add_friend()  # no of friends returned
            print("No of friends : %d" % no)
        elif menuchoice == "3":
            send_massage()
        elif menuchoice == "4":
            read_message()
        elif menuchoice == '5':
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
    default = raw_input("Do you want to select from the previous status??(Y/N)")
    if default.upper() == 'N':
        new_status_message = raw_input("Which status you want to set ??")
        if len(new_status_message) > 0:
            updated_status_message = new_status_message  # updates status
            STATUS_MESSAGES.append(updated_status_message)  # Entered in the list
            print(updated_status_message + " : is now set as your as status")
        else:
            print("Please enter a valid status...")    # invalid status
            updated_status_message = current_status_message  # assign previous status
            print(updated_status_message + " : Remains as your as status")
    elif default.upper() == 'Y':
            item_position = 1
            for message in STATUS_MESSAGES:
                print("%d . %s" % (item_position, message))
                item_position = item_position + 1
            menu_selection = int(raw_input("What is your desired status?"))
            if len(STATUS_MESSAGES) >= menu_selection:
                updated_status_message = STATUS_MESSAGES[menu_selection - 1]  # set desired status
                print(updated_status_message + " : is now set as your as status")  # print desired status
            else:
                print("invalid raw_input...")
                updated_status_message = current_status_message  # assign previous status
    else:
        print("invalid raw_input")
        pass
    return updated_status_message


def add_friend():
    new_friend = {"Name": "", "Salutation": "", "age": 0, "Rating": 0.0, "Chats": []}
    new_friend["Name"] = raw_input("Whats your friend spy name?")
    new_friend["Salutation"] =raw_input("what would be the salutation, Mr. or Mrs??")
    new_friend["Name"] = new_friend["Salutation"] + " " + new_friend["Name"]
    new_friend["age"] = int(raw_input("what is friends age?"))
    new_friend["Rating"] = float(raw_input("what's your friend spy rating??"))
    if len(new_friend["Name"])>0 and 12 < new_friend["age"] < 50:  # add friend
        Friends.append(new_friend)
    else:     # invalid details
        print("Sorry we can't add your friend's details please try again")
    return len(Friends)


def select_a_friend():  # select friends from the list
    item_no = 0
    if len(Friends) != 0:
        for friend in Friends:
            print("%d . %s" % (item_no+1, friend["Name"]))
            item_no = item_no + 1
        friend_no = int(raw_input("Select your Friend : "))
        if friend_no <= len(Friends) and friend_no != 0:
            print("You selected %d no Friend" % friend_no)
            return friend_no-1
        else:
            print("Wrong raw_input, plz try again......")
    else:
        print("Sorry no Friend added till now, plz add a friend first.... ")
        friend_no = add_friend()
        print("No. of Friends : %d" % friend_no)
        select_a_friend()


def send_massage():  # sends the message to selected friend
    selection = select_a_friend()
    image = "ac1.jpg"
    out_path = "ac3.jpg"
    text = raw_input("what text do you want to encode :")
    Steganography.encode(image, out_path, text)
    text = "You : " + text
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "send_by_me": True
    }

    print("Message sent... ")

    Friends[selection]["Chats"].append(new_chat)


def read_message():  # reads the message received from the friend
    selection = select_a_friend()

    image = "ac3.jpg"
    text = Steganography.decode(image)
    text = Friends[selection]["Name"] + " : " + text
    new_chat = {
        "message": text,
        "time": datetime.now(),
        "send_by_me": False
    }
    Friends[selection]["Chats"].append(new_chat)
    print(text)


user = raw_input("Do you want to continue with the default user ?(Y/N)")
new_user = 0
if user.upper() == 'Y':

    from spy_details import spy

    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to SpyChat.... ' %
          (spy["Salutation"], spy["name"], spy["age"], spy["Rating"]))
else:
    new_user = 1
    entry()
STATUS_MESSAGES = ['Crazy me...', ' Mandir wahin banaenge...', 'lol']
Friends = []
spy_chat()
