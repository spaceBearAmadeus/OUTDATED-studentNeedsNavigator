import psycopg2
import sqlQueries as sq 
import connectionDetails as cd

#IN HERE, PUT VANILLA SQL COMMANDS AS METHODS
class dbConnector:
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname 
        self.user = user 
        self.password = password
        self.port = port 
        self.cur = self.create_connection()
        
    def create_connection(self):
        self.conn = psycopg2.connect(host=self.host,
                                dbname=self.dbname,
                                user=self.user,
                                password=self.password,
                                port=self.port)
        self.cur = self.conn.cursor()
        self.conn.commit()
        try:
            pass 
        except:
            if self is super():
                print("Vanilla Database connecter initiated and cursor created!!!")
        finally:
            return self.cur and self.conn 
    
    def execute_sql(self, sql_query):
        self.cur.execute(sql_query)
        self.conn.commit()
        try:
            pass
        except:
            if self is super():
                print("Vanilla SQL Query initiated!")
        #self.conn.close()
        
    def new_student_table_query(self, new_table_name):
        create_new_student_table = f'''CREATE TABLE {new_table_name} (
                                  name varchar(40) PRIMARY KEY,
                                  instrument varchar(40) NOT NULL,
                                  lesson_time int,
                                  day_of_study varchar(40),
                                  age int,
                                  keyword_comments varchar(100),
                                  status int)'''
        return create_new_student_table
        


#IN HERE, PUT POSTGRES SPECIFIC COMMANDS AS METHODS
class PostgresConnector(dbConnector):
    def __init__(self, host, dbname, user, password, port):
        super().__init__(host, dbname, user, password, port)
        #self.conn = self.create_postgres_connection()
        
    def create_postgres_connection(self):
        self.conn = super().create_connection()
        print("Postgres Connection and Cursor Established!")
        return self.conn
    
    def close_postgres_connection(self):
        self.conn.close()
        self.cur.close()
        print("Postgres connection and cursor closed!!!!")
        
    def execute_pg(self, pg_query):
        self.cur.execute(pg_query)
        self.conn.commit()
        print("Postgres command executed!")
        #self.conn.close()
        
    def create_index(self, index_name, table, col):
        conn = self.create_postgres_connection()
        self.cur.execute(super().execute_sql(f'''CREATE INDEX {index_name} on {table} ({col})'''))
        conn.commit()
          
    def store_binary(string):
        str_store = psycopg2.Binary(string)
        print(f"An object capable of holding: {string} has been created!")
        return str_store
        
    


db_connect = dbConnector(cd.hostname,
                         cd.db_name,
                         cd.username,
                         cd.pwd,
                         cd.port_id)

pg_connector = PostgresConnector(db_connect.host,
                                 db_connect.dbname,
                                 db_connect.user,
                                 db_connect.password,
                                 db_connect.port)


pg_connector.create_postgres_connection()

#new_table = pg_connector.new_student_table_query('Students_0822')
#pg_connector.execute_pg(pg_query=new_table)
#pg_connector.execute_sql(sql_query=new_table)