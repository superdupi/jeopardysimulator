from tkinter import *

def startGame():
    startButton.pop()
    AnswerA = Button(gameStats, text='A:___')
    AnswerA.pack(fill=X)

    AnswerB = Button(gameStats, text='B:___')
    AnswerB.pack(fill=X)

    AnswerC = Button(gameStats, text='C:___')
    AnswerC.pack(fill=X)

    AnswerD = Button(gameStats, text='D:___')
    AnswerD.pack(fill=X)
    

root = Tk()
root['bg'] = 'light yellow'

gameBoard = Canvas(root, width=560, height=400, bg='blue')

gameBoard.create_rectangle(10, 10, 110, 75, fill='red')
gameBoard.create_rectangle(120, 10, 220, 75, fill='red')
gameBoard.create_rectangle(230, 10, 330, 75, fill='red')
gameBoard.create_rectangle(340, 10, 440, 75, fill='red')
gameBoard.create_rectangle(450, 10, 550, 75, fill='red') 


gameStats = Frame(root, width=300, height=400)

playerName = Label(gameStats, text='Welcome to Jeopardy!')
playerName.pack()

startButton = Button(gameStats, text='Start Game', command=startGame)
startButton.pack(fill=X)




gameBoard.pack(side=LEFT, expand=YES, fill=BOTH)
gameStats.pack(side=RIGHT, expand=YES, fill=BOTH)

mainloop()
