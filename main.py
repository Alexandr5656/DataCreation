import random
import string


class Person:
    
    def init(self,UID ,  USERNAME, PASSWORD,  F_NAME, L_NAME, EMAIL, CREATION_DATE, LAST_ACCESS_DATE):
        self.uid= UID
        self.username = USERNAME
        self.password = PASSWORD
        self.f_name = F_NAME
        self.l_name = L_NAME
        self.email = EMAIL
        self.creation_date = CREATION_DATE
        self.last_access_date = LAST_ACCESS_DATE
        self.friends = []
class Friendship:
    def init(self,FOLLOWER_UID, FOLLOWEE_UID, DATE_FRIENDED):
        self.follow_uid = FOLLOWER_UID
        self.follee_uid = FOLLOWEE_UID
        self.date_friended = DATE_FRIENDED
def createPeople(total):
    people = []
    for i in range (total):
        people.append(Person(getChar8,))

def getChar8():
    varChar = ""
    for i in range (8):
        varChar+=(random.choice(string.ascii_letters))

    return varChar