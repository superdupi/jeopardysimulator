from Tkinter import *

masterQ = [a, b, c, d, e, f]

Q = ['q1', 'q2', 'q3', 'q4', 'q5']
A = ['a1', 'a2', 'a3', 'a4', 'a5']

index = 0
for letter in masterQ:
    letter = Q[index]
    index += 1

for letter in masterQ:
    print letter
    
def display():
    print Q[qNum]

root = Tk()

mainCanvas = Canvas(root, bg='black', width=500, height=500)
 
    

mainCanvas.pack()

mainloop()
