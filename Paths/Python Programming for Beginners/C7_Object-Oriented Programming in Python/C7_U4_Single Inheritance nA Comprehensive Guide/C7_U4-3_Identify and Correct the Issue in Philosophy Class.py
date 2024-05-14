class Academia:
    
    def __init__(self, subject):
        self.subject = subject

    def lecture(self):
        print("Lecture on ", self.subject, " is going on.")

class Philosophy(Academia):

    def change_topic(self, new_subject):
        self.subject = new_subject
        print("Discussion topic has changed to ", self.subject)

subject = Philosophy("Metaphysics")
subject.lecture()
subject.change_topic("Ethics")
subject.lecture()