from main import Student, Session, engine, Base 
'''######################################################'''


"""#this autocreates a table based on the params"""
Base.metadata.create_all(engine)

"""#use sqlalchemy to connect to postgres and add student info"""
local_session = Session(bind=engine)

"""#new batch to be inserted"""
new_student_batch1 = [
                      ('Cal Moffe', 'piano', 'cell', 600, 'W', 60, 'driven, perceptive', 5),
                      ('Mason Miller', 'guitar', 'contact thru store', 300, 'T', 8, 'creative, personable', 4.5),
                      ('Emma Miller', 'piano', 'contact thru store', 330, 'T', 6, 'creative, redirection', 3)
                      ]  

"""#empty container for user input and quick transport"""
batch_container = []

"""#Navigator class for extra functionality for batch inserts!"""
class Navigator(Student):
    #method for batch inserting that iterates over batch list
    def batch_insert(self,  batch_info):
        for name, instrument, contact, time, day, age, keywords, favorability in batch_info:
            student = Student(name=name, instrument=instrument, contact_info=contact, lesson_time=time, 
                              day_of_study=day, age=age, keyword_comments=keywords, 
                              status=favorability)
            local_session.add(student)
        local_session.commit()
    
    #method that prompts user to add info to batch_list    
    def add_new_row_to_batch(self, batch):
        name = input("Student's name: ")
        inst = input("Instrument: ")
        contact = input("Method of contact: ")
        time = int(input("Time of lesson: "))
        day = input("Lesson day: ")
        age = int(input("Age: "))
        keywords = input("Any keywords to describe student: ")
        status = int(input("How well is it going with this student?(1lowest-5highest): "))
        new_student_info = (name, inst, contact, time, day, age, keywords, status)
        batch.append(new_student_info)
        return batch


"""#critical child used to traverse client user actions..inherits StudentsFall2022 which also inherits declarative_base()"""
nav = Navigator()

"""HARDCODED BATCH MIXED WITH USER INPUT FOR DB INSERT"""
#user prompted to ADD a new entry to batch that already has data inside
#nav.add_new_row_to_batch(batch=new_student_batch1)
#batch insert into db
#nav.batch_insert(batch_info=new_student_batch1)

"""
IF YOU DO NOT HAVE EVERY FEATURE REQUIRED FOR BATCH INSERT, 
USE THE METHOD BELOW TO INDIVIDUALLY ADD STUDENT WITH n FEATURES
"""
#new_student = Student(name='Marian C', instrument='piano', keyword_comments='driven, planning, loyal')
#local_session.add(new_student)
#local_session.commit()


"""MULTIPLE USER INPUTS INTO EMPTY BATCH CONTAINER PER BATCH INSERT"""
#chain user being prompted for new info
#nav.add_new_row_to_batch(batch=batch_container)
#nav.add_new_row_to_batch(batch=batch_container)
#nav.batch_insert(batch_info=batch_container)

