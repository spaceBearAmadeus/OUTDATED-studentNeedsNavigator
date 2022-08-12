import psycopg2
import connectionDetails as cd

#IN HERE, PUT VANILLA SQL COMMANDS AS METHODS
class dbConnector:
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
        print("Postgres connection and cursor closed!!!!")
        
    def store_binary(self, string):
        str_store = psycopg2.Binary(string)
        print(f"An object capable of holding: {string} has been created!")
        return str_store
    
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

#object used to generate strings that are sql queries
sq = SqlQuery()

#create postgress connection
pg_connector.create_connection()

#generate string that is a create new table query (with drop)
new_table = sq.create_new_student_table_query('Students_0822')
#use parent method to execute the string
pg_connector.execute_sql(new_table, item=None)

#generate string that is an insert query with arg as the table u are inserting into
new_row = sq.new_insert_student_query('Students_0822')
#new batch of inputs
new_student_batch1 = [('Mason Miller', 'guitar', 300, 'T', 8, 'creative, personable', 4.5),
                      ('Emma Miller', 'piano', 330, 't', 6, 'creative, redirection', 3)]

#iterate over this list and execute each one
for student in new_student_batch1:
    pg_connector.execute_sql(sql_query=new_row, item=student)

#close pg connection
pg_connector.close_connection()