from Tkinter import *

root = Tk()
root['bg'] = 'light yellow'
gameBoard = Canvas(root, width=560, height=430, bg='black')

Qs = ['1q1', '1q2', '1q3', '1q4', '1q5', '2q1', '2q2', '2q3', '2q4', '2q5', '3q1', '3q2', '3q3', '3q4', '3q5', '4q1', '4q2', '4q3', '4q4', '4q5', '5q1', '5q2', '5q3', '5q4', '5q5']
As = ['1a1', '1a2', '1a3', '1a4', '1a5', '2a1', '2a2', '2a3', '2a4', '2a5', '3a1', '3a2', '3a3', '3a4', '3a5', '4a1', '4a2', '4a3', '4a4', '4a5', '5a1', '5a2', '5a3', '5a4', '5a5']


class QAButton(Button):##max 25
    idCounter = 0
    def __init__(self, parent, num):
        Button.__init__(self, parent)
        self['text'] = Qs[QAButton.idCounter]
##        self['text'] = 'Question {0}'.format(QAButton.idCounter)
        self['command'] = DisplayQuestion
        self.QAnum = x
        self.pack()
        QAButton.idCounter += 1
    def QAnum(self):
        return self.QAnum
    
def DisplayQuestion():
    print QAButton.idCounter

x = 0

for question in Qs:
    QAButton(gameBoard, x)
##    questions = Button(gameBoard, text=x, command=DisplayQuestion)
##    questions.pack()
    print Qs[x], As[x], x
    x = x + 1





gameBoard.pack(side=LEFT, expand=YES, fill=BOTH)

mainloop()
