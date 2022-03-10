def displayMenu():
    print("what would you like to do?")
    print("\t(a) Add new student")
    print("\t(v) View students")
    print("\t(q) Quit")
    choice = input("Type one letter (a/v/q):").strip()

    return choice

def doAdd():
    print("in adding")  
def doView():
    print("in viewning") 

choice = displayMenu()
while(choice != 'q'):
    if choice == 'a':
        doAdd()
    elif choice == 'v':
        doView()
    elif choice != 'q':
        print ("\n\nplease select either a,v or q")
    choice=displayMenu()        


choice = displayMenu () 
print("you chose {}".format(choice))  

students=[]
def readmodules():
    return{}

def doAdd(students):
    currentStudents = {}
    currentStudents["name"]=input("enter name:")
    currentStudents["modules"]=readmodules()

    students.append (currentStudents)

doAdd(students)
doAdd(students) 
print(students)   

