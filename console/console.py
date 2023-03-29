"""This module contains a console for the PyJS-SQL project.

The console provides an interactive command line interface for users to interact
with the PyJS-SQL library using Python, SQLAlchemy and MySQLdb.

"""

import cmd
from sqlalchemy import create_engine
import MySQLdb

# Create a MySQL database engine
engine = create_engine('mysql://user:password@localhost/db_name', echo=True)

# Create a connection to the MySQL database
conn = MySQLdb.connect(host="localhost", user="user", passwd="password", db="db_name")

# Create a cursor for executing SQL statements
cur = conn.cursor()

class SQLConsole(cmd.Cmd):
    """A console for executing SQL statements using SQLAlchemy and MySQLdb."""

    intro = 'Welcome to the SQL console. Type help or ? to list commands.\n'
    prompt = '(sql) '

    def do_execute(self, arg):
        """Execute an SQL statement."""
        try:
            # Execute the SQL statement and commit the transaction
            cur.execute(arg)
            conn.commit()
            # Print the number of affected rows
            print(f'{cur.rowcount} rows affected.')
        except Exception as e:
            # Rollback the transaction if an error occurs
            conn.rollback()
            print(f'Error: {e}')

    def do_exit(self, arg):
        """Exit the console."""
        print('Exiting the SQL console.')
        conn.close()
        return True

if __name__ == '__main__':
    SQLConsole().cmdloop()
