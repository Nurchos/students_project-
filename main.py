from db.database import init_db
from db.queries import (
    add_student,
    get_students,
    update_student,
    delete_student
)


init_db()

add_student("Alex", 18, "Python")
add_student("John", 20, "Backend")

students = get_students()

for student in students:
    print(student)

update_student(1, "Mike")

delete_student(2)