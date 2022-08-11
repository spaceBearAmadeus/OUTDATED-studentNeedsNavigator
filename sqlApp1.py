import psycopg2
import sqlQueries as sq 
import connectionDetails as cd

class dbConnector:
    def __init__(self, host, dbname, user, password, port):
        self.host = host
        self.dbname = dbname 
        self.user = user 
        self.password = password
        self.port = port 
        #self.cur, self.conn = self.create_connection()
        
    def create_connection(self):
        self.conn = psycopg2.connect(host=self.host,
                                dbname=self.dbname,
                                user=self.user,
                                password=self.password,
                                port=self.port)
        self.cur = self.conn.cursor()
        self.conn.commit()
        if self.create_connection is not super():
            print("Vanilla Database connecter initiated and cursor created!!!")
        else:
            pass
        return self.cur, self.conn 
    
    def execute_sql(self, sql_query):
        self.cur.execute(f'''{sql_query}''')
        self.conn.commit()
        self.conn.close()
        

class PostgresConnector(dbConnector):
    def __init__(self, host, dbname, user, password, port):
        super().__init__(host, dbname, user, password, port)
        
    def create_postgres_connection(self):
        self.conn = super().create_connection()
        print("Postgres Connection and Cursor Established!")
        
    def execute_pg(self, pg_query):
        self.cur.execute(super().execute_sql(sql_query=pg_query))
        self.conn.commit()
        print("Postgres command executed!")
        self.conn.close()
        
    def store_binary(string):
        str_store = psycopg2.Binary(string)
        print(f"An object capable of holding: {string} has been created!")
        
    
vanilla_db_connector = dbConnector(cd.hostname,
                                   cd.db_name,
                                   cd.username,
                                   cd.pwd,
                                   cd.port_id)

#vanilla_db_connector.create_connection()

pg_connector = PostgresConnector(cd.hostname,
                                   cd.db_name,
                                   cd.username,
                                   cd.pwd,
                                   cd.port_id)


pg_connector.create_postgres_connection()