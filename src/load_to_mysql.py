
import mysql.connector
import pandas as pd
from getpass import getpass

# Load CSV dataset
df = pd.read_csv("data/student_placement_data.csv")

print("Total records found:", len(df))

password = getpass("Enter MySQL root password: ")

try:
    connection = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=password,
        database="student_placement_db"
    )

    cursor = connection.cursor()

    query = """
    INSERT INTO students (
        student_id,
        student_name,
        department,
        cgpa,
        attendance,
        aptitude_score,
        technical_skills,
        internship,
        placement_status
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    records = list(df.itertuples(index=False, name=None))

    cursor.executemany(query, records)

    connection.commit()

    print("Successfully imported", cursor.rowcount, "students!")

    cursor.close()
    connection.close()

except mysql.connector.Error as error:
    print("Database error:", error)
