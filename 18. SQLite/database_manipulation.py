#       TASK 23     #  


"""
Follow these steps:
    ● Create a Python file called database_manip.py. Write the code to do the
    following tasks:
    ○ Create a table called python_programming.
    ○ Insert the following new rows into the python_programming table:

    id      name                     grade
    55      Carl Davis               61
    66      Dennis Fredrickson       88
    77      Jane Richards            78
    12      Peyton Sawyer            45
    2       Lucas Brooke             99


    ○ Select all records with a grade between 60 and 80.
    ○ Change Carl Davis's grade to 65.
    ○ Delete Dennis Fredrickson's row.
    ○ Change the grade of all students with an id greater than 55 to a
    grade of 80.
    ○ Include a screenshot in your submission showing the
    python_programming table contents in the DB Browser for SQLite.

"""


import sqlite3

# Connect to the SQLite database (it will be created if it doesn't exist)
conn = sqlite3.connect('task.db')
cursor = conn.cursor()

# Create the python_programming table
create_table_sql = """
CREATE TABLE IF NOT EXISTS python_programming (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    grade INTEGER NOT NULL)
;
"""

cursor.execute(create_table_sql)
conn.commit()

# Insert new rows into the python_programming table
insert_data_sql = """
INSERT INTO python_programming (id, name, grade)
VALUES
    (55, 'Carl Davis', 61),
    (66, 'Dennis Fredrickson', 88),
    (77, 'Jane Richards', 78),
    (12, 'Peyton Sawyer', 45),
    (2, 'Lucas Brooke', 99)
;
"""

cursor.executescript(insert_data_sql)
conn.commit()

# Select all records with a grade between 60 and 80
select_query = """
SELECT * FROM python_programming
WHERE grade BETWEEN 60 AND 80;
"""


cursor.execute(select_query)
results = cursor.fetchall()

print("Records with grades between 60 and 80:")
for row in results:
    print(row)


# Change Carl Davis's grade to 65
update_grade_sql = """
UPDATE python_programming
SET grade = 65
WHERE name = 'Carl Davis';
"""

cursor.execute(update_grade_sql)
conn.commit()

# Delete Dennis Fredrickson's row
delete_row_sql = """
DELETE FROM python_programming
WHERE name = 'Dennis Fredrickson';
"""

cursor.execute(delete_row_sql)
conn.commit()

# Change the grade of all students with an id greater than 55 to 80
update_grade_for_ids_sql = """
UPDATE python_programming
SET grade = 80
WHERE id > 55;
"""

cursor.execute(update_grade_for_ids_sql)
conn.commit()

# Display the final table contents
cursor.execute("SELECT * FROM python_programming")
final_results = cursor.fetchall()

print("Final contents of the python_programming table:")
for row in final_results:
    print(row)

# Close the connection
conn.close()
