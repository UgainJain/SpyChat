name = input("What's your spy name??")  # name
if len(name)>0 :
    print("Yay, the name is good.")
    Salutation = input("What would be your spy salutation, Mr. ,Mrs or Ms.")   # salutation
    full_name = Salutation + " " + name
    print("Alright " + full_name + ", I would like to know little more about you....")
    age = int( input("what's your age?" ))
    if 20 < age < 50: #age
        print("Alright,")
        rating = float(input("whats ur Spy rating??")) # rating
        if 2.5 <= rating < 3.5:
            print(" U can always do better")
        elif 3.5 <= rating < 4.5:
            print("Yup, you are one of good ones")
        elif rating >= 4.5:
            print("Ooo, thts an ace")
        else:
            print("We can always use somebody to help in the office.")
        ol= bool(input("Are u online???"))# online or not
        if ol != False:
             print("Authentication complete, welcome" + Salutation + " " + name + " with age ")
             print(repr(age) + " and rating of " + repr(rating) + " Proud to have u you on board")
        else:
            print("  ")
    else:
        print("Sorry you are not of the correct age to be a spy")
else:
    print("This name is not valid please try with a better name")
