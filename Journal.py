from main import Journal, Session, engine, Base 
import pandas as pd
import numpy as np
'''######################################################'''

"""this is the connection details for this script interacting with db"""
CONNECTION = 'postgresql://postgres:07141989@localhost:5432/my_coding_journey'

"""#this autocreates a table based on the params"""
Base.metadata.create_all(engine)

"""#use sqlalchemy to connect to postgres and add student info"""
local_session = Session(bind=engine)


class Pencil:
    def add_new_entry(self):
        new_entry = input("Tell me what you are thinking: ")
        journal = Journal(entry=new_entry)
        local_session.add(journal)
        local_session.commit()
        
pencil = Pencil()
pencil.add_new_entry()