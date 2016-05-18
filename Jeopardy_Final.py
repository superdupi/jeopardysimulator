from Tkinter import *
import random
import sqlite3
conn = sqlite3.connect('jeopardy.db')
c = conn.cursor()
root = Tk()

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM, fill=BOTH) 

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

def Cat1An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat1A[0]
    Answer = Label(aCanvas, width=60, height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat1A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat2An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat2A[0]
    Answer = Label(aCanvas, width=60, height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat2A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat3An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat3A[0]
    Answer = Label(aCanvas, width=60, height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat3A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat4An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat4A[0]
    Answer = Label(aCanvas, width=60, height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat4A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat5An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=2000, height=1000, bg='black')
    currentAnswer = Cat5A[0]
    Answer = Label(aCanvas, width=60, height=7, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat5A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def masterCatQu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black')
    if index < 5:
        currentQuestion = Cat1Q[0]
        Cat1Q.pop(0)
        showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat1An)
    if index >= 5 and index < 10:
        currentQuestion = Cat2Q[0]
        Cat2Q.pop(0)
        showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat2An)
    if index >= 10 and index < 15:
        currentQuestion = Cat3Q[0]
        Cat3Q.pop(0)
        showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat3An)
    if index >= 15 and index < 20:
        currentQuestion = Cat4Q[0]
        Cat4Q.pop(0)
        showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat4An)
    if index >= 20:
        currentQuestion = Cat5Q[0]
        Cat5Q.pop(0)
        showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat5An)
    Question = Label(qCanvas, width=60, height=7, text=currentQuestion)
    Question.pack(fill=BOTH)
    showAnswer.pack(fill=BOTH)
    quitButton(toplevel)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

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


cursor = conn.execute("SELECT qnum, catagory, cqnum, question, answer FROM TESTJEOPARDY")

currentCat = 0
currentQues = 0
for row in cursor:
    if row[2] not in CategoryNames:
        CategoryNames.append(row[2])
        
random.shuffle(CategoryNames)


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


randomizer(Cat1Q, Cat1A)
randomizer(Cat2Q, Cat2A)
randomizer(Cat3Q, Cat3A)
randomizer(Cat4Q, Cat4A)
randomizer(Cat5Q, Cat5A)

labels = []
for index in range(5):
    CatName = CategoryNames[0]
    label = Label(root, text=CatName, bg="light grey", width=20, height=6)
    CategoryNames.pop(0)
    label.grid(padx=2, pady=2, row=1, column=index)
    labels.append(label)

buttons = []
qValue = 0
for index in range(25):
    qValue += 200
    if qValue > 1000:
        qValue = 200
    button = Button(root, bg="white", text=qValue, width=20, height=6, relief=GROOVE, command=lambda index=index: masterCatQu(index))
    button.grid(padx=2, pady=2, row=((index%5)+5), column=(index/5))
    buttons.append(button)


root.mainloop()
