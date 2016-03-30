import sqlite3
conn = sqlite3.connect('jeopardy.db')
c = conn.cursor()
def read_db():
    c.execute('SELECT * FROM TESTJEOPARDY')
    for row in c.fetchall():
        print(row)

print "Opened database successfully"

read_db()

##conn.execute('DROP TABLE TESTJEOPARDY')
##print "Table deleted!"
##
##conn.execute('''CREATE TABLE TESTJEOPARDY
##    (QNUM INT PRIMARY KEY NOT NULL,
##    CQNUM INT,
##    CATAGORY CHAR(50),
##    QUESTION CHAR(100),
##    ANSWER CHAR(50));''')
##
##print "Table created successfully"
##
##quesNum = 1
##catQuesNum = 1
##response = 'y'
##CAT = raw_input("Insert first catagory: ")
##
##while response == 'y':
##    print "Current catagory is: ", CAT
##    newCat = raw_input("New Column?: (y/n)")
##    while newCat != 'y' and newCat != 'n':
##        newCat = raw_input("Incorrect response, try again: (y/n): ")
##    if newCat == 'y':
##        catQuesNum = 1
##        CAT = raw_input("Enter new catagory name: ")
##    QUES = raw_input("Enter the question: ")
##    ANS = raw_input("Enter answer: ")
##
##    conn.execute('INSERT INTO TESTJEOPARDY VALUES (?, ?, ?, ?, ?)', (quesNum, CAT, catQuesNum, QUES, ANS))
##    conn.commit()
##    print "Row has been added!"
##    print
##
##    quesNum = quesNum + 1
##    catQuesNum = catQuesNum + 1
##    while response != 'y' and response != 'n':
##        response = raw_input("Incorrect response, input again: (y/n): ")

cursor = conn.execute("SELECT qnum, catagory, cqnum, question, answer FROM TESTJEOPARDY")

for row in cursor:
    print "QUESTION NUMBER ", row[0]
    print "CATAGORY: ", row[1]
    print "CATAGORY QUESTION ", row[2]
    print "QUESTION: ", row[3]
    print "ANSWER: ", row[4]
    print

print "Operation done successfully"
