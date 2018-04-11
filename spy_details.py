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
    def __init__(self, spy_name, friend_name, message, sent_by_me):
        self.spy_name = spy_name
        self.friend_name = friend_name
        self.message = message
        self.sent_by_me = sent_by_me
        self.time = datetime.now()


spy = Spy("Ugain", "Mr.", 21, 4)