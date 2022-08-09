import sqlite3

#def greetUser(mode_type):
#    DATABASE = input(f"Hey, my name is Rose and I love helping people with information and data! I am in {mode_type} MODE.  Please enter the name of the database you would like to query...")
#    return DATABASE

#DATABASE = greetUser('Database')

class Product:
    
    __database= ''
    #sucess = print('Action Completed!')
    
    def __init__(self, database=None):
        if database is not None:
            self.__database = database
            self.conn = sqlite3.connect(self.__database) #'students.db'
            #self.conn = sqlite3.connect('students08_22.db')
            self.cur = self.conn.cursor()
            #self.__database = database
            #self.createTable()
            
    @property
    def database(self):
        return self.__database
    
    @database.setter
    def database(self, value):
        value = input(f"Please enter the name of the database you would like to query...")
        self.__database = value 
        
        
    def __repr__(self):
        return f"Awesome!  We are connected to {self.__database}"
        
    def createNewStudentTable(self, new_table_name): #new table by month
        #self.c.execute("""DROP TABLE products""") #<--deletes table
        self.cur.execute(f"""CREATE TABLE IF NOT EXISTS {new_table_name}(
                            name TEXT PRIMARY KEY, 
                            instrument TEXT,
                            lesson_time REAL,
                            day_of_study TEXT,
                            age REAL,
                            comments TEXT,
                            status REAL    
                        )""")
        #automatically creates a favorable index based on their status column
        #this favorability is based on the status of the student
        self.cur.execute(f"""CREATE INDEX favorability ON {new_table_name}(
                            status
                        )""")
        print(f"{new_table_name} created!!!\n Action Completed!")
        print("Index created!")
        self.conn.commit()
        self.conn.close()
    
       
    def insert(self, table, item):
        self.cur.execute(f"""INSERT OR IGNORE INTO {table} VALUES (?,?,?,?,?,?,?)""",
                       item)
        #^THIS REQUIRES 6 VALUES AS AN ARG!
        print(f"STUDENT INSERTED INTO {table}...ACTION COMPLETED!")
        self.conn.commit()
        self.conn.close()
        
    def dropTable(self, table_to_drop):
        self.cur.execute(f"""DROP TABLE {table_to_drop}""")
        print(f'{table_to_drop} DROPPED FROM {self.__database}!')
        self.conn.commit()
        self.conn.close()
        
    def read(self, table, data):
        if data == 'all':
            self.cur.execute(f"""SELECT * FROM {table}""")
            #amount = int(input("How many rows may I fetch for you?: "))
            #rows = self.c.fetchmany(amount)
            rows = self.cur.fetchall()
            self.conn.commit()
            print(rows)
            return rows
        if data == 'many':
            self.cur.execute(f"""SELECT * FROM {table}""")
            selection = int(input("How many rows would you like to view?: "))
            rows = self.cur.fetchmany(selection)
            self.conn.commit()
            print(rows)
            return rows
        if data == 'one':
            self.cur.execute(f"""SELECT * FROM {table}""")
            selection = int(input("Which entry would you like to view?: "))
            rows = self.cur.fetchmany(selection)
            self.conn.commit()
            print(rows)
            return rows
        else:
            print("Please enter something valid...")
        print("action completed!!!")
            

            
      
    
    #CREATE CUSTOM INPUT FOR NEW ROW!
    
        
    