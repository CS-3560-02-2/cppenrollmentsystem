import sqlite3
import os
from sqlite3.dbapi2 import OperationalError


# Get the directory of the current file
CURRENT_DIR = os.path.dirname(__file__)
# Set the db path to current directory
DB_PATH = os.path.join(CURRENT_DIR, "enrollmentsystem.db")

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()


def executeScriptFromFile(filename):
    """Executes commands from an sql file

    Args:
        filename (sql file): sql file to execute
    """

    with open(filename, "r", encoding="utf-8") as sql_file:
        sql_script = sql_file.read()

    # all SQL commands (split on ';')
    sqlCommands = filter(None, sql_script.split(";"))
    # Execute every command from the input file
    for command in sqlCommands:
        # This will skip and report errors
        # For example, if the tables do not yet exist, this will skip over
        # the DROP TABLE commands
        try:
            cursor.execute(command)
        except OperationalError as msg:
            print("Command skipped: ", msg)


executeScriptFromFile("enrollmentsystem.db.sql")

conn.commit()
conn.close()
