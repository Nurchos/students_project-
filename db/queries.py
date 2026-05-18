from db.database import connect_db


def add_student(name, age, course):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO student (name, age, course) VALUES (?, ?, ?)",
        (name, age, course)
    )

    connection.commit()
    connection.close()


def get_students():
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    connection.close()

    return students


def update_student(student_id, new_name):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "UPDATE student SET name = ? WHERE id = ?",
        (new_name, student_id)
    )

    connection.commit()
    connection.close()


def delete_student(student_id):
    connection = connect_db()
    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()