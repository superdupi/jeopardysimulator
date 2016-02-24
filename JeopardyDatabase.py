import sqlite3
conn = sqlite3.connect('jeopardy.db')
print "Opened database successfully"


##conn.execute('DROP TABLE TESTJEOPARDY')
##print "Table deleted!"

conn.execute('''CREATE TABLE TESTJEOPARDY
    (QNUM INT PRIMARY KEY NOT NULL,
    CATAGORY CHAR(50),
    QUESTION CHAR(100),
    ANSWER CHAR(50));''')

print "Table created successfully"


q = 1
response = 'y'
while response == 'y':
    CAT = raw_input("Enter the catagory of your question: ")
    QUES = raw_input("Enter the question: ")
    ANS = raw_input("Enter answer: ")
    
    conn.execute('INSERT INTO TESTJEOPARDY VALUES (?, ?, ?, ?)', (q, CAT, QUES, ANS))
    conn.commit()
    print "Row has been added!"
    print
    
    q = q + 1
    response = raw_input("Add another row? (y/n): ")
    while response != 'y' and response != 'n':
        response = raw_input("Incorrect response, input again: (y/n): ")

cursor = conn.execute("SELECT qnum, catagory, question, answer FROM TESTJEOPARDY")

for row in cursor:
    print "QUESTION NUMBER ", row[0]
    print "CATAGORY: ", row[1]
    print "QUESTION: ", row[2]
    print "ANSWER: ", row[3]
    print

print "Operation done successfully"

