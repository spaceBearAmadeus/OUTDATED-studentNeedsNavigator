import pandas as pd 
import connectionDetails as cd 
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, DateTime, Integer, Float, create_engine 
from datetime import datetime
import os 
'''#######################################################'''


'''#method used to create an f string containing the sqlalchemy conn string
    required to connect to postgress via sqlalchemy.create_engine()'''
def define_connection(dialect_and_driver, username, password, host, port, db_name):
    connection_string = f"{dialect_and_driver}://{username}:{password}@{host}:{port}/{db_name}"
    return connection_string

'''#instance of a correctly formmated sqlalchemy conn string using admin logindetails'''
CONNECTION = define_connection(cd.conn_type, cd.username, cd.pwd, 
                               cd.hostname, cd.port_id, cd.db_name)

'''#that which pertains to a database in sqla'''
Base = declarative_base()
'''#that which interacts with postgres and base, think cursor()'''
engine = create_engine(CONNECTION, echo=True)

'''# 
class Student
    name varchar(40) PRIMARY KEY,
    instrument varchar(40) NOT NULL,
    lesson_time int,
    day_of_study varchar(40),
    age int,
    date_started datetime,
    keyword_comments varchar(100),
    status float
#'''
#################################
#################################
'''#
Student object dedicated to the creation of tables, inserting of rows, and manipulation of 
    SQL to all things pertaining to this program's STUDENTS(the target content!)...
    ...user=Teacher, target=Students...as time goes on, simply change the __tablename__

Below is a custom instance of Base, that uses all of it's sql interaction methods,
    but has params that are inherent to the table you will be interacting with
    within the desired db(db is defined in the CONNECTION variable)#'''
class Student(Base):
    #this is a class that inherits from the base instance of declarative_base()...
    #...it is a holder of attributes that pertains to a TABLE...declarative base is a TABLE CREATOR!
    #this method represents these params as *args, **kwargs!!
    __tablename__="Students_Summer_2022", 
    name = Column(String(25), primary_key=True)
    instrument = Column(String(25), nullable=False)
    contact_info = Column(String(40))
    lesson_time = Column(Integer())
    day_of_study = Column(String(25))
    age = Column(Float())
    date_entered = Column(DateTime(), default=datetime.utcnow)
    keyword_comments = Column(String(50))
    status = Column(Float())
    
    def __repr__(self):
        return f"<Student: {self.name}, {self.instrument}, {self.contact_info}, {self.lesson_time}, {self.day_of_study}, {self.age}, {self.date_entered}, {self.keyword_comments}, {self.status}>"

'''#instantiate sessionmaker'''
Session = sessionmaker(engine)

'''#######################################################'''
'''########################END###########################'''