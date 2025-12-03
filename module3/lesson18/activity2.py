class flashcard:
    def __init(self,word,meaning):
        self.word=word
        self.meaning=meaning
    def __str__(self):
        #we will return to a nstring
        return self.word+'()'+self.meaning+')'
flash=[]
print("welcome to flashcard application")
#the following loop will be repeated until
#user stops to add the flashcards
while(True):
    word=input("enter the name you want to add to flashcard")
    meaning=input("enter the meaning of thw word")
    flash.append(flashcard(word,meaning))
    option=int(input("enter0,if you want to add another flashcard otherwise enter1:"))
    if(option):
        break
#printing all the flashcards
print("\nYour flashcards")
for i in flash:
    print(">",i)