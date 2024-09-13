import mysql.connector
import datetime
import time
import os

class DBConnection:
    """
    Class to handle connection with Database
    """
    def __init__(self):
        self._db_con = None
        self._db_session = None

    def mysql_connect(self):
        # This method is to establish a connection to the MySQL database
       print("enter connec")
       self.__enter__()

    def __enter__(self):
        """
        Method to create the  connection
        """
        self._db_con = mysql.connector.connect(
        host=os.environ['DB_SERVER'],
        user=os.environ['DB_USR'],
        password=os.environ['DB_PWD'])
        self._db_session = self._db_con.cursor()
        return self._db_session
    
    def mysql_close(self):
        self.__exit__()

    def __exit__(self, exception_type=None, exception_value=None, traceback=None):
        """
        Method to close the connection
        """
        # db_con = mysql_connect()
        # # Create a cursor to interact with the database
        # db_session = db_con.cursor()
        # Close the cursor and database connection
        if self._db_session:
            self._db_session.close()
        if self._db_con:
            self._db_con.close()
        # db_session.close()
        # db_con.close()