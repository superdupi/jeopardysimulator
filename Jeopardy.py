from Tkinter import *
import random
import sqlite3
conn = sqlite3.connect('jeopardy.db')
c = conn.cursor()
root = Tk()
print "Opened database successfully"

class quitButton(Button):
    def __init__(self, parent):
        Button.__init__(self, parent)
        self['text'] = 'Quit'
        self['command'] = parent.destroy
        self.pack(side=BOTTOM, fill=BOTH) 

def Cat1An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat1A[0]
    Answer = Label(aCanvas, width=22, height=6, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat1A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat2An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat2A[0]
    Answer = Label(aCanvas, width=22, height=6, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat2A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat3An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat3A[0]
    Answer = Label(aCanvas, width=22, height=6, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat3A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat4An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=800, height=500, bg='black')
    currentAnswer = Cat4A[0]
    Answer = Label(aCanvas, width=22, height=6, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat4A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    

def Cat5An():
    answerlevel = Toplevel(bg='green')
    aCanvas = Canvas(answerlevel, width=2000, height=1000, bg='black')
    currentAnswer = Cat5A[0]
    Answer = Label(aCanvas, width=22, height=6, text=currentAnswer)
    Answer.pack(fill=BOTH)
    Cat5A.pop(0)
    quitButton(answerlevel)
    aCanvas.pack(side=LEFT, expand=YES, fill=BOTH)    


def Cat1Qu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black')
    currentQuestion = Cat1Q[0]
    Question = Label(qCanvas, width=22, height=6, text=currentQuestion)
    Question.pack(fill=BOTH)
    Cat1Q.pop(0)
    showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat1An)
    showAnswer.pack(fill=BOTH)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

def Cat2Qu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black') 
    currentQuestion = Cat2Q[0]
    Question = Label(qCanvas, width=22, height=6, text=currentQuestion)
    Question.pack(fill=BOTH)
    Cat2Q.pop(0)
    showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat2An)
    showAnswer.pack(fill=BOTH)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

def Cat3Qu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black') 
    currentQuestion = Cat3Q[0]
    Question = Label(qCanvas, width=22, height=6, text=currentQuestion)
    Question.pack(fill=BOTH)
    Cat3Q.pop(0)
    showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat3An)
    showAnswer.pack(fill=BOTH)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

def Cat4Qu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black') 
    currentQuestion = Cat4Q[0]
    Question = Label(qCanvas, width=22, height=6, text=currentQuestion)
    Question.pack(fill=BOTH)
    Cat4Q.pop(0)
    showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat4An)
    showAnswer.pack(fill=BOTH)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

def Cat5Qu(index):
    toplevel = Toplevel(bg='blue')
    qCanvas = Canvas(toplevel, width=800, height=500, bg='black') 
    currentQuestion = Cat5Q[0]
    Question = Label(qCanvas, width=22, height=6, text=currentQuestion)
    Question.pack(fill=BOTH)
    Cat5Q.pop(0)
    showAnswer = Button(qCanvas, text="Reveal Answer", command=Cat5An)
    showAnswer.pack(fill=BOTH)
    qCanvas.pack(side=LEFT, expand=YES, fill=BOTH)
    buttons[index].config(state="disabled")

CategoryNames = []
##CategoryNames = ['Music', 'Comp Sci', 'The Walking Dead', 'Breaking Bad', 'Marvel']

##Cat1Q = []
##Cat1A = []
##Cat2Q = []
##Cat2A = []
##Cat3Q = []
##Cat3A = []
##Cat4Q = []
##Cat4A = [] 
##Cat5Q = []
##Cat5A = []

Cat1Q = ['MusicQ1', 'MusicQ2', 'MusicQ3', 'MusicQ4', 'MusicQ5']
Cat1A = ['MusicA1', 'MusicA2', 'MusicA3', 'MusicA4', 'MusicA5']
Cat2Q = ['CompSciQ1', 'CompSciQ2', 'CompSciQ3', 'CompSciQ4', 'CompSciQ5']
Cat2A = ['CompSciA1', 'CompSciA2', 'CompSciA3', 'CompSciA4', 'CompSciA5']
Cat3Q = ['WalkingDeadQ1', 'WalkingDeadQ2', 'WalkingDeadQ3', 'WalkingDeadQ4', 'WalkingDeadQ5']
Cat3A = ['WalkingDeadA1', 'WalkingDeadA2', 'WalkingDeadA3', 'WalkingDeadA4', 'WalkingDeadA5']
Cat4Q = ['BreakingBadQ1', 'BreakingBadQ2', 'BreakingBadQ3', 'BreakingBadQ4', 'BreakingBadQ5']
Cat4A = ['BreakingBadA1', 'BreakingBadA2', 'BreakingBadA3', 'BreakingBadA4', 'BreakingBadA5']
Cat5Q = ['MarvelQ1', 'MarvelQ2', 'MavelQ3', 'MarvelQ4', 'MarvelQ5']
Cat5A = ['MarvelA1', 'MarvelA2', 'MavelA3', 'MarvelA4', 'MarvelA5']
cursor = conn.execute("SELECT qnum, catagory, cqnum, question, answer FROM TESTJEOPARDY")

for row in cursor:
    if row[2] not in CategoryNames:
        CategoryNames.append(row[2])
for cat in CategoryNames:
    print cat

random.shuffle(CategoryNames) 
labels = []
for index in range(5):
    CatName = CategoryNames[0]
    label = Label(root, text=CatName, bg="light grey", width=20, height=6)
    CategoryNames.pop(0)
    label.grid(padx=2, pady=2, row=1, column=index)
    labels.append(label)

# A collection (list) to hold the references to the buttons created below
buttons = []
qValue = 0
for index in range(25):
    qValue += 200
    if qValue > 1000:
        qValue = 200
    if index < 5:
        button = Button(root, bg="white", text=qValue, width=20, height=6, relief=GROOVE,
                    command=lambda index=index: Cat1Qu(index))
    if index >= 5 and index < 10:    
        button = Button(root, bg="White", text=qValue, width=20, height=6, relief=GROOVE,
                    command=lambda index=index: Cat2Qu(index))
    if index >= 10 and index < 15:    
        button = Button(root, bg="White", text=qValue, width=20, height=6, relief=GROOVE,
                    command=lambda index=index: Cat3Qu(index))
    if index >= 15 and index < 20:    
        button = Button(root, bg="White", text=qValue, width=20, height=6, relief=GROOVE,
                    command=lambda index=index: Cat4Qu(index))
    if index >= 20:    
        button = Button(root, bg="White", text=qValue, width=20, height=6, relief=GROOVE,
                    command=lambda index=index: Cat5Qu(index))
    # Add the button to the window
    button.grid(padx=2, pady=2, row=((index%5)+5), column=(index/5))

    # Add a reference to the button to 'buttons'
    buttons.append(button)


root.mainloop()
