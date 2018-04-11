from steganography.steganography import Steganography
import csv
from spy_details import Spy, ChatMessage

STATUS_MESSAGES = ['Crazy me...', ' Mandir wahin banaenge...', 'lol']
Friends = []


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
            print("Please enter a valid status...")  # invalid status
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
    Name = raw_input("Whats your friend spy name?")
    Salutation = raw_input("what would be the salutation, Mr. or Mrs??")
    age = int(raw_input("what is friends age?"))
    Rating = float(raw_input("what's your friend spy rating??"))
    if len(Name) > 0 and 12 < age < 50:  # add friend
        spy1 = Spy(Name, Salutation, age, Rating)
        Friends.append(spy1)
        with open('friends.csv', 'a') as friends_data:
            writer = csv.writer(friends_data)
            writer.writerow([spy1.name, spy1.salutation, spy1.rating, spy1.age, spy1.is_online])

    else:  # invalid details
        print("Sorry we can't add your friend's details please try again")
    return len(Friends)


def select_a_friend():
    item_no = 0
    if len(Friends) != 0:
        for friend in Friends:
            print("%d . %s" % (item_no + 1, friend.name))
            item_no = item_no + 1
        friend_no = int(raw_input("Select your Friend : "))
        if friend_no <= len(Friends) and friend_no != 0:
            print("You selected %d no Friend" % friend_no)
            return friend_no - 1
        else:
            print("Wrong raw_input, plz try again......")
    else:
        print("Sorry no Friend added till now, plz add a friend first.... ")
        friend_no = add_friend()
        print("No. of Friends : %d" % friend_no)
        select_a_friend()


def send_massage(spy_name):
    selection = select_a_friend();
    image = raw_input(" Name of image to be encoded :")
    out_path = "ac3.jpg"
    text = raw_input("what text do you want to encode :")
    Steganography.encode(image, out_path, text)
    print("Message sent... ")
    chat = ChatMessage(spy_name=spy_name, friend_name=Friends[selection].name, message=text, sent_by_me=True)
    with open('chats.csv', 'a') as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([spy_name, Friends[selection].name, text, True])
    Friends[selection].chats.append(chat)



def read_message(spy_name):
    selection = select_a_friend()
    image = raw_input("Name of image to be decoded : ")
    text = Steganography.decode(image)
    chat = ChatMessage(spy_name=spy_name, friend_name=Friends[selection].name, message=text, sent_by_me=True)
    Friends[selection].chats.append(chat)
    with open('chats.csv', 'a') as chat_data:
        writer = csv.writer(chat_data)
        writer.writerow([spy_name, Friends[selection].name, text, False])
    print(text)


def print_chats(spy_name):
    selection = select_a_friend()
    friendname = str(Friends[selection].name)
    from termcolor import colored
    with open('chats.csv', 'rb') as chat_data:
        read2 = csv.reader(chat_data)
        for row in read2:
            chats = ChatMessage(spy_name=row[0], friend_name=row[1], message=row[2], sent_by_me=row[3])
            print type(chats.friend_name), type(friendname)
            frend = str(chats.friend_name)
            print(frend, friendname)
            if frend == friendname:
                if chats.sent_by_me == True:
                    print colored(spy_name, 'red')
                    print colored("On time :" + chats.time, 'blue')
                    print("Message" + chats.message)
                elif chats.sent_by_me is False:
                    print colored(Friends[selection].name, 'red')
                    print colored("On time : if c" + chats.time, 'blue')
                    print("Message" + chats.message)
            else:
                print("no chat found")


def load_Friends():
    with open('friends.csv', 'rb') as friends_data:
        read = csv.reader(friends_data)
        for row in read:
            spy = Spy(name=row[0], salutation=row[1], rating=float(row[2]), age=int(row[3]))
            Friends.append(spy)
    with open('chats.csv', 'rb') as chat_data:
        read2 = csv.reader(chat_data)
        for friend in range(len(Friends)):
            for row in read2:
                chat = ChatMessage(spy_name=row[0], friend_name=row[1], message=row[2], sent_by_me=row[3])
                Friends[friend].chats.append(chat)


def spy_chat(spy_name, spy_salutation, spy_age):
    show_menu = True
    current_status_message = None
    while show_menu:
        print("What do you want to do?")
        menu_choices = "1. Add a status update \n2. Add a friend  \n3. Send message \n4. Read a message \n5. Print " \
                       "chat \n6. Exit the Application " \
                       "\nInput :- "
        menuchoice = raw_input(menu_choices)
        if menuchoice == "1":
            current_status_message = add_status(current_status_message)
        elif menuchoice == "2":
            no = add_friend()  # no of friends returned
            print("No of friends : %d" % no)
        elif menuchoice == "3":
            send_massage(spy_name)
        elif menuchoice == "4":
            read_message(spy_name)
        elif menuchoice == "5":
            print_chats(spy_name)
        elif menuchoice == '6':
            print("QUITTING....")
            show_menu = False

        else:
            print("invalid input")
            pass


user = raw_input("Do you want to continue with the default user ?(Y/N)")

if user.upper() == 'Y':

    from spy_details import spy

    print('Welcome,%s  %s with %d years of age and %.1f rating. Welcome to SpyChat.... ' %
          (spy.salutation, spy.name, spy.age, spy.rating))
    load_Friends()

elif user.upper() == "N":
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
            print("Authentication complete, welcome " + full_name + " with age " + repr(age) + " and rating of " + repr(
                rating) + " Proud to have u you on board")
            spy = Spy(name, salutation, age, rating)
        else:
            print("Sorry you are not of the correct age to be a spy")
            exit()
    else:
        print("This name is not valid please try with a better name")
else:
    print("You chose an invalid option . Plz run again......")

spy_chat(spy.name, spy.salutation, spy.age)
