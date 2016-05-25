##  Import all the modules needed for this assignment, namely Tkinter, SQLite, and Random
from Tkinter import *
import random
import sqlite3
conn = sqlite3.connect('jeopardy.db')
c = conn.cursor()
root = Tk()
root.configure(bg="black")
root.wm_title("Let's Play Jeopardy!")


##  A class for quit buttons, which appear in every popup.
class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self['bg'] = "#040072"
        self['fg'] = "white"
        self.pack(side=BOTTOM, fill=BOTH)

        
##A randomizer tools that takes two lists with matching objects per index and
##    shuffles these lists while maintaining pairing. This is used to randomize
##    question/answer lists
def randomizer(A, B):
    temp1 = []        
    temp2 = []        
    index_shuf = range(len(A))
    random.shuffle(index_shuf)
    for i in index_shuf:
        temp1.append(A[i])
        temp2.append(B[i])
    for i in range(len(A)):
        A[i] = temp1[i]
        B[i] = temp2[i]   


##A function that creates a pop-up for questions in the "X" column (X is a number
##    given in the function name). It does this by creating a toplevel, and on this
##    toplevel, it creates a label widget, with the text defined within the function.
##    This text is given by taking the first element from Answer List X, and then
##    deleting this first element after assignment. There also exists a quit button.
def Cat1An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat1A[0]
    Answer = Label(aCanvas, width=60, bg="#0e07c5", fg="white", font=(None, 15), height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat1A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat2An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat2A[0]
    Answer = Label(aCanvas, width=60, bg="#0e07c5", fg="white", font=(None, 15), height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat2A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat3An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat3A[0]
    Answer = Label(aCanvas, width=60, bg="#0e07c5", fg="white", font=(None, 15), height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat3A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat4An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat4A[0]
    Answer = Label(aCanvas, width=60, bg="#0e07c5", fg="white", font=(None, 15), height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat4A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat5An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=2000, height=1000, bg='black')
    currentAnswer = Cat5A[0]
    Answer = Label(aCanvas, width=60, bg="#0e07c5", fg="white", font=(None, 15), height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat5A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)

##masterQuestion is responsible for creating the primary pop-up which reveals the question
##    upon clicking a button on the main board. It takes in 'index' as an argument, and this
##    index is responsible for obtaining information from the correct list. Since each column
##    contains five buttons, and there are 25 buttons in all, the category in question is defined
##    in sequences of five starting from 0 (eg. An index of 0-4 would be category 1, while 15-19
##    would be category 3. When called, it takes the index, and sets the variable "currentQuestion"
##    as the first element of the proper Question List. After assigning a value to this variable,
##    it deletes this first element, and also creates a button calling the correct command for an 
##    answer popup.Subsequently, a label displaying "currentQuestion" in this toplevel, along with
##    a quit button. "masterQuestion" also uses the index to search through the button list for the
##    button in position index and disables it, so this button cannot be reclicked on the main board.

def masterQuestion(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black')
    if index < 5:
        currentQuestion = Cat1Q[0]
        Cat1Q.pop(0)
        showAnswer = Button(qCanvas, bg="#040072", fg="white", text="Reveal Answer", command=Cat1An)
    if index >= 5 and index < 10:
        currentQuestion = Cat2Q[0]
        Cat2Q.pop(0)
        showAnswer = Button(qCanvas, bg="#040072", fg="white", text="Reveal Answer", command=Cat2An)
    if index >= 10 and index < 15:
        currentQuestion = Cat3Q[0]
        Cat3Q.pop(0)
        showAnswer = Button(qCanvas, bg="#040072", fg="white", text="Reveal Answer", command=Cat3An)
    if index >= 15 and index < 20:
        currentQuestion = Cat4Q[0]
        Cat4Q.pop(0)
        showAnswer = Button(qCanvas, bg="#040072", fg="white", text="Reveal Answer", command=Cat4An)
    if index >= 20:
        currentQuestion = Cat5Q[0]
        Cat5Q.pop(0)
        showAnswer = Button(qCanvas, bg="#040072", fg="white", text="Reveal Answer", command=Cat5An)
    Question = Label(qCanvas, width=60, height=7, bg="#0e07c5", fg="white", font=(None, 15), text=currentQuestion)
    Question.pack(fill=BOTH)
    showAnswer.pack(fill=BOTH)
    quitButton(toplevel)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

##These are lists that will be filled with elements from the database. The first
##    is a list of Category Names, while the remaining are 5 pairs of question and
##    answer lists, one for each column on the main board.

CategoryNames = []
Cat1Q = []
Cat1A = []
Cat2Q = []
Cat2A = []
Cat3Q = []
Cat3A = []
Cat4Q = []
Cat4A = [] 
Cat5Q = []
Cat5A = []


##After executing the SQL that obtains each row in the table TESTJEOPARDY, we cycle through
##    each row and check the category name. If the category name does not exist in list
##    "CategoryNames" (which is initially empty), it adds the name to the list. Once completed,
##    the list "CategoryNames" is shuffled.
cursor = conn.execute("SELECT qnum, catagory, cqnum, question, answer FROM TESTJEOPARDY")
for row in cursor:
    if row[2] not in CategoryNames:
        CategoryNames.append(row[2])        
random.shuffle(CategoryNames)


##We execute the same SQL command again, and cycle through each row once again. This time,
##    we check to see if the current row's category name matches the first 5 elements in
##    the randomized list "CategoryNames". If it is a match, the question and answer of the
##    row are added to the appropriate list. This fills all 10 columns once we cycle through
##    every row.
cursor = conn.execute("SELECT qnum, catagory, cqnum, question, answer FROM TESTJEOPARDY")
for row in cursor:
    if CategoryNames[0] == row[2]:
        Cat1Q.append(row[3])
        Cat1A.append(row[4])
    if CategoryNames[1] == row[2]:
        Cat2Q.append(row[3])
        Cat2A.append(row[4])
    if CategoryNames[2] == row[2]:
        Cat3Q.append(row[3])
        Cat3A.append(row[4])
    if CategoryNames[3] == row[2]:
        Cat4Q.append(row[3])
        Cat4A.append(row[4])
    if CategoryNames[4] == row[2]:
        Cat5Q.append(row[3])
        Cat5A.append(row[4])

##After filling in our 10 lists, we want to randomize them so that we get different questions
##    every new game. Because we created the list with each question's answer having a matching
##    index, it is important to maintain index syncronization. To do this, we use the "randomizer"
##    function, explained above.
randomizer(Cat1Q, Cat1A)
randomizer(Cat2Q, Cat2A)
randomizer(Cat3Q, Cat3A)
randomizer(Cat4Q, Cat4A)
randomizer(Cat5Q, Cat5A)


##We create five labels, one by one, by taking the first element of list "CategoryNames" and assigning
##    it to variable "CatName". We create the label using "CatName" as text, and then we delete the
##    first element. 
for index in range(5):
    CatName = CategoryNames[0]
    label = Label(root, text=CatName, bg="#0e07c5", fg="yellow", font=(None, 15), width=20, height=4)
    CategoryNames.pop(0)
    label.grid(padx=2, pady=2, row=1, column=index)


##Before creating the buttons, we create an empty list for the buttons. This list will be used to disabale
##    clicked buttons. We also have a variable called "qValue", which is used as text for the buttons. It
##    represents the points the question is worth, and increases by 200 until we reach a new column, where
##    it reverts back to 200. We cycle through a range of 25 and create a button, calling masterQuestion,
##    which takes in the current index within range 25. This index represents the position of the button in
##    the list, and each new button is added to this list the end of each loop.
buttons = []
qValue = 0
for index in range(25):
    qValue += 200
    if qValue > 1000:
        qValue = 200
    button = Button(root, bg="#0e07c5", fg="white", text=qValue, font=(None, 15), width=20, height=4, relief=GROOVE, command=lambda index=index: masterQuestion(index))
    button.grid(padx=2, pady=2, row=((index%5)+5), column=(index/5))
    buttons.append(button)


root.mainloop()
