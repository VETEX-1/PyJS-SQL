"""This module contains a console for the PyJS-SQL project.

The console provides an interactive command line interface for users to interact
with the PyJS-SQL library using Python, SQLAlchemy and MySQLdb.

"""
from sqlalchemy import create_engine
import MySQLdb
import cmd

from history import CommandHistory

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
    history = CommandHistory()

    def do_execute(self, arg):
        """Execute an SQL statement."""
        try:
            # Execute the SQL statement and commit the transaction
            cur.execute(arg)
            conn.commit()
            # Print the number of affected rows
            print(f'{cur.rowcount} rows affected.')
            # Add the command to the history
            self.history.add_command(arg)
        except Exception as e:
            # Rollback the transaction if an error occurs
            conn.rollback()
            print(f'Error: {e}')

    def do_exit(self, arg):
        """Exit the console."""
        print('Exiting the SQL console.')
        conn.close()
        return True

    def emptyline(self):
        """Called when an empty line is entered."""
        pass

    def do_EOF(self, arg):
        """Exit the console on EOF."""
        print('Exiting the SQL console.')
        conn.close()
        return True

    def get_command(self):
        """Override the default method to retrieve the command, allowing for navigation through the command history."""
        command = input(self.prompt)
        if command.strip() == '':
            return ''
        elif command.strip() == '!!':
            # Execute the previous command
            prev_command = self.history.get_previous_command()
            if prev_command is not None:
                print(prev_command)
                return prev_command
            else:
                return ''
        elif command.strip() == '!':
            # Execute the next command
            next_command = self.history.get_next_command()
            if next_command is not None:
                print(next_command)
                return next_command
            else:
                return ''
        else:
            # Add the command to the history
            self.history.add_command(command)
            return command

if __name__ == '__main__':
    SQLConsole().cmdloop()
