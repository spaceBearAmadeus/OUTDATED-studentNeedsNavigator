import psycopg2
import connectionDetails as cd
import newStudents as ns 

class SqlQuery:
    def create_new_student_table_query(self, new_table_name):
        create_new_student_table = f'''CREATE TABLE IF NOT EXISTS {new_table_name} (
                                  name varchar(40) PRIMARY KEY,
                                  instrument varchar(40) NOT NULL,
                                  lesson_time int,
                                  day_of_study varchar(40),
                                  age int,
                                  keyword_comments varchar(100),
                                  status float)'''
        return create_new_student_table
    
    def new_insert_student_query(self, table_name_to_be_inserted_into):
        insert_new_student0822 = f'''INSERT INTO {table_name_to_be_inserted_into} (name, instrument, lesson_time, day_of_study, age, keyword_comments, status) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
        return insert_new_student0822
    
    
    def create_index(self, index_name, table, col):
        new_index = f'''CREATE INDEX {index_name} on {table} ({col})'''
        return new_index

#IN HERE, PUT VANILLA SQL COMMANDS AS METHODS
class dbConnector(SqlQuery):
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname 
        self.user = user 
        self.password = password
        self.port = port 
        
    def create_connection(self):
        return None
    
    def close_connection(self):
        return None 
                
    def execute_sql(self, sql_query, item):
        self.cur.execute(sql_query, item)
        self.conn.commit()
        #try:
        #    pass
        #except:
        #    if self is super():
        #        print("Vanilla SQL Query initiated!")
        #self.conn.close()

#IN HERE, PUT POSTGRES SPECIFIC COMMANDS AS METHODS
class PostgresConnector(dbConnector):
    def __init__(self, host, dbname, user, password, port):
        super().__init__(host, dbname, user, password, port)
        self.conn = self.create_connection()
        self.cur = self.conn.cursor()
        
    def create_connection(self):
        self.conn = psycopg2.connect(host=self.host,
                                     dbname=self.dbname,
                                     user=self.user,
                                     password=self.password,
                                     port=self.port)
        self.cur = self.conn.cursor()
        self.conn.commit()
        return self.conn
    
    def close_connection(self):
        self.conn.close()
        self.cur.close()
        goodbye = "Thank you for using me.  Shutting down now..."
        print(f"Postgres connection and cursor closed!!!!\n{goodbye}")
        
        
    def insert_and_tally(self, insert_batch, table_to_insert):
        amt_students = []
        for index, student in enumerate(insert_batch):
            index = 1
            pg_connector.execute_sql(sql_query=pg_connector.new_insert_student_query(f'{table_to_insert}'),
                                     item=student)
            index += 1
        amt_students.append(index)
        print(f"There are {index} students in total in this batch!")
        
        
    def store_binary(self, string):
        str_store = psycopg2.Binary(string)
        print(f"An object capable of holding: {string} has been created!")
        return str_store
    
#object used for login and execute_sql
db_connect = dbConnector(cd.hostname,
                         cd.db_name,
                         cd.username,
                         cd.pwd,
                         cd.port_id)

#object used for postgres connection, and close connection(has execute sql in it)
pg_connector = PostgresConnector(db_connect.host,
                                 db_connect.dbname,
                                 db_connect.user,
                                 db_connect.password,
                                 db_connect.port)


try:
    pg_connector.create_connection()
    pg_connector.execute_sql(sql_query=pg_connector.create_new_student_table_query('Students_0822'),
                             item=None)
    pg_connector.insert_and_tally(insert_batch=ns.new_student_batch1,
                                  table_to_insert='Students_0822')
except Exception as error:
        print(f"whoops you got an f{error} ERROR!!!!!!!!!!!!!!!!!!!!!!!!!!! TRY AGAIN LOL")
finally:
    pg_connector.close_connection()