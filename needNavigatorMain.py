from socket import create_connection
import sqlite3

#def greetUser(mode_type):
#    DATABASE = input(f"Hey, my name is Rose and I love helping people with information and data! I am in {mode_type} MODE.  Please enter the name of the database you would like to query...")
#    return DATABASE

#DATABASE = greetUser('Database')


class db_connection:
    def __init__(self, database):
        self.database = database
        self.conn = create_connection(self.database)
        self.cursor = self.conn.cursor()
    
    def create_connection(self, database):
        conn = sqlite3.connect(database)
        print(f"Connected to {database} database!")
        return conn
        
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        self.conn.commit()
        self.conn.close()
    
    def read(sql):
        connection = create_connection()
        df = 
        
        connection.commit()
        connection.close()
        return df
    def write(df):
        connection = self.create_connect()
        df = connection.write(df,table)
        connection.commit()
        connection.close()
        return df

class SqliteConnection(db_connection):
    def __init__(self):
        super.__init__()
    
    









class PostgressConnection(db_connection):

    def __init__(self, host,db_name,user,password,key_code):
        super.__init__(host,db_name,user,password)
        self.key_code = key_code


    def create_connect(self):
        print('some postgress conneciton object')
        connection= self.host+self.db_name+self.user+self.password
    def write(df):
        print('some postgress operation')
        connection = self.create_connect()
        df = connection.write(df,table)
        connection.commit()
        connection.close()
        return df
    def post_opperation():
        print('some post operation')



class sqlServerConnection(PostgressConnection):

    def __init__(self, host,db_name,user,password):
         self.host = host
         self.db_name = db_name
         self.user = user
         self.password = password
        

    def create_connect(self):
        print('some sql conneciton object')
        connection= self.host+self.db_name+self.user+self.password

    def exicute_sql(sql):
        print('some sql conneciton exicute')
        connection = self.create_connect()
        connection.exicute(sql)
        connection.commit()
        connection.close()