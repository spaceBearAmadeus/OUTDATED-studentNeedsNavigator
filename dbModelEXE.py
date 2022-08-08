from dbModel import Product

#create a new instance of Product() that connects to the database="Students_2022.db"
db = Product(database=('Students_2022.db'))
#prints a sentence that states which database we are connected to!
print(repr(db))

#a list of commands that are available to you
command_list = ['create', 'insert', 
                'drop', 'read', 'quit']

#a menu that allows you to see your options
def getCommand():
    command = input(f"Hi! Please enter a command({command_list}): ")
    return command

#instantiate a new command for our model:
command = getCommand()

while True and command != "quit":
    try:
        #GOING TO MAKE THIS MORE DYNAMIC BY BEING ABLE TO SELECT ANYY TABLE NOT JUST STUDENTS0822!!##
        if command == "create":
            selection = input("Please enter the name of the Table you would like to create: ")
            #the db object has a method called createNewStudentTable() that we are using to create a new table called 'students_0822' within Students_2022.db....this is made possible by the cur attribute within the Product() class!
            db.createNewStudentTable(selection)
            command = getCommand()
        
        if command == "insert":
            selection = input("Please enter the name of the Table you would like to insert into: ")
            #func that creates a tuple of TEXT and REAL that are the y axes of the student info!
            def getItemInfo():
                name = input("Please enter Student Name: ")
                instrument = input("Please enter the Instrument that the student is studying: ")
                lesson_time = int(input("Please enter the Lesson Time for this student: "))
                day_of_study = input("Please enter the Day of Study for this student: ")
                student_age = int(input("Please enter the Age of this student: "))
                lesson_comments = input("Please enter any comment you have about this student: ")
                status = int(input("Please enter how well you think it is going with this Student(1(worst) - 5(best): "))
                item_info = (name, 
                            instrument, 
                            lesson_time, 
                            day_of_study, 
                            student_age, 
                            lesson_comments,
                            status)
                return item_info
            #instantiate a new row(student) with information as a tuple 
            new_item_info = getItemInfo()
            db.insert(table=(selection), item=new_item_info)
            command = getCommand()
            
        if command == "drop":
            selection = input("Please type in table that you would like to drop: ")
            db.dropTable(table_to_drop=(selection))
            command = getCommand()
            
        if command == "read":
            selection = input("Please type in table that you would like to read: ")
            how_many = input("How much would you like to read?(one, many, all): ")
            db.read(table=(selection), data=(how_many))
            command = getCommand()
    except:
        if command not in command_list:
            print("That is not valid.  Please enter a valid option: ")
            command = getCommand()
                
        
#prints a sentence that states which database we are connected to!
#print(repr(db))
