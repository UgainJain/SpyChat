# name = "Ugain jain"
# salutation = "Mr."
# full_name = salutation + " "+ name
# age = 21
# rating = 3.8
# status = "Crazy me...."

#  spy = {"name": "Ugain", "Salutation": "Mr", "age": 21, "Rating": 3.8, "Status": "CRazy mee...."}
from datetime import datetime


class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:

    def __init__(self, message, sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy("Ugain jain", "Mr.", 21, 4)
friend_one = Spy('Raja', 'Mr.', 27, 4.9)
friend_two = Spy('Mata Hari', 'Ms.', 21, 4.39)
friend_three = Spy('No', 'Dr.', 37, 4.95)