
# Python Final Project

This dataset includes a mix of categorical and numerical variables. "Name" and "Address" are categorical variables represented as strings, "Age" is a numerical variable represented as an integer, "Salary" is a numerical variable represented as a float, and "Is Married" is a categorical variable represented as a boolean.
Step 1: Import Libraries
python
import sqlite3
import pandas as pd
Step 2: Connecting to SQLite Database
python
# Create a SQLite database connection
conn = sqlite3.connect("employee_data.db")
This line establishes a connection to a SQLite database named "employee_data.db". If the database does not exist, it will be created.

Step 3: Creating a Cursor Object
python
# Create a cursor object to interact with the database
cursor = conn.cursor()
A cursor is a pointer that allows you to interact with the SQLite database. You can execute SQL commands using this cursor.

Step 4: Create a Table
python
# Create a table in the database
cursor.execute('''
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        age INTEGER,
        salary REAL,
        is_married BOOLEAN,
        address TEXT
    )
''')
This block of code creates a table named "employees" with columns for ID, Name, Age, Salary, Is Married, and Address. The IF NOT EXISTS clause ensures that the table is created only if it doesn't already exist.
Step 5: Commit Changes
python
# Commit the changes to the database
conn.commit()
This line saves the changes made to the database. Without this line, any changes made (such as creating a table) won't be persisted.

Step 6: Read CSV Data into Pandas DataFrame
python
# Read the CSV data into a Pandas DataFrame
df = pd.read_csv("synthetic_employee_data.csv")
This line uses Pandas to read the CSV file ("synthetic_employee_data.csv") into a DataFrame.

Step 7: Insert Data into SQLite Table
python
# Insert the data from the DataFrame into the SQLite table
df.to_sql('employees', conn, if_exists='replace', index=False)
This line inserts the data from the DataFrame into the SQLite table named "employees". The if_exists='replace' parameter ensures that if the table already exists, it will be replaced with the new data.

Step 8: Commit Changes Again
python
# Commit the changes to the database
conn.commit()
Once again, commit the changes to ensure that the data is persisted in the database.

Step 9: Close Database Connection
python
# Close the database connection
conn.close()
This line closes the connection to the SQLite database. It's good practice to close the connection after you have finished working with the database.

After running this script, you should have a SQLite database file named "employee_data.db" with a table named "employees" containing the synthetic employee data.

